# Forum deep dive 01 — product-opportunity report

[Evidence file](EVIDENCE.md) · [Idea register](../../REGISTER.md) · [Decisions](../../DECISIONS.md) · [Forum directory](../../forums/README.md)

**Research date:** 17 November 2026 · **Forums:** HoseHeads, KartPulse, Grassroots Motorsports (GRM), Speed-Talk

This is a research finding. It approves no product, changes no register status, and authorises no purchase, supplier contact or engineering. Every candidate below stays a research finding unless an existing record already gives it another status.

**Register state.** While this research was running, the owner recorded new direction on main (17 November 2026): a commercial screening filter, his tyre-gauge motivation and price target, and several deprioritisations. This report has been reconciled with those records, and the statuses it quotes are as they stand after that update.

Money is in Australian dollars excluding GST unless marked. Working rate: A$1 ≈ US$0.69 (US$1 ≈ A$1.45), mid-November 2026. Competitor prices are web-search summaries seen on 17 November 2026 unless marked otherwise; JLCPCB/LCSC prices were fetched directly that day.

---

## 1. Recommendation

**No new product from these four forums clears the bar for development.** Four of the strongest forum findings, chosen for evidence strength and plausible fit, were each given an independent validation aimed at refuting them. All four failed:

| Tested idea | Why it fails |
|---|---|
| Engine-protection warning module | US$16–63 switch-and-lamp kits do the core job; US$123–250 alarm gauges with sender and recall do the rest. |
| Tyre-gauge checker sold as a product | A 0.1–0.25 % test gauge plus a tank valve costs about US$320–400, and nobody in 13+ gauge threads asked for a checker. |
| Load-cell valve-spring force tester | Proform already sells a digital vise/press tester at US$178–240. It also sits next to an existing owner rejection (RD-020). |
| Ignition/start tester for spec kart engines | 36 % of identified no-start causes were not electrical; a A$15 spark checker and a meter cover most of the rest; looms differ by engine. |

Two things deserve further, cheap investigation. Neither is a clean new product.

1. **Low-pressure tyre gauge — the existing investigation (RD-003).** This is the best-supported customer problem in the whole pass: racers on three forums say they cannot trust their gauge at low pressures. Australian shelf prices leave room (a Longacre digital that sells for US$87–112 is listed at A$365), and the owner's own target, recorded the same day, is genuine accuracy at about A$250 retail or less. The forum evidence sharpens the requirements; it does not change the status or solve the sensor-route problem already recorded.
2. **A simple torsion-bar consistency checker — a narrower version of the paused RD-017.** Sprint-car racers have asked for an affordable tester for 14 years, the mainstream instrument is listed at US$3,541, and the forum's own practice is to *compare* bars rather than measure absolute rate. That reframing speaks to part of the recorded validation blocker. The economics are marginal at A$150/hour, and the HoseHeads evidence was mostly not readable at source, so this earns three low-cost checks, not a build.

**Against the owner's screening filter** — reachable demand where existing choices are expensive, unreliable or unavailable, and at least 100 % markup on complete COGS. Both shortlisted items fit the demand side on paper: gauges that racers do not trust, and a US$3,541 tester with no cheap alternative found on sale. Neither has yet shown that buyers *strongly* want it at a stated price. On the markup side, the torsion kit clears the target at mid-case only if owner build time is left out of COGS (section 4.6).

A structural point explains most of the rejections. With owner time at A$150/hour, 150–400 development hours cost A$22,000–60,000 before any cash outlay. Recovering that over 100–150 units needs A$200–600 of contribution per unit *after* build and support labour. Sub-A$400 gadgets with an hour of owner time per unit cannot do it, however cheap the electronics are. The realistic targets are instruments where incumbents charge thousands, or derivatives that reuse a design SkidLabz already has.

---

## 2. Ranked comparison

Classification: (1) new to the register, (2) new evidence for an existing idea, (3) narrower or materially different version, (4) repeat of a rejection, (5) already adequately solved.

| # | Candidate | Problem evidence | Existing alternatives | Evidence of spending | Fit, build and support | Mid-case economics (section 4) | Register | Confidence | Disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Low-pressure tyre gauge (existing investigation) | Strong and repeated: KartPulse 5 threads, 32 posters, 2019–2025; GRM 8+ threads; one HoseHeads report | Adequate at US$87–325 in the US; expensive in Australia | Real: racers buy US$90–400 gauges and keep a second as a "benchmark" | Good fit; calibration labour is the cost driver | Not re-costed here; price ceiling evidence only | RD-003 — class 2 | Problem: high. Commercial case: unresolved | Continue the existing investigation with these requirements |
| 2 | Torsion-bar consistency checker kit | Repeated over 14 years by about eight separate seekers; only two threads read in full | Weak below US$3,000; small-run cheap units appeared and faded | Moderate: "cash in hand" wanted posts for used units (2017, 2023) | Own market; mechanical fixture and trust are the hard parts | Positive only in the favourable corner | RD-017 — class 2 and 3 | Low to moderate | Three cheap checks, then decide |
| 3 | Engine-protection warning module | Strong on GRM (10+ threads); not corroborated on the other three forums | Strong at both price tiers | People buy US$30–250 solutions today | Sender, plumbing and support heavy; liability | Negative | RD-089 / RD-090; RD-032 dropped — class 2 | High that it fails | Not recommended |
| 4 | Tyre-gauge checker as a product | Trust problem is real; zero requests for a checker | Test gauge plus valve; trade check stations; maker recalibration | None for a checker | Value is calibration authority, which a small unaccredited maker cannot sell | Negative | RD-092 — class 3 | High that it fails as a product | Keep only as an internal fixture for RD-003 |
| 5 | Load-cell valve-spring force tester | Strong on Speed-Talk (15 threads, 15+ users) | Exists at US$178–240 | Builders pay US$180–1,800 | Poor: calibration reference, wrong customer base | Negative | RD-020 rejected — class 4 | High that it fails | Not recommended |
| 6 | Kart ignition/start-circuit tester | Recurring problem, zero product requests in 72 threads | A$15 spark checker, load tester, meter | People swap US$36–190 parts instead | Poor: six or more loom variants, no engines on hand | Negative in every case | RD-029 / RD-083 — class 3 | High that it fails | Not recommended |

---

## 3. The two shortlisted items

### 3.1 Low-pressure tyre gauge — new evidence for RD-003

**In one sentence:** a handheld digital gauge for roughly 4–30 psi whose selling point is that the reading is right, settles quickly and can be shown to be right.

**Buyer and job.** Owner-driver kart racers and parents (about 5–15 psi), sprint-car and dirt-oval teams (rear tyres about 4.5–8 psi), autocrossers and club racers. The job is setting and re-checking pressures alone, in seconds, and believing the number.

**What the threads establish.**
- KartPulse: five gauge threads from 2019 to 2025 with 32 distinct posters, about ten of whom report a fault or a doubt — analogue needles creeping, gauges disagreeing by "a couple psi", drift after drops, slow settling, and stored-data gauges losing data ([KP-01](https://forums.kartpulse.com/t/best-tire-pressure-gauge-for-karting/4027), [KP-02](https://forums.kartpulse.com/t/prisma-air-gauge-vs-longacre-digital-pro/12252), [KP-03](https://forums.kartpulse.com/t/anyone-using-the-new-prisma-hiprema4-tire-pressure-temperature-gauges/6142), [KP-27](https://forums.kartpulse.com/t/tire-pressure-gauge-reading/14240)). These threads were read directly.
- GRM: at least eight threads say gauges disagree and drift; workarounds are "always use the same gauge" and "three gauges and vote" ([GRM-23](https://grassrootsmotorsports.com/forum/grm/did-we-reach-a-consensus-on-tire-pressure-gauges/181353/page1/), [GRM-24](https://grassrootsmotorsports.com/forum/grm/does-the-world-really-need-a-t/184363/page1/)). Search-summary evidence only.
- HoseHeads: a team's new gauge read 1.5 lb out at an indicated 8 lb — a 19 % error at sprint-car pressures (May 2017, read directly, [HH-01](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/digital-bleeders-1031071)).

**Minimum useful feature set, in the users' words.** One low range; stated accuracy at the bottom of the range; first reading stable in a few seconds; survives a drop; a chuck that suits small kart hubs; a bleed button. No memory, app or temperature — the gauges that added those are the ones with reported data-loss faults, which supports DEC-013.

**Why someone would choose it.** In the US, not obviously: the Longacre Semi-Pro digital at [US$87–112](https://www.ogracing.com/products/longacre-semi-pro-digital-tire-gauge-0-60-psi) and Prisma at about US$250–325 are liked, with owners reporting 7–10 years of service. In Australia the same Longacre is listed at [A$365](https://revolutionracegear.com.au/product/l-acre-semi-pro-digital-0-60-psi-tyre-gauge/) — about 2.3–2.9 times the US price at the working rate, though the search tool reported that listing as well over a year old — a basic Longacre 0–15 psi analogue at [A$109](https://www.revolutionracegear.com.au/product/longacre-0-15-psi-tyre-gauge/), and an Intercomp digital at [A$606.90](https://www.speedwayspares.com.au/products/intercomp-digital-tire-gauge-0-100psi) (shown sold out). The reason to buy would be a locally supported gauge with a credible low-range accuracy statement at well under the imported price.

**Owner's recorded motivation and target (17 November 2026).** The register now records that the owner's long-serving Intercomp began zero-drifting in cold, damp conditions, that a replacement at about A$960–980 felt unjustifiable, that a roughly A$250 Longacre disappointed him, and that his target is genuine accuracy and repeatability at about A$250 retail or less. The forum evidence is independent of that account and points the same way on trust. One difference is worth keeping: KartPulse owners of the Longacre digital are mostly satisfied with it. Neither his experience nor theirs is a controlled comparison. The Intercomp listing found in this pass (A$606.90, a 0–100 psi model, sold out) is lower than his recollection; model and date may differ.

**Strongest evidence.** Repetition across three forums and seven years, plus real spending: racers pay US$90–400 and some keep a second gauge purely as a benchmark.

**Strongest objection.** "The number is just a reference" — many racers only need repeatability, and the forums show no unhappiness with the mid-priced Longacre digital. One KartPulse poster's reaction to a US$300 gauge was "hard pass".

**Register relationship.** RD-003 stays "Investigation / samples". This is class 2 evidence. It addresses none of DEC-011 (failed custom sensor route), DEC-012 (plumbing) or DEC-040 (bleed valves). One relevant supply fact: the only suitable low-cost sensor found in batch stock at JLCPCB was the ST LPS28DFWTR ([C3263277](https://jlcpcb.com/partdetail/C3263277), about US$5.30 at 30, 115 in stock). Its typical absolute accuracy was reported as about ±0.36 % in the 4 bar mode (search summary of the datasheet — confirm on the PDF), so stated low-range accuracy would have to come from per-unit calibration. Honeywell ABP2 parts showed stock of one to four. Treat that as an input to the RD-003 repository, not a design choice.

**Biggest unresolved issue.** Whether a small-batch route can hold stated low-range accuracy at a landed cost that works at Australian price points. That question already belongs to RD-003's cost gate.

**Cheapest sensible next step.** Add the forum requirements above to the RD-003 sample assessment. RD-003 needs a calibration reference in any case; one 0.05–0.1 % master gauge with a tyre-valve manifold would serve that and would also let SkidLabz offer a free gauge check at a race meeting. Counting how many gauges are checked, how far out they are, and how many owners then ask about a better gauge is the cheapest market test available.

**Reject or pause if** the samples cannot hold the accuracy RD-003 sets for itself across about 4–15 psi, over temperature and after a drop test, or the complete unit cost exceeds what section 4.5 allows at the owner's A$250 retail target.

### 3.2 Torsion-bar consistency checker kit — narrower version of RD-017

**In one sentence:** a load cell, an angle sensor and a small display that turn the racer's own torsion arm, stop and tube into a repeatable bar checker, reporting rate and comparing it with the bar's previous reading or its partner.

**Buyer and job.** Sprint-car, midget, micro and wingless teams, and the parts and shock shops that test bars as a service. The job is confirming a bar is what it is stamped, pairing bars, and spotting one that has gone soft or taken a set after a season or a crash.

**What the threads establish.**
- A January 2011 thread, read in full ([HH-02](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/torsion-bar-tester-841457)): a racer wants the maker of a simple manual tester "built just like a torsion tube on a car", with standard bushings, an arm bearing on a load sensor and a stop bolt turned to load the bar. A small-run unit of that kind had existed and faded. A hobbyist had built his own "to check bar consistency". A promotional reply priced the AccuForce dyno "in the mid $5000.00 range". A new poster in January 2013 wrote that testers "cost a lot" and asked for drawings; another in January 2015 asked for any Intercomp owner. Neither got a reply.
- Index rows seen on the live site, threads not opened: a 2009 request for tester designs ([HH-03](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/torsion-bar-tester-731127)); unanswered questions about the Maxim X-Check in 2010 and 2020 ([HH-04](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/maxim-x-check-torsion-bar-checker-anyone-use-them-803401), [HH-05](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/x-check-torsion-bar-rater-need-info-1114238)); and wanted-to-buy posts for used AccuForce or Maxwell dynos in 2017 and 2023, the second "cash in hand" ([HH-06](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/torsion-bar-dyno-wanted-1065891), [HH-07](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/wanted-torsion-bar-dyno-1134418)).
- Search-engine summary of the 2009 replies (not read at source, HH-21): Intercomp's tester "three grand"; a DIY rig of a load cell and a two-foot degree wheel for about US$100, pulling the arm to the same angle each way and expecting the two readings to agree within 10 %; and the objection "pay a speed shop".
- Current price: Intercomp's 48-inch digital torsion bar tester is listed at [US$3,540.99 at Summit Racing](https://www.summitracing.com/parts/ICP-100451), shown "Not Available" (search-result summary). That is about A$5,130 before freight and GST.

**Minimum useful feature set (our inference).** Load and angle captured together over a short sweep, up and down, with the midline used to cancel bushing friction; rate displayed in the units racers use; a stored value per bar so the next test shows the change; and a check procedure against a bar the owner keeps as a reference. No dyno graphs, no PC.

**Why someone would choose it.** It would cost a fraction of a US$3,500–5,500 instrument, ship in a small box, and answer the question the threads actually ask — "is this bar the same as that one, and the same as last time?"

**Strongest evidence.** The same request from about eight separate people between 2009 and 2023, two home builders, and no reply ever reporting a satisfactory cheap unit.

**Strongest objection.** Demand is a trickle, not a queue; shops already sell bar testing as a service; and a US$30 angle gauge with a scale pad gets a careful racer most of the way. The evidence base is also thin in quality: only two HoseHeads threads were read at source, and nothing technical after 2023 was found there.

**Register relationship — what has and has not changed.** RD-017 is paused because no economical trusted reference bar, dyno or verification rig was available. Two things bear on that blocker:
- *From the forum:* users frame the need as comparison and consistency, not traceable absolute rate. A comparator needs repeatability and a stable check bar, not a reference dyno.
- *Our engineering inference, not forum evidence:* force can be checked with known weights and angle with a reference block, and two or three new bars rated once by a commercial tester would give check standards. Whether a shop in Australia offers that rating, and at what fee, is not established.

This addresses the blocker in principle only. It does not show that a kit on a real car repeats well enough, and it does not show buyers would trust it. RD-017's status should not change on this evidence. The record's boundary also stands: no fatigue or remaining-life claim from rate alone.

**Fit with the owner's screening filter.** Existing choices are expensive (US$3,541) and the cheap ones appear to be unavailable, and these are SkidLabz's own customers — the two conditions the filter names. What is not shown is that buyers strongly want it: the evidence is a trickle of posts, the newest from 2023.

**Biggest unresolved issue.** Repeatability in a fixture the customer supplies. Bar rate rises with the fourth power of diameter, so adjacent 0.025-inch bar sizes near one inch differ by about 10 % in rate (our calculation). Telling sizes apart is therefore easy; detecting a bar that has lost a few per cent needs repeatability of about 1–2 % across removal and refitting, with bushing friction, arm flex and off-axis loading all in play.

**Cheapest sensible next step.** In order: (a) the owner decides whether a comparative specification answers the RD-017 concern; (b) one or two hours on an unrestricted connection to re-read the linked threads and check whether the Maxim X-Check, AccuForce, Maxwell or any sub-US$800 tester is on sale today; (c) a half-day bench trial on an available car using equipment already on hand — a digital angle gauge and a scale pad or borrowed load cell — measuring two or three bars through ten remove-and-refit cycles.

**Reject if** a satisfactory tester under about US$800 is already on sale; the bench trial spreads more than about 3 % on the same bar; fewer than about eight of twenty racers and shops asked would pay around A$800–1,000; or the owner judges the validation concern unanswered.

---

## 4. Small-batch economics

### 4.1 Assumptions

- Batches of about 25 units, sold direct. A reseller margin of about 30 % would come off the price and is not included.
- Prices and costs exclude GST. This assumes SkidLabz is GST-registered so GST on purchases is recoverable — **unverified**. Australian shelf prices quoted in this report are assumed to include GST. Export sales are treated as GST-free.
- Freight to the customer is charged separately. US duty or tariff on Australian goods was not researched.
- Owner labour is A$150/hour and is always shown on its own line.
- Each input is a range. "Mid" is the midpoint; "best" pairs low costs with the high price; "worst" the reverse.
- Basis labels: the cost inputs for items V1–V4 are the independent validators' engineering estimates, built on current JLCPCB/LCSC prices and published retail prices that are itemised with part numbers and links in [EVIDENCE.md](EVIDENCE.md#4-candidate-validations). The torsion-kit inputs are our own engineering estimates. **None of these is a quotation.**
- The 10, 25 and 50 units-a-year columns are scenarios, not forecasts. No market size is claimed.

### 4.2 What a product has to earn

Contribution needed per unit, after build and support labour, to recover a given one-time cost:

| One-time cost including owner time | over 50 units | over 100 units | over 150 units | over 250 units |
|---|---:|---:|---:|---:|
| A$15,000 (100 h) | A$300 | A$150 | A$100 | A$60 |
| A$30,000 (200 h) | A$600 | A$300 | A$200 | A$120 |
| A$45,000 (300 h) | A$900 | A$450 | A$300 | A$180 |
| A$60,000 (400 h) | A$1,200 | A$600 | A$400 | A$240 |

### 4.3 Mid-case comparison of the five items modelled

| Per unit, A$ ex-GST | Torsion kit | V1 warning kit | V2 gauge checker | V3 spring puck | V4 kart tester |
|---|---:|---:|---:|---:|---:|
| Selling price | 798 | 288 | 550 | 360 | 116 |
| Cash cost (materials, inbound freight, yield, packaging, fees, warranty) | 350 | 156 | 235 | 289 | 57 |
| **Cash contribution** | **447** | **132** | **315** | **72** | **59** |
| Owner time, build and support (hours) | 1.83 | 1.04 | 2.39 | 1.40 | 1.50 |
| Owner labour at A$150/h | 275 | 156 | 359 | 210 | 225 |
| **Contribution after owner labour** | **172** | **−24** | **−44** | **−138** | **−166** |
| One-time owner hours | 295 | 325 | 172 | 174 | 165 |
| One-time cash (prototypes, fixtures, references) | 4,260 | 8,500 | 3,330 | 5,510 | 2,250 |
| **One-time total including owner time** | **48,510** | **57,250** | **29,205** | **31,535** | **27,000** |
| Break-even units, cash outlay only | 10 | 64 | 11 | 77 | 38 |
| Break-even units, everything including owner time | 281 | never | never | never | never |
| Same, best case | 50 | 240 | 89 | 240 | never |

Price evidence behind each column: torsion kit A$580–1,015 (US$400–700) is an **unresolved assumption** set against a US$3,541 incumbent and a US$100 DIY rig; V1 US$149–249 against alarm gauges at US$123–250; V2 A$450–650 against a self-assembled reference at US$320–400; V3 US$199–299 against Proform at US$178–240; V4 US$60–100 against a A$15 spark checker and a US$71 pulse checker.

**Reading.** Four of the five lose money on every unit once owner time is counted, before any development is recovered. The cheap electronics are not the constraint: materials are A$45–260, while owner labour is A$156–359 a unit.

### 4.4 Torsion-bar kit in detail (our engineering estimate)

| Per unit, A$ ex-GST | Best | Mid | Worst | Basis |
|---|---:|---:|---:|---|
| Selling price | 1,015 | 798 | 580 | Unresolved assumption |
| Display unit board (MCU, bridge ADC, display, battery) | 16 | 21 | 25 | Validator's assembled-board estimate from current JLCPCB prices (CS1237 US$0.46, STM32G030 US$1.09, 0.96" OLED US$1.74) |
| Angle pod electronics | 10 | 28 | 45 | Current JLCPCB price: LSM6DSO US$2.89 at 30 (low end) to IIS2ICLX inclinometer US$18.64 at 30 (high end), plus board estimate |
| Load cell | 36 | 62 | 87 | Published price US$50 (Phidgets 500 kg S-type); direct-from-maker US$25–60 is an unresolved assumption |
| Enclosures, saddle adapters, cables, case, batteries, manual | 75 | 128 | 180 | Engineering estimate |
| Inbound freight, yield, packaging, fees, warranty | 71 | 113 | 155 | Engineering estimate (8–15 % inbound, 3–8 % yield, 3–6 % fees, 2–5 % warranty) |
| **Cash cost** | **208** | **350** | **492** | |
| **Cash contribution** | **807** | **447** | **88** | |
| Owner time: assembly, load and angle check, packing, support | 1.25 h | 1.83 h | 2.42 h | Engineering estimate |
| **Contribution after owner labour** | **619** | **172** | **−275** | |
| One-time owner hours (electronics, firmware, fixture and procedure, validation, documentation) | 190 | 295 | 400 | Engineering estimate |
| One-time cash (prototypes, test weights, reference bars and their rating, development fixture) | 2,320 | 4,260 | 6,200 | Engineering estimate; bar price US$179–186 published; rating fee unresolved |
| **One-time total** | **30,820** | **48,510** | **66,200** | |

| Mid-case result per year | 10 units | 25 units | 50 units |
|---|---:|---:|---:|
| Cash contribution | 4,474 | 11,185 | 22,371 |
| Contribution after owner labour | 1,724 | 4,310 | 8,621 |
| Owner hours consumed | 18 | 46 | 92 |
| Years to recover the one-time total | 28.1 | 11.3 | 5.6 |

| Sensitivity (other inputs at mid) | Contribution after labour | Break-even units | Years at 10 / 25 / 50 a year |
|---|---:|---:|---|
| Mid case | 172 | 281 | 28.1 / 11.3 / 5.6 |
| Price at A$580 | −28 | never | never |
| Price at A$1,015 | 373 | 130 | 13.0 / 5.2 / 2.6 |
| Price at A$1,300 (about US$900) | 635 | 76 | 7.6 / 3.1 / 1.5 |
| Owner time per unit halved (outsourced assembly, light support) | 310 | 157 | 15.7 / 6.3 / 3.1 |
| Development held to 190 hours | 172 | 190 | 19.0 / 7.6 / 3.8 |
| Materials at the high end | 55 | 886 | 88.6 / 35.4 / 17.7 |
| Price A$1,015, owner time halved and 190 hours together | 510 | 64 | 6.4 / 2.6 / 1.3 |

**Reading.** The kit recovers its cash outlay in about ten units, so the cash risk is small. Counting owner time, it pays back in under three years only if it sells for about A$1,000 or more, needs under an hour of owner time a unit, and is developed in about 190 hours — and then only at 25–50 units a year. **Price is the sensitivity that destroys it:** at A$580 each unit loses money after labour. A complete bench fixture was not costed; its steel, machining and freight resemble the profile that led to the scales rejection (RD-018).

### 4.5 Tyre gauge: what the price points allow

RD-003 has its own cost records, so no bill of materials is estimated here. The table shows what Australian price points allow. Two tests are applied: the owner's target of at least 100 % markup on complete COGS, taking 4.5 % for selling fees; and the amount left for materials and development after 8 % for fees and warranty and half an hour of owner time per unit (A$75). The fee, warranty and time figures are **unresolved assumptions**.

| Shelf price inc. GST | Price ex-GST | Complete COGS allowed at 100 % markup | Left for materials and development recovery |
|---:|---:|---:|---:|
| 250 (the owner's target) | 227 | 109 | 134 |
| 275 | 250 | 119 | 155 |
| 330 | 300 | 143 | 201 |
| 365 (the listed Longacre Semi-Pro price) | 332 | 158 | 230 |

**Reading.** At the owner's A$250 target the complete gauge — sensor, electronics, chuck, hose, bleed valve, case, assembly and calibration — has to come in at about A$109 or less to meet the markup target. That is the number the RD-003 samples and any OEM route need to be tested against.

### 4.6 Against the owner's 100 % markup target

The register's filter is net selling revenue of at least twice complete COGS. Whether owner build time counts as COGS is the owner's call, so both readings are shown, at mid-case.

| Mid case, A$ ex-GST | Torsion kit | V1 warning kit | V2 gauge checker | V3 spring puck | V4 kart tester |
|---|---:|---:|---:|---:|---:|
| Net selling revenue (price less selling fees) | 762 | 276 | 525 | 344 | 111 |
| Complete COGS allowed at 100 % markup | 381 | 138 | 263 | 172 | 55 |
| COGS, bought-in only (materials, inbound freight, yield, packaging) | 286 | 133 | 191 | 260 | 47 |
| Net revenue ÷ COGS, bought-in only | 2.66× | 2.07× | 2.75× | 1.32× | 2.33× |
| Owner build labour at A$150/h | 194 | 119 | 278 | 154 | 169 |
| COGS including owner build labour | 480 | 252 | 469 | 414 | 216 |
| Net revenue ÷ COGS including build labour | 1.59× | 1.09× | 1.12× | 0.83× | 0.51× |

**Reading.** On bought-in cost alone, four of the five clear twice COGS. Once owner build time is counted as part of the product, none does. The torsion kit comes closest and would need either a price near A$1,000 or build time cut to roughly half an hour. This is the same conclusion as section 4.3 reached by the owner's own measure: assembly and calibration labour, not parts, decides these products.

---

## 5. Other credible leads worth retaining

None of these is recommended for work now. Each records the useful unresolved question.

| Lead | Evidence | Why it is held | Register |
|---|---|---|---|
| Replacement readout for older wired corner-scale sets | Four GRM threads, about 2021–2025, five or six owners; a US$300 repair quote; a discontinued maker ([GRM-17](https://grassrootsmotorsports.com/forum/shop-talk/making-old-discontinued-race-scales-useful-again/271888/page1/), [GRM-18](https://grassrootsmotorsports.com/forum/grm/connectorspins-for-intercomp-scales/256324/page1/)) | Speaks to part of RD-049's blocker by showing a US installed base with failing electronics. It does not establish compatible pads, a calibration method or volume. Two of four cases were fixed with a part under US$20. Search-summary evidence. | RD-049 — class 2. RD-018 unaffected |
| Self-contained brake-pad temperature logger | One December 2025 maker build for about US$85 against commercial kits at US$1,600–2,750 ([GRM-02](https://grassrootsmotorsports.com/forum/grm/diy-brake-temperature-logging-tool-take-2/283478/page1/)) | A single maker and no stated demand. Generic four-channel thermocouple SD loggers already sell for [US$271–399](https://www.globaltestsupply.com/product/triplett-tmdl400-wall-mount-thermocouple-data-logger-sd). Temperature paint is the common answer. | RD-086 / RD-025 — class 3 |
| Phone-free kart "dumb dash" (lap time, RPM, one temperature) | Ten KartPulse threads, 2018–2026, six or more separate askers ([KP-07](https://forums.kartpulse.com/t/simple-laptimer-and-data-logger/2944), [KP-08](https://forums.kartpulse.com/t/racing-without-a-gauge/9622), [KP-22](https://forums.kartpulse.com/t/mychron-6-discussion-comparison-reviews-etc/13272), [KP-23](https://forums.kartpulse.com/t/cheap-timing-solutions/13252)) | Budget beginners with weak willingness to pay; used MyChron and Alfano units are plentiful; a hobbyist attempt failed on the display. It meets the same display-sourcing blocker as RD-015. | RD-095 — class 2. RD-094 was deprioritised by the owner on 17 November 2026 (phone timing is adequate competition), which matches the timing-only finding here: class 5 |
| Cam-profile measuring electronics for a user-built stand | Twelve Speed-Talk threads, 2010–2026; complete systems "around $4,700" ([ST-16](https://www.speed-talk.com/forum/viewtopic.php?t=71472), [ST-17](https://www.speed-talk.com/forum/viewtopic.php?t=69294)) | Performance Trends sells an electronics-only kit at US$1,799 and a DIY software route exists. The value and the support load are in the analysis software. | RD-026 — class 2 / 3 |
| Ignition-advance logging; distributor-machine refresh | Twelve or more machine owners, 2012–2025; one statement that only a discontinued Innovate box logs advance ([ST-39](https://www.speed-talk.com/forum/viewtopic.php?t=68996)) | A static vintage niche; programmable ignitions remove the need. Does not answer RD-041's doubt about reachable demand. | RD-041 — class 2 / 3 |
| Orphaned dyno electronics and software | The most repeated complaint on Speed-Talk: 30 or more owners, 25 or more threads, 2012–2026; upgrade quotes of US$15,000–28,000 ([ST-29](https://www.speed-talk.com/forum/viewtopic.php?t=71891)) | Now served by retrofit kits from about US$5,295. Only tiny-volume adapters remain, each inviting open-ended support of 30-year-old consoles. | No record — class 1; class 5 for full retrofit |
| Tyre-temperature and in-tyre pressure for karts | Five KartPulse threads; AiM infrared kit about US$600–660; one abandoned DIY build ([KP-04](https://forums.kartpulse.com/t/kart-tyre-temperature-data/3752), [KP-24](https://forums.kartpulse.com/t/tpms-in-karting/8347)) | The need is voiced by kart users; the advantage is not shown. "What would you do with that information?" recurs. Mounting is chassis-specific. The owner's Speedway rejection and its recorded reasons are untouched. | RD-046 — class 2 |
| Timing lights that can be trusted on CDI and multi-spark | Three partial Speed-Talk threads with 23, 13 and 7 authors ([ST-40](https://www.speed-talk.com/forum/viewtopic.php?t=46619)) | A cheap commodity category; nobody asked for a product; the fault is often the leads. | No record — class 1 |
| Kart fuel-tester scarcity | One November 2025 wanted post for Digatron testers "even if they do not work" ([KP-26](https://forums.kartpulse.com/t/fuel-tester/5169)) | Unconfirmed hint that the incumbent is scarce. One search found no statement either way. A supply gap would not change the tiny official market that led to the rejection. | RD-035 — class 4 |

**Evidence for products already in development** (no change to scope or status):

- **Race-control receiver (RD-002).** One-way receivers are appearing in US karting: one sprint track mandated them for 2025 and another requires a named brand ([KP-21](https://forums.kartpulse.com/t/one-way-radios-in-sprint-racing/13565)). Only nine posters, and incumbents at about US$85–100 "do the job". Minor complaints are earbud quality and fit for children. A market note only; frequency and transmitter compatibility were not examined.
- **RevMax (RD-001).** A search-summary thread says teams choose gears from the memory tach's maximum rpm (HH-26). Web-search summaries list the Tel-Tac II at US$325–360 and at A$652.80 and A$801.68 at two Australian sellers, both shown sold out. The register now also records the owner's informal estimate that about 70 % of people in the pits he observes have no Tel-Tac, with some saying they would buy at about A$400. The listings are consistent with a price gap; they are not demand evidence, and they add no feature request.
- **Electronic bleeders (RD-016).** The one large thread read in full shows buyers paying about US$1,000–1,200 (2015–2017 posts) for crew time saved and confidence in the set point, against US$225–360 mechanical sets that others find adequate ([HH-01](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/digital-bleeders-1031071)). Nothing clears the recorded blockers. One new consideration to check in the source project: a web-search summary reports a granted US patent on an axle-mounted solenoid design (US 9,566,833) and a later related one.
- **Knock meter (RD-012).** One 2015 request for a stand-alone indicator, plus a technical caution: experienced builders say block-sensor knock detection is unreliable with solid-roller valvetrains and forged pistons ([ST-41](https://www.speed-talk.com/forum/viewtopic.php?t=44489)). Nothing here answers the owner's recorded concern about niche use and uncertain volume.
- **PDM (RD-011).** GRM summaries show budget PDMs at about US$200 and open-source designs. That makes the commercial case harder; the parked status is unchanged.
- **Pit helmet warmer (RD-117).** Listed by the owner after the forum work began. No evidence was gathered on it in this pass.

---

## 6. Already solved, poor economics, or a repeat of an existing rejection

### Tested in depth and set aside

Full price tables, cost inputs and kill criteria are in [EVIDENCE.md section 4](EVIDENCE.md#4-candidate-validations).

**V1 — Engine-protection warning module (RD-089, RD-090; RD-032 dropped).** The strongest cluster on GRM: ten or more threads from 2012 to 2024, including drivers who missed gauges while an engine failed ([GRM-03](https://grassrootsmotorsports.com/forum/grm/how-useful-are-oil-pressure-gauges/151781/page1/), [GRM-04](https://grassrootsmotorsports.com/forum/grm/what-gauges-do-you-really-need/178621/page1/)). It fails because the function is already on sale at both ends: a [Longacre adjustable switch-and-lamp kit at US$56–63](https://www.ogracing.com/products/longacre-oil-pressure-warning-light-kit-15-50-psi), sprint-car battery versions at US$52–80, alarm gauges with sender and recall at US$123–250, and the [SPA/Racetech DG200](https://www.rallynuts.com/racetech/DG200-B.html) dual gauge with on-unit thresholds, peak recall and an external lamp output at about £134–202 ex VAT. A SkidLabz kit is estimated at A$190–350 including labour before any development recovery. The other three forums did not corroborate the need. No evidence addresses why RD-032 was dropped, and an "engine protection" claim runs against DEC-019.

**V2 — Tyre-gauge checker as a product (RD-092).** The trust problem is real, but nobody asked for a checker in five KartPulse gauge threads or eight-plus GRM threads. A racer can assemble one from a [Dwyer DPG-103](https://www.itm.com/product/dwyer-dpg-103-pressure-gauge-digital-30psi) (0.25 %, US$309–342) or [Keller LEO2](https://www.instrumart.com/products/30984/keller-leo2-digital-pressure-gauge) (under 0.1 %, from US$330) and a US$3–5 tank valve. Intercomp recertifies its own gauges. The product's value would be calibration authority, which an unaccredited small maker is worst placed to sell and which export customers could not practically renew. Worth keeping as an internal fixture and a free track-side check (section 3.1). RD-092 stays unadopted.

**V3 — Load-cell valve-spring force tester (adjacent to rejected RD-020).** Speed-Talk shows 15 or more users over 15 years distrusting cheap hydraulic testers ([ST-02](https://www.speed-talk.com/forum/viewtopic.php?t=68722), [ST-05](https://www.speed-talk.com/forum/viewtopic.php?t=59918)). But the [Proform 66836](https://90racing.com/products/proform-66836) digital mini is already sold at US$178–224, and the [66842 with a height micrometer](https://www.jegs.com/i/proform-778-66842-digital-valve-spring-tester-with-micrometer-0-01-in-increments-backlit-display) at US$183–240. The validator's materials estimate alone is A$175–345. The binding error is usually height, not force: at 300–700 lb/in, ten thousandths of an inch is 3–7 lb. The RD-020 record already notes that a basic load-cell-and-display product was compared with inexpensive options, so this is effectively class 4. Whether the Proform units are accurate was not established.

**V4 — Ignition and start-circuit tester for spec kart engines (narrower RD-029 and RD-083).** The validator read 72 KartPulse threads. Of 33 faults with an identified cause, 12 were not electrical at all (flooding, carburation, mechanical). A breakout could have helped in at most 16, and in at least nine of those a voltmeter while cranking, a load tester or a jumper did the same job. Pulse indication, the one distinctive function, was decisive in about two cases. Nobody asked for a tester. Looms differ across at least four IAME generations, three Rotax and Vortex, and SkidLabz has no engines or known-bad parts to test against. The price ceiling is about US$60–100.

### Not pursued further — the forum evidence itself settles it

| Idea | Finding | Register |
|---|---|---|
| Complete corner-weight scales | Borrow, buy used at US$350–1,000 or new at about US$600–800; DIY rigs disappoint. Reinforces the rejection. | RD-018 — class 4 |
| Toe, alignment, rear track width, kart lasers | Tape, strings and a US$30 angle box are judged adequate; the US$315–400 kart laser set is entrenched and liked. No repeatability advantage shown. | RD-043 parked; RD-042 deprioritised 17 November 2026 — class 4 / 5 |
| Brake-pressure and bias gauges | GRM's main thread calls live gauges "a waste of time"; US$60 gauges cover a one-off set-up. | RD-047 — class 4 |
| Lap timers and GPS loggers | Well served: phone apps at US$20, GPS units at US$160–200, used loggers. | RD-094, deprioritised 17 November 2026 — class 5 |
| Analogue sensors into CAN loggers | An existing four-channel module sells for US$149.95; the remaining pain is per-logger mapping and support. | RD-072; RD-019, deprioritised 17 November 2026 — class 3 tending to 5 |
| Fuel-used display | No request found; endurance teams use stint time and measured fills. | RD-048 — negative evidence |
| Kill switch that spares the alternator | Nine or more threads, but they ask how to wire existing parts; solid-state isolators and PDM logic exist; car-specific and safety-critical. | No record — class 1, largely 5 |
| Temporary recorder for track-only faults | A recurring scenario with no product request; each case was solved another way. | RD-088, RD-087 — class 2 |
| Mechanical-injection checks | Repeated procedure and trust questions, 2007–2017, all search-summary grade; leak-down testers at US$74–155 and a digital high-speed checker at about US$332 exist. | RD-028 — class 5 |
| Magneto timing box | One thread; boxes sell for US$52–131. | RD-030 — class 5 |
| Crew timing and transponders | Incumbent systems plus a phone app that already gives crews lap times. | RD-051 — class 4 |
| Loggers in winged sprint cars | The objection is rules and analysis labour, not hardware cost. | RD-004, RD-019 — class 4 / 5 |
| Rear-end squaring, shock dyno testing | An established squaring tool; dyno testing is bought as a service. | RD-042, RD-027 — class 5 |
| Jet measuring, leak-down, weather meters, battery testers | Pin kits, commodity testers and existing meters cover each. | RD-039, RD-099, RD-083; RD-085, deprioritised 17 November 2026 — class 4 / 5 |
| Blow-by, whistler and capacity checking, rod-bolt stretch, sonic testers, valve run-out, flow-bench electronics | Speed-Talk adds nothing that addresses any recorded reason; each has adequate products. | RD-037, RD-033/034, RD-021, RD-024, RD-040, RD-023 — class 4 / 5 |
| EGT, wideband and AFR tools | Answered with existing brands; one expert objection to EGT on constant-flow injection. | RD-025, RD-082–084 — class 5 |
| Driver cooling (cool-suit systems) | A strong DIY culture at US$80–100 a box; nobody asked for a controller. | RD-121, dropped 17 November 2026 — class 4 |
| Chassis noise finders | Knock-off sets with poor sensors, a US$40 DIY route and an established product. | RD-118, dropped 17 November 2026 — class 4 |
| Preset tyre inflators and inflator gauges | Kart racers already use inflator gauges; no gap voiced. | RD-119, dropped 17 November 2026 — class 4 |
| Budget race radios, small-engine dyno electronics | Existing vendors cover them; regulatory, tiny and support-heavy. | No record or name only — class 1 / 5 |

---

## 7. Research coverage and access limitations

| Forum | How it was read | Coverage | Limits |
|---|---|---|---|
| **KartPulse** | Directly, through the forum's public data endpoints | 6,652 topic titles screened across eight technical categories (2016–2026); 87 threads fetched; a further 68 read for the ignition validation | Photos and outbound links not opened; several megathreads sampled by keyword. Posters are mostly US owner-drivers; few Australians. |
| **Speed-Talk** | Directly, as a guest, including guest search | About 39,200 titles filtered; 126 topics opened; 113 searches; posts from 2004 to 15 November 2026 | Guest search omits roughly mid-2009 to late 2019, covered by titles only. Attachments hidden from guests. Paid forums not accessible. Sections labelled as needing registration were in fact readable to a guest on the day. |
| **Grassroots Motorsports** | **Search summaries only** | About 138 searches; 31 threads reached substantive detail (18 cross-confirmed), 27 partial, about 70 by title only | The site answers automated requests with a bot challenge, which was not circumvented. No thread page was read. Dates, reply counts and attribution are less certain than for the other forums. |
| **HoseHeads** | **Mostly not readable** | Two threads read in full; about 106 live titles skimmed; about 70 older threads known through search-engine summaries | The depth target was not met. The site has moved platform, searches titles only, rate-limited the reader and then blacklisted its address. No evasion was attempted. Nothing technical from 2024–2026 was found; the newest substantive posts read are from May 2017. |

Further points:

- **Depth target of 15–25 threads per forum:** met for KartPulse and Speed-Talk; met for GRM only in the search-summary sense; not met for HoseHeads.
- **Manufacturer and retailer pages could not be opened** from the research environment. Competitor prices are therefore search-result summaries, with the link each summary came from. JLCPCB and LCSC prices were read directly.
- **Register corrections found along the way.** The three HoseHeads sample links in the forum directory now open unrelated threads. Working locations for two are given in section 3.2; the Tech Talk board appears not to have been migrated. The directory's note that Speed-Talk's registered sections are closed to guests did not hold on the day.
- **Independence.** Each of the four validations was run separately and briefed to refute the idea. The torsion-bar assessment and all tables in section 4 are the coordinator's own work and have not had the same independent challenge.
- **The register moved during the research.** Ten owner updates landed on main on 17 November 2026 after the forum work had been briefed. The researchers and validators worked from the earlier register; this report and the register links in the evidence file were reconciled afterwards. Thread-level "Register" lines in the ledger keep the classes assigned at the time.
- **Not done:** no accounts, posts, messages, vendor contact or purchases. Private groups and social media, where current sprint-car technical talk has probably moved, were outside scope.

---

## 8. Next validation actions, by value and effort

All are proposals for the owner to accept or decline.

| # | Action | Effort | Cost | What it settles |
|---|---|---|---|---|
| 1 | Decide whether a comparative, consistency-only specification answers the RD-017 validation concern | 15 minutes | None | Whether the torsion lead is alive at all |
| 2 | On an ordinary browser, re-read the linked HoseHeads torsion threads and check current availability and price of the Maxim X-Check, AccuForce, Maxwell, Intercomp 100451 and any tester under US$800 | 1–2 hours | None | Whether a cheap satisfactory tester already exists — the main kill criterion |
| 3 | Add the forum-derived gauge requirements to the RD-003 sample assessment (range, low-end accuracy statement, settle time, drop robustness, no memory), and test complete cost against about A$109 at the owner's A$250 retail target | 30 minutes | None | Keeps RD-003 testing against what users say they want and what the price allows |
| 4 | Bench trial of in-car torsion-bar measurement with equipment already on hand: two or three bars, ten remove-and-refit cycles each | Half a day | None if equipment is on hand | Whether about 2–3 % repeatability is reachable without a dedicated fixture |
| 5 | Ask eight to ten racers and shops at meetings: do you test bars, how, what do you pay, would you pay about A$800–1,000 for a kit | Spread over two or three meetings | None | Willingness to pay, the weakest part of the torsion evidence |
| 6 | When RD-003 acquires its calibration reference, run a free gauge check at one meeting and record gauges checked, errors found and enquiries | One meeting | Within RD-003's own decisions | Market test for RD-003; final check on RD-092 |
| 7 | Desk check of the scale-readout lead: which pad families fail, connector and excitation, whether a brand-specific replacement already exists | 2 hours | None | Whether RD-049's "known compatible pads" condition can be met |
| 8 | Read the GRM threads cited in sections 5 and 6 directly in a browser before relying on any of them | 1–2 hours | None | Upgrades search-summary evidence to read evidence |
| 9 | Register upkeep: add the brand names listed in the evidence file to the competitor lists when convenient | 1 hour | None | Avoids rediscovering them |

Stop conditions are stated with each shortlisted item in section 3. If actions 1 and 2 go against the torsion lead, actions 4 and 5 are unnecessary.
