# RD-011 — Standalone motorsport PDM

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Parked — priority / go-no-go** |
| Stage reached | Feasibility and architecture recorded; no schematic, PCB or firmware |
| Kind | product |
| Repository | [Open development repo](https://github.com/Brnoutkng/Skidlabz-PDM) |
| Repository state | Dedicated repo on main; feasibility snapshot 13 October. Older control entry saying no repo is superseded. |
| Evidence basis | Dated repository feasibility and owner deferment context |
| Evidence confidence | high; confidence in this record, not product readiness |
| Evidence date | 2026-10-13 |
| Last reviewed | 2026-11-17 |

## Idea

Protected power distribution and simple switch/sensor logic for older-style race cars.

## Why it is at this status

Explicitly parked at a go/no-go decision point. Paper investigation found no technical show-stopper; this is not a cost rejection or physical validation.

## Next useful step

If promoted, continue with actual floorplan, schematic, exact sourcing/quotes and prototype current/thermal validation.

## What would justify reopening or advancing it

Deliberate owner decision to allocate development effort and accept a viable commercial plan.

## Names and search terms

SkidLabz PDM, Power distribution module

## Decisions and boundaries to retain

- No display required in base PDM.
- Future CAN dash/accessories remain optional, not prerequisites.
- Do not repeat the feasibility investigation or reopen settled connectors without evidence.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| 2026-10-13 | Feasibility completed sufficiently for go/no-go; project parked, not abandoned. |

## Recorded implementation decisions

- [DEC-017 — Starting full engineering automatically after the feasibility study](../DECISIONS.md#dec-017)

## Sources

[R_PDM](../SOURCES.md#r_pdm), [R_PDM_FEASIBILITY](../SOURCES.md#r_pdm_feasibility)
