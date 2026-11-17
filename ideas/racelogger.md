# RD-004 — RaceLogger Dev-1

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Active season/internal tool** |
| Stage reached | Personal development hardware received; bring-up and complete-system validation pending |
| Kind | internal-tool |
| Repository | [Open development repo](https://github.com/Brnoutkng/SkidLabz-RaceLogger) |
| Repository state | Main dated 22 September; current Dev-1 package on claude/awesome-turing-wasmtz at e17b089, 3 October. |
| Evidence basis | Repository and recovered owner hardware-arrival report |
| Evidence confidence | high; confidence in this record, not product readiness |
| Evidence date | 2026-11-04 |
| Last reviewed | 2026-11-17 |

## Idea

Capture ECU operating data and direct wideband lambda on a common timebase for the owner's race-car tuning.

## Why it is at this status

Owner simplified the integrated design into a personal Dev-1 tool. Board arrival is reported; physical operation and reliable logging are not yet established.

## Next useful step

Program and bring up received hardware, verify ECU/wideband capture, then reliable storage and PC import.

## What would justify reopening or advancing it

Commercialization only after a useful working logger and explicit owner decision to support it as a product.

## Names and search terms

RaceLogger, Minimal development logger

## Decisions and boundaries to retain

- Current Dev-1 is a personal development tool, not an approved commercial product.
- Preserve the existing TechEdge/LogWorks workflow.
- Reliable capture comes before a new live dashboard.
- RaceCal remains independent of logging.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| 2026-10-01 | Complex integrated architecture parked in favour of minimal personal Dev-1. |
| 2026-10-03 | Dev-1 manufacturing package recorded. |
| 2026-11-04 | Owner reported logger boards arrived; programming/test readiness remained unresolved. |

## Recorded implementation decisions

- [DEC-022 — Complex integrated-PCBA logger as the next build](../DECISIONS.md#dec-022)
- [DEC-023 — New live dashboard before reliable logging](../DECISIONS.md#dec-023)

## Sources

[R_LOGGER_SCOPE](../SOURCES.md#r_logger_scope), [R_LOGGER_DEV1](../SOURCES.md#r_logger_dev1), [R_LOGGER_PACKAGE](../SOURCES.md#r_logger_package), [R_CONTROL](../SOURCES.md#r_control), [L-JOBS](../SOURCES.md#l-jobs)
