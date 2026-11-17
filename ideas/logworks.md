# RD-005 — LogWorks

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Active season/internal tool** |
| Stage reached | Implemented test-day logging and analysis application |
| Kind | internal-tool |
| Repository | [Open development repo](https://github.com/Brnoutkng/SkidLabz-RaceLogger) |
| Repository state | Application lives in apps/LogWorks inside RaceLogger; not a missing standalone repo. |
| Evidence basis | Repository and undated active-race-season control entry |
| Evidence confidence | high; confidence in this record, not product readiness |
| Evidence date | Individual decision date not established; see dated sources |
| Last reviewed | 2026-11-17 |

## Idea

PC logging, download, live display and tuning analysis for the existing wideband workflow.

## Why it is at this status

Existing operational software is retained while new logger hardware is developed; no separate commercial launch decision found.

## Next useful step

Preserve test-day reliability; integrate new logger hardware after its capture format and behavior are proven.

## What would justify reopening or advancing it

A specific operational blocker or validated new logger integration.

## Names and search terms

TechEdge logging and analysis application

## Decisions and boundaries to retain

- Separate from RaceCal; calibration must not depend on logging.
- Existing PC dashboard is distinct from deferred onboard display and proposed commercial dash.
- Historical rules rationale is not a current compliance assessment.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| Date not established | Logging/analysis kept in a separate application from offline calibration. |
| Date not established | Existing TechEdge support retained during RaceLogger development. |

## Recorded implementation decisions

- [DEC-024 — Removing the working TechEdge 3A2 workflow when RaceLogger develops](../DECISIONS.md#dec-024)

## Sources

[R_LOGWORKS](../SOURCES.md#r_logworks), [R_CONTROL](../SOURCES.md#r_control)
