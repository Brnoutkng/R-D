#!/usr/bin/env python3
"""Render the human-readable register from its versioned JSON records (stdlib only)."""
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
payload=json.loads((ROOT/'data/ideas.json').read_text())
ideas=payload['ideas']
evidence=json.loads((ROOT/'data/sources.json').read_text())
sources={s['id']:s for s in evidence['sources']}
decisions=json.loads((ROOT/'data/decisions.json').read_text())['decisions']
by_slug={i['slug']:i for i in ideas}
LABELS={
 'active-development':'Active development', 'active-internal':'Active season/internal tool',
 'active-as-needed':'Active as needed', 'active-background':'Active background work',
 'investigation':'Investigation / samples', 'paused-cost':'Paused — cost',
 'paused-priority':'Parked — priority / go-no-go', 'paused-validation':'Paused — validation',
 'paused-sourcing':'Paused — sourcing', 'paused-feasibility':'Paused — feasibility',
 'paused-scope':'Paused — scope', 'research-only':'Research only', 'sourcing-only':'Sourcing only',
 'future-option':'Future option', 'deprioritized':'Deprioritised',
 'rejected-commercial':'Rejected — commercial', 'rejected-scope':'Dropped — scope/owner decision',
 'mixed-scope':'Earlier scope rejected; later scope unapproved',
 'historical-unadopted':'Historical suggestion — unadopted', 'superseded':'Superseded / reference'
}
CATS=['Core products','Workshop and race tools','Pit equipment','Supporting resale products','Software and internal tools',
      'Future variants and accessories','Historical reference','Business infrastructure','Unadopted research suggestions']

def cell(value): return str(value or 'Not established').replace('|','\\|').replace('\n',' ')
def link(i,prefix=''): return f"[{i['id']} — {i['name']}]({prefix}ideas/{i['slug']}.md)"
def write(path,lines):
    target=ROOT/path;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text('\n'.join(lines).rstrip()+'\n')
def refs(ids,prefix=''):
    return ', '.join(f"[{x}]({prefix}SOURCES.md#{x.lower()})" for x in ids)
def bullet(items): return ['- '+str(x) for x in items]

required=['id','slug','name','status','stage','summary','reason','repo_state','basis','confidence','next_step','reopen_trigger','source_ids']
assert len(by_slug)==len(ideas),'Duplicate slugs'
assert len({i['id'] for i in ideas})==len(ideas),'Duplicate IDs'
assert len(sources)==len(evidence['sources']),'Duplicate source IDs'
for i in ideas:
    assert all(k in i for k in required),i['slug']
    assert i['status'] in LABELS,i['status']
    assert all(x in sources for x in i['source_ids']),(i['slug'],i['source_ids'])
    if i.get('parent_slug'): assert i['parent_slug'] in by_slug,i['slug']
for d in decisions: assert d['product_slug'] in by_slug,d['id']

main=[i for i in ideas if i['status']!='historical-unadopted']
history=[i for i in ideas if i['status']=='historical-unadopted']
lines=['# Product and idea register','',f"Reviewed {payload['reviewed_on']} · Australia/Melbourne",'',
 'This is the place to check what was considered, how far it got, why it stopped and what would justify another look.',
 '',f"**{len(main)} primary records** are listed here. **{len(history)} unadopted research/naming records** are in [Research suggestions](RESEARCH_SUGGESTIONS.md). These are catalogue records, not a count of active products.",'',
 '[Home](README.md) · [Detailed decisions](DECISIONS.md) · [Corrections and uncertainty](RECONCILIATION.md) · [Sources and coverage](SOURCES.md)','',
 '## How to read the status','',
 'Status describes the decision to proceed, pause or stop. Stage describes work actually completed. A repository, clean design check, sample purchase or prepared manufacturing package is not proof of a validated or released product. Open an idea for its sources, history and resume condition.','']
for cat in CATS:
    group=[i for i in main if i['category']==cat]
    if not group: continue
    lines += [f'## {cat}','', '| Idea | Where it stands | Stage reached | Repository | Why / remaining gate |','| --- | --- | --- | --- | --- |']
    for i in group:
        repo=f"[Repo]({i['repo']})" if i.get('repo') else 'No dedicated repo found'
        if i['kind']=='resale': repo='Sourcing record; no dev repo'
        lines.append(f"| {link(i)} | {LABELS[i['status']]} | {cell(i['stage'])} | {repo} | {cell(i['reason'])} |")
    lines.append('')
write('REGISTER.md',lines)

lines=['# Unadopted research and naming suggestions','',
 'These ideas were raised in research or early naming discussions. Their inclusion preserves history; it does not make them approved products, rejected owner decisions or current development work.',
 '',f'{len(history)} records · [Main register](REGISTER.md) · [Source limitations](SOURCES.md)','',
 '| Idea | What was proposed | Evidence / disposition |','| --- | --- | --- |']
for i in history: lines.append(f"| {link(i)} | {cell(i['summary'])} | {cell(i['reason'])} |")
write('RESEARCH_SUGGESTIONS.md',lines)

for i in ideas:
    repo=f"[Open development repo]({i['repo']})" if i.get('repo') else 'No dedicated development repo found'
    lines=[f"# {i['id']} — {i['name']}",'','[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)','',
       '| Field | Record |','| --- | --- |',f"| Status | **{LABELS[i['status']]}** |",f"| Stage reached | {cell(i['stage'])} |",f"| Kind | {cell(i['kind'])} |",
       f"| Repository | {repo} |",f"| Repository state | {cell(i['repo_state'])} |",f"| Evidence basis | {cell(i['basis'])} |",f"| Evidence confidence | {cell(i['confidence'])}; confidence in this record, not product readiness |",
       f"| Evidence date | {i.get('evidence_date') or 'Individual decision date not established; see dated sources'} |",f"| Last reviewed | {i['reviewed_on']} |",'',
       '## Idea','',i['summary'],'','## Why it is at this status','',i['reason'],'','## Next useful step','',i['next_step'],'','## What would justify reopening or advancing it','',i['reopen_trigger'],'']
    if i.get('aliases'): lines += ['## Names and search terms','',', '.join(i['aliases']),'']
    if i.get('parent_slug'): lines += ['## Related record','',link(by_slug[i['parent_slug']],'../'),'']
    if i.get('boundaries'): lines += ['## Decisions and boundaries to retain','']+bullet(i['boundaries'])+['']
    if i.get('history'):
        lines+=['## Decision history','','| Date | Decision / evidence |','| --- | --- |']
        for h in i['history']:lines.append(f"| {h.get('date') or 'Date not established'} | {cell(h['decision'])} |")
        lines+=['']
    related=[d for d in decisions if d['product_slug']==i['slug']]
    if related: lines+=['## Recorded implementation decisions','']+[f"- [{d['id']} — {d['approach']}](../DECISIONS.md#{d['id'].lower()})" for d in related]+['']
    lines+=['## Sources','',refs(i['source_ids'],'../'),'']
    write(Path('ideas')/(i['slug']+'.md'),lines)

lines=['# Decisions, rejections and holds','',
 'Check the reason and reopening condition before repeating a search. A rejected component or architecture does not automatically reject its parent product. A deferred option is not a permanent rejection.',
 '', '[Main register](REGISTER.md) · [Corrections](RECONCILIATION.md) · [Sources](SOURCES.md)','',
 '## Product-level stops and holds','','| Record | Disposition | Reason | Condition for another look |','| --- | --- | --- | --- |']
for i in main:
    if i['status'].startswith(('paused','rejected')) or i['status'] in ['deprioritized','mixed-scope','superseded']:
        lines.append(f"| {link(i)} | {LABELS[i['status']]} | {cell(i['reason'])} | {cell(i['reopen_trigger'])} |")
lines+=['','## Implementation and scope decisions','',f'{len(decisions)} more specific records follow. These are linked from each parent idea.','']
for d in decisions:
    lines += [f"### {d['id']}",'',f"**{d['approach']}** · {link(by_slug[d['product_slug']])}",'',
              f"**Disposition:** {d['status'].replace('_',' ')}. **Evidence date:** {d.get('evidence_date') or 'not individually established'}.",'',d['reason'],'',
              '**Reopen/advance condition:** '+d['reopen_trigger'],'']
    if d.get('source_url'):lines+=['[Repository source]('+d['source_url']+'). '+d.get('source_note',''),'']
    else:lines+=[refs(d.get('source_ids',[])) or d.get('source_note','See parent record.'),'']
write('DECISIONS.md',lines)

lines=['# Sources and coverage','',
 'Review date: 17 November 2026, Australia/Melbourne. This is an evidence-based historical catalogue, not a new engineering validation or a live supplier/stock audit.','',
 '## What was reviewed','',
 '- All 13 accessible existing SkidLabz project repositories, plus the R-D destination.',
 '- Recursive default-branch trees and branch inventories; materially newer or different development branches were followed.',
 '- 154 relevant repository planning, product, status, research, decision and historical documents across the three review groups.',
 '- Recovered chat excerpts from the available history, including explicit owner decisions and earlier assistant suggestions.',
 '- Two saved Markdown product/job lists read in full; additional saved-source excerpts where returned by historical retrieval.','',
 '## Limits','',
 '- This is not an exhaustive export/read of every conversation, deleted branch, issue or PR. The full latest 16–17 November brainstorm was not retrievable; affected records say so.',
 '- The source search returned no durable conversation URLs. Chat sources are identified by date/topic and evidence type; none of the tool-local result labels are presented as real links.',
 '- A global control-file update date does not date every contained project decision. Specific owner decisions and newer project evidence can supersede stale entries.',
 '- Private development sources remain in their original repositories. This public register records general concepts and decisions; detailed engineering, negotiated prices, order/payment/contact data and raw source dumps are not copied.',
 '- Evidence confidence is about the historical record. It is not a claim of electrical, mechanical, regulatory or commercial qualification.',
 '- Commit snapshot dates below are GitHub UTC dates. Dates explicitly written in source documents are preserved as written; the review date uses Melbourne time.','',
 '## Repository snapshots','','| Repository | Main snapshot | Source date (UTC) | Role |','| --- | --- | --- | --- |']
for r in evidence['repositories']:
    lines.append(f"| [{r['name']}]({r['url']}) | [{r['main_sha'][:8]}]({r['url']}/tree/{r['main_sha']}) | {r['main_date']} | {cell(r['role'])} |")
lines+=['','### Additional branch evidence','']
for r in evidence['repositories']:
    for b in r.get('additional_branches',[]):
        lines+=[f"- **{r['name']} / {b['name']}** — [{b['sha'][:8]}]({r['url']}/tree/{b['sha']}): {b['notes']}"]
lines+=['','## Source catalogue','']
for s in evidence['sources']:
    lines += [f"### {s['id']}",'',f"**{s['title']}**",'',f"Type: {s['type']}. Source date: {s.get('date') or 'not individually established'}.",'']
    if s.get('url'): lines+=['[Open source]('+s['url']+')','']
    lines += [s.get('notes',''),'']
write('SOURCES.md',lines)
print(json.dumps(dict(records=len(ideas),primary=len(main),unadopted=len(history),decisions=len(decisions),sources=len(sources),status_counts=Counter(i['status'] for i in ideas)),indent=2))

