# RD-012 — Portable Knock Meter

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Parked — priority / go-no-go** |
| Stage reached | Actual-instrument schematic candidate and research exist; no routed/released PCB |
| Kind | product |
| Repository | [Open development repo](https://github.com/Brnoutkng/SkidLabz-KnockMeter) |
| Repository state | Dedicated repo; latest engineering/owner guidance 27 October. Schematic exists, but layout/order release does not. |
| Evidence basis | Repository and direct owner commercial-priority clarification |
| Evidence confidence | high; confidence in this record, not product readiness |
| Evidence date | 2026-11-17 |
| Last reviewed | 2026-11-17 |

## Idea

Portable knock-listening and LED indication instrument with independent volume and sensitivity controls.

## Why it is at this status

Lower current priority because the owner sees a niche use case and uncertain sales volume, rather than electronics complexity or making cost as the main barrier. Sourcing, fit and release checks also remain; the product itself was not rejected.

## Next useful step

On reactivation, complete exact controls/assembly fit, sensor/loom sourcing and costed actual-instrument prototype proposal.

## What would justify reopening or advancing it

Owner promotes it after a convincing customer/use-case and commercial-demand case, with practical fit/cost/sourcing checks retained.

## Names and search terms

KnockMeter, Knockometer, Standalone knock monitor, Filtered knock listener

## Decisions and boundaries to retain

- Monitor/listen only; no ignition control or validated engine-protection claim.
- Separate owner-built test rigs were rejected.
- Battery data is a parallel release dependency, not a reason to stop unrelated work.
- Offline replay and schematic checks are not physical knock-detection validation.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| 2026-10-25 | Owner rejected additional homemade test rigs; continue toward actual assembled instrument. |
| 2026-10-27 | Continue controls, connectors and real fit; battery work remains bounded and parallel. |
| Date not established | Subsequent owner priority places the project below current products; no permanent rejection. |
| 2026-11-17 | Owner clarified that mainstream commercially viable products come first; KnockMeter is relatively simple to make but its use case and likely sales volume are the concern. |

## Recorded implementation decisions

- [DEC-018 — Separate owner-built Prototype 0A/0B test rigs](../DECISIONS.md#dec-018)
- [DEC-019 — Automatic ignition control, engine-protection promises and broad connected/logging features](../DECISIONS.md#dec-019)
- [DEC-020 — Analogue selectable-filter and precision-rectifier baseline](../DECISIONS.md#dec-020)
- [DEC-021 — Boost-supply architecture](../DECISIONS.md#dec-021)

## Sources

[R_KNOCK_STATUS](../SOURCES.md#r_knock_status), [R_KNOCK_PRIORITY](../SOURCES.md#r_knock_priority), [R_KNOCK_CONTROLS](../SOURCES.md#r_knock_controls), [L-JOBS](../SOURCES.md#l-jobs), [C-NOV17-PRIORITY](../SOURCES.md#c-nov17-priority)
