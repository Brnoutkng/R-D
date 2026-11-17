# RD-008 — FlowCal injector-bench software

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Parked — priority / go-no-go** |
| Stage reached | Application and calculation core developed; complete physical bench acceptance not established by this review |
| Kind | internal-tool |
| Repository | [Open development repo](https://github.com/Brnoutkng/SkidLabz-FlowCal) |
| Repository state | Standalone repo established 8 September with UI, calculation core, persistence and tests. |
| Evidence basis | Repository and cross-project control; pause decision individually undated |
| Evidence confidence | high; confidence in this record, not product readiness |
| Evidence date | Individual decision date not established; see dated sources |
| Last reviewed | 2026-11-17 |

## Idea

Record manually measured injector flow and derive flow/dead-time results while retaining raw measurements.

## Why it is at this status

Explicitly inactive unless the owner reactivates it; not rejected on cost or feasibility.

## Next useful step

No automatic new development; on reactivation, verify the Windows workflow and real bench measurements.

## What would justify reopening or advancing it

Explicit owner reactivation for a real injector-bench need.

## Names and search terms

Injector flow and dead-time calculator

## Decisions and boundaries to retain

- Not the separate digital flow-bench processor opportunity.
- Does not automatically control bench hardware or edit ECU calibrations.
- Repository migration and software tests do not establish bench validation.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| 2026-09-08 | Moved to its standalone canonical repository without implying new hardware validation. |
| Date not established | Marked inactive unless owner reactivates; no cost rejection recorded. |

## Recorded implementation decisions

- [DEC-032 — Injector-set matching UI and automatic bench hardware control](../DECISIONS.md#dec-032)

## Sources

[R_FLOWCAL](../SOURCES.md#r_flowcal), [R_FLOWCAL_MIGRATION](../SOURCES.md#r_flowcal_migration), [R_CONTROL](../SOURCES.md#r_control)
