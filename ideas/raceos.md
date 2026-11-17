# RD-006 — RaceOS

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Active season/internal tool** |
| Stage reached | Implemented race ECU firmware with partial physical engine-test evidence |
| Kind | internal-tool |
| Repository | [Open development repo](https://github.com/Brnoutkng/SkidLabz-RaceOS) |
| Repository state | Canonical standalone repo; main dated 22 September. Active label comes from a control entry without its own decision date. |
| Evidence basis | Repository, physical test records and cross-project control |
| Evidence confidence | high; confidence in this record, not product readiness |
| Evidence date | Individual decision date not established; see dated sources |
| Last reviewed | 2026-11-17 |

## Idea

Focused engine strategy for the existing race ECU and owner's calibration workflow.

## Why it is at this status

An active race-season tool; accepted hybrid direction retains proven low-level behavior. Further calibration and track evidence remain separate.

## Next useful step

Address real tuning blockers and collect engine/track evidence for the changes actually in use.

## What would justify reopening or advancing it

A measured engine/track problem or explicitly selected requirement, not a general rewrite.

## Names and search terms

RaceOS Hybrid, RaceFuel, RaceSpark

## Decisions and boundaries to retain

- Not a commercially released universal ECU.
- RaceFuel/RaceSpark are strategy modules, not separate hardware products.
- Clean-sheet rewrite and wholesale routine deletion are superseded.
- Passing earlier physical stages does not validate every later calibration.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| 2026-08-11 | Hybrid architecture retained; clean-sheet and mass-deletion paths frozen/superseded. |
| 2026-08-28 | Recorded physical engine-test stages completed; later track validation remains distinct. |

## Recorded implementation decisions

- [DEC-025 — Clean-sheet ECU firmware as the active architecture](../DECISIONS.md#dec-025)
- [DEC-026 — Mass deletion of inherited OSE routines](../DECISIONS.md#dec-026)
- [DEC-027 — Ordinary high-speed UART-style bit-banging on the investigated ECU outputs](../DECISIONS.md#dec-027)

## Sources

[R_RACEOS](../SOURCES.md#r_raceos), [R_RACEOS_ENGINE](../SOURCES.md#r_raceos_engine), [R_ECU_ARCHIVE](../SOURCES.md#r_ecu_archive), [R_CONTROL](../SOURCES.md#r_control)
