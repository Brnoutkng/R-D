# RD-002 — Speedway race-control receiver

[Register](../REGISTER.md) · [Research history](../RESEARCH_SUGGESTIONS.md) · [Decisions](../DECISIONS.md)

| Field | Record |
| --- | --- |
| Status | **Active development** |
| Stage reached | R2 board and manufacturing preparation; physical prototype validation pending |
| Kind | product |
| Repository | [Open development repo](https://github.com/Brnoutkng/SkidLabz-SpeedwayReceiver) |
| Repository state | Main is older R1 history. Active R2 evidence is claude/r2-bk4819-carrier at c432c87, dated 12 November. |
| Evidence basis | Repository and recovered owner decisions |
| Evidence confidence | high; confidence in this record, not product readiness |
| Evidence date | 2026-11-12 |
| Last reviewed | 2026-11-17 |

## Idea

Compact rechargeable receive-only race-control radio with physical controls and headphone audio.

## Why it is at this status

R2 replaces the expensive earlier commercial architecture. Chip supply intake is resolved; the finished receiver is not yet physically proven.

## Next useful step

Finish actual assembly-preview checks, build prototypes and test RF/audio, runtime and mounted-display/enclosure fit.

## What would justify reopening or advancing it

Measured failure or loss of a viable low-volume supply path.

## Names and search terms

Race Receiver, R2, BK4819 receiver, R1/P16B/P17

## Decisions and boundaries to retain

- Receive-only; no transmission, telemetry, logging or app.
- Chip receipt proves intake, not authenticity or finished-radio performance.
- Older P16B boards retain test value; do not label them physically worthless.
- Mounted display retained; folded-ribbon arrangements are superseded.

## Decision history

| Date | Decision / evidence |
| --- | --- |
| 2026-11-05 | Owner moved toward lower-cost R2 and domestic chip consignment. |
| 2026-11-12 | R2 requirements record chip receipt into the assembler's parts library. |

## Recorded implementation decisions

- [DEC-006 — Historical BK4802P and ADF7021 RF architectures](../DECISIONS.md#dec-006)
- [DEC-007 — CC1120 R1/P16B/P17 as the current production route](../DECISIONS.md#dec-007)
- [DEC-008 — Permanent ban on BK4819 because it lacked a usable production supply route](../DECISIONS.md#dec-008)
- [DEC-009 — Overseas radio-chip consignment through Australia or an overseas distributor](../DECISIONS.md#dec-009)
- [DEC-010 — Folded-FPC OLED, socketed display connections and portrait layout](../DECISIONS.md#dec-010)

## Sources

[R_RECEIVER_R2_SCOPE](../SOURCES.md#r_receiver_r2_scope), [R_RECEIVER_R2_STATUS](../SOURCES.md#r_receiver_r2_status), [R_RECEIVER_PREVIEW](../SOURCES.md#r_receiver_preview), [C-NOV13-17](../SOURCES.md#c-nov13-17)
