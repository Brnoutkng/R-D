# Current state

**Register review: 17 November 2026 — Australia/Melbourne**

The catalogue contains **116 entries** and **45 detailed approach decisions**, assembled from **13 accessible development repositories**, relevant branches and recovered chats. The main register has **68 records**; another **48 historical unadopted suggestions** are retained separately. Individual evidence dates vary; this page is a catalogue snapshot, not a statement that every project was checked physically today.

## Main projects and tools

| Item | Where it is at | What matters next |
|---|---|---|
| [RevMax](ideas/revmax.md) | Active preproduction. Working prototype; first-batch assembly preparation continuing. | Remaining assembly parts, gasket/sealing, manufacturer preview checks and assembled production-intent verification. Earlier unresolved connector-selection status is superseded. |
| [Speedway receiver](ideas/receiver.md) | Active R2 development and manufacturing preparation. Chip intake resolved. | Actual assembly checks and physical RF/audio/runtime/mechanical testing. Supply receipt does not establish that the finished receiver works. |
| [Tyre gauge](ideas/tyre-gauge.md) | Investigation and sample assessment. | Identify/test samples and validate an affordable complete-product route. A failed custom sensor route did not reject the whole gauge opportunity. |
| [Street Hit Pro](ideas/street-hit-pro.md) | Hardware developed, paused on manufacturing economics. | A viable finished-product cost and clear hardware baseline before further commitment. The simplified hardware branch is unfinished. |
| [Street Hit App](ideas/street-hit-app.md) | Companion measurement core exists; active as needed. | Accept repeated-pull evidence and maintain the analysis core when useful; this does not require restarting hardware orders. Hardware remains the product's main value; averaging is optional. |
| [PDM](ideas/pdm.md) | Feasibility documented; parked at a go/no-go point. | Owner priority and a viable development plan. It is not recorded as technically impossible or permanently cost-rejected. |
| [Knock Meter](ideas/knock-meter.md) | Lower priority; schematic candidate and research exist. | When resumed: exact controls/assembly fit, sensor/loom sourcing, costing and an actual-instrument prototype proposal. Separate homemade test rigs were rejected. |
| [RaceLogger](ideas/racelogger.md) | Active personal development tool; boards reported received. | Programming, bring-up and complete-system capture validation. Commercialization is a separate future decision. |
| [LogWorks](ideas/logworks.md), [RaceOS](ideas/raceos.md), [RaceCal](ideas/racecal.md) | Active internal race-season tools. | Preserve useful operation and resolve actual tuning/logging problems. Older commit dates do not make these parked products. |
| [FlowCal](ideas/flowcal.md) | Software developed; inactive unless reactivated. | Real injector-bench need and complete physical acceptance. Separate from the proposed digital flow-bench processor. |

## Other decisions that must not be lost

- **[Digital race dash](ideas/digital-race-dash.md):** paused at display sourcing; do not skip ahead to PCB or enclosure design.
- **[Electronic tyre bleeders](ideas/electronic-bleeders.md):** mechanical, valve and cost feasibility remains open; no validated prototype is established.
- **[RaceScales](ideas/race-scales.md):** later commercial rejection supersedes the old “ready to order” entry.
- **[On-engine valve-spring checker](ideas/valve-spring-checker.md):** rejected on competition, limited expected sales and poor commercial case.
- **[SprintTach](ideas/sprinttach-history.md):** historical predecessor to RevMax, not another active tach product.
- **[ECU Development archive](ideas/ecu-archive.md):** retains history and shared project control; the standalone repositories own current technical work.

The complete dispositions and reasons are in [REGISTER.md](REGISTER.md) and [DECISIONS.md](DECISIONS.md). Historical suggestions remain visible without becoming approved projects.

## Evidence still missing or qualified

Current production PCBA order placement, arrival and completed physical testing are not inferred from upload packages, design files or assembly previews. Record those events only when specific evidence is available.

Some chat-only ideas have no separate repo, exact decision date or recovered reason. Their records retain that uncertainty. The available material does not establish that every historical suggestion was accepted or rejected.

Main is not equally current in every source repo: important R2 receiver, Street Hit and historical SprintTach work appears on other branches. Likewise, a global control-file update date does not refresh every embedded project entry. [RECONCILIATION.md](RECONCILIATION.md) records these conflicts and corrections.

## Maintenance

### Competitor references

Two linked lists now preserve the business and brand names recovered from our product discussions: [resellers and distributors](competitors/RESELLERS.md) and [manufacturers and product brands](competitors/MANUFACTURERS.md). The initial recovery contains 207 historical records, including separately labelled software, OEM leads, adjacent markets and unresolved names. It is not a list of 207 verified competitors or approved suppliers.

Use [the competitor index](competitors/README.md) and its source/name-correction notes before repeating a catalogue review. Maker/reseller classification is distinct from the status of a SkidLabz project.

### Updating records

Update the underlying JSON records, preserve existing IDs and decision history, add the evidence source, then run `python scripts/render_register.py`. This register update does not alter any development repository.

Competitor records use `data/competitors.json` and `data/competitor_sources.json`; regenerate their two lists and evidence pages with `python scripts/render_competitors.py`.
