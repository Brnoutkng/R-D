# RD-014 — ECU Development archive and project control

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Superseded / reference** |
| Stage reached | Historical technical archive; cross-project control host retained |
| Kind | infrastructure |
| Repository | [Open development repo](https://github.com/Brnoutkng/SkidLabz-ECU-Development) |
| Repository state | Main control snapshot dated 12 November; historical technical files are not current standalone project authorities. |
| Evidence basis | Repository migration/status records and cross-project control |
| Evidence confidence | high; confidence in this record, not product readiness |
| Evidence date | 2026-11-12 |
| Last reviewed | 2026-11-17 |

## Idea

Original repository containing historical firmware/application work and the shared project-control record.

## Why it is at this status

Technical products now have standalone canonical repos. Retain provenance and control without duplicating their product entries.

## Next useful step

Maintain control and historical references; undertake technical work in the corresponding standalone repos.

## What would justify reopening or advancing it

No new product implied; use only for control/provenance or explicit owner-directed archival work.

## Names and search terms

Original SkidLabz monorepo

## Decisions and boundaries to retain

- Not an additional ECU product.
- Old RaceCal, LogWorks and FlowCal copies must not be counted again.
- Global control-file date does not mean every embedded project status was refreshed.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| 2026-08-11 | Clean-sheet architecture frozen in favour of hybrid development. |
| 2026-09-08 | Standalone repository migrations separate current product authority from monorepo history. |
| 2026-11-12 | Cross-project control file remains hosted here. |

## Recorded implementation decisions

- [DEC-035 — Treating monorepo technical copies as current standalone products or duplicate projects](../DECISIONS.md#dec-035)

## Sources

[R_ECU_ARCHIVE](../SOURCES.md#r_ecu_archive), [R_ECU_CLEANSHEET](../SOURCES.md#r_ecu_cleansheet), [R_FLOWCAL_MIGRATION](../SOURCES.md#r_flowcal_migration), [R_CONTROL](../SOURCES.md#r_control)
