# Decisions, rejections and holds

Check the reason and reopening condition before repeating a search. A rejected component or architecture does not automatically reject its parent product. A deferred option is not a permanent rejection.

[Main register](REGISTER.md) · [Corrections](RECONCILIATION.md) · [Sources](SOURCES.md)

## Product-level stops and holds

| Record | Disposition | Reason | Condition for another look |
| --- | --- | --- | --- |
| [RD-008 — FlowCal injector-bench software](ideas/flowcal.md) | Parked — priority / go-no-go | Explicitly inactive unless the owner reactivates it; not rejected on cost or feasibility. | Explicit owner reactivation for a real injector-bench need. |
| [RD-009 — Street Hit Pro](ideas/street-hit-pro.md) | Paused — cost | Manufacturing economics were too close to complete competing devices. The hardware is the product's main value; app progress does not clear its cost hold. | Materially improved complete-product cost/supply path and explicit owner restart. |
| [RD-011 — Standalone motorsport PDM](ideas/pdm.md) | Parked — priority / go-no-go | Explicitly parked at a go/no-go decision point. Paper investigation found no technical show-stopper; this is not a cost rejection or physical validation. | Deliberate owner decision to allocate development effort and accept a viable commercial plan. |
| [RD-012 — Portable Knock Meter](ideas/knock-meter.md) | Parked — priority / go-no-go | Lower current priority because the owner sees a niche use case and uncertain sales volume, rather than electronics complexity or making cost as the main barrier. Sourcing, fit and release checks also remain; the product itself was not rejected. | Owner promotes it after a convincing customer/use-case and commercial-demand case, with practical fit/cost/sourcing checks retained. |
| [RD-013 — SprintTach historical predecessor](ideas/sprinttach-history.md) | Superseded / reference | Current product development moved to RecallTach/RevMax; the historical repo is not a second live product. | Only explicit owner reactivation for a clearly different need. |
| [RD-014 — ECU Development archive and project control](ideas/ecu-archive.md) | Superseded / reference | Technical products now have standalone canonical repos. Retain provenance and control without duplicating their product entries. | No new product implied; use only for control/provenance or explicit owner-directed archival work. |
| [RD-015 — Digital race dash](ideas/digital-race-dash.md) | Paused — sourcing | No suitably priced display has been established with adequate daylight readability, integrated controller/carrier and accessible front mounting. | A suitable display with verified size, mounting, daylight performance, price and small-quantity supply. |
| [RD-016 — Sprintcar electronic tyre bleeders](ideas/electronic-bleeders.md) | Paused — feasibility | Practical retention, economical valve supply, pressure-control validation and overall assembly cost remain open. | Credible retention proof, affordable repeatable valve supply and a viable complete-unit cost. |
| [RD-017 — Torsion-bar tester](ideas/torsion-bar-tester.md) | Paused — validation | No economical trusted reference bar/dyno or verification rig was available; a full rig would consume disproportionate time and cost. | An affordable credible reference/verification route or explicit reactivation with that limitation accepted. |
| [RD-018 — RaceScales / complete corner-weight scales](ideas/race-scales.md) | Rejected — commercial | Quoted supply and pad manufacturing were too costly; local complete products undercut direct-China offers. Large pads, calibration and freight defeated the intended economics. | A materially different, verified complete-set or pad supply cost; another electronics-only cost estimate is insufficient. |
| [RD-019 — Commercial wideband / analogue race-car logger](ideas/wideband-logger.md) | Deprioritised | Owner excludes this standalone engine logger from the mainstream shortlist: he considers logging already covered by modern aftermarket ECUs and factory tuning ecosystems, leaving a smaller and shrinking older-carburetted-car niche. This is his commercial judgment, not a measured market-size finding. Earlier scope questions remain unresolved. | Owner identifies a sufficiently broad, underserved paying use case despite ECU/tuning-system logging, followed by a viable simple architecture. |
| [RD-020 — On-engine digital valve-spring pressure checker](ideas/valve-spring-checker.md) | Rejected — commercial | Owner rejected it because many alternatives already exist, expected racer sales are low and the commercial case is poor. | A materially different demonstrated market or differentiated product case, with deliberate owner reopening. |
| [RD-022 — Plug-in solid-state relay](ideas/plug-in-ssr.md) | Deprioritised | Owner explicitly deprioritized it for now because of Chinese competition and perceived commercial viability. It remains a possible later add-on, not a current development priority or permanently rejected product. | Owner revisits it after evidence of a worthwhile differentiated use case and viable economics despite existing competition; exact load/socket, heat and inrush constraints would still need assessment. |
| [RD-027 — Shock absorber dyno](ideas/shock-dyno.md) | Parked — priority / go-no-go | The project was considered too large for the current workload and stage of the business. | Time, resources and a deliberate move into a substantially larger development project. |
| [RD-028 — Mechanical-injection setup / service tester](ideas/mfi-service-tester.md) | Deprioritised | The saved control file deprioritizes this idea. A recovered assistant recap cites limited Australian equipment access and a tiny local market; the original owner wording for that rationale was not recovered. | A demonstrated reachable customer base and repeatable access to relevant equipment for validation. |
| [RD-029 — Pro-Mag / race-ignition diagnostic tools](ideas/race-ignition-diagnostics.md) | Deprioritised | The saved control file deprioritizes this idea. A recovered assistant recap cites limited Australian equipment access and a tiny local market; the original owner wording for that rationale was not recovered. | A credible market and practical access to representative ignition systems. |
| [RD-030 — Standalone magneto timer](ideas/magneto-timer.md) | Deprioritised | The saved control file deprioritizes this idea. A recovered assistant recap cites limited Australian equipment access and a tiny local market; the original owner wording for that rationale was not recovered. | A verified differentiated use case and reachable buyers. |
| [RD-031 — Generic transmission controller](ideas/transmission-controller.md) | Dropped — scope/owner decision | Owner dropped the idea; a more specific cost or technical rejection rationale was not recovered. | A new explicit product/use-case decision, not an assumption that the old idea remains queued. |
| [RD-032 — EngineGuard / general engine-protection monitor](ideas/engine-guard.md) | Dropped — scope/owner decision | Owner dropped EngineGuard and retained a simple knock monitor without automatic ignition control. Later direct-input warning/recall monitor suggestions do not establish a reopening. | A clearly differentiated revised scope selected by the owner. |
| [RD-033 — Whistler / compression-ratio checker](ideas/whistler-compression.md) | Rejected — commercial | The recovered discussion placed this inspection-tool group in a tiny official/specialist market; approved-model requirements further limit some applications. | A demonstrated buyer pool and, where relevant, acceptance of an alternative instrument. |
| [RD-034 — Engine cubic-capacity checker](ideas/capacity-checker.md) | Rejected — commercial | The recovered discussion placed this inspection-tool group in a tiny official/specialist market; approved-model requirements further limit some applications. | A demonstrated buyer pool and, where relevant, acceptance of an alternative instrument. |
| [RD-035 — Fuel-legality tester](ideas/fuel-legality.md) | Rejected — commercial | The recovered discussion placed this inspection-tool group in a tiny official/specialist market; approved-model requirements further limit some applications. | A demonstrated buyer pool and, where relevant, acceptance of an alternative instrument. |
| [RD-036 — Camshaft legality checker](ideas/cam-legality.md) | Rejected — commercial | The recovered discussion placed this inspection-tool group in a tiny official/specialist market; approved-model requirements further limit some applications. | A demonstrated buyer pool and, where relevant, acceptance of an alternative instrument. |
| [RD-037 — Blow-by meter](ideas/blow-by-meter.md) | Rejected — commercial | The recovered discussion placed this inspection-tool group in a tiny official/specialist market; approved-model requirements further limit some applications. | A demonstrated buyer pool and, where relevant, acceptance of an alternative instrument. |
| [RD-038 — Piston ring filer](ideas/ring-filer.md) | Rejected — commercial | Owner considered the potential market insufficient and asked to return to the technical GitHub projects. | New evidence of a meaningful market or a substantially different useful product. |
| [RD-039 — Jet comparator](ideas/jet-comparator.md) | Rejected — commercial | Owner considered the potential market insufficient and asked to return to the technical GitHub projects. | New evidence of a meaningful market or a substantially different useful product. |
| [RD-040 — Valve-runout tester](ideas/valve-runout.md) | Rejected — commercial | Owner considered the potential market insufficient and asked to return to the technical GitHub projects. | New evidence of a meaningful market or a substantially different useful product. |
| [RD-042 — Chassis squaring / alignment tools](ideas/chassis-alignment.md) | Deprioritised | Owner deprioritized chassis squaring for the current shortlist: in his view a roughly $2 tape measure is strong competition and racers are unlikely to pay much for the suggested alternative, including his roughly $35 example. | Explicit owner reconsideration based on a specific unmet need and credible advantage over existing alternatives. |
| [RD-043 — Electronic / dedicated toe-measuring tool](ideas/toe-tool.md) | Parked — priority / go-no-go | Owner challenged its value because it competes with a simple tape measure. | A demonstrable repeatability or usability advantage over the existing simple method. |
| [RD-044 — Digital tyre-stagger measuring gadget](ideas/digital-stagger.md) | Rejected — commercial | Owner did not retain the electronic gadget as a useful commercial candidate. | A concrete advantage and buyer case beyond a low-cost tape. |
| [RD-045 — Generic race setup app](ideas/generic-setup-app.md) | Dropped — scope/owner decision | Not retained in the owner shortlist; the exact detailed rejection rationale was not recovered. | A defined unmet workflow and explicit selection of a revised product. |
| [RD-046 — Tyre pyrometer / fast temperature capture](ideas/tyre-temperature.md) | Earlier scope rejected; later scope unapproved | Owner rejected the usefulness of tyre pyrometry for his initial Speedway/dirt-racing context: tyres cool rapidly after exiting, wet track/water can affect the measurement, and he reports logging is prohibited in his classes. Live external sensing would add complexity. A newer broader quick-capture proposal remains unapproved research, evidenced in a secondary recap. | A distinct circuit/kart customer need and specific capture advantage, with actual owner adoption. |
| [RD-047 — Two-channel brake-pressure / bias tester](ideas/brake-pressure-tester.md) | Earlier scope rejected; later scope unapproved | Owner said these gauges are not generally used in the initial Wingless/Speedway market. A later workshop/two-circuit proposal needs differentiation and buyer validation. | A validated workshop customer case and a practical fitting/bleeding/safe-testing method. |
| [RD-049 — Limited reader for existing scale pads](ideas/scale-reader.md) | Earlier scope rejected; later scope unapproved | Earlier owner rejected retrofit demand because local racers generally did not own suitable scales. Later low-cost reader research did not establish a new market or owner approval. | A real installed-base/customer need, known compatible pads and an independently developable implementation. |
| [RD-051 — MYLAPS-compatible live crew timing display](ideas/crew-timing-display.md) | Rejected — commercial | Owner did not expect sufficient unit sales to support the recurring data/licensing and support economics. | A viable authorised data-access model and demonstrated sales volume. |
| [RD-053 — Laminated helmet tear-offs](ideas/helmet-tearoffs.md) | Paused — sourcing | Fit, optical quality, lamination, pack counts and MOQ per pattern remain unverified. | A concrete existing-pattern sample/quote; resume the saved shortlist rather than restart broad research. |
| [RD-057 — Aluminium AN spanner set](ideas/an-spanners.md) | Paused — cost | Observed supplier pricing left too little margin against the retail benchmark. | A materially cheaper equivalent-quality complete set and delivered quote. |
| [RD-059 — Folding mechanic / track mat](ideas/mechanic-mat.md) | Paused — cost | Bulky shipping and minimum quantities make a low-volume add-on difficult. | A manageable stock order with credible landed economics. |
| [RD-068 — RaceOS-to-logger telemetry bridge](ideas/telemetry-bridge.md) | Paused — validation | Basic experiments exist, but the complete candidate was expressly not burn-approved or run in an ECU in its source record. | A selected telemetry baseline and reviewed physical complete-system validation. |
| [RD-094 — GPS lap timer](ideas/gps-lap-timer.md) | Deprioritised | Owner does not consider a standalone lap timer a mainstream shortlist opportunity, citing MyLaps and Race Monitor on phones as adequate competition for the use he has in mind. | Explicit owner reconsideration based on a specific unmet need and credible advantage over existing alternatives. |
| [RD-118 — Chassis noise finder](ideas/chassis-noise-finder.md) | Dropped — scope/owner decision | Steven rejected this suggestion as an occasional workshop-use tool rather than a core, frequently needed race-day product. He is seeking recurring essential electronics useful across motorsport disciplines. | Explicit owner reconsideration based on a materially different recurring race-day use case; no further investigation is currently requested. |
| [RD-119 — Preset tyre inflator](ideas/preset-tyre-inflator.md) | Dropped — scope/owner decision | Owner rejected it for the current shortlist because it competes with what he sees as an approximately $5 chuck plus an existing gauge. | Explicit owner reconsideration supported by a differentiated recurring customer need. |
| [RD-120 — Brake-fluid testing tool](ideas/brake-fluid-tester.md) | Dropped — scope/owner decision | Owner rejected the current suggestion as infrequently needed and competing with common testers he estimates at approximately $2.80. | Explicit owner reconsideration supported by a differentiated recurring customer need. |

## Implementation and scope decisions

45 more specific records follow. These are linked from each parent idea.

### DEC-001

**Original complex RecallTach architecture** · [RD-001 — RevMax recall tachometer](ideas/revmax.md)

**Disposition:** rejected. **Evidence date:** not individually established.

Owner selected a simple recall tach; the earlier circuit and inherited SprintTach complexity were rejected as excessive.

**Reopen/advance condition:** Only reconsider a feature or circuit when a measured requirement shows the current simple product cannot meet it.

[Repository source](https://github.com/Brnoutkng/SkidLabz-RecallTach/blob/692b0c63cbef3bc12e607dc93f097831f77fb875/README.md). Historical rejection retained in current README; exact decision date was not established by this audit.

### DEC-002

**Earlier OLED, Newhaven graphic LCD and Newhaven TFT display implementations** · [RD-001 — RevMax recall tachometer](ideas/revmax.md)

**Disposition:** superseded. **Evidence date:** 2026-09-29.

Successive display studies were replaced by the owner-selected EA TFT020 implementation; archived studies are evidence, not current manufacturing authority.

**Reopen/advance condition:** A demonstrated issue or materially changed supply requirement must justify reopening display selection.

[Repository source](https://github.com/Brnoutkng/SkidLabz-RecallTach/blob/692b0c63cbef3bc12e607dc93f097831f77fb875/engineering/TFT020_BETA1_ARCHITECTURE_TRANSITION.md). 29 September is the explicit EA TFT020 owner-selection date; earlier display routes were superseded in several steps.

### DEC-003

**Genuine Switchcraft-only production connector supply** · [RD-001 — RevMax recall tachometer](ideas/revmax.md)

**Disposition:** rejected. **Evidence date:** 2026-11-11.

Low-quantity supply and cost were unsuitable for repeat production; CAZN 2C was selected for the production route.

**Reopen/advance condition:** Reconsider only if viable repeat supply and complete production economics change.

[Repository source](https://github.com/Brnoutkng/SkidLabz-RecallTach/blob/692b0c63cbef3bc12e607dc93f097831f77fb875/engineering/REVMAX_CAZN_SOCKET_2026-11-11.md). Selection does not establish physical two-way interchangeability or completed production qualification.

### DEC-004

**CAZN 2B connector variant** · [RD-001 — RevMax recall tachometer](ideas/revmax.md)

**Disposition:** rejected. **Evidence date:** 2026-11-11.

Its contact geometry did not match the genuine connector requirement; 2C became the selected variant.

**Reopen/advance condition:** Only a changed interface requirement or new measured compatibility evidence could justify reconsideration.

[Repository source](https://github.com/Brnoutkng/SkidLabz-RecallTach/blob/692b0c63cbef3bc12e607dc93f097831f77fb875/engineering/REVMAX_CAZN_SOCKET_2026-11-11.md). A rejected connector variant does not mean the selected CAZN 2C route remains undecided.

### DEC-005

**Old case opening, connector orientation and pre-Q05 stack as current production authority** · [RD-001 — RevMax recall tachometer](ideas/revmax.md)

**Disposition:** superseded. **Evidence date:** 2026-11-12.

Later connector/case alignment work and the Q05 case/PCB stack replaced earlier geometry; the old fit problems must not be carried forward as though no adjustment occurred.

**Reopen/advance condition:** Use the latest agreed mechanical revision; reopen only for a mismatch in actual manufacturing or assembly evidence.

[Repository source](https://github.com/Brnoutkng/SkidLabz-RecallTach/blob/692b0c63cbef3bc12e607dc93f097831f77fb875/CURRENT_STATUS.md). The source records the November case/connector sequence; later owner chat confirms case and PCB adjustments. Physical validation remains separate.

### DEC-006

**Historical BK4802P and ADF7021 RF architectures** · [RD-002 — Speedway race-control receiver](ideas/receiver.md)

**Disposition:** superseded. **Evidence date:** not individually established.

Historical radio branches were displaced by subsequent receiver development and are not the current R2 baseline.

**Reopen/advance condition:** Revisit only after a concrete R2 performance or supply failure and an explicit architecture decision.

[Repository source](https://github.com/Brnoutkng/SkidLabz-SpeedwayReceiver/blob/31a4d1eeeeb7f0ac42b5412249a66eff2172189d/PRODUCT_REQUIREMENTS.md). The exact per-chip rejection rationale/date was not recovered; do not invent a technical impossibility. R2 is documented in the newer branch.

### DEC-007

**CC1120 R1/P16B/P17 as the current production route** · [RD-002 — Speedway race-control receiver](ideas/receiver.md)

**Disposition:** superseded. **Evidence date:** 2026-11-06.

Manufacturing economics and display/assembly problems prompted the owner-authorized BK4819 R2 route; existing P16B hardware still has test value.

**Reopen/advance condition:** Only return to this route if measured results or changed economics justify it; do not discard existing hardware evidence.

[Repository source](https://github.com/Brnoutkng/SkidLabz-SpeedwayReceiver/blob/c432c87d76d46302f8d173bc4bb7e9f9db02ba36/R2_BRANCH_STATUS.md). 6 November R2 branch status records the new route. Newer owner chat says P16B mechanical fixes may also be useful; it is not categorically worthless.

### DEC-008

**Permanent ban on BK4819 because it lacked a usable production supply route** · [RD-002 — Speedway race-control receiver](ideas/receiver.md)

**Disposition:** superseded. **Evidence date:** 2026-11-12.

The owner reopened BK4819 through domestic consignment, and the R2 requirements record chips received into JLC's parts library.

**Reopen/advance condition:** Reopen the supply decision only if repeat supply fails; chip intake alone does not prove receiver performance.

[Repository source](https://github.com/Brnoutkng/SkidLabz-SpeedwayReceiver/blob/c432c87d76d46302f8d173bc4bb7e9f9db02ba36/PRODUCT_REQUIREMENTS.md). 12 November is the documented parts-library receipt, superseding the old supply prohibition.

### DEC-009

**Overseas radio-chip consignment through Australia or an overseas distributor** · [RD-002 — Speedway race-control receiver](ideas/receiver.md)

**Disposition:** rejected. **Evidence date:** 2026-11-07.

Freight, intake fees and lead time made that route unsuitable for production; domestic seller-to-factory consignment subsequently worked.

**Reopen/advance condition:** Reconsider only if the total route economics change and domestic supply is no longer viable.

[Repository source](https://github.com/Brnoutkng/SkidLabz-SpeedwayReceiver/blob/c432c87d76d46302f8d173bc4bb7e9f9db02ba36/PRODUCT_REQUIREMENTS.md). The owner rejection is recorded under consigned-parts rules; later domestic receipt is dated 12 November.

### DEC-010

**Folded-FPC OLED, socketed display connections and portrait layout** · [RD-002 — Speedway race-control receiver](ideas/receiver.md)

**Disposition:** rejected. **Evidence date:** 2026-11-06.

Owner mechanical rules require a landscape receiver with a positively supported soldered display module; prior alternatives created assembly, freight or vibration concerns.

**Reopen/advance condition:** Only an explicit product change backed by assembly and durability evidence should reopen these choices.

[Repository source](https://github.com/Brnoutkng/SkidLabz-SpeedwayReceiver/blob/c432c87d76d46302f8d173bc4bb7e9f9db02ba36/PRODUCT_REQUIREMENTS.md). These are rejected implementation approaches, not rejection of the receiver product.

### DEC-011

**Custom direct-thread precision sensor route at the investigated cost and supply terms** · [RD-003 — Precision motorsport tyre-pressure gauge](ideas/tyre-gauge.md)

**Disposition:** rejected. **Evidence date:** 2026-10-06.

The preferred custom sensor route failed target cost/supply economics. That rejected architecture does not reject the tyre-gauge opportunity.

**Reopen/advance condition:** A verified sensor/source must meet both low-pressure measurement needs and realistic small-batch economics.

[Repository source](https://github.com/Brnoutkng/SkidLabz-ECU-Development/blob/a37441426a518616c0cd13791518f99fda0fda41/SKIDLABZ_PROJECT_CONTROL.yaml). The tyre-gauge entry explicitly reopened OEM-first investigation on 6 October. The file's global November update is not the decision date; October sample assessment remains later evidence.

### DEC-012

**Internal barbed sensor/tube stack or custom machined manifold as the automatic V1 default** · [RD-003 — Precision motorsport tyre-pressure gauge](ideas/tyre-gauge.md)

**Disposition:** not approved. **Evidence date:** 2026-09-22.

Owner preferred an off-the-shelf metal junction with a direct-thread sensor. The barbed stack remained a fallback, and custom manifold work was not the default.

**Reopen/advance condition:** Reconsider only after documenting failure of the preferred route and comparing actual assembly, measurement and cost evidence.

[Repository source](https://github.com/Brnoutkng/SkidLabz-TyreGauge/blob/fe75912285a8cd8673b403b2005528b4d5bfa257/docs/PLUMBING_STACK_P0.md). Fallback is not a categorical technical rejection. Subsequent sensor economics and sample results must be reconciled before choosing a new architecture.

### DEC-013

**Bluetooth/app/cloud, tyre-temperature and logging features in simple V1** · [RD-003 — Precision motorsport tyre-pressure gauge](ideas/tyre-gauge.md)

**Disposition:** out of scope. **Evidence date:** not individually established.

V1 prioritizes low-pressure accuracy, repeatability, temperature stability and straightforward use over feature count.

**Reopen/advance condition:** Add only if an explicit later product decision identifies customer value without compromising the measurement product.

[Repository source](https://github.com/Brnoutkng/SkidLabz-TyreGauge/blob/fe75912285a8cd8673b403b2005528b4d5bfa257/README.md). Display resolution is also not proof of accuracy; no production accuracy claim is established by these requirements.

### DEC-014

**Proceeding with the original hardware economics unchanged** · [RD-009 — Street Hit Pro](ideas/street-hit-pro.md)

**Disposition:** parked. **Evidence date:** 2026-11-04.

Manufacturing cost was the blocker; electronics approached complete competitor pricing before the rest of the finished product. Hardware development exists, but the product is not permanently rejected.

**Reopen/advance condition:** Demonstrate viable complete-product economics and select the actual hardware baseline before another spin.

[Repository source](https://github.com/Brnoutkng/SkidLabz-ECU-Development/blob/a37441426a518616c0cd13791518f99fda0fda41/SKIDLABZ_PROJECT_CONTROL.yaml). Cost hold is corroborated by project control and the parent's recovered 4 November owner clarification; the date comes from that chat, not the YAML global timestamp.

### DEC-015

**Treating the SAM-M10Q simplified alternative as fabrication-ready** · [RD-009 — Street Hit Pro](ideas/street-hit-pro.md)

**Disposition:** not approved. **Evidence date:** 2026-09-15.

The simplification is an unfinished redesign with outstanding layout errors and connections; it has no released manufacturing package or proven physical performance.

**Reopen/advance condition:** First select it explicitly as the baseline, close its existing design/sourcing checks and re-cost the finished product.

[Repository source](https://github.com/Brnoutkng/SkidLabz-Street-Hit-Pro/blob/2ce320a30b13b4340568e2bcb8ce303e2c1aaa41/hardware/REV_A_LAYOUT_NOTES.md). The branch was checkpointed as stopped work. This does not establish rejection of the integrated-antenna idea itself.

### DEC-016

**Making three-run averaging compulsory for the product** · [RD-010 — Street Hit companion app and analysis core](ideas/street-hit-app.md)

**Disposition:** superseded. **Evidence date:** 2026-11-04.

The owner's later direction makes averaging optional; older app scope must not convert this into an app-led product or mandatory workflow.

**Reopen/advance condition:** Change only through an explicit product decision informed by real repeatability data.

[Repository source](https://github.com/Brnoutkng/SkidLabz-Street-Hit-App/blob/d831ab01ca5e34ebe90b8b1102f5036eed79281f/docs/PRODUCT_SCOPE.md). The linked document contains the older rule. Its supersession is from the parent's recovered 4 November owner clarification; source note must accompany the link.

### DEC-017

**Starting full engineering automatically after the feasibility study** · [RD-011 — Standalone motorsport PDM](ideas/pdm.md)

**Disposition:** parked. **Evidence date:** 2026-10-13.

The PDM was left at a deliberate go/no-go point. Paper feasibility exists, but no decision to fund the next engineering phase was recorded; it was not rejected for cost.

**Reopen/advance condition:** An explicit proceed decision should lead to floorplan, exact sourcing/quotes and physical high-current validation.

[Repository source](https://github.com/Brnoutkng/Skidlabz-PDM/blob/1f1f5969c49bd968aabcb7fa5c34fffc4e1a75f8/README.md). Do not infer product rejection from preliminary cost estimates or absence of schematic/PCB work.

### DEC-018

**Separate owner-built Prototype 0A/0B test rigs** · [RD-012 — Portable Knock Meter](ideas/knock-meter.md)

**Disposition:** rejected. **Evidence date:** 2026-10-25.

Owner rejected separate homemade rigs; the next meaningful hardware path is the professionally assembled actual instrument.

**Reopen/advance condition:** Reopen only on an explicit owner change of direction; do not rename the same rig request.

[Repository source](https://github.com/Brnoutkng/SkidLabz-KnockMeter/blob/734f13a260ceda82c307945538f1c2f641ce4dde/CLAUDE.md). Latest repo guidance reviewed is 27 October; exact original owner rejection date was not established.

### DEC-019

**Automatic ignition control, engine-protection promises and broad connected/logging features** · [RD-012 — Portable Knock Meter](ideas/knock-meter.md)

**Disposition:** out of scope. **Evidence date:** not individually established.

The agreed product is a standalone listening/indication instrument. ECU control, automatic retard and added display/logging/connectivity functions are outside that scope.

**Reopen/advance condition:** A separate explicit product decision and appropriate validation would be required.

[Repository source](https://github.com/Brnoutkng/SkidLabz-KnockMeter/blob/734f13a260ceda82c307945538f1c2f641ce4dde/docs/PROJECT_STATUS.md). This is a product boundary, not evidence that such functions are technically impossible.

### DEC-020

**Analogue selectable-filter and precision-rectifier baseline** · [RD-012 — Portable Knock Meter](ideas/knock-meter.md)

**Disposition:** superseded. **Evidence date:** not individually established.

An ADC/DSP candidate replaced the earlier analogue route to reduce parts and simplify the instrument.

**Reopen/advance condition:** Revisit only if measured signal-chain performance justifies a different architecture.

[Repository source](https://github.com/Brnoutkng/SkidLabz-KnockMeter/blob/734f13a260ceda82c307945538f1c2f641ce4dde/docs/DECISION_REGISTER.md). The DSP implementation remains a candidate; offline replay does not establish production detection accuracy.

### DEC-021

**Boost-supply architecture** · [RD-012 — Portable Knock Meter](ideas/knock-meter.md)

**Disposition:** rejected. **Evidence date:** not individually established.

The project rejected the extra noise and part-count burden of a boost route.

**Reopen/advance condition:** Reopen only if the actual instrument cannot meet its measured supply/output requirements without it.

[Repository source](https://github.com/Brnoutkng/SkidLabz-KnockMeter/blob/734f13a260ceda82c307945538f1c2f641ce4dde/docs/DECISION_REGISTER.md). No exact rejection date recovered. Battery compatibility remains a parallel release dependency, not a reason to halt all other work.

### DEC-022

**Complex integrated-PCBA logger as the next build** · [RD-004 — RaceLogger Dev-1](ideas/racelogger.md)

**Disposition:** parked. **Evidence date:** 2026-10-01.

Owner parked the complex board and chose a simpler Dev-1 for the current car's tuning work; Dev-1 is explicitly a personal development tool.

**Reopen/advance condition:** Only resume product-grade integration after useful logger behavior is demonstrated and the owner chooses that scope.

[Repository source](https://github.com/Brnoutkng/SkidLabz-RaceLogger/blob/e17b089e9e15371a708dfe70c33cae337da74d96/hardware/dev1-minimal/DEV1_ARCHITECTURE.md). 1 October is the owner-approved Dev-1 architecture checkpoint documenting the earlier park/simplify instruction.

### DEC-023

**New live dashboard before reliable logging** · [RD-004 — RaceLogger Dev-1](ideas/racelogger.md)

**Disposition:** deferred. **Evidence date:** not individually established.

The first useful logger needs ECU telemetry, direct wideband lambda and aligned onboard session logging; display work comes afterwards.

**Reopen/advance condition:** Reliable capture/storage and a concrete display requirement must come first.

[Repository source](https://github.com/Brnoutkng/SkidLabz-RaceLogger/blob/8e39b18ebf1b6e1c363713411570802eb71fe040/README.md). Separate from the already existing LogWorks PC dashboard and the later commercial race-dash concept.

### DEC-024

**Removing the working TechEdge 3A2 workflow when RaceLogger develops** · [RD-005 — LogWorks](ideas/logworks.md)

**Disposition:** not approved. **Evidence date:** not individually established.

The existing 3A2/LogWorks path remains supported while the new hardware is developed alongside it; no retirement decision exists.

**Reopen/advance condition:** Only an explicit supported migration decision should change the working test-day path.

[Repository source](https://github.com/Brnoutkng/SkidLabz-RaceLogger/blob/8e39b18ebf1b6e1c363713411570802eb71fe040/README.md). Records absence of an approval, not an invented proposal that the owner rejected.

### DEC-025

**Clean-sheet ECU firmware as the active architecture** · [RD-006 — RaceOS](ideas/raceos.md)

**Disposition:** archived. **Evidence date:** 2026-08-11.

The clean-sheet route accumulated software defects before physical ECU execution; the hybrid approach retained the known-running hardware/timing foundation.

**Reopen/advance condition:** Only an explicit architecture change justified by evidence should revive it.

[Repository source](https://github.com/Brnoutkng/SkidLabz-ECU-Development/blob/a37441426a518616c0cd13791518f99fda0fda41/firmware/RaceOS-CleanSheet-Archive/README.md). Frozen historical work, not another active ECU product.

### DEC-026

**Mass deletion of inherited OSE routines** · [RD-006 — RaceOS](ideas/raceos.md)

**Disposition:** superseded. **Evidence date:** 2026-08-11.

The accepted hybrid progressively replaces selected control strategy and can leave harmless inactive code; broad deletion is not the current method.

**Reopen/advance condition:** Reopen only for a demonstrated problem and an explicit architecture decision.

[Repository source](https://github.com/Brnoutkng/SkidLabz-ECU-Development/blob/a37441426a518616c0cd13791518f99fda0fda41/docs/PROJECT_STATUS.md). Historical implementation approach, not a separate product or current to-do.

### DEC-027

**Ordinary high-speed UART-style bit-banging on the investigated ECU outputs** · [RD-006 — RaceOS](ideas/raceos.md)

**Disposition:** rejected. **Evidence date:** not individually established.

The investigated output/timing constraints made that telemetry approach unsuitable; later work used a different signalling architecture.

**Reopen/advance condition:** New hardware/timing evidence and independent review would be needed before changing the telemetry route.

[Repository source](https://github.com/Brnoutkng/SkidLabz-ECU-Development/blob/d5b45f8b80abb223ed062dae374cf1d6ca135f92/docs/RACEOS_ESP32_TELEMETRY_INVESTIGATION.md). The investigation spans multiple revisions through early September; exact rejection date is not assigned. Physical pin experiments do not validate the complete later system.

### DEC-028

**Universal ROM suite or live logging/analysis inside RaceCal** · [RD-007 — RaceCal](ideas/racecal.md)

**Disposition:** out of scope. **Evidence date:** 2026-08-02.

RaceCal is a focused offline calibration tool. Logging and live analysis belong in a separate test-day application, not a required calibration dependency.

**Reopen/advance condition:** An explicit new product/use-case decision must precede expanding this boundary.

[Repository source](https://github.com/Brnoutkng/SkidLabz-RaceCal/blob/99caa3280ce258d828923e0b2811ec3190851bf5/docs/RACECAL_PROJECT_SUMMARY.md). 2 August dates the explicit logging closure; the general focused-app boundary is also recorded. Historical rules rationale is not a fresh compliance claim.

### DEC-029

**Map B and map-switching work for the recorded car** · [RD-007 — RaceCal](ideas/racecal.md)

**Disposition:** out of scope. **Evidence date:** 2026-08-01.

The recorded car requirements used a permanent Map A and did not permit the proposed switch input; it was not a useful task for that setup.

**Reopen/advance condition:** A verified different car/use case and explicit owner request would be required.

[Repository source](https://github.com/Brnoutkng/SkidLabz-RaceCal/blob/99caa3280ce258d828923e0b2811ec3190851bf5/docs/RACECAL_PROJECT_SUMMARY.md). Do not generalize this historical car-specific decision to all current racing regulations.

### DEC-030

**Permanent Trigg migration wizard and open-ended reverse engineering** · [RD-007 — RaceCal](ideas/racecal.md)

**Disposition:** rejected. **Evidence date:** 2026-08-02.

The one-off calibration migration was sufficiently completed; a permanent wizard and further optional reverse engineering were unnecessary.

**Reopen/advance condition:** A repeated real migration need or concrete unresolved issue must be explicitly reopened.

[Repository source](https://github.com/Brnoutkng/SkidLabz-RaceCal/blob/99caa3280ce258d828923e0b2811ec3190851bf5/docs/RACECAL_PROJECT_SUMMARY.md). Two related closures share the recorded date; neither is an active product blocker.

### DEC-031

**Injector sizing assistant** · [RD-007 — RaceCal](ideas/racecal.md)

**Disposition:** rejected. **Evidence date:** 2026-08-02.

Existing flow configuration and duty estimates covered the actual need; inverse sizing recommendations relied on unverified assumptions.

**Reopen/advance condition:** A validated method and explicit unmet user need would be required.

[Repository source](https://github.com/Brnoutkng/SkidLabz-RaceCal/blob/99caa3280ce258d828923e0b2811ec3190851bf5/docs/RACECAL_PROJECT_SUMMARY.md). Do not confuse this dropped recommendation wizard with existing injector calibration features or FlowCal.

### DEC-032

**Injector-set matching UI and automatic bench hardware control** · [RD-008 — FlowCal injector-bench software](ideas/flowcal.md)

**Disposition:** out of scope. **Evidence date:** not individually established.

The bench already handles set matching, while FlowCal records and calculates manually measured results; hardware control would be a separate project.

**Reopen/advance condition:** An explicit need beyond the current bench workflow and a separate scope decision are required.

[Repository source](https://github.com/Brnoutkng/SkidLabz-FlowCal/blob/6aa0fd8d321fb8a2d666015ac69675ba7de6a3b6/README.md). Matching is excluded in the README; hardware-control exclusion is also recorded in the same snapshot's CLAUDE.md. Application inactivity is a separate owner-priority state.

### DEC-033

**Historical VI-511 segmented-display production route** · [RD-013 — SprintTach historical predecessor](ideas/sprinttach-history.md)

**Disposition:** rejected. **Evidence date:** not individually established.

The recorded small-quantity availability, minimum order and lead-time economics did not fit initial production.

**Reopen/advance condition:** Materially higher volume or a viable existing low-quantity display source would be needed, within an explicit new product decision.

[Repository source](https://github.com/Brnoutkng/SkidLabz-SprintTach/blob/f58b3cdfb9900cb17b1e0d4e17723f32088ed2ef/hardware/rev2-sourcing/LCD-CANDIDATES.md). Historical precursor decisions; current RevMax display selection remains authoritative.

### DEC-034

**VI-415 and small-digit alternatives as the next production display** · [RD-013 — SprintTach historical predecessor](ideas/sprinttach-history.md)

**Disposition:** rejected. **Evidence date:** not individually established.

The pilot rescue display lacked the required production digit count, and several alternatives had inadequate readable digit size; an earlier pinout concern was not the decisive reason.

**Reopen/advance condition:** Only a changed display requirement or a demonstrated suitable module justifies revisiting them.

[Repository source](https://github.com/Brnoutkng/SkidLabz-SprintTach/blob/f58b3cdfb9900cb17b1e0d4e17723f32088ed2ef/hardware/rev2-sourcing/LCD-CANDIDATES.md). VI-415 retained pilot-rescue value. Rejection for the next production design is not rejection of the historical pilot itself.

### DEC-035

**Treating monorepo technical copies as current standalone products or duplicate projects** · [RD-014 — ECU Development archive and project control](ideas/ecu-archive.md)

**Disposition:** superseded. **Evidence date:** not individually established.

RaceOS, RaceCal, RaceLogger and FlowCal were extracted into canonical repositories; the old monorepo retains history and the shared control file.

**Reopen/advance condition:** Use archived content for provenance; update implementation in its current canonical repository.

[Repository source](https://github.com/Brnoutkng/SkidLabz-ECU-Development/blob/a37441426a518616c0cd13791518f99fda0fda41/docs/MIGRATION_NOTES.md). Several migrations occurred on different dates; no single decision date is assigned.

### DEC-036

**Rim-mounted TPMS-style electronic bleeder** · [RD-016 — Sprintcar electronic tyre bleeders](ideas/electronic-bleeders.md)

**Disposition:** rejected. **Evidence date:** 2026-11-04.

Rotating mass/force, packaging and test practicality made this unsuitable; centre-axle work resumed.

**Reopen/advance condition:** New physical evidence resolving the rotating installation problems.

[L-JOBS](SOURCES.md#l-jobs)

### DEC-037

**Mechanical tank-and-bleeder route** · [RD-016 — Sprintcar electronic tyre bleeders](ideas/electronic-bleeders.md)

**Disposition:** rejected. **Evidence date:** 2026-10-25.

Owner reported difficult setting, extra fittings and practical dust/G-force failure concerns.

**Reopen/advance condition:** A materially different proven practical solution, not another generic mechanical recommendation.

[L-BLEEDER](SOURCES.md#l-bleeder)

### DEC-038

**Previously investigated SMC valve** · [RD-016 — Sprintcar electronic tyre bleeders](ideas/electronic-bleeders.md)

**Disposition:** rejected. **Evidence date:** 2026-10-25.

Commercial cost and availability did not fit the product.

**Reopen/advance condition:** A verified affordable repeatable supply or materially changed economics.

[L-BLEEDER](SOURCES.md#l-bleeder)

### DEC-039

**Latching/servo/proportional valve or pump expansion** · [RD-016 — Sprintcar electronic tyre bleeders](ideas/electronic-bleeders.md)

**Disposition:** deferred. **Evidence date:** 2026-10-25.

Complexity, failure behaviour, sourcing and scope were not justified for the initial concept.

**Reopen/advance condition:** A demonstrated need that the simple chosen route cannot meet.

[L-BLEEDER](SOURCES.md#l-bleeder)

### DEC-040

**Large industrial bleed valves or expensive imported bare cartridges** · [RD-003 — Precision motorsport tyre-pressure gauge](ideas/tyre-gauge.md)

**Disposition:** rejected. **Evidence date:** 2026-09-25.

Wrong physical format or commercially unsuitable small-quantity delivered cost.

**Reopen/advance condition:** A correctly sized repeatably buyable low-pressure cartridge with viable economics.

[C-SEP25](SOURCES.md#c-sep25)

### DEC-041

**OEM/white-label tach sourcing as an automatically approved replacement** · [RD-001 — RevMax recall tachometer](ideas/revmax.md)

**Disposition:** not approved. **Evidence date:** 2026-09-16.

Historical buy-versus-build research never established a suitable validated replacement for current RevMax.

**Reopen/advance condition:** An actually purchasable platform meeting the established practical requirements.

[R_SPRINT_SCOPE](SOURCES.md#r_sprint_scope)

### DEC-042

**Exposed face stickers and labour-heavy home wet coating** · [RD-001 — RevMax recall tachometer](ideas/revmax.md)

**Disposition:** deprioritized. **Evidence date:** not individually established.

Durability concerns and manual finishing burden led to the selected supplier-made face direction.

**Reopen/advance condition:** New material/process evidence without increasing assembly burden.

[R-REVMAX-FACE](SOURCES.md#r-revmax-face)

### DEC-043

**Custom segmented-LCD glass for the initial small batch** · [RD-013 — SprintTach historical predecessor](ideas/sprinttach-history.md)

**Disposition:** deferred. **Evidence date:** not individually established.

Tooling, minimum quantity and amortisation were not justified for the initial volume.

**Reopen/advance condition:** Materially greater volume or a demonstrably viable tooling/supply offer.

[R_SPRINT_DISPLAYS](SOURCES.md#r_sprint_displays)

### DEC-044

**Starting PCB/case before the display is sourced** · [RD-015 — Digital race dash](ideas/digital-race-dash.md)

**Disposition:** not approved. **Evidence date:** 2026-11-04.

The display is the first selection; otherwise its cost, mounting and daylight performance can invalidate the design.

**Reopen/advance condition:** The existing display requirements are met by a verified supply.

[C-NOV04](SOURCES.md#c-nov04)

### DEC-045

**Loose individual sheets or universal-fit stock assumptions** · [RD-053 — Laminated helmet tear-offs](ideas/helmet-tearoffs.md)

**Disposition:** out of scope. **Evidence date:** 2026-10-22.

Owner selected laminated stacks; actual helmet fitment and pack definition must be retained.

**Reopen/advance condition:** An explicit different customer/use-case decision.

[L-SIDE](SOURCES.md#l-side)
