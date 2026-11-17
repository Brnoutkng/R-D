# Independent review of forum deep dive 01

[Original report](REPORT.md) · [Original evidence](EVIDENCE.md) · [Research index](../README.md)

**Reviewed:** 17 November 2026. **Input baseline:** [94339a8](https://github.com/Brnoutkng/R-D/commit/94339a8853fe94e3073b33a1ea8cf785b6dd2955).

This review checks the report's arithmetic, manufacturing assumptions, selected competitor comparisons and torsion-bar conclusions. The original report and evidence are retained as the research record; the corrections and qualifications below should accompany their conclusions. This is desk research, not physical validation or supplier quotations.

## Assessment

**Holding new product development is reasonable. Several commercial conclusions are more certain than the evidence supports.** The existing tyre-gauge investigation receives useful problem evidence. The gauge checker remains suitable to retain as an internal-fixture concept; this review does not recommend selling it. The torsion-bar idea remains paused: a possible lower-cost verification route has been suggested, but its adequacy and cost have not been established.

The report generally separates one-time development, recurring production work, support and cash. There is no demonstrated wholesale double-counting of development as per-unit labour. The important limitation is that the recurring task times are estimates for largely owner-finished products, rather than measured production routings or quotations for a repeatable 25-unit manufacturing route.

## 1. Selected competitor pages checked directly

| Comparison | Directly observed evidence | Implication |
|---|---|---|
| QuickCar 61-712 water-temperature warning kit | The [cited Appletree product page](https://www.appletreeauto.com/quick-light-water-temperature-kit-61-712) displays **US$37.99**, with a preset 235°F switch, warning light and wiring. | The report's **US$15.99 / US$16 floor is not supported by the cited product listing**. Inexpensive warning kits still exist. A fixed single-channel kit is not equivalent to every inferred function of a two-channel programmable event recorder. |
| Proform 66842 spring tester | [JEGS](https://www.jegs.com/i/proform-778-66842-digital-valve-spring-tester-with-micrometer-0-01-in-increments-backlit-display) displays **US$199.99** for the digital tester with height micrometer tube. It is used in an external vise, with 0.01-inch height graduations and 2 lb display increments. | A low-priced competing attachment is real. This supports the competitive objection. It does not establish the competitor's measurement uncertainty, temperature performance or sensing principle, and it is not a complete bench press/frame. |
| Longacre Semi-Pro 52-53003 | The [manufacturer](https://longacreracing.com/products/semi-pro-digital-tire-pressure-gauge-0-60-psi) displays **US$99.99**, 0–60 psi range, 0.1 psi increments and a stated accuracy of **0.3 lb / 0.5%**. | Resolution is not accuracy. The stated 0.3 psi accuracy figure is material when assessing a low-pressure product; a 0.1 psi display does not establish 0.1 psi measurement accuracy. |
| Australian Longacre listing | [Revolution Racegear](https://revolutionracegear.com.au/product/l-acre-semi-pro-digital-0-60-psi-tyre-gauge/) still displays **A$365** and a matching Semi-Pro description, but exposes an internal SKU rather than the manufacturer's number. Its [terms](https://revolutionracegear.com.au/terms-conditions/) describe prices as excluding GST unless stated otherwise; the product page does not settle this. | The displayed local price is corroborated. Exact part-number and tax treatment should be confirmed before claiming a fully comparable landed-price gap. Do not silently use A$365 ÷ 1.1 as a verified ex-GST price. |
| Intercomp 100451 torsion tester | The [Summit listing](https://www.summitracing.com/parts/ICP-100451) identifies the tester and says **Not Available**; the retrieved page exposes no price. | **US$3,540.99 was not independently reconfirmed as a current purchasable price.** Preserve it as the original report's indexed-price observation. The current availability and price of equivalent alternatives remain unresolved. |

Prices above are retrieved public listings, not completed checkout or delivery quotations. The report's working currency conversion was not independently revalidated in this review.

The existence of cheap warning products is meaningful evidence against a basic warning kit. The stronger statement that competitors provide the candidate's entire proposed function set is not established by the simple switch/lamp comparison. Conversely, extra features do not establish willingness to pay for a new module.

## 2. What the labour model does and does not establish

At midpoint the five models allocate approximately **1.04–2.39 owner hours per sale** for production and support. At A$150/hour that becomes approximately A$156–359. These times are explicitly estimates in [the inputs](EVIDENCE.md#4-candidate-validations).

The relevant uncertainty is the amount of operator work required by a viable production route. For example, V1 gives an outsourced-harness estimate as well as an owner-built harness route, but the main model uses the latter. V4 has no cable-house quotation. V2's per-unit temperature check does not distinguish operator touch time from elapsed test time that might be batched. None of this establishes a faster achievable process; it establishes that the manufacturing route remains an assumption.

Positive cash contribution and failure to earn A$150 per owner hour are different findings. The report correctly shows both. The four negative midpoint contributions after owner labour mean those products fail that economic hurdle under those time assumptions. They do not mean every sale necessarily consumes cash. Paid subcontract work would introduce an actual cash cost.

For an existing project, evaluate remaining work and reusable design assets rather than automatically charging all past development again. **The V2 gauge-checker model is not a cost model of the existing RD-003 tyre gauge.**

## 3. Material model corrections and qualifications

| Issue | Correction / interpretation |
|---|---|
| Torsion payback prose says recovery within three years requires about A$1,000 price, under one owner hour per unit and 190 development hours together. | Its own sensitivity table gives **2.6 years at 50 units/year with price alone raised to A$1,015**, retaining the other midpoint assumptions: 1.83 hours per unit and 295 development hours. The combined improvements are one possible route, not necessary conditions. Neither that price nor that sales rate has buyer validation. |
| V2 support time is not itemised in its validator input table. | The source table gives **1.5–2.2 hours of production work**; the model uses **1.83–2.95 hours including support**. This implies an additional **20–45 minutes per sale**, about **A$81 at midpoint**. That assumption moves midpoint contribution from about **+A$37 after stated build labour** to **−A$44 including the added support**. It may be a prudent allowance, but it must be identified as added, unmeasured support time. The internal-fixture disposition need not change. |
| The time-halving sensitivity is described using outsourced assembly. | With cash costs unchanged, this is a time-reduction sensitivity. An outsourced-production scenario must add the supplier's charge and relevant fixture/process costs. The table does not establish outsourcing economics. |
| Cash development recovery after about ten torsion-kit sales is described as small cash risk. | This omits the working capital of a whole batch. Using the model's own midpoint bought-in cost of about A$286 per unit, 25 units are roughly **A$7,150**, in addition to **A$4,260** one-time cash: roughly **A$11,400 before sales**, subject to payment timing and which allowances are paid upfront. This is an illustration from the model, not a new supplier quote. |
| Annual results omit some recurring reference costs. | V2 lists annual master-reference calibration and V3 lists periodic calibration costs. Their annual contribution/payback tables do not deduct those ongoing fixed costs. Treat the tables as contribution before such costs, not complete profit forecasts. |

Smaller arithmetic/presentation corrections: 150–400 development hours at A$150/hour recovered over 100–150 units span **A$150–600 per unit**, rather than A$200–600. Whole-unit break-even quantities should round upward; for example, the reconstructed torsion midpoint is approximately **281.36, requiring 282 sold units**, and V1 midpoint cash recovery approximately **64.15, requiring 65**. These small rounding changes do not alter the development recommendation.

## 4. The A$250 tyre-gauge cost ceiling is useful and conditional

Under the report's assumptions of a GST-inclusive A$250 retail price, recoverable purchase GST, a 4.5% selling fee calculated on ex-GST revenue and net revenue of twice complete COGS:

`(250 / 1.10) × (1 − 0.045) / 2 = A$108.52`

If the fee is instead calculated on the full A$250 payment, the ceiling is approximately **A$108.01**. Thus **about A$108–109 complete product cost** is a sensible screening threshold under those assumptions.

That allowance includes the saleable product's assembly and calibration under the report's complete-COGS interpretation; it is not just a parts budget. If half an hour of owner production time at A$150/hour is assumed within it, approximately A$33.52 remains for bought-in and other production costs. **The half-hour is not a measured requirement for RD-003.** An OEM or other production route must be assessed using its own verified costs and work content.

The report's A$134 figure is a different calculation: money remaining after an 8% fees/warranty allowance and A$75 labour, available for materials and development recovery. It is not a second cost ceiling that simultaneously satisfies the 100% markup target.

## 5. Torsion-bar validation remains unresolved

Describe the proposal as **a possible lower-cost verification route whose adequacy and cost remain unestablished**. Do not treat the original blocker as solved in principle merely by renaming the instrument a consistency checker.

- The existing idea already includes comparing bars and tracking change. The proposed product still promises stamped-rate checking and detecting changes across removal, refitting and time. It must distinguish bar changes from fixture, mounting, sensor and environmental changes. [NIST's terminology guidance](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology) distinguishes short-term repeatability under unchanged conditions from agreement under changed conditions.
- Up/down averaging cancels friction only under the assumed symmetry. If the measured torques are `T + f_up` and `T − f_down`, their mean is `T + (f_up − f_down)/2`. Residual friction remains when the two terms differ; fixture compliance, geometry and sensor error also remain. The report's cancellation claim needs experimental support.
- The approximately 10.4% stiffness difference from increasing diameter from 1.000 to 1.025 inches is an idealized same-material, same-length solid-bar calculation. Hollow construction and effective length change the comparison. It does not establish that practical identification is easy.
- A rate change does not by itself establish permanent set. A neutral-angle shift can occur without a corresponding stiffness change, and a procedure that re-zeroes the installation could miss it. The existing prohibition on fatigue/remaining-life claims remains appropriate.
- Define any percentage acceptance threshold: observed range, standard deviation and uncertainty of a before/after difference are different quantities. The suggested 1–2% and 3% numbers have not been established as product requirements.

The HoseHeads ledger contains **one fully read torsion thread**; the other fully read HoseHeads thread concerns digital bleeders. Wanted posts for complete dynos do not establish willingness to buy the proposed customer-fixture kit at its assumed price. The current competitive gap remains unproven because availability and pricing of several named alternatives were not established.

## 6. Demand evidence needs the right negative test

Repeated complaints, workarounds and actual spending can identify an opportunity even when nobody explicitly asks for the proposed instrument. Replace “nobody asked for a checker/tester” as a decisive rejection with **“paid demand for this proposed solution was not demonstrated.”**

Likewise, a non-electrical cause does not automatically make an electrical diagnostic check valueless: ruling out an electrical fault may save time. Whether the proposed kart tester does that faster or more reliably than existing tools remains unproved. Compatibility, available alternatives, support and customer value are legitimate separate objections.

The statement that a small unaccredited maker cannot sell calibration authority is too categorical as a commercial conclusion. The unresolved question is how SkidLabz would establish and maintain credible measurement performance and customer trust at acceptable cost. This review does not establish that route or recommend commercialising the checker.

## 7. Decisions retained

| Item | Interpretation after review |
|---|---|
| RD-003 tyre gauge | Continue the existing investigation under its own scope. The repeated low-pressure trust problem is useful evidence; the manufacturing route and product economics remain to be demonstrated. |
| RD-017 torsion-bar tester | Keep paused. The comparator proposal is a research lead, with the complete measurement method, current alternatives and willingness to pay unresolved. |
| Gauge checker/reference station | Retain as an internal-fixture concept; no new commercial development recommendation. |
| Warning module, spring tester and kart tester | No development recommendation. The competitive and scope objections remain useful, with the price, functional-equivalence and estimated-labour qualifications above. |

No product status, source-project design, purchase or supplier contact is changed by this review. The most useful result is an evidence trail that distinguishes a demonstrated competing product, a credible customer problem and an estimated production cost.
