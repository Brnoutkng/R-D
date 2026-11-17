# RD-007 — RaceCal

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Active season/internal tool** |
| Stage reached | Substantial offline calibration application implemented |
| Kind | internal-tool |
| Repository | [Open development repo](https://github.com/Brnoutkng/SkidLabz-RaceCal) |
| Repository state | Canonical standalone repo; main dated 26 September. Changelog is newer than README version heading. |
| Evidence basis | Repository and undated active-race-season control entry |
| Evidence confidence | high; confidence in this record, not product readiness |
| Evidence date | Individual decision date not established; see dated sources |
| Last reviewed | 2026-11-17 |

## Idea

Focused Windows application to edit, review and export ECU calibrations in practical engineering units.

## Why it is at this status

Active race-season tuning tool. Current effort supports the actual tune, rather than a new broad software product.

## Next useful step

Resolve material tuning workflow problems and verify relevant changes in the real use case.

## What would justify reopening or advancing it

A concrete recurring calibration need or explicit broader-product decision.

## Names and search terms

TuneWorks

## Decisions and boundaries to retain

- Offline calibration; no mandatory dependency on logging.
- Not a universal ROM editor or released general tuning suite.
- Previously dropped one-off wizards and speculative assistants stay closed without a new need.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| 2026-08-02 | TuneWorks renamed RaceCal; logging kept separate and one-off migration/assistant features dropped. |
| 2026-09-26 | Standalone main includes additional implemented/unreleased application work. |

## Recorded implementation decisions

- [DEC-028 — Universal ROM suite or live logging/analysis inside RaceCal](../DECISIONS.md#dec-028)
- [DEC-029 — Map B and map-switching work for the recorded car](../DECISIONS.md#dec-029)
- [DEC-030 — Permanent Trigg migration wizard and open-ended reverse engineering](../DECISIONS.md#dec-030)
- [DEC-031 — Injector sizing assistant](../DECISIONS.md#dec-031)

## Sources

[R_RACECAL](../SOURCES.md#r_racecal), [R_RACECAL_CHANGELOG](../SOURCES.md#r_racecal_changelog), [R_RACECAL_HISTORY](../SOURCES.md#r_racecal_history), [R_CONTROL](../SOURCES.md#r_control)
