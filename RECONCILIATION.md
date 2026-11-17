# Corrections and unresolved evidence

Reviewed 17 November 2026, Australia/Melbourne.

This page records the conflicts resolved while building the register. A file's latest commit can update one project while leaving other entries unchanged. The dates and scope of the actual decisions matter more than the global timestamp.

[Register](REGISTER.md) · [Sources](SOURCES.md) · [Detailed decisions](DECISIONS.md)

## Status corrections retained

| Item | Older statement | Evidence retained in this register |
| --- | --- | --- |
| [Valve-spring checker](ideas/valve-spring-checker.md) | Strong maybe | Owner rejected it on 20 October and reaffirmed removal on 27 October: many existing alternatives, limited racer sales and a poor commercial case. [Sources](SOURCES.md#c-oct20) |
| [RaceScales](ideas/race-scales.md) | Ready to order | Later owner statements reject the import and own-pad routes on economics. The 4 November saved job list retains commercial rejection. Later assistant proposals do not constitute reopening. [Sources](SOURCES.md#c-oct20) |
| [PDM](ideas/pdm.md) | No repo; future idea | The PDM repo exists and records completed paper feasibility, parked at a go/no-go point. It is neither a bare new idea nor a demonstrated physical product. [Source](SOURCES.md#r_pdm) |
| [Knock Meter](ideas/knock-meter.md) | Maybe only; or entirely blocked by battery | A dedicated repo and instrument schematic candidate exist. Later controls/fit/cost work is documented. The owner rejected separate homemade rigs; the product itself was not rejected. Current portfolio priority is lower. [Source](SOURCES.md#r_knock_priority) |
| [Receiver](ideas/receiver.md) | R1/CC1120 is current; BK4819 prohibited or supply unresolved | The newer R2 branch records an adopted BK4819 route and parts intake into the assembly library. This resolves that supply step, not RF/audio/runtime or finished-device validation. [Source](SOURCES.md#r_receiver_r2_scope) |
| [RevMax](ideas/revmax.md) | Production connector undecided | CAZN 2C and corresponding case/PCB changes were adopted. Final assembly, sealing/gasket and physical production checks remain; compatibility is not assumed proved. [Source](SOURCES.md#r_revmax_connector) |
| [RaceLogger](ideas/racelogger.md) | No hardware ordered; integrated board is next | Newer minimal Dev-1 work and owner-reported board arrival supersede those statements. Dev-1 is explicitly a personal development tool. The complex integrated design is parked. [Sources](SOURCES.md#r_logger_dev1) |
| [Street Hit Pro](ideas/street-hit-pro.md) | Main has requirements only; app is the product | Hardware branches contain actual design/manufacturing-package work. Owner identifies hardware as the value and manufacturing cost as the hold. The SAM simplification remains unfinished. [Sources](SOURCES.md#c-nov04) |
| [Street Hit App](ideas/street-hit-app.md) | Three-run averaging is compulsory; app work must wait for hardware | Newer owner direction makes averaging optional. The implemented analysis core remains active as needed, and real-data characterisation does not require a hardware order. [Sources](SOURCES.md#c-nov04) |
| [Tyre gauge](ideas/tyre-gauge.md) | Product rejected because the precision sensor route failed | The cost/supply failure belongs to that route. Gauge investigation and sample assessment continue; no candidate has been declared a validated production solution here. [Sources](SOURCES.md#r_tyre_status) |
| [RaceOS](ideas/raceos.md), [RaceCal](ideas/racecal.md), [LogWorks](ideas/logworks.md) | Old commits mean parked | These remain active season/internal tools in the control record. Commit age alone does not change owner priority. [Source](SOURCES.md#r_control) |
| [FlowCal](ideas/flowcal.md) | Another name for the airflow-bench idea | FlowCal is developed injector-flow/dead-time software. The digital flow-bench processor is a separate research opportunity. [Source](SOURCES.md#r_flowcal) |
| [SprintTach](ideas/sprinttach-history.md) | Another current tach product | Historical predecessor and reference material for RevMax. Its branches contain real pilot history, but it is not a second active product. [Source](SOURCES.md#r_sprint_pilot) |

## Where the record remains qualified

The original full 16–17 November brainstorming thread was not returned by the available history search. Secondary recaps identify a retained-total fuel display, fast tyre-temperature capture and renewed brake-tester ideas. These are retained with the evidence limitation. The rod-bolt gauge also has an earlier independent owner nomination.

The newer broad-market temperature, brake-test and scale-reader suggestions do not erase earlier objections to their initial Speedway use cases. Each record preserves both the old decision and the unadopted later scope.

For the transmission controller and EngineGuard, the owner dropping them is established, but a more specific reason was not recovered. For the mechanical-injection tester, Pro-Mag diagnostic tools and magneto timer, deprioritisation is recorded; the access/market rationale is from an assistant recap and is attributed that way.

Prepared board files and assembly previews do not establish an order, and parts receipt does not establish operation. Current production PCBA placement and complete physical qualification are left unconfirmed where no specific evidence was recovered.

The source retrieval also returned unrelated purchases and repairs. These were not converted into product ideas: a bought sensor does not establish an air-ride-controller project, and race-car differential parts do not establish a SkidLabz drivetrain product.

## Future updates

Update the existing idea when new evidence appears. Preserve the old decision, date the new one and explain what changed. An old maybe label, a repeated assistant suggestion or a global file timestamp is not sufficient evidence to reactivate a rejected product.

This narrative is maintained alongside the JSON records. Generated indexes and idea pages are rebuilt with `python scripts/render_register.py`.
