#!/usr/bin/env python3
"""Render the public technical-community directory from data/forums.json."""

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'data/forums.json').read_text())
OUT = ROOT / 'forums'
OUT.mkdir(exist_ok=True)
ROWS = DATA['communities']
BY_ID = {r['id']: r for r in ROWS}
SECTIONS = {s['id']: s for s in DATA['sections']}

PRIORITY = {'first_pass': 'First pass', 'targeted': 'Targeted', 'archive': 'Archive first'}
VERIFIED = {
    'technical_content': 'Technical text reviewed',
    'index_only': 'Index only',
    'identity_only': 'Identity verified; content unsampled',
    'access_unverified': 'Access/content unverified',
    'closed': 'Closed; no available archive verified',
    'historical_destination_uncertain': 'Historical text; live destination uncertain',
}


def table_text(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def link(label, url):
    return '[' + label.replace('[', '\\[').replace(']', '\\]') + '](' + url + ')'


def local_link(rid, label=None):
    r = BY_ID[rid]
    return link(label or r['name'], SECTIONS[r['section']]['file'] + '#' + rid)


def order(row):
    state = row['verification']
    bucket = 2 if state in {'access_unverified', 'closed', 'historical_destination_uncertain'} else 1 if state in {'index_only', 'identity_only'} else 0
    return bucket, {'first_pass': 0, 'targeted': 1, 'archive': 2}[row['priority']], row['name'].lower()


def card(r):
    lines = [f'<a id="{r["id"]}"></a>', '', f'### {r["name"]}', '',
             f'**{PRIORITY[r["priority"]]} · {VERIFIED[r["verification"]]} · {r["region"]}**', '',
             link('Home / community', r['home_url']) + '  ',
             '**Disciplines:** ' + ', '.join(r['disciplines']) + '.', '']
    if r['technical_urls']:
        lines += ['**Technical starting points:** ' + '; '.join(link(x['label'], x['url']) for x in r['technical_urls']) + '.', '']
    else:
        lines += ['**Technical starting points:** No specific accessible technical section was verified in this pass.', '']
    lines += ['**Research use**', ''] + ['- ' + x for x in r['useful_for']] + ['']
    a = r['activity']
    date = a['observed_date'] or 'No exact date established'
    lines += ['**Observed dated evidence:** ' + date + '. ' + a['note'] + ' ' + link('Evidence', a['evidence_url']) + '.', '',
              '**Access:** ' + r['access_note'], '']
    if r['example_threads']:
        lines += ['**Sample discussions**', '']
        for t in r['example_threads']:
            when = t['date'] or 'date not established'
            level = '; index/title only' if t.get('evidence_level') == 'index_only' else ''
            lines += ['- ' + link(t['title'], t['url']) + f' — {when}{level}. ' + t['signal']]
        lines += ['']
    else:
        lines += ['**Sample discussions:** No substantive thread example was verified in this pass.', '']
    lines += ['**Limits:** ' + ' '.join(r['limitations']), '']
    sources = list(dict.fromkeys(r['source_urls']))
    if sources:
        lines += ['**Supporting sources:** ' + ' · '.join(link(str(i + 1), u) for i, u in enumerate(sources)) + '.', '']
    return lines


def render_section(section):
    rows = sorted([r for r in ROWS if r['section'] == section['id']], key=order)
    lines = [f'# {section["title"]}', '', '[Directory index](README.md) · [What the discussions suggest](RESEARCH_NOTES.md)', '',
             f'**Reviewed {DATA["reviewed_on"]} · {len(rows)} directory entries**', '', section['description'], '',
             'Priorities describe research usefulness, not audience size. An observed date is evidence from a sample, not a claim about the site’s latest activity. Read the access and verification labels before using a source.', '',
             '## Quick index', '', '| Community | Research priority | Evidence / access | Observed date |', '|---|---|---|---|']
    for r in rows:
        lines.append('| ' + ' | '.join(table_text(v) for v in [link(r['name'], '#' + r['id']), PRIORITY[r['priority']], VERIFIED[r['verification']], r['activity']['observed_date'] or 'Unknown']) + ' |')
    lines += ['', '## Useful search terms', '', ', '.join('`' + x + '`' for x in section['search_terms']) + '.', '',
              'Related sources: ' + '; '.join(local_link(rid) for rid in section['crossovers']) + '.', '', '## Community notes', '']
    for r in rows:
        lines += card(r)
    if section['id'] == 'reddit':
        lines += ['## Names checked but not independently verified', '',
                  'These eight exact subreddit names are follow-up leads. They are **not** included in the 22 verified community identities above. A failed fetch is not evidence that a subreddit is absent, private or inactive. Similar spellings are not assumed to be aliases.', '',
                  '| Name / candidate URL | What remains unresolved | Verified route or alternative |', '|---|---|---|']
        for r in DATA['unverified_reddit_candidates']:
            lines.append('| ' + ' | '.join(table_text(v) for v in [link(r['name'], r['home_url']), r['reason'], r['alternative']]) + ' |')
        lines += ['', 'General racing news, gaming and highlight feeds were not included merely to make the list longer. r/F1Technical and r/NHRA are targeted engineering context; r/esp32 is included for a specific automotive logging discussion. None is a substitute for evidence from likely customers.', '']
    (OUT / section['file']).write_text('\n'.join(lines).rstrip() + '\n')


def render_index():
    kinds = Counter(r['kind'] for r in ROWS)
    verifications = Counter(r['verification'] for r in ROWS)
    examples = sum(len(r['example_threads']) for r in ROWS)
    lines = ['# Technical racing forums and communities', '',
             f'**Reviewed {DATA["reviewed_on"]} — Australia/Melbourne**', '',
             f'This directory records **{len(ROWS)} source locations: {kinds["forum"]} forum/support-board locations and {kinds["reddit"]} Reddit communities**, with **{examples} linked sample discussions or indexed topic leads**. Eight additional exact Reddit names remain unverified and are listed separately. Some forum entries are inaccessible leads or historical names, including one confirmed closed forum; this is not a claim that all locations are active or fully inspected.', '',
             'The aim is to find recurring technical jobs, awkward workarounds and equipment problems that could inform SkidLabz R&D. Keep the problem, its evidence and the existing decision together. Start with the shortlist below, then use a discipline page for the full directory.', '',
             '## Browse by discipline', '', '| Area | Entries | Where to look |', '|---|---:|---|']
    for s in DATA['sections']:
        count = sum(r['section'] == s['id'] for r in ROWS)
        lines.append(f'| {link(s["title"], s["file"])} | {count} | ' + {
            'sprint_dirt': 'HoseHeads, 4m, regional oval forums and important access gaps',
            'karting': 'Bob’s 4 Cycle, KartPulse, international/club boards and historical archives',
            'circuit': 'Grassroots Motorsports, TMO, Rennlist, endurance and platform boards',
            'drift_drag': 'Driftworks, CLASS RACER, Bracket Talk, Speed-Talk and engine/platform boards',
            'electronics': 'PCMHacking, HPA, Link, MoTeC, DIY ECU and student engineering communities',
            'reddit': '22 verified identities, technical examples, search links and eight unverified names',
        }[s['id']] + ' |')
    lines += ['', '**Research output:** [Problem themes, existing idea links and search method](RESEARCH_NOTES.md).', '',
              '**Capture a new finding:** [Forum finding template](../templates/FORUM_FINDING_TEMPLATE.md).', '',
              '## First places to search', '',
              'This is an editorial shortlist for our technical interests, not a traffic ranking. HoseHeads is valuable for remembered historical threads; its present technical activity needs a separate check.', '',
              '| Source | Why start there |', '|---|---|']
    for pick in DATA['shortlist']:
        lines.append('| ' + local_link(pick['id']) + ' | ' + table_text(pick['reason']) + ' |')
    reddit_ids = ['reddit_cartrackdays', 'reddit_autocross', 'reddit_karting', 'reddit_dragracing', 'reddit_fsae', 'reddit_ecu_tuning', 'reddit_enginebuilding', 'reddit_carhacking', 'reddit_projectcar', 'reddit_speeduino', 'reddit_hptuners']
    lines += ['', '**Reddit first pass:** ' + ', '.join(local_link(rid) for rid in reddit_ids) + '.', '',
              'Use r/Drifting, r/DirtRacing and r/SprintCarRacing with a narrow technical search; general feeds contain substantial nontechnical material. Vendor and embedded communities are especially useful once a specific integration problem has been identified.', '',
              '## Important corrections and access qualifications', '',
              '- **HoseHeads:** the two torsion-tester threads from 2009 and 2011 are preserved in its entry. They establish historical discussion, not current demand. The dedicated technical index contains spam.',
              '- **4m:** a fresh-looking Powertrain bump was spam on an old thread. A separate substantive September 2026 chassis question supplies the recent technical evidence.',
              '- **MoTeC:** the old forum redirects to the current Zendesk support community; the directory records the working destination and i2 category.',
              '- **Zilvia:** its own closure notice was verified. No usable archive was confirmed; it remains a historical name, not a place to start live research.',
              '- **DragStuff:** old indexed technical material exists, but a changed live destination has uncertain continuity. Check the destination before relying on it.',
              '- **Yellow Bullet, The Turbo Forums, Indiana Open Wheel, The Dirt Forum, Karting1, TenTenths and other labelled leads:** inaccessible or insufficiently verified in this pass. Failed retrieval is not closure evidence.',
              '- **eKartingNews, Kartbook, Mazda Racers and FSAE.com:** the sampled material is primarily archival. A recent news/sidebar item or site clock was not counted as new forum activity.', '',
              '## What was actually verified', '', '| Evidence level | Locations | Meaning |', '|---|---:|---|']
    for state, meaning in DATA['verification_meanings'].items():
        lines.append(f'| {VERIFIED[state]} | {verifications[state]} | {meaning} |')
    lines += ['', '## How to interpret and maintain this directory', '']
    lines += ['- ' + m for m in DATA['method']]
    lines += ['', '### Research priority', '', '| Label | Meaning |', '|---|---|']
    for key, meaning in DATA['priority_meanings'].items():
        lines.append(f'| {PRIORITY[key]} | {meaning} |')
    lines += ['', '### Coverage boundaries', ''] + ['- ' + g for g in DATA['coverage_gaps']]
    lines += ['', '### Updating the files', '',
              'Edit [data/forums.json](../data/forums.json), preserve existing community IDs and evidence dates, then regenerate the directory:', '',
              '```sh', 'python scripts/render_forums.py', '```', '',
              'The seven index/directory pages are generated. [RESEARCH_NOTES.md](RESEARCH_NOTES.md) is the curated interpretation and is maintained separately. [REGISTER.md](../REGISTER.md), [DECISIONS.md](../DECISIONS.md) and the [competitor lists](../competitors/README.md) remain the records for existing product status, rejected approaches and market references.', '']
    (OUT / 'README.md').write_text('\n'.join(lines))


if __name__ == '__main__':
    assert len(BY_ID) == len(ROWS), 'Duplicate community IDs'
    for section in DATA['sections']:
        render_section(section)
    render_index()
    print(f'Rendered directory for {len(ROWS)} locations across {len(DATA["sections"])} sections.')
