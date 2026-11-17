# RD-010 — Street Hit companion app and analysis core

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Active as needed** |
| Stage reached | M1 measurement core and real-data ingestion implemented; production app unfinished |
| Kind | companion |
| Repository | [Open development repo](https://github.com/Brnoutkng/SkidLabz-Street-Hit-App) |
| Repository state | Separate companion repository; M1 merged into main on 16 September. |
| Evidence basis | Repository and recovered owner scope correction |
| Evidence confidence | high; confidence in this record, not product readiness |
| Evidence date | 2026-11-04 |
| Last reviewed | 2026-11-17 |

## Idea

Analysis engine and intended phone interface supporting Street Hit Pro performance comparisons.

## Why it is at this status

The comparison/ingestion core exists and is retained as needed. Repeatability still needs physical evidence; wider app work follows the hardware product economics and priority.

## Next useful step

Accept repeated unchanged-pull data when practical, quantify the comparison floor, and maintain the existing analysis core as needed.

## What would justify reopening or advancing it

Relevant real-data evidence or an actual analysis requirement; this work does not require a new hardware order.

## Names and search terms

Street Hit App, SHP software

## Related record

[RD-009 — Street Hit Pro](../ideas/street-hit-pro.md)

## Decisions and boundaries to retain

- Companion to Street Hit Pro, not a separately approved software product.
- No finished mobile UI or direct hardware BLE integration evidenced.
- Synthetic sensitivity results do not establish real-world detection accuracy.
- Older mandatory-three-run scope is superseded; averaging is optional.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| 2026-09-16 | M1 real RaceBox ingestion and measurement characterization merged. |
| 2026-11-04 | Owner clarified that hardware is primary and averaging is an optional capability. |

## Recorded implementation decisions

- [DEC-016 — Making three-run averaging compulsory for the product](../DECISIONS.md#dec-016)

## Sources

[R_STREET_APP](../SOURCES.md#r_street_app), [R_STREET_DATA](../SOURCES.md#r_street_data), [R_CONTROL](../SOURCES.md#r_control), [C-NOV04](../SOURCES.md#c-nov04)
