# Current state

**Register review: 17 November 2026 — Australia/Melbourne**

The catalogue contains **126 entries** and **45 detailed approach decisions**, assembled from **13 accessible development repositories**, relevant branches and recovered chats. The main register has **80 records**; another **46 historical unadopted suggestions** are retained separately. Individual evidence dates vary; this page is a catalogue snapshot, not a statement that every project was checked physically today.

## Main projects and tools

| Item | Where it is at | What matters next |
|---|---|---|
| [RevMax](ideas/revmax.md) | Active preproduction. Working prototype; first-batch assembly preparation continuing. | Remaining assembly parts, gasket/sealing, manufacturer preview checks and assembled production-intent verification. Earlier unresolved connector-selection status is superseded. |
| [Speedway receiver](ideas/receiver.md) | Active R2 development and manufacturing preparation. Chip intake resolved. | Actual assembly checks and physical RF/audio/runtime/mechanical testing. Supply receipt does not establish that the finished receiver works. |
| [Tyre gauge](ideas/tyre-gauge.md) | Investigation and sample assessment. | Identify/test samples and validate an affordable complete-product route. A failed custom sensor route did not reject the whole gauge opportunity. |
| [Street Hit Pro](ideas/street-hit-pro.md) | Hardware developed, paused on manufacturing economics. | A viable finished-product cost and clear hardware baseline before further commitment. The simplified hardware branch is unfinished. |
| [Street Hit App](ideas/street-hit-app.md) | Companion measurement core exists; active as needed. | Accept repeated-pull evidence and maintain the analysis core when useful; this does not require restarting hardware orders. Hardware remains the product's main value; averaging is optional. |
| [PDM](ideas/pdm.md) | Feasibility documented; parked at a go/no-go point. | Owner priority and a viable development plan. It is not recorded as technically impossible or permanently cost-rejected. |
| [Knock Meter](ideas/knock-meter.md) | Lower priority due to niche use case and uncertain sales volume; schematic candidate and research exist. | When resumed: exact controls/assembly fit, sensor/loom sourcing, costing and an actual-instrument prototype proposal. Separate homemade test rigs were rejected. |
| [RaceLogger](ideas/racelogger.md) | Active personal development tool; boards reported received. | Programming, bring-up and complete-system capture validation. Commercialization is a separate future decision. |
| [LogWorks](ideas/logworks.md), [RaceOS](ideas/raceos.md), [RaceCal](ideas/racecal.md) | Active internal race-season tools. | Preserve useful operation and resolve actual tuning/logging problems. Older commit dates do not make these parked products. |
| [FlowCal](ideas/flowcal.md) | Software developed; inactive unless reactivated. | Real injector-bench need and complete physical acceptance. Separate from the proposed digital flow-bench processor. |

## New investigation · 28 November 2026

- **[Methanol fuel fault-finder](ideas/methanol-fault-finder.md):** comparative trackside diagnostic. Bench plan documented; wait to bundle parts with another order. No instrument results or engine cutoff established.
- **[Adjustable RPM switch](ideas/adjustable-rpm-switch.md):** idea only. First application and demand are undecided.
- **[Programmable carburetted-engine ignition](ideas/programmable-carb-ignition.md):** future option. Existing boxes already offer onboard MAP and timing tables; no build commitment.
- **[Direct-fire ignition conversion](ideas/direct-fire-conversion.md):** future option. Retained distributor sensing or standalone crank trigger; target engine and ignition mode open.
- **[Carbon-fibre sprintcar throttle bellcrank](ideas/carbon-throttle-bellcrank.md):** owner-used for years; manufacturing was the blocker. New contacts make a small-batch route worth reconsidering.

## Latest owner direction

Mainstream commercial demand takes priority over technical progress alone. The owner prioritizes tech dashes, gauges, tools and pit equipment. The [plug-in SSR](ideas/plug-in-ssr.md) is explicitly deprioritized for now because of competition and perceived viability, retained only as a possible later add-on. The [pit helmet warmer](ideas/pit-helmet-warmer.md) is a new user-proposed research candidate for cool-weather visor fogging, not an approved build. Alternatives, demand, heat/material safety, effectiveness and complete-product economics remain unverified.

## Commercial screening filter

The owner's clarified filter is **reachable demand**, not a requirement for a mass market: a niche is acceptable when buyers strongly want the product and existing choices are expensive, unreliable or unavailable. Prioritize a credible advantage and access to those customers. This clarifies, rather than globally reverses, the individual product decisions below.

Target **at least 100% markup on complete COGS**: net selling revenue of twice complete COGS gives **50% gross margin before other costs**. This is not 100% margin or net profit. Count the complete saleable product, not just its electronics; selling fees, development, overheads and other costs still need allowance. No product's margin is established merely by recording this target.

RevMax's supporting evidence includes the owner's informal pit observations and some expressions of willingness to buy around $400, not a representative survey or confirmed orders. Complete scales remain blocked by pad economics.

## Other decisions that must not be lost

- **[Digital race dash](ideas/digital-race-dash.md):** paused at display sourcing; do not skip ahead to PCB or enclosure design.
- **[Electronic tyre bleeders](ideas/electronic-bleeders.md):** mechanical, valve and cost feasibility remains open; no validated prototype is established.
- **[RaceScales](ideas/race-scales.md):** later commercial rejection supersedes the old “ready to order” entry.
- **[On-engine valve-spring checker](ideas/valve-spring-checker.md):** rejected on competition, limited expected sales and poor commercial case.
- **[SprintTach](ideas/sprinttach-history.md):** historical predecessor to RevMax, not another active tach product.
- **[ECU Development archive](ideas/ecu-archive.md):** retains history and shared project control; the standalone repositories own current technical work.

- **[Standalone engine logger](ideas/wideband-logger.md):** deprioritized by the owner for the mainstream shortlist because existing ECU/tuning-system logging leaves what he views as a smaller older-carburetted niche. Personal RaceLogger/LogWorks scope is unchanged.

The complete dispositions and reasons are in [REGISTER.md](REGISTER.md) and [DECISIONS.md](DECISIONS.md). Historical suggestions remain visible without becoming approved projects.

## Evidence still missing or qualified

Current production PCBA order placement, arrival and completed physical testing are not inferred from upload packages, design files or assembly previews. Record those events only when specific evidence is available.

Some chat-only ideas have no separate repo, exact decision date or recovered reason. Their records retain that uncertainty. The available material does not establish that every historical suggestion was accepted or rejected.

Main is not equally current in every source repo: important R2 receiver, Street Hit and historical SprintTach work appears on other branches. Likewise, a global control-file update date does not refresh every embedded project entry. [RECONCILIATION.md](RECONCILIATION.md) records these conflicts and corrections.

## Maintenance

### Competitor references

Two linked lists now preserve the business and brand names recovered from our product discussions: [resellers and distributors](competitors/RESELLERS.md) and [manufacturers and product brands](competitors/MANUFACTURERS.md). The initial recovery contains 207 historical records, including separately labelled software, OEM leads, adjacent markets and unresolved names. It is not a list of 207 verified competitors or approved suppliers.

Use [the competitor index](competitors/README.md) and its source/name-correction notes before repeating a catalogue review. Maker/reseller classification is distinct from the status of a SkidLabz project.

### Technical research communities

The [forum directory](forums/README.md), reviewed 17 November 2026, contains **78 source locations: 56 forum/support-board locations and 22 Reddit communities**. It includes technical sections, 89 sample discussion/index links, observed evidence dates and access limitations. Eight additional exact Reddit names remain unverified and are listed separately. Inaccessible boards, historical material and the confirmed Zilvia closure are labelled; directory inclusion does not establish current activity.

[Research notes](forums/RESEARCH_NOTES.md) preserve practical problems around simple engine logging, recording reliability, tyre workflows, integration, instrument use and measurement trust. They also link existing decisions, including the torsion-tester validation pause, rejected generic setup app and timing-display economics. This source-directory addition changes no product status or development repository.

### Research investigations

[Forum deep dive 01](research/forum-deep-dive-01/REPORT.md), 17 November 2026, tested product opportunities against HoseHeads, KartPulse, Grassroots Motorsports and Speed-Talk. **No new product cleared the bar and no status changed.** Four ideas received independent desk-research challenges and were set aside on competition, demand, compatibility and estimated economics: an engine-protection warning module, a tyre-gauge checker sold as a product, a load-cell valve-spring force tester and a kart ignition tester. Two items earned cheap follow-up only: new requirements evidence for the existing [tyre gauge](ideas/tyre-gauge.md) investigation, and a narrower comparative version of the paused [torsion-bar tester](ideas/torsion-bar-tester.md), for which a possible lower-cost verification route is proposed but its adequacy and cost remain unestablished. Against the owner's markup target, the report puts the complete-cost ceiling for the tyre gauge at about A$108–109 at the A$250 retail target, conditional on its GST, selling-fee and complete-COGS assumptions. Evidence quality differs by forum: Grassroots Motorsports was read through search summaries only and HoseHeads was mostly unreadable. The [evidence file](research/forum-deep-dive-01/EVIDENCE.md) holds the thread ledger, prices and register links; the [research index](research/README.md) lists investigations.

The same pass corrected the forum directory: HoseHeads has moved platform and its three sample links were updated to current addresses.

A subsequent [independent review](research/forum-deep-dive-01/REVIEW.md) confirmed several competitor listings, corrected the US$16 warning-kit comparison, and identified qualifications in the unquoted labour, payback and torsion claims. The desk model is a screening scenario, not measured production performance. Existing product dispositions are preserved.

### Updating records

Update the underlying JSON records, preserve existing IDs and decision history, add the evidence source, then run `python scripts/render_register.py`. This register update does not alter any development repository.

Competitor records use `data/competitors.json` and `data/competitor_sources.json`; regenerate their two lists and evidence pages with `python scripts/render_competitors.py`.

Technical community records use `data/forums.json`; regenerate the directory with `python scripts/render_forums.py`. Maintain `forums/RESEARCH_NOTES.md` as the separate, sourced interpretation.








