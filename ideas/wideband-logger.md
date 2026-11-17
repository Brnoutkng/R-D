# RD-019 — Commercial wideband / analogue race-car logger

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Deprioritised** |
| Stage reached | Use-case and feature investigation; no dedicated commercial development repo |
| Kind | product |
| Repository | No dedicated development repo found |
| Repository state | No dedicated development repository found in the 13 accessible SkidLabz source repositories. |
| Evidence basis | Recovered discussion and direct owner commercial-priority decision |
| Evidence confidence | medium; confidence in this record, not product readiness |
| Evidence date | 2026-11-17 |
| Last reviewed | 2026-11-17 |

## Idea

A simple wideband, RPM and analogue-input logging product for older race cars.

## Why it is at this status

Owner excludes this standalone engine logger from the mainstream shortlist: he considers logging already covered by modern aftermarket ECUs and factory tuning ecosystems, leaving a smaller and shrinking older-carburetted-car niche. This is his commercial judgment, not a measured market-size finding. Earlier scope questions remain unresolved.

## Next useful step

Retain as a deprioritized concept, not a current mainstream product investigation. Do not reopen merely because another older-car logging request is found.

## What would justify reopening or advancing it

Owner identifies a sufficiently broad, underserved paying use case despite ECU/tuning-system logging, followed by a viable simple architecture.

## Decisions and boundaries to retain

- Separate from the existing personal RaceLogger Dev-1 and LogWorks tools.
- Later lambda-plus-RPM recording proposals are related research, not proof this project restarted.
- Expansion, wireless and extra channels are optional scope ideas, not requirements automatically approved for a first product.
- Six configurable analogue logging channels were accepted in the concept; wireless and EGT expansion were optional.
- This decision does not reject all logging products or change personal RaceLogger/LogWorks work.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| 2026-11-17 | Owner removed the standalone engine logger from the mainstream shortlist, citing existing logging in modern aftermarket ECUs and factory tuning ecosystems; he regards the remaining older-carburetted niche as smaller/shrinking. No market-size statistics or universal ECU capabilities were established. |

## Sources

[C-OCT04](../SOURCES.md#c-oct04), [C-NOV15](../SOURCES.md#c-nov15), [R_CONTROL](../SOURCES.md#r_control), [C-NOV17-LOGGER-PRIORITY](../SOURCES.md#c-nov17-logger-priority)
