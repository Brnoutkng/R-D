# Sources and coverage

Review date: 17 November 2026, Australia/Melbourne. This is an evidence-based historical catalogue, not a new engineering validation or a live supplier/stock audit.

## What was reviewed

- All 13 accessible existing SkidLabz project repositories, plus the R-D destination.
- Recursive default-branch trees and branch inventories; materially newer or different development branches were followed.
- 154 relevant repository planning, product, status, research, decision and historical documents across the three review groups.
- Recovered chat excerpts from the available history, including explicit owner decisions and earlier assistant suggestions.
- Two saved Markdown product/job lists read in full; additional saved-source excerpts where returned by historical retrieval.

## Limits

- This is not an exhaustive export/read of every conversation, deleted branch, issue or PR. The full latest 16–17 November brainstorm was not retrievable; affected records say so.
- The source search returned no durable conversation URLs. Chat sources are identified by date/topic and evidence type; none of the tool-local result labels are presented as real links.
- A global control-file update date does not date every contained project decision. Specific owner decisions and newer project evidence can supersede stale entries.
- Private development sources remain in their original repositories. This public register records general concepts and decisions; detailed engineering, negotiated prices, order/payment/contact data and raw source dumps are not copied.
- Evidence confidence is about the historical record. It is not a claim of electrical, mechanical, regulatory or commercial qualification.
- Commit snapshot dates below are GitHub UTC dates. Dates explicitly written in source documents are preserved as written; the review date uses Melbourne time.

## Repository snapshots

| Repository | Main snapshot | Source date (UTC) | Role |
| --- | --- | --- | --- |
| [SkidLabz-RecallTach](https://github.com/Brnoutkng/SkidLabz-RecallTach) | [692b0c63](https://github.com/Brnoutkng/SkidLabz-RecallTach/tree/692b0c63cbef3bc12e607dc93f097831f77fb875) | 2026-11-12 | Current RevMax development and production preparation |
| [SkidLabz-SpeedwayReceiver](https://github.com/Brnoutkng/SkidLabz-SpeedwayReceiver) | [31a4d1ee](https://github.com/Brnoutkng/SkidLabz-SpeedwayReceiver/tree/31a4d1eeeeb7f0ac42b5412249a66eff2172189d) | 2026-11-02 | Receiver development; main retains older R1 history |
| [SkidLabz-RaceLogger](https://github.com/Brnoutkng/SkidLabz-RaceLogger) | [8e39b18e](https://github.com/Brnoutkng/SkidLabz-RaceLogger/tree/8e39b18ebf1b6e1c363713411570802eb71fe040) | 2026-09-22 | Personal logger development and canonical LogWorks application |
| [SkidLabz-TyreGauge](https://github.com/Brnoutkng/SkidLabz-TyreGauge) | [fe759122](https://github.com/Brnoutkng/SkidLabz-TyreGauge/tree/fe75912285a8cd8673b403b2005528b4d5bfa257) | 2026-10-20 | Precision gauge investigation and sensor/sample evidence |
| [SkidLabz-RaceOS](https://github.com/Brnoutkng/SkidLabz-RaceOS) | [f35b4782](https://github.com/Brnoutkng/SkidLabz-RaceOS/tree/f35b4782cf52d0f3c6175e10e0725101eef9080c) | 2026-09-22 | Canonical race ECU firmware |
| [SkidLabz-RaceCal](https://github.com/Brnoutkng/SkidLabz-RaceCal) | [99caa328](https://github.com/Brnoutkng/SkidLabz-RaceCal/tree/99caa3280ce258d828923e0b2811ec3190851bf5) | 2026-09-26 | Canonical offline tuning application |
| [SkidLabz-FlowCal](https://github.com/Brnoutkng/SkidLabz-FlowCal) | [6aa0fd8d](https://github.com/Brnoutkng/SkidLabz-FlowCal/tree/6aa0fd8d321fb8a2d666015ac69675ba7de6a3b6) | 2026-09-08 | Standalone injector-bench application; inactive unless reactivated |
| [SkidLabz-Street-Hit-Pro](https://github.com/Brnoutkng/SkidLabz-Street-Hit-Pro) | [870444df](https://github.com/Brnoutkng/SkidLabz-Street-Hit-Pro/tree/870444df8ace530f1db4a19f12c6696e4a13b055) | 2026-09-14 | Hardware product; main is stale relative to historical implementation branches |
| [SkidLabz-Street-Hit-App](https://github.com/Brnoutkng/SkidLabz-Street-Hit-App) | [d831ab01](https://github.com/Brnoutkng/SkidLabz-Street-Hit-App/tree/d831ab01ca5e34ebe90b8b1102f5036eed79281f) | 2026-09-16 | Companion measurement/analysis engine; not independent commercial product |
| [Skidlabz-PDM](https://github.com/Brnoutkng/Skidlabz-PDM) | [1f1f5969](https://github.com/Brnoutkng/Skidlabz-PDM/tree/1f1f5969c49bd968aabcb7fa5c34fffc4e1a75f8) | 2026-10-13 | Parked PDM feasibility/architecture record |
| [SkidLabz-KnockMeter](https://github.com/Brnoutkng/SkidLabz-KnockMeter) | [734f13a2](https://github.com/Brnoutkng/SkidLabz-KnockMeter/tree/734f13a260ceda82c307945538f1c2f641ce4dde) | 2026-10-26 | Instrument schematic candidate and research; latest notes dated 27 October Melbourne |
| [SkidLabz-SprintTach](https://github.com/Brnoutkng/SkidLabz-SprintTach) | [b434cb3e](https://github.com/Brnoutkng/SkidLabz-SprintTach/tree/b434cb3ebe15b130900a18362d1c31acd34502ee) | 2026-09-16 | Historical recall-tach predecessor and decision evidence |
| [SkidLabz-ECU-Development](https://github.com/Brnoutkng/SkidLabz-ECU-Development) | [a3744142](https://github.com/Brnoutkng/SkidLabz-ECU-Development/tree/a37441426a518616c0cd13791518f99fda0fda41) | 2026-11-12 | Historical monorepo and cross-project control host |

### Additional branch evidence

- **SkidLabz-SpeedwayReceiver / claude/r2-bk4819-carrier** — [c432c87d](https://github.com/Brnoutkng/SkidLabz-SpeedwayReceiver/tree/c432c87d76d46302f8d173bc4bb7e9f9db02ba36): Materially newer R2 requirements, board and manufacturing preparation.
- **SkidLabz-RaceLogger / claude/awesome-turing-wasmtz** — [e17b089e](https://github.com/Brnoutkng/SkidLabz-RaceLogger/tree/e17b089e9e15371a708dfe70c33cae337da74d96): Current minimal Dev-1 architecture and manufacturing package.
- **SkidLabz-RaceLogger / claude/racelogger-integrated-pcba-8b92qf** — [6bf5fd5a](https://github.com/Brnoutkng/SkidLabz-RaceLogger/tree/6bf5fd5ac33e0e2c6e447dabf1660684aa458a04): Parked complex integrated hardware route.
- **SkidLabz-RaceOS / telemetry** — [79409d30](https://github.com/Brnoutkng/SkidLabz-RaceOS/tree/79409d30c1106f31956a5e392cb4d2047c58d426): Historical candidate research; not evidence of complete physical validation or engine release.
- **SkidLabz-Street-Hit-Pro / claude/rev-a-schematic-bom-yyj68i** — [1d0aad25](https://github.com/Brnoutkng/SkidLabz-Street-Hit-Pro/tree/1d0aad25d196f594766457702179e3709f2cea58): Original hardware prototype manufacturing package.
- **SkidLabz-Street-Hit-Pro / rev-a-sam-m10q-simplified** — [2ce320a3](https://github.com/Brnoutkng/SkidLabz-Street-Hit-Pro/tree/2ce320a30b13b4340568e2bcb8ce303e2c1aaa41): Stopped unfinished simplification; not manufacturing-released.
- **SkidLabz-KnockMeter / claude/trusting-gates-1sxei7** — [0f6504c0](https://github.com/Brnoutkng/SkidLabz-KnockMeter/tree/0f6504c0346273190699b7d9663cc2324501f35c): Older candidate; main's later controls/case/owner notes supersede it.
- **SkidLabz-SprintTach / claude/pilot-build-5-units** — [a883eea8](https://github.com/Brnoutkng/SkidLabz-SprintTach/tree/a883eea8de5ac265a3d52d502db9cd8c112df785): Historical segmented-display pilot.
- **SkidLabz-SprintTach / claude/sprint-tach-recovery-cai1n4** — [020ede87](https://github.com/Brnoutkng/SkidLabz-SprintTach/tree/020ede87811b333aba83378fb526033caf682c08): Historical firmware/recovery and sourcing work.
- **SkidLabz-SprintTach / claude/tft-tacho-prototype-v1** — [f58b3cdf](https://github.com/Brnoutkng/SkidLabz-SprintTach/tree/f58b3cdfb9900cb17b1e0d4e17723f32088ed2ef): Historical TFT prototype and retained pilot/display decisions; not current RevMax.
- **SkidLabz-ECU-Development / claude/raceos-esp32-telemetry-investigation-goylsg** — [d5b45f8b](https://github.com/Brnoutkng/SkidLabz-ECU-Development/tree/d5b45f8b80abb223ed062dae374cf1d6ca135f92): Historical telemetry investigation; successive candidates are not complete-system validation.

## Source catalogue

### R_CONTROL

**Cross-project control record**

Type: repository. Source date: 2026-11-12.

[Open source](https://github.com/Brnoutkng/SkidLabz-ECU-Development/blob/a37441426a518616c0cd13791518f99fda0fda41/SKIDLABZ_PROJECT_CONTROL.yaml)

Global snapshot date; many individual statuses are undated or stale. Newer specific owner and repository evidence takes precedence.

### R_REVMAX_STATUS

**RevMax production-preparation status**

Type: repository. Source date: 2026-11-12.

[Open source](https://github.com/Brnoutkng/SkidLabz-RecallTach/blob/692b0c63cbef3bc12e607dc93f097831f77fb875/CURRENT_STATUS.md)

Dated repository checkpoint; later assembly-parts and gasket updates come from recovered owner discussions.

### R_REVMAX_SCOPE

**RevMax product requirements**

Type: repository. Source date: not individually established.

[Open source](https://github.com/Brnoutkng/SkidLabz-RecallTach/blob/692b0c63cbef3bc12e607dc93f097831f77fb875/PRODUCT_REQUIREMENTS.md)

Pinned scope; snapshot taken from 12 November main. No production-validation claim.

### R_REVMAX_DECISIONS

**RevMax product and commercial decisions**

Type: repository. Source date: 2026-10-13.

[Open source](https://github.com/Brnoutkng/SkidLabz-RecallTach/blob/692b0c63cbef3bc12e607dc93f097831f77fb875/REVMAX_PRODUCT_DECISIONS.md)

Retained product boundaries; subsequent sourcing changes are recorded elsewhere.

### R_REVMAX_CONNECTOR

**RevMax production connector adoption**

Type: repository. Source date: 2026-11-11.

[Open source](https://github.com/Brnoutkng/SkidLabz-RecallTach/blob/692b0c63cbef3bc12e607dc93f097831f77fb875/engineering/REVMAX_CAZN_SOCKET_2026-11-11.md)

Supersedes the earlier undecided-connector state; physical production fit/mating checks remain distinct.

### R_RECEIVER_R2_SCOPE

**R2 receiver requirements and chip intake**

Type: repository. Source date: 2026-11-12.

[Open source](https://github.com/Brnoutkng/SkidLabz-SpeedwayReceiver/blob/c432c87d76d46302f8d173bc4bb7e9f9db02ba36/PRODUCT_REQUIREMENTS.md)

Active R2 branch; supply intake resolved. Chip receipt does not establish radio or assembled-product performance.

### R_RECEIVER_R2_STATUS

**R2 development and manufacturing-preparation record**

Type: repository. Source date: not individually established.

[Open source](https://github.com/Brnoutkng/SkidLabz-SpeedwayReceiver/blob/c432c87d76d46302f8d173bc4bb7e9f9db02ba36/R2_BRANCH_STATUS.md)

Pinned 12 November branch snapshot contains older dated sections; read with updated requirements.

### R_RECEIVER_PREVIEW

**R2 assembly-preview notes**

Type: repository. Source date: 2026-11-07.

[Open source](https://github.com/Brnoutkng/SkidLabz-SpeedwayReceiver/blob/c432c87d76d46302f8d173bc4bb7e9f9db02ba36/manufacturing/R2_A0_2/JLC_ORDER_NOTES.md)

Preparation and preview evidence, not evidence that an assembled R2 was ordered or tested.

### R_TYRE_STATUS

**Tyre gauge handover and sample state**

Type: repository. Source date: 2026-10-20.

[Open source](https://github.com/Brnoutkng/SkidLabz-TyreGauge/blob/fe75912285a8cd8673b403b2005528b4d5bfa257/CURRENT_STATUS.md)

Samples believed received; exact identification and testing not verified.

### R_TYRE_COST_GATE

**Tyre gauge packaged-sensor cost gate**

Type: repository. Source date: not individually established.

[Open source](https://github.com/Brnoutkng/SkidLabz-TyreGauge/blob/fe75912285a8cd8673b403b2005528b4d5bfa257/docs/PACKAGED_TRANSDUCER_SCREEN_A0.md)

A custom precision-sensor route failed economics; this does not reject the complete product opportunity.

### R_TYRE_SCOPE

**Precision tyre gauge scope**

Type: repository. Source date: not individually established.

[Open source](https://github.com/Brnoutkng/SkidLabz-TyreGauge/blob/fe75912285a8cd8673b403b2005528b4d5bfa257/README.md)

Pinned main snapshot; measurement accuracy and viable supply are open.

### R_LOGGER_SCOPE

**RaceLogger scope and validation limits**

Type: repository. Source date: 2026-09-22.

[Open source](https://github.com/Brnoutkng/SkidLabz-RaceLogger/blob/8e39b18ebf1b6e1c363713411570802eb71fe040/README.md)

Main snapshot; newer Dev-1 branch and owner hardware-arrival evidence supersede old physical-status statements.

### R_LOGGER_DEV1

**Minimal Dev-1 personal logger decision**

Type: repository. Source date: 2026-10-01.

[Open source](https://github.com/Brnoutkng/SkidLabz-RaceLogger/blob/e17b089e9e15371a708dfe70c33cae337da74d96/hardware/dev1-minimal/DEV1_ARCHITECTURE.md)

Owner's personal development logger; previous integrated design parked, no commercial release implied.

### R_LOGGER_PACKAGE

**Dev-1 manufacturing package**

Type: repository. Source date: 2026-10-03.

[Open source](https://github.com/Brnoutkng/SkidLabz-RaceLogger/blob/e17b089e9e15371a708dfe70c33cae337da74d96/hardware/dev1-minimal/manufacturing/jlc_dev1/JLC_MANUFACTURING_REVIEW.md)

Manufacturing preparation is established; later board receipt is owner-reported.

### R_LOGWORKS

**LogWorks application and test-day workflow**

Type: repository. Source date: 2026-09-22.

[Open source](https://github.com/Brnoutkng/SkidLabz-RaceLogger/blob/8e39b18ebf1b6e1c363713411570802eb71fe040/apps/LogWorks/README.md)

Existing application in RaceLogger; historical competition-rule rationale is not a fresh rules-compliance finding.

### R_RACEOS

**Canonical RaceOS firmware**

Type: repository. Source date: 2026-09-22.

[Open source](https://github.com/Brnoutkng/SkidLabz-RaceOS/blob/f35b4782cf52d0f3c6175e10e0725101eef9080c/README.md)

Implemented internal race-season firmware; no general commercial ECU release inferred.

### R_RACEOS_ENGINE

**RaceOS physical engine-test evidence**

Type: repository. Source date: not individually established.

[Open source](https://github.com/Brnoutkng/SkidLabz-RaceOS/blob/f35b4782cf52d0f3c6175e10e0725101eef9080c/firmware/RaceOS-Hybrid/docs/H081_CAR_TEST_DAY_PACKAGE_REPORT.txt)

Reports physical stages on 26/28 August; does not establish complete race/track validation of later calibrations.

### R_RACECAL

**RaceCal offline calibration application**

Type: repository. Source date: not individually established.

[Open source](https://github.com/Brnoutkng/SkidLabz-RaceCal/blob/99caa3280ce258d828923e0b2811ec3190851bf5/README.md)

README version header is older than the changelog; use together.

### R_RACECAL_CHANGELOG

**RaceCal implemented and unreleased changes**

Type: repository. Source date: 2026-09-26.

[Open source](https://github.com/Brnoutkng/SkidLabz-RaceCal/blob/99caa3280ce258d828923e0b2811ec3190851bf5/CHANGELOG.md)

Main snapshot includes later unreleased application work.

### R_RACECAL_HISTORY

**RaceCal naming, scope and dropped-feature history**

Type: repository. Source date: not individually established.

[Open source](https://github.com/Brnoutkng/SkidLabz-RaceCal/blob/99caa3280ce258d828923e0b2811ec3190851bf5/docs/RACECAL_PROJECT_SUMMARY.md)

Historical summary records dated August decisions; later implementation state comes from canonical sources.

### R_FLOWCAL

**FlowCal injector-bench application**

Type: repository. Source date: 2026-09-08.

[Open source](https://github.com/Brnoutkng/SkidLabz-FlowCal/blob/6aa0fd8d321fb8a2d666015ac69675ba7de6a3b6/README.md)

Software exists; owner reactivation and actual bench validation remain distinct.

### R_FLOWCAL_MIGRATION

**FlowCal standalone-repository provenance**

Type: repository. Source date: 2026-09-08.

[Open source](https://github.com/Brnoutkng/SkidLabz-FlowCal/blob/6aa0fd8d321fb8a2d666015ac69675ba7de6a3b6/MIGRATION_PROVENANCE.md)

Repository extraction did not establish hardware/bench validation.

### R_STREET_SCOPE

**Street Hit Pro hardware scope**

Type: repository. Source date: 2026-09-14.

[Open source](https://github.com/Brnoutkng/SkidLabz-Street-Hit-Pro/blob/870444df8ace530f1db4a19f12c6696e4a13b055/README.md)

Main is stale relative to hardware branches. Newer owner decisions make hardware primary and averaging optional.

### R_STREET_NEO_PACKAGE

**Street Hit original prototype manufacturing package**

Type: repository. Source date: 2026-09-15.

[Open source](https://github.com/Brnoutkng/SkidLabz-Street-Hit-Pro/blob/1d0aad25d196f594766457702179e3709f2cea58/hardware/manufacturing/rev-a/README.md)

Prototype design package on historical branch; no physical product qualification inferred.

### R_STREET_SAM_LAYOUT

**Street Hit simplified hardware checkpoint**

Type: repository. Source date: 2026-09-15.

[Open source](https://github.com/Brnoutkng/SkidLabz-Street-Hit-Pro/blob/2ce320a30b13b4340568e2bcb8ce303e2c1aaa41/hardware/REV_A_LAYOUT_NOTES.md)

Unfinished alternative with outstanding routing/errors; not fabrication released.

### R_STREET_APP

**Street Hit analysis core M1**

Type: repository. Source date: 2026-09-16.

[Open source](https://github.com/Brnoutkng/SkidLabz-Street-Hit-App/blob/d831ab01ca5e34ebe90b8b1102f5036eed79281f/README.md)

Real RaceBox ingestion exists; production UI and real-world repeatability verdicts do not.

### R_STREET_DATA

**Street Hit repeated-pull evidence gate**

Type: repository. Source date: 2026-09-16.

[Open source](https://github.com/Brnoutkng/SkidLabz-Street-Hit-App/blob/d831ab01ca5e34ebe90b8b1102f5036eed79281f/docs/RACEBOX_DATA_REQUEST.md)

Repeated unchanged pulls needed to establish real-world comparison limits; mandatory averaging language is superseded by newer owner direction.

### R_PDM

**PDM feasibility, parked state and resume point**

Type: repository. Source date: 2026-10-13.

[Open source](https://github.com/Brnoutkng/Skidlabz-PDM/blob/1f1f5969c49bd968aabcb7fa5c34fffc4e1a75f8/README.md)

Explicitly parked at go/no-go, not abandoned; no schematic or PCB.

### R_PDM_FEASIBILITY

**PDM feasibility and commercial drivers**

Type: repository. Source date: 2026-10-13.

[Open source](https://github.com/Brnoutkng/Skidlabz-PDM/blob/1f1f5969c49bd968aabcb7fa5c34fffc4e1a75f8/docs/feasibility-and-cogs-2026-10-13.md)

Desk feasibility and estimates only; no physical high-current/thermal validation or quote.

### R_KNOCK_STATUS

**Knock Meter engineering candidate status**

Type: repository. Source date: not individually established.

[Open source](https://github.com/Brnoutkng/SkidLabz-KnockMeter/blob/734f13a260ceda82c307945538f1c2f641ce4dde/docs/PROJECT_STATUS.md)

Contains updates through 26 October; newest owner priority and controls notes supersede older workflow language.

### R_KNOCK_PRIORITY

**Knock Meter latest owner direction**

Type: repository. Source date: 2026-10-27.

[Open source](https://github.com/Brnoutkng/SkidLabz-KnockMeter/blob/734f13a260ceda82c307945538f1c2f641ce4dde/CLAUDE.md)

No separate owner-built test rigs. Battery is a parallel release dependency, not blanket stop.

### R_KNOCK_CONTROLS

**Knock Meter controls and assembly-fit study**

Type: repository. Source date: 2026-10-27.

[Open source](https://github.com/Brnoutkng/SkidLabz-KnockMeter/blob/734f13a260ceda82c307945538f1c2f641ce4dde/docs/engineering/FRONT_CONTROLS_SOURCING_AND_FIT_2026-10-27.md)

Exact controls/footprints, assembly availability and fit remain current engineering work; no layout/order release.

### R_SPRINT_SCOPE

**SprintTach historical requirements baseline**

Type: repository. Source date: 2026-09-16.

[Open source](https://github.com/Brnoutkng/SkidLabz-SprintTach/blob/b434cb3ebe15b130900a18362d1c31acd34502ee/README.md)

Main understates later historical branch work. Product superseded by current RecallTach/RevMax.

### R_SPRINT_PILOT

**SprintTach historical pilot production record**

Type: repository. Source date: not individually established.

[Open source](https://github.com/Brnoutkng/SkidLabz-SprintTach/blob/f58b3cdfb9900cb17b1e0d4e17723f32088ed2ef/hardware/compact-v1/PRODUCTION-STATUS.md)

Records a small pilot in production; exact order date not recorded. Does not qualify current RevMax.

### R_SPRINT_DISPLAYS

**SprintTach historical display decisions**

Type: repository. Source date: not individually established.

[Open source](https://github.com/Brnoutkng/SkidLabz-SprintTach/blob/f58b3cdfb9900cb17b1e0d4e17723f32088ed2ef/hardware/rev2-sourcing/LCD-CANDIDATES.md)

Retains production-supply/readability rejections and unselected candidates; historical, not current RevMax sourcing.

### R_ECU_ARCHIVE

**ECU archive and hybrid-architecture decision**

Type: repository. Source date: 2026-08-11.

[Open source](https://github.com/Brnoutkng/SkidLabz-ECU-Development/blob/a37441426a518616c0cd13791518f99fda0fda41/docs/PROJECT_STATUS.md)

Technical next-work language is historical; standalone repositories are canonical.

### R_ECU_CLEANSHEET

**Frozen clean-sheet firmware archive**

Type: repository. Source date: not individually established.

[Open source](https://github.com/Brnoutkng/SkidLabz-ECU-Development/blob/a37441426a518616c0cd13791518f99fda0fda41/firmware/RaceOS-CleanSheet-Archive/README.md)

Superseded implementation of the same firmware effort, not another active product.

### C-OCT04

**Product feasibility and workshop-tool discussions, 4–5 October 2026**

Type: recovered-chat. Source date: 2026-10-04.

Recovered user and assistant excerpts. Includes torsion testing, engine workshop instruments, PDM, logger, knock monitoring and explicit market/scope rejections. Whole transcript and conversation URL were not returned.

### C-OCT20

**Commercial product status and owner rejections, 20 October 2026**

Type: recovered-chat. Source date: 2026-10-20.

Recovered owner statements reject RaceScales on economics and valve-spring checker on competition and limited sales. These supersede older maybe/ready labels.

### C-OCT27

**Valve-spring checker removal reaffirmed, 27 October 2026**

Type: recovered-chat. Source date: 2026-10-27.

Recovered owner instruction: removed from commercial list; do not put it back in the queue.

### C-OCT02

**Speedway product-fit and setup-tool discussion, 2 October 2026**

Type: recovered-chat. Source date: 2026-10-02.

Recovered owner comments on dirt tyre-temperature tools, brake-pressure gauges, toe tools and scale retrofit demand. Later broader-market proposals are not evidence of reactivation.

### C-SEP14

**Initial Speedway product shortlist, 14 September 2026**

Type: recovered-chat. Source date: 2026-09-14.

Recovered owner shortlist: gauge, scales, alignment and recall tach; dirt tyre temperatures, digital stagger and generic setup app were rejected/parked.

### C-NOV04

**Commercial review and display/Street Hit decisions, 4 November 2026**

Type: recovered-chat. Source date: 2026-11-04.

Recovered owner requirements: dash stops at suitable screen sourcing; Street Hit is hardware-led and manufacturing-cost constrained. Side-product and receiver reviews also recovered.

### C-NOV08

**Product and hardware status review, 8 November 2026**

Type: recovered-chat. Source date: 2026-11-08.

Recovered status updates for tyre-gauge samples, centre-axle bleeders and ongoing product work. Arrival, selection and physical validation are kept separate.

### C-NOV12

**Solid-state relay, Motion Raceworks/RIFE and PLEX discussion, 12 November 2026**

Type: recovered-chat. Source date: 2026-11-12.

Owner proposed a plug-in solid-state relay and requested brand research. The additional accessory, sensor and monitor ideas were assistant suggestions; approval and feasibility are not established.

### C-NOV15

**RayTech Automotive review request, 15 November 2026**

Type: recovered-chat. Source date: 2026-11-15.

Owner requested investigation of the brand. Throttle/stack balancing, lambda-plus-RPM recording and related alternatives were research suggestions, not selected development projects.

### C-NOV17-RECAP

**Recovered recent idea-search recap, 17 November 2026**

Type: recovered-chat. Source date: 2026-11-17.

Secondary assistant recap names fast tyre-temperature capture, limited scale reader, brake tester, fuel-used display and rod-bolt gauge. Full 16–17 November Looser brainstorm was not retrievable; owner acceptance/rejection must not be invented.

### C-AUG02-04

**Early software ecosystem and naming discussion, 2–4 August 2026**

Type: recovered-chat. Source date: 2026-08-04.

RaceCal was owner-selected. CalcLab, TuneVault and other family names/capabilities were assistant proposals unless separately evidenced in actual repositories. Names are not proof of separate products.

### C-OCT12-TIMING

**MYLAPS live crew timing display decision, 12 October 2026**

Type: recovered-chat. Source date: 2026-10-12.

Recovered owner rejection: would not sell sufficient units. Research discussed recurring data/API cost, local feeds and support complexity. This was a display concept, not a replacement transponder.

### C-OCT11-RECAP

**Earlier product-queue recap, 11 October 2026**

Type: recovered-chat. Source date: 2026-10-11.

Recovered assistant recap mentions digital stagger, generic weather meter and leak-down tester among commercially uninteresting or low-priority ideas. It does not provide a direct owner decision for each.

### C-SEP25

**Tyre-gauge bleed-valve sourcing, 25 September 2026**

Type: recovered-chat. Source date: 2026-09-25.

Recovered owner constraints reject physically large industrial valves and commercially unsuitable imported bare cartridges; no approved alternative source established.

### C-OCT21-22

**Supporting products sourcing discussions, 21–22 October 2026**

Type: recovered-chat. Source date: 2026-10-22.

Eleven-product side list and sourcing/decision board recovered. Supplier listing prices were not quotes; START/SAMPLE labels were research priorities, not completed purchases.

### C-NOV13-17

**Recent RevMax and receiver progress in available conversation context**

Type: recovered-chat. Source date: 2026-11-17.

Owner reports adopted case/PCB connector changes, assembly preview work and gasket finalisation. Financial/payment records intentionally excluded. Does not establish production PCBA order placement or finished-product qualification.

### L-SIDE

**SkidLabz_Side_Products.md, 21–22 October 2026**

Type: private-file. Source date: 2026-10-22.

Saved source read in full during this review. Four user-nominated ideas: SP-001 through SP-004. Supplies, quotes, samples and custom-tooling assumptions remain unverified.

### L-JOBS

**SkidLabz_Master_Job_List_2026-11-04.md**

Type: private-file. Source date: 2026-11-04.

Saved source read in full. Confirms hardware arrivals and portfolio holds; dated source, superseded where later evidence exists.

### L-BLEEDER

**Sprintcar bleeder feasibility and mechanical concept, 25–26 October 2026**

Type: private-file-excerpt. Source date: 2026-10-26.

Source-file excerpts recovered through personal context, not a fresh complete document audit. Records component/architecture holds and rejected valve economics.

### R-PRO-TACH

**Historical SprintTach future Pro scope**

Type: repository. Source date: 2026-09-16.

[Open source](https://github.com/Brnoutkng/SkidLabz-SprintTach/blob/b434cb3ebe15b130900a18362d1c31acd34502ee/docs/requirements.md)

Future variants only; current Basic scope is distinct.

### R-GAUGE-VARIANTS

**TyreGauge sensor study and hypothetical variants**

Type: repository. Source date: 2026-10-20.

[Open source](https://github.com/Brnoutkng/SkidLabz-TyreGauge/blob/fe75912285a8cd8673b403b2005528b4d5bfa257/docs/PRESSURE_SENSOR_DEEP_DIVE_A0.md)

Research-paper suggestions, not approved additional products.

### R-TELEMETRY

**RaceOS telemetry candidate and limitations**

Type: repository. Source date: 2026-09-03.

[Open source](https://github.com/Brnoutkng/SkidLabz-RaceOS/blob/f35b4782cf52d0f3c6175e10e0725101eef9080c/firmware/RaceOS-Hybrid/docs/TELEMETRY_P10_CANDIDATE.md)

Complete candidate is not physically validated; basic experiments are not complete-system proof.

### R-REVMAX-FACE

**RevMax front-face manufacturing investigation**

Type: repository. Source date: not individually established.

[Open source](https://github.com/Brnoutkng/SkidLabz-RecallTach/blob/692b0c63cbef3bc12e607dc93f097831f77fb875/mechanical/REVMAX_FRONT_FACE_MANUFACTURING.md)

Historical process decisions; later procurement and design updates supersede old waiting states.

### C-NOV17-HELMET

**Owner proposal: pit helmet warmer for cool-weather visor fogging**

Type: direct owner voice discussion. Source date: 2026-11-17.

Steven described recurring visor fogging in cooler Australian speedway conditions and proposed researching a helmet warmer. His impression of expensive or hard-to-obtain alternatives is owner-reported, not a verified market finding. No build approval. Latest clarification: gentle heat on a stand between sessions for first-lap cold-visor fogging; add to list only, no large investigation. USB power is an open question.

### C-NOV17-PRIORITY

**Owner clarification: mainstream commercial demand before niche instruments**

Type: direct owner voice discussion. Source date: 2026-11-17.

Steven clarified that KnockMeter is not principally blocked by electronics complexity or making cost: the limited use case and expected sales are the concern. Mainstream commercially viable products take priority. This does not permanently reject KnockMeter.

### C-NOV17-TYRE-MOTIVATION

**Owner's firsthand tyre-gauge experience and product motivation**

Type: direct owner voice discussion. Source date: 2026-11-17.

Personal experience with an approximately 15–16-year-old Intercomp developing cold/damp zero drift, dissatisfaction with a roughly A$250 Longacre, and recalled Intercomp replacement price of A$960–980. Owner wants real accuracy and repeatability near or below A$250. Not a controlled benchmark, verified current price, measured component cost or validated product solution.

### C-NOV17-SSR-PRIORITY

**Owner decision: plug-in SSR later add-on, not current priority**

Type: direct owner voice discussion. Source date: 2026-11-17.

Steven explicitly deprioritized the plug-in SSR because of Chinese competition and perceived viability, while retaining it as a possible later add-on. Focus remains mainstream tech dashes, gauges, tools and pit equipment. This records owner judgment, not an independently measured market verdict.

### C-NOV17-LOGGER-PRIORITY

**Owner decision: standalone engine logger not a mainstream shortlist priority**

Type: direct owner voice discussion. Source date: 2026-11-17.

Steven cited existing logging in aftermarket ECU and factory tuning ecosystems, including PCMTEC on a BA Falcon as an example. He views the remaining older-carburetted niche as smaller/shrinking. This is a commercial-priority judgment, not quantified market research or a rejection of all logging. Personal relationship details are not needed in this public catalogue.

### C-NOV17-PYROMETER

**Owner's Speedway pyrometer rejection rationale**

Type: direct owner voice discussion. Source date: 2026-11-17.

Steven described rapid tyre cooling after leaving the track, wet track/water, reported logging prohibitions in his classes, and live external sensing complexity. These reinforce his existing Speedway rejection, do not establish universal class rules, and do not reopen the idea.

### C-NOV17-NOISE

**Owner declines chassis noise finder suggestion**

Type: direct owner voice discussion. Source date: 2026-11-17.

Steven rejected a chassis noise finder suggestion as occasional workshop equipment rather than a core recurring race-day need. He seeks recurring essential electronics across disciplines. This is not a global rejection of workshop tools, nor evidence the suggestion was previously a registered product.

### C-NOV17-MARKET-JUDGMENTS

**Owner screening of inflator, lap timer, brake-fluid tester and chassis squaring**

Type: direct owner voice discussion. Source date: 2026-11-17.

Steven judged these suggestions unsuitable for the current mainstream shortlist: preset inflation competes with an approximately $5 chuck plus gauge; phone MyLaps/Race Monitor reduce his perceived standalone timer opportunity; a common brake tester costs around $2.80 and is infrequently needed; chassis squaring competes with an approximately $2 tape and low willingness to pay (his approximately $35 example). These are his estimates and judgments, not independently verified current prices, currency conversions, universal user behaviour or evidence that unlike instruments perform identically. Cheap brake-fluid pens must not be conflated with actual boiling-point testers.

### C-NOV17-COMMERCIAL-FILTER

**Owner commercial filter: reachable demand and complete-product markup**

Type: direct owner voice discussion. Source date: 2026-11-17.

Reachable niches are acceptable where desire is strong and existing options are expensive, unreliable or unavailable. Target is at least 100% markup on complete COGS, equivalent to 50% gross margin before other costs when revenue is twice COGS. Owner's informal pit observation is roughly 70% without Tel-Tac and some stated interest near $400; not survey data, orders or general market statistics. Pad costs remain the complete-scales blocker.

### C-NOV17-WEATHER

**Owner assessment of dedicated weather/air-density tuning meters**

Type: direct owner voice discussion. Source date: 2026-11-17.

Steven judged a dedicated tuning meter not a mainstream win because of modern EFI, seeing a shrinking market mainly in mechanical injection. This records his commercial assessment, not measured market statistics or a universal technical claim.

### C-NOV17-DRIVER-COOLING

**Owner rejects driver-cooling suggestion on scope**

Type: direct owner voice discussion. Source date: 2026-11-17.

Steven considered newly suggested driver cooling too mechanical and potentially safety/approval-oriented. No specific approval requirement was verified. This does not reject the separate pit helmet-warmer idea.

### C-NOV28-METHANOL-FAULT-FINDER

**Methanol fault-finder scope and bench decision**

Type: owner discussion and feasibility review. Source date: 2026-11-28.

Owner described a comparative trackside diagnostic and deferred standalone purchasing. The detailed bench plan is retained privately. No water concentration or instrument performance was established.

### R-METHANOL-CAP-SENSOR

**Texas Instruments FDC2214 capacitance converter**

Type: manufacturer documentation. Source date: not individually established.

[Open source](https://www.ti.com/product/FDC2214)

Supports the measurement principle only; does not establish performance in methanol samples.

### C-NOV28-RPM-SWITCH

**Adjustable RPM switch idea**

Type: owner discussion. Source date: 2026-11-28.

Owner raised a simple adjustable RPM switch for the ideas register. No use case or development decision was established.

### R-MR-MODULE-RPM-SWITCH

**Mr Module Shift Light Controller**

Type: manufacturer listing. Source date: 2026-11-28.

[Open source](https://mrmodule.com.au/product/shift-light-controller/)

An Australian standalone RPM-activated output benchmark; the listing does not establish sales volume.

### C-NOV28-CARB-IGNITION

**Programmable carburetted-engine ignition idea**

Type: owner discussion. Source date: 2026-11-28.

Concept only; the owner has not committed to building it.

### R-MSD-ULTRA-6AL-PLUS

**MSD Ultra 6AL Plus**

Type: manufacturer documentation. Source date: 2026-11-28.

[Open source](https://www.holley.com/products/ignition/ignition_boxes/street_and_strip/6_series_performance_ignition_boxes/parts/65233)

Direct capacitive-discharge benchmark with onboard MAP and an RPM-by-load timing table.

### R-CB-BLACK-BOX

**CB Performance Black Box**

Type: manufacturer documentation. Source date: 2026-11-28.

[Open source](https://www.cbperformance.com/product-p/2013.htm)

Adjacent distributor timing control module with an integrated MAP sensor.
