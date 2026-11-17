# RD-001 — RevMax recall tachometer

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Active development** |
| Stage reached | Working prototype; preproduction and first-batch assembly preparation |
| Kind | product |
| Repository | [Open development repo](https://github.com/Brnoutkng/SkidLabz-RecallTach) |
| Repository state | Dedicated development repo; main status dated 12 November. Later owner discussions update parts and gasket progress. |
| Evidence basis | Repository and recovered owner decisions |
| Evidence confidence | high; confidence in this record, not product readiness |
| Evidence date | 2026-11-17 |
| Last reviewed | 2026-11-17 |

## Idea

Simple battery-powered live and last-run maximum RPM instrument for grassroots Speedway.

## Why it is at this status

Working prototype established. Remaining assembly parts, gasket/sealing and production checks are still being completed.

## Next useful step

Complete assembly parts and gasket, finish manufacturer preview checks, then verify assembled production-intent units.

## What would justify reopening or advancing it

Revisit settled architecture only for a measured fault or materially changed supply/cost evidence.

## Names and search terms

Rev-Max, RecallTach, RPM recall tach

## Decisions and boundaries to retain

- Simple RPM and maximum recall; no app, wireless, logging or dash expansion in V1.
- An upload-ready package does not establish that production boards were ordered.
- Production connector selection is settled; actual mating and assembled fit still require verification.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| 2026-11-02 | Owner reported the prototype coil-negative input working. |
| 2026-11-11 | Production connector route selected and board changes recorded; earlier undecided state superseded. |
| 2026-11-12 | Updated assembly package reached upload-review stage; not production release. |
| 2026-11-17 | Recovered owner discussions show assembly-parts and gasket work continuing. |

## Recorded implementation decisions

- [DEC-001 — Original complex RecallTach architecture](../DECISIONS.md#dec-001)
- [DEC-002 — Earlier OLED, Newhaven graphic LCD and Newhaven TFT display implementations](../DECISIONS.md#dec-002)
- [DEC-003 — Genuine Switchcraft-only production connector supply](../DECISIONS.md#dec-003)
- [DEC-004 — CAZN 2B connector variant](../DECISIONS.md#dec-004)
- [DEC-005 — Old case opening, connector orientation and pre-Q05 stack as current production authority](../DECISIONS.md#dec-005)
- [DEC-041 — OEM/white-label tach sourcing as an automatically approved replacement](../DECISIONS.md#dec-041)
- [DEC-042 — Exposed face stickers and labour-heavy home wet coating](../DECISIONS.md#dec-042)

## Sources

[R_REVMAX_STATUS](../SOURCES.md#r_revmax_status), [R_REVMAX_SCOPE](../SOURCES.md#r_revmax_scope), [R_REVMAX_DECISIONS](../SOURCES.md#r_revmax_decisions), [R_REVMAX_CONNECTOR](../SOURCES.md#r_revmax_connector), [C-NOV13-17](../SOURCES.md#c-nov13-17)
