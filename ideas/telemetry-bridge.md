# RD-068 — RaceOS-to-logger telemetry bridge

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Paused — validation** |
| Stage reached | Research/code candidate exists within ECU/RaceOS repos; complete-system proof absent |
| Kind | component |
| Repository | [Open development repo](https://github.com/Brnoutkng/SkidLabz-RaceOS) |
| Repository state | Research/component work within RaceOS and the historical ECU repository; no separate commercial product repo. |
| Evidence basis | Repository research and candidate limits |
| Evidence confidence | high; confidence in this record, not product readiness |
| Evidence date | 2026-09-03 |
| Last reviewed | 2026-11-17 |

## Idea

Read-only ECU data transfer into a separate logger or display.

## Why it is at this status

Basic experiments exist, but the complete candidate was expressly not burn-approved or run in an ECU in its source record.

## Next useful step

Use the existing candidate and evidence if this route is selected; do not confuse simulation or pin tests with end-to-end operation.

## What would justify reopening or advancing it

A selected telemetry baseline and reviewed physical complete-system validation.

## Related record

[RD-004 — RaceLogger Dev-1](../ideas/racelogger.md)

## Sources

[R-TELEMETRY](../SOURCES.md#r-telemetry)
