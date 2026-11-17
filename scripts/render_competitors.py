#!/usr/bin/env python3
"""Render the two historical competitor registers from their source records."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'data/competitors.json').read_text())
SOURCES = json.loads((ROOT / 'data/competitor_sources.json').read_text())['sources']
RECORDS = DATA['records']
TARGET = ROOT / 'competitors'
TARGET.mkdir(exist_ok=True)

def clean(value):
    return str(value).replace('|', '\\|').replace('\n', ' ').strip()

def table(rows):
    lines = ['| Business / brand | What we discussed | Role and qualifications | Sources |', '|---|---|---|---|']
    for r in sorted(rows, key=lambda x: x['name'].casefold()):
        name = f"[{clean(r['name'])}]({r['website']})" if r['website'] else clean(r['name'])
        name = f'<a id="{r["id"]}"></a>**{name}**'
        if r['aliases']:
            name += '<br>Also recorded: ' + clean('; '.join(r['aliases']))
        detail = clean(r['role'])
        if r['qualification']:
            detail += '<br>' + clean(r['qualification'])
        refs = ' · '.join(f'[{sid}](SOURCES.md#{sid.lower()})' for sid in r['historical_sources'])
        for i, url in enumerate(dict.fromkeys(r['classification_sources']), 1):
            refs += f' · [Role evidence{f" {i}" if i>1 else ""}]({url})'
        lines.append(f"| {name} | {clean(r['discussion_context'])} | {detail} | {refs} |")
    return lines

def section(lines, title, rows, note=None, collapsed=False):
    if not rows:
        return
    lines += ['', f'## {title}', '']
    if note:
        lines += [note, '']
    if collapsed:
        lines += ['<details>', f'<summary>Show {len(rows)} historical references</summary>', '']
    lines += table(rows)
    if collapsed:
        lines += ['', '</details>']

def rows_for(primary, section_name):
    return [r for r in RECORDS if r['primary_list']==primary and r['section']==section_name]

def intro(title, other, page):
    return [f'# {title}', '', '**Reviewed 17 November 2026 — Australia/Melbourne.**', '', f'[Competitor register](README.md) · [{other}]({page}) · [History, coverage and name corrections](SOURCES.md) · [Main R-D index](../README.md)', '']

resellers = intro('Resellers, distributors and race shops','Manufacturers and product brands','MANUFACTURERS.md')
resellers += ['Businesses recovered from our discussions as catalogue references, race shops, distributors or sourcing channels. The manufacturer page holds the corresponding product makers/brands. Mixed businesses are cross-listed where their own-product and resale roles are both supported.', '', 'The **Sources** column separates the historical mention (H/R references) from evidence used to classify the business. A current website does not prove current stock, a trading relationship or a recommendation.', '']
section(resellers,'Australian motorsport and performance sellers',rows_for('resellers','australia'))
section(resellers,'International motorsport retailers',rows_for('resellers','international'), 'Smiley’s is retained with its historical identity qualification. US Speedway Motors is kept separate from the unresolved Queensland label.')
section(resellers,'Businesses with both own-product and resale roles',[r for r in RECORDS if 'resellers' in r['also_listed_in']], 'These are the same records shown in the maker list, not additional companies. Selling a maker’s own products alone does not automatically make it a reseller.')
section(resellers,'Broader tool and component-retail sources',rows_for('resellers','general_sources'), 'These were specific sourcing or market-position references. They are not all direct finished-product competitors.')
section(resellers,'Historical names still needing identity checks',rows_for('resellers','unresolved'), 'Preserved exactly enough to find the earlier discussion. No guessed website or manufacturer classification is attached.')
(TARGET / 'RESELLERS.md').write_text('\n'.join(resellers)+'\n')

makers = intro('Manufacturers and product brands','Resellers, distributors and race shops','RESELLERS.md')
makers += ['Product makers, own-product brands and developers recovered from our work. The role column distinguishes a documented manufacturer from an own-brand supplier or developer; it does not claim every catalogue item is manufactured in-house.', '', '**Start with the race tools, electronics and engine/workshop sections.** Older adjacent markets, software, OEM leads and unresolved historical names follow in their own sections. Brand families remain searchable without being presented as unrelated legal companies.', '']
for key,title,note in [
    ('race_tools','Race instruments, setup tools and practical race products',None),
    ('electronics','Engine electronics, sensors and data logging',None),
    ('engine_tools','Engine inspection, workshop and suspension equipment',None),
    ('gps','GPS performance measurement',None),
    ('side_products','Tyre-care, helmet and consumable product brands','Helmet names may be fitment or consumable references rather than direct electronics competitors.'),
    ('legacy','Legacy products and brands','These remain useful historical benchmarks. Any operating-status note is limited to the cited product range or official notice; absence of a working website does not prove closure.'),
    ('adjacent_engine_parts','Earlier engine and driveline brands','From the earlier general performance-parts and driveline discussions. Inclusion does not imply direct overlap with the current SkidLabz electronics range.'),
]:
    section(makers,title,rows_for('manufacturers',key),note)
section(makers,'Mixed product supplier cross-reference',[r for r in RECORDS if 'manufacturers' in r['also_listed_in']], 'Also listed in the reseller register because third-party distribution is a documented part of the business.')
section(makers,'Software products and calculator publishers',rows_for('manufacturers','software'), '**These are software/reference products, not physical manufacturers.** RaceBase is grouped under Computech above; Circle Track App is grouped under Wehrs Machine. MegaLogViewer is grouped with EFI Analytics.')
section(makers,'Finished-product OEM and private-label sourcing leads',rows_for('manufacturers','oem_leads'), '**These are historical sourcing leads, not approved suppliers or confirmed direct competitors.** Unverified grouped names preserve the recovered wording; they do not establish common ownership. No claimed OEM relationship to Longacre, Intercomp or another brand is inferred.',collapsed=True)
section(makers,'Donor/side-product references with manufacturing role unverified',rows_for('manufacturers','side_products_pending'), 'These complete-product names were discussed, but the available evidence is insufficient for an actual-manufacturer claim.',collapsed=True)
section(makers,'Unresolved product and maker identities',rows_for('manufacturers','unresolved'), 'Names/models retained for continuity. They are not counted as verified manufacturers.',collapsed=True)
section(makers,'Early performance-market business references',rows_for('manufacturers','early_business_references'), 'Recovered from an early business/brand research list. They were not a completed competitive product assessment, and this section does not assign them a verified manufacturer or reseller role. Personalities, media, events and teams are excluded.',collapsed=True)
makers += ['', '## Other historical names without a competitor classification', '', f'These additional mentions are preserved for search continuity, outside the {len(RECORDS)} business/brand records. They are not assigned a maker, reseller or OEM relationship.', '', '| Recovered names | Context and limitation | History |', '|---|---|---|']
for item in DATA.get('unclassified_mentions', []):
    refs = ' · '.join(f'[{sid}](SOURCES.md#{sid.lower()})' for sid in item['historical_sources'])
    makers.append(f"| {clean('; '.join(item['names']))} | {clean(item['context'])} | {refs} |")
(TARGET / 'MANUFACTURERS.md').write_text('\n'.join(makers)+'\n')

counts = Counter(r['primary_list'] for r in RECORDS)
readme = [
    '# Competitors and market references', '',
    'Two places to check the businesses and product brands we have already discussed:', '',
    '- **[Resellers, distributors and race shops](RESELLERS.md)** — Rocket Industries, VPW, Smiley’s, IBRP, QSS and the other retail/sourcing references.',
    '- **[Manufacturers and product brands](MANUFACTURERS.md)** — Longacre, Intercomp, AFCO, JOES, QuickCar, Tel-Tac, RACEceiver and the other product-maker references.', '',
    'Each record says why the name came up, preserves useful aliases/product names, links the historical evidence and records the role/classification source where available. Businesses with both roles have one underlying record and appear in both views.', '',
    '## Coverage', '',
    f"The review recovered **{len(RECORDS)} business, brand and historical reference records**: **{counts['resellers']} primarily filed with sellers** and **{counts['manufacturers']} filed with product makers/developers and their related historical references**. This is not a count of verified competing companies: the second group includes software, OEM sourcing leads, legacy brands and unresolved names, each visibly separated.", '',
    'The evidence comprises recovered chat summaries, saved research and relevant source documents from the existing review of 13 accessible development repositories. It is not a complete transcript export of every chat. Newly found names should be added with their historical context rather than assumed to have been discussed before.', '',
    '## How to use the lists', '',
    'Search the brand, business or product alias before starting another catalogue review. A historical mention does not mean we selected that supplier, confirmed a commercial opportunity or reactivated a product. Current project decisions remain in the [ideas register](../REGISTER.md).', '',
    'The most useful distinctions are kept explicit:', '',
    '- Tel-Tac includes Oval Track Pro/OTP; Rugged Radios includes Nitro Bee Xtreme.',
    '- RIFE is linked to Motion Raceworks; Proflow to VPW; Aeroflow to Rocket Industries.',
    '- RaceBase is Computech software; Circle Track App is Wehrs Machine software.',
    '- The recorded raceparts.com.au source is Barnier Race Parts. QSS is Performance Wholesale’s speedway division.',
    '- Smiley’s historical shorthand, Speedway Motors Queensland, Clarksons and other ambiguous labels retain qualifications.', '',
    'See [sources and name corrections](SOURCES.md) for the evidence and exclusions.', '',
    '## Maintenance', '',
    'Edit [competitors.json](../data/competitors.json) and [competitor_sources.json](../data/competitor_sources.json), then regenerate these pages:', '',
    '```sh', 'python scripts/render_competitors.py', '```', '',
    'Preserve aliases and historical reasons. Separate the evidence that a name was mentioned from the evidence that classifies the business. Add no new competitor merely because it appears in current search results.', '',
    '**Review date:** 17 November 2026, Australia/Melbourne. Raw conversations, private transaction details and engineering source content are not reproduced here.'
]
(TARGET / 'README.md').write_text('\n'.join(readme)+'\n')

src = ['# Competitor sources, coverage and name corrections', '', '[Competitor index](README.md) · [Resellers](RESELLERS.md) · [Manufacturers/product brands](MANUFACTURERS.md)', '',
       '## How evidence is used', '',
       '**Historical evidence** establishes that a name appeared in our work. H references are recovered conversation or saved-file summaries; they are not original transcript exports and have no invented chat permalinks. R references are pinned repository documents. Where the original mention was an assistant suggestion, the record remains a historical research reference rather than an owner-approved competitor or supplier.', '',
       '**Role evidence** links official business pages, product documentation or, where explicitly qualified, a historical brand-authored document/identified partner source. The review verifies identity/role to the stated extent. It is not a current-stock, product-performance, factory audit or price check.', '',
       '## Name corrections and relationships', '',
       '| Historical name | Treatment | Evidence |', '|---|---|---|']
corrections = [
    ('Oval Track Pro / OTP','Grouped under Tel-Tac, not QuickCar or an independent company.','Tel-Tac'),
    ('Nitro Bee Xtreme','Grouped under Rugged Radios.','Rugged Radios'),
    ('RACEceiver / Fusion Plus / Element','RACEceiver brand belongs to Innovative Spectator Products; models are aliases.','RACEceiver'),
    ('RIFE','Motion Raceworks product brand; searchable brand record retained.','RIFE Sensors'),
    ('Proflow','Official VPW Group relationship retained.','Proflow'),
    ('Aeroflow','Official Rocket Industries brand relationship retained.','Aeroflow'),
    ('BRP / Australian Racing Parts at raceparts.com.au','Corrected to Barnier Race Parts; kept separate from Australian Racing Products.','Barnier Race Parts'),
    ('Speedway Spares at speedwayspares.com.au','Grouped under QSS, a Performance Wholesale division.','Queensland Speedway Spares'),
    ('Ian Bochetta','Verified spelling Ian Boettcher Race Parts; old transcript alias retained.','Ian Boettcher Race Parts'),
    ('RaceBase','Computech software, not another manufacturer.','Computech'),
    ('Circle Track App','Wehrs Machine software, not another manufacturer.','Wehrs Machine & Racing Products'),
    ('Whistler','Katech compression-ratio tester; not a generic cranking-compression gauge company.','Katech'),
    ('PCS eight-channel box','Powertrain Control Solutions EGT module in this context.','Powertrain Control Solutions'),
    ('Kestrel','Nielsen-Kellerman product brand.','Kestrel'),
    ('GTR Developments','Historical bleeder brand. Current motorsport website/status unverified; unrelated property-company domain is not used.','GTR Developments'),
    ('Digatron','Motorsport instrument brand/channel, distinct from the unrelated digatron.com battery-testing business.','Digatron'),
    ('Bosch Motorsport Shop Australia','Official shop terms identify Robert Bosch (Australia) Pty Ltd as operator.','Bosch Motorsport Shop Australia'),
]
by_name = {r['name']:r for r in RECORDS}
for old,treatment,name in corrections:
    r=by_name[name]
    links=' · '.join(f'[Role evidence {i}]({url})' for i,url in enumerate(dict.fromkeys(r['classification_sources']),1)) or 'Unverified; qualification retained'
    src.append(f'| {clean(old)} | {clean(treatment)} | {links} |')
src += ['', 'The following are deliberately unresolved: the precise Smiley’s entity intended by every old mention; Speedway Motors Queensland; Clarksons/Clarkso’s versus a possible Clarko’s spelling; the historical Triplex label; M&W setup-block maker attribution; VTAC/VMAC; TPS/Willy Willy; and several OEM leads. Their records retain what is known without filling gaps with a similarly named business.', '', '## Historical source register', '']
for s in SOURCES:
    src += [f'### {s["id"]}', '', f'**{s["title"]}** — {s["dates"]}.', '', s['note']]
    for url in s['urls']:
        src += ['', f'[Pinned source]({url})']
    src += ['']
src += ['## Exclusions', '']
for e in DATA['exclusions']:
    src += [f'### {e["group"]}', '', e['note'], '']
(TARGET / 'SOURCES.md').write_text('\n'.join(src)+'\n')

print(f'Rendered two lists plus index/evidence pages from {len(RECORDS)} canonical records.')
