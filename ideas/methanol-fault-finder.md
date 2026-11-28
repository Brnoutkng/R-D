# RD-122 — Methanol fuel fault-finder

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Investigation / samples** |
| Stage reached | Bench feasibility plan documented; no prototype or test results |
| Kind | product |
| Repository | No dedicated development repo found |
| Repository state | R&D record only; no dedicated development repository or hardware build. |
| Evidence basis | Owner-reported trackside troubleshooting experience and desk feasibility review. |
| Evidence confidence | High for the intended use and purchase decision; performance and demand unverified; confidence in this record, not product readiness |
| Evidence date | 2026-11-28 |
| Last reviewed | 2026-11-28 |

## Idea

A quick electronic check for suspect methanol during race-night fault finding. Compare a capped sample with known-good fuel before chasing ignition or injection faults.

## Why it is at this status

A comparative capacitive measurement is worth a small bench trial, but normal fuel and temperature variation may obscure the signal. No validated water detection limit or in-service engine cutoff has been established.

## Next useful step

Bundle a populated capacitance-sensor breakout, temperature sensor and electrode foil into a future parts order. Use a single fixed sample holder and log repeat readings on a laptop; no separate order or custom hardware for the first trial.

## What would justify reopening or advancing it

Advance only if suspect and fresh samples can be distinguished repeatably despite normal fuel and temperature variation, with a response quick enough for trackside troubleshooting.

## Names and search terms

Methanol moisture tester, Wet methanol checker

## Decisions and boundaries to retain

- Comparison only until validated: not a calibrated water-percentage reading, scrutineering test or safe-to-race decision.
- Capped samples only for bench feasibility; no powered in-tank probe or deliberately contaminated fuel in an engine.
- Keep the working RevMax tester intact. No screen, custom PCB or second sensor channel in the first trial.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| 2026-11-28 | Retained the trackside fault-finder concept. Wait to combine the bench parts with a future order rather than paying separate freight. |

## Sources

[C-NOV28-METHANOL-FAULT-FINDER](../SOURCES.md#c-nov28-methanol-fault-finder), [R-METHANOL-CAP-SENSOR](../SOURCES.md#r-methanol-cap-sensor)
