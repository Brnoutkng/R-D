# RD-125 — Direct-fire ignition conversion for carburetted engines

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Future option** |
| Stage reached | Owner idea and initial technical comparison; no prototype |
| Kind | product |
| Repository | No dedicated development repo found |
| Repository state | R&D idea only; no dedicated hardware build. |
| Evidence basis | Owner proposal and manufacturer trigger and ignition documentation. |
| Evidence confidence | High for the idea and general trigger distinction; engine compatibility and commercial viability unverified; confidence in this record, not product readiness |
| Evidence date | 2026-11-28 |
| Last reviewed | 2026-11-28 |

## Idea

Retrofit a carburetted engine to use electronically controlled coils instead of distributing spark through the cap and rotor. Consider retaining the distributor as a position sensor or using a dedicated crank trigger.

## Why it is at this status

Feasibility depends on the stock trigger pattern, desired ignition mode and installation requirements. No target engine, architecture or development commitment selected.

## Next useful step

If revisited, select one candidate engine and establish what position and cycle information its stock distributor provides before choosing the trigger and coil architecture.

## What would justify reopening or advancing it

A specific engine family with a practical trigger, coil and harness package and an advantage over existing distributorless conversions.

## Names and search terms

Distributorless ignition conversion, Multi-coil ignition retrofit

## Decisions and boundaries to retain

- Standard distributor pickup compatibility is engine dependent; a simple repeating pulse train does not itself identify the firing cylinder.
- Keep wasted spark and fully sequential direct fire distinct. Sequential ignition needs full engine-cycle position information.
- Related to the programmable carburetted-engine ignition box (RD-124), but not a requirement for that product.
- No development or purchasing implied.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| 2026-11-28 | Owner proposed direct-fire conversion as a separate future option. Keep distributor-based sensing and dedicated crank triggering open. |

## Sources

[C-NOV28-DIRECT-FIRE](../SOURCES.md#c-nov28-direct-fire), [R-HALTECH-TRIGGER-SYNC](../SOURCES.md#r-haltech-trigger-sync), [R-ELECTROMOTIVE-XDI](../SOURCES.md#r-electromotive-xdi)
