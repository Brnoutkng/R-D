# RD-009 — Street Hit Pro

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Paused — cost** |
| Stage reached | Hardware design and original prototype package exist; cost-rework alternative unfinished |
| Kind | product |
| Repository | [Open development repo](https://github.com/Brnoutkng/SkidLabz-Street-Hit-Pro) |
| Repository state | Main is stale. Original prototype package on claude/rev-a-schematic-bom-yyj68i; separate rev-a-sam-m10q-simplified branch stopped unfinished. |
| Evidence basis | Repository and recovered owner decisions |
| Evidence confidence | high; confidence in this record, not product readiness |
| Evidence date | 2026-11-04 |
| Last reviewed | 2026-11-17 |

## Idea

Hardware-led portable GPS/RPM device for acceleration testing and before/after tuning comparison, with a phone interface.

## Why it is at this status

Manufacturing economics were too close to complete competing devices. The hardware is the product's main value; app progress does not clear its cost hold.

## Next useful step

Recover the intended hardware baseline and establish viable finished-product economics before another prototype commitment.

## What would justify reopening or advancing it

Materially improved complete-product cost/supply path and explicit owner restart.

## Names and search terms

Street Hit, GPS/RPM performance tester

## Decisions and boundaries to retain

- Companion app is not the main commercial proposition.
- Three-run averaging is optional under newer owner direction.
- Unfinished simplified branch is not manufacturing-ready.
- Design files do not prove an ordered or validated physical product.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| 2026-09-15 | Original hardware reached a prototype upload package; simplified integrated-antenna alternative stopped unfinished. |
| 2026-11-04 | Owner reiterated hardware-first value, optional averaging and manufacturing-cost blocker. |

## Recorded implementation decisions

- [DEC-014 — Proceeding with the original hardware economics unchanged](../DECISIONS.md#dec-014)
- [DEC-015 — Treating the SAM-M10Q simplified alternative as fabrication-ready](../DECISIONS.md#dec-015)

## Sources

[R_STREET_SCOPE](../SOURCES.md#r_street_scope), [R_STREET_NEO_PACKAGE](../SOURCES.md#r_street_neo_package), [R_STREET_SAM_LAYOUT](../SOURCES.md#r_street_sam_layout), [R_CONTROL](../SOURCES.md#r_control), [C-NOV04](../SOURCES.md#c-nov04)
