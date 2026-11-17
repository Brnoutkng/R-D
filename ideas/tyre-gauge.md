# RD-003 — Precision motorsport tyre-pressure gauge

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Investigation / samples** |
| Stage reached | Dedicated repo; transducer and donor-gauge sample assessment; complete-product route not yet validated |
| Kind | product |
| Repository | [Open development repo](https://github.com/Brnoutkng/SkidLabz-TyreGauge) |
| Repository state | Dedicated repo; latest handover 20 October. Sample identity/testing still unconfirmed in that record. |
| Evidence basis | Repository and cross-project control; newer owner status still needed |
| Evidence confidence | high; confidence in this record, not product readiness |
| Evidence date | 2026-11-08 |
| Last reviewed | 2026-11-17 |

## Idea

Handheld low-pressure digital gauge focused on stable, repeatable measurement and manual bleed.

## Why it is at this status

One custom precision-sensor route failed cost/supply economics. The complete product remains open, with samples and an OEM route needing verification.

## Next useful step

Identify and test received transducers, and evaluate any complete OEM candidate against actual low-pressure performance and landed economics.

## What would justify reopening or advancing it

A verified low-quantity measurement/source route meeting both accuracy and cost requirements.

## Names and search terms

TyreGauge, Digital tyre gauge

## Decisions and boundaries to retain

- Product is not rejected merely because one sensor route failed.
- Display resolution is not measurement accuracy.
- No app, cloud, tyre-temperature or session-logging burden in V1.
- Newer sample/testing updates supersede blanket no-samples wording; exact present sample inventory and full performance are not established by this review.
- Owner's target is genuine accuracy and repeatability at approximately A$250 retail or less, materially better than cheap gauges; this is a target, not a validated achievable specification.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| 2026-10-06 | OEM/private-label-first investigation reopened in project control. |
| 2026-10-20 | Handover reports sample transducers believed arrived, with identity and tests unresolved. |
| 2026-11-17 | Owner explained the firsthand motivation: his approximately 15–16-year-old Intercomp had been exceptionally accurate in his experience, but began zero drifting in cold, damp racing conditions. A replacement around A$960–980 felt unjustifiable. A roughly A$250 Longacre disappointed him and appeared similar to inexpensive Chinese digital gauges, including foam packing. These are owner-reported experiences and price recollections, not controlled accuracy comparisons or verified current quotations. |
| 2026-11-17 | After inspecting the Intercomp, the owner perceived its electronics as inexpensive-looking and wants genuine accuracy and repeatability around or below A$250 retail. Appearance is not measured BOM cost, and the Longacre accuracy impression has not been independently verified. This motivation does not change sample-testing or project status. |

## Recorded implementation decisions

- [DEC-011 — Custom direct-thread precision sensor route at the investigated cost and supply terms](../DECISIONS.md#dec-011)
- [DEC-012 — Internal barbed sensor/tube stack or custom machined manifold as the automatic V1 default](../DECISIONS.md#dec-012)
- [DEC-013 — Bluetooth/app/cloud, tyre-temperature and logging features in simple V1](../DECISIONS.md#dec-013)
- [DEC-040 — Large industrial bleed valves or expensive imported bare cartridges](../DECISIONS.md#dec-040)

## Sources

[R_TYRE_STATUS](../SOURCES.md#r_tyre_status), [R_TYRE_COST_GATE](../SOURCES.md#r_tyre_cost_gate), [R_TYRE_SCOPE](../SOURCES.md#r_tyre_scope), [R_CONTROL](../SOURCES.md#r_control), [C-NOV08](../SOURCES.md#c-nov08), [C-NOV17-TYRE-MOTIVATION](../SOURCES.md#c-nov17-tyre-motivation)
