# Forum deep dive 01 — evidence

[Report](REPORT.md) · [Idea register](../../REGISTER.md) · [Decisions](../../DECISIONS.md) · [Forum directory](../../forums/README.md) · [Competitor lists](../../competitors/README.md)

**Research date:** 17 November 2026 · **Forums:** HoseHeads, KartPulse, Grassroots Motorsports (GRM), Speed-Talk

This file holds the evidence behind [REPORT.md](REPORT.md). It records what was seen and where; it approves nothing and changes no register status. Forum posts are paraphrased, posters are not named, and prices quoted from posts are historical.

## Contents

1. [How to read this file](#1-how-to-read-this-file)
2. [Independent repeats and contradictory evidence](#2-independent-repeats-and-contradictory-evidence)
3. [Thread ledger](#3-thread-ledger) — [HoseHeads](#hoseheads) · [KartPulse](#kartpulse) · [Grassroots Motorsports](#grassroots-motorsports) · [Speed-Talk](#speed-talk)
4. [Candidate validations](#4-candidate-validations) — current competitor sources, prices and cost inputs
5. [Links to matching R&D ideas and decisions](#5-links-to-matching-rd-ideas-and-decisions)
6. [Searches and sections that produced little useful evidence](#6-searches-and-sections-that-produced-little-useful-evidence)
7. [Unknowns that materially affect the conclusions](#7-unknowns-that-materially-affect-the-conclusions)
8. [Names not yet in the competitor lists](#8-names-not-yet-in-the-competitor-lists)
9. [Economics model output](#9-economics-model-output)

## 1. How to read this file

**How much of each forum was actually read.** This differs sharply by forum and is the most important qualification on the evidence.

| Forum | Evidence level | What that means |
|---|---|---|
| KartPulse | Threads read directly | Post text, dates and poster counts come from the forum's public data. |
| Speed-Talk | Threads read directly as a guest | Long posts were shown truncated; attachments are hidden from guests; search omits about mid-2009 to late 2019. |
| Grassroots Motorsports | **Search summaries only** | The site answers automated requests with a bot challenge, which was not circumvented. No thread page was read. Entries are graded S2, S or P. |
| HoseHeads | **Two threads read; the rest index rows or search summaries** | The site moved platform, rate-limited the reader and then blacklisted its address. No evasion was attempted. Entries are graded D, I or S. |

**Grades used in the ledger.**

- GRM — **S2**: substantive, cross-confirmed in two or more searches. **S**: substantive from one focused search. **P**: partial, first post or snippet only.
- HoseHeads — **D**: thread read in full on the live site. **I**: live index or search row only (title, preview, dates, counts). **S**: search-engine summary of a legacy page, not read. **W**: off-site web-search summary.

**Classification codes in "Register" lines.** (1) new to the register; (2) new evidence for an existing idea; (3) narrower or materially different version of an existing idea; (4) repeat of something already rejected; (5) already adequately solved by an existing product. A class does not change any status.

**Prices.**

- A price in a forum post is what that poster said on that date. It is not a current price.
- Current competitor prices are **web-search summaries seen on 17 November 2026**. Manufacturer and retailer pages could not be opened from the research environment, so the linked page was not itself read. Listing dates are mostly unknown.
- JLCPCB and LCSC component prices were fetched directly on 17 November 2026, in US dollars, excluding assembly fees, freight and GST.
- Working exchange rate: A$1 ≈ US$0.69, from [a dated rate table](https://www2.trustnet.com/Currencies/CurrencyHistory.aspx?SourceT=USDAUD) showing 0.6849 on 11 November 2026 and [a reference rate](https://exchangerate.guru/aud/usd/) of 0.70 on 2 November 2026 (both search summaries).

**Cost basis labels.** Every cost figure in section 4 carries one of: current supplier price; published manufacturer or distributor price; engineering estimate; unresolved assumption. None is a quotation.

**Source statements and our reading are kept apart.** In the ledger, the line "Inference (ours)" is our reading. Everything above it is what the thread or summary showed.

**Entry numbering.** HH, KP, GRM and ST numbers are local to this file.

## 2. Independent repeats and contradictory evidence

Each row groups independent examples of the same practical problem with the objections and adequate alternatives found alongside them.

| Problem | Independent examples | Contradictory evidence and adequate alternatives | Register |
|---|---|---|---|
| Cannot trust a tyre gauge at low pressure | KartPulse: five threads, 32 posters, about ten reporting a fault or doubt (KP-01, KP-02, KP-03, KP-27). GRM: eight or more threads (GRM-23, GRM-24). HoseHeads: a new gauge 1.5 lb out at 8 lb (HH-01, May 2017). | Longacre digital and Prisma owners report 7–10 years of good service (KP-02). "The number is just a reference." "$300? Hard pass." A cheap digital gauge was reported at about 1 % in a test cited on GRM. | RD-003, class 2; RD-092, class 3 |
| Checking torsion-bar rate without a US$3,000–5,500 instrument | About eight separate seekers, 2009–2023 (HH-02, HH-03, HH-04, HH-05, HH-06, HH-07, HH-21); two home builders. | "Pay a speed shop"; dyno services advertised (HH-08, HH-09, HH-31). No one reports owning a commercial unit. Only HH-02 was read in full. | RD-017, class 2 and 3 |
| Drivers miss gauges; stock warning switches trip too low | GRM: ten or more threads, 2012–2024 (GRM-03 to GRM-10). | Switch-and-lamp kits and alarm gauges already do it (section 4, V1). Gauge advocates say lights miss slow trends. Not corroborated on KartPulse, Speed-Talk or HoseHeads. | RD-089, RD-090, class 2; RD-032 not addressed |
| Cheap valve-spring testers are not trusted | Speed-Talk: 15 threads, 15 or more users, 2010–2026 (ST-01 to ST-15). Three use bathroom scales; two built their own. | Digital testers exist from US$178 (section 4, V3). Some want analogue only. Height error, not force, explained one "7–9 % low" case. | Adjacent to RD-020, class 3 tending to 4 |
| Diagnosing no-start faults on spec kart engines | KartPulse: four threads in the first pass (KP-11, KP-12) and 68 more in validation; a recurring seasonal problem. | Zero requests for a tester. 12 of 33 identified causes were not electrical. Spark checkers, load testers and a meter cover most cases (section 4, V4). | RD-029, RD-083, class 3 |
| Lap time and RPM without a US$550–770 logger | KartPulse: ten threads, six or more separate askers, 2018–2026 (KP-07, KP-08, KP-22, KP-23). | Used loggers are plentiful and last 20 years; a GPS unit and phone cover timing. A hobbyist's unit failed on vibration and a weak screen. | RD-095, RD-094, class 2; timing-only class 5 |
| Tyre temperature and in-tyre pressure | KartPulse: five threads (KP-04, KP-05, KP-06, KP-24). GRM: DIY loggers and the chore of capturing readings (GRM-25, GRM-26). | "What would you do with that information?" One owner's data showed no link to lap time. A DIY build was abandoned. An integrated gauge-and-probe product exists at US$449. | RD-046, class 2 |
| Dead readouts on older wired scale sets | GRM: four threads, five or six owners, about 2021–2025 (GRM-17, GRM-18). | Two of four fixed with a part under US$20; new complete sets at US$600–800 cap the price (GRM-19). KartPulse and HoseHeads scale threads concern levelling and procedure, not readouts (KP-10, HH-29). | RD-049, class 2; RD-018, class 4 |
| Orphaned shop instruments (dynos, cam checkers, distributor machines) | Speed-Talk: 30 or more dyno owners across 25 or more threads (ST-27 to ST-35); cam measuring (ST-16 to ST-26); distributor machines (ST-36 to ST-39). | Whole-system retrofits now exist; one owner converted at "about 20 %" of the maker's route. Every installation differs. | No record, class 1 (5 for retrofit); RD-026; RD-041 |
| Holding rear tyre pressure with bleeders | HoseHeads: one thread, about 27 posters, 22,674 views (HH-01). | The thread is split: some call the electronic units over-priced and report mechanical bleeders within 1 lb; others say the unit paid for itself in cleaning time. Rules risk raised in the first post. | RD-016, class 2 |
| Getting more data channels cheaply | GRM (GRM-01, GRM-14); KartPulse (KP-22, KP-25). | An analogue-to-CAN module exists at US$149.95. In sprint cars the objection is rules and analysis labour, not hardware (HH-27). "The hard part is the analysis." | RD-072, RD-019, class 3 tending to 5 |
| Alignment and toe measurement | GRM (GRM-22); KartPulse (KP-15, KP-16). | Tape, strings and a US$30 angle box judged adequate; the kart laser set is liked. | RD-043, RD-042, class 4 / 5 |

## 3. Thread ledger

One entry per substantive thread, grouped by forum. Each forum section also lists the products and prices named, the searches that found little, and its own unknowns. Evidence levels and codes are explained in section 1.

### HoseHeads

#### Coverage and access

- **Only partly readable.** Pass dated 2026-11-17 (two sessions). Only 2 threads were read in full; everything else is an index row or a search-engine summary. The 15–25 full-thread target was not met.
- **Platform move.** hoseheadforums.com is now an Odoo-based forum, not the ColdFusion board the register describes. The old Tech Talk index URL (`forum.cfm?forumID=17`) now redirects (HTTP 301) to the new home page. Only one board is listed: "HoseHeads Sprint Car General Forum" (60,760 threads, 345,322 replies, about 103 million views). No Tech Talk, micro-sprint, midget or classifieds board is listed.
- **Existing register links are broken.** Legacy `ThreadID` links now open unrelated threads: 27849 opens a 2007 results thread, 50895 a 2007 BBQ thread and 95811 a thread titled "Sweet". Corrected locations: [Torsion bar tester (2011)](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/torsion-bar-tester-841457) and [digital bleeders](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/digital-bleeders-1031071). The 2009 "torsion bar tester" thread was seen only as a live index row ([HH-03](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/torsion-bar-tester-731127)); it was not opened, so its replies are known only from a search summary (HH-21).
- **Tech Talk apparently not migrated** (inference from one test). A title search for "scaling" found five news threads about teams "scaling back" and not the Tech Talk thread "Scaling sprint cars". A search-engine snapshot suggested the legacy Tech Talk board was small (about 150 threads, moderated, with spam rows). Most technical discussion always lived in the General board.
- **Search is title-only.** Guest search matches thread titles, not post bodies, and equipment words are rare in titles: "tester" 2 threads, "bleeder" 3, "gauge" 4, "scaling" 5 (all news), "pop off tester" 0, in 60,760 threads. Absence of a topic is weak evidence of absence.
- **Blocked twice, then blacklisted.** Session 1: after about a dozen requests in two minutes the site's security layer returned HTTP 403 "Rate Limit Exceeded", reading the proxy's rotating addresses as a distributed scraper sweep; retries at 05:43, 05:56 and 06:32 UTC also failed. Session 2: fetching resumed at one request per 86 seconds; five pages were fetched, then the sixth (10:23:10 UTC) returned 403 "Blacklisted IP Address". Fetching stopped for good. **No evasion was attempted** (no alternate hostnames, header changes, third-party readers or archives). Robots.txt and the sitemap were never obtained. Internet Archive was blocked by the session's network policy (one probe); WebFetch did not resolve the site.
- **Counts.** 16 live pages fetched (10 requests refused). 2 threads read in full. About 106 thread titles skimmed on the live site. About 115 legacy titles surfaced through search-engine summaries (about 70 technical). About 40 domain-filtered plus 4 unfiltered discovery search calls, and 25 off-site product/price/patent checks. Date range seen: 2007 to 17 November 2026. The search engine's index of the site is narrow: the same roughly 70 threads recurred across about 40 queries.
- **Spam.** None visible in the 20 newest General rows (three low-content "Racking up the posts!" filler threads on 8 Nov 2026 are not commercial spam). Neither fully read thread has a spam bump. The spam the register noted was on the legacy Tech Talk index, which is no longer reachable.
- **Current activity versus historical evidence (kept separate).** *Current:* the General board is active daily (latest reply 17 Nov 2026), but the 20 newest threads are news, statistics, schedules and fan debate; the only technical-sounding title is "KSE Steering Gears" (not read). *Historical:* the most recent substantive technical posts actually read are 22–25 May 2017 (HH-01). The most recent technical-title activity seen is index-only (dates, content not verified): 15 Aug 2023, 12 Feb 2023, 20 Jan 2021, 4 Apr 2020. Nothing technical from 2024–2026 was found. On this sample HoseHeads looks like a historical archive (mostly 2007–2017), not a live technical venue; that is sample-limited, not proof of absence.
- **Evidence grades.** **D** = thread read in full on the live site (first post and all replies). **I** = live index/search row only (title, preview, dates, counts); thread not opened. **S** = search-engine summary of a legacy page, not directly read; per-post dates are usually absent and years are the engine's estimate or inferred from thread-ID order. **W** = off-site web-search summary (retailer listings, patents, press); not directly read, capture dates unknown, prices are listing snapshots, not quotes. Treat I and S items as not-read threads.

#### Threads

**HH-01 · [digital bleeders](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/digital-bleeders-1031071) · D**
- *Dates / evidence:* started 7 Jul 2015; 37 replies, 22,674 views (most-viewed equipment thread seen). Three genuine bursts: 7–13 Jul 2015, 26–28 May 2016 (patent argument), 22–25 May 2017. No spam bumps. Legacy ThreadID 95811 (legacy link now misdirects).
- *Who:* about 27 posters: 410/360 sprint-car owner-drivers and crew (customers); one non-US team (probably Australia or New Zealand — our inference from the wording); the electronic bleeder's maker (Swindell) posting openly as the maker (vendor).
- *Job and problem:* hold rear tyre pressure through a run and set it quickly. Mechanical bleeders need cleaning about every race, are slow to set and need spares pre-set. The maker's in-wheel recording: a 9 lb bleeder reached 12–13 lb on track and was back to 9.3 lb by the pits, so a pit check hides it. A new gauge read 1.5 lb out at an indicated 8 lb (22 May 2017).
- *Workaround / products named (US$, at post date):* Conroy diaphragm set $350 (Jul 2015); Conroy Pneu "gold" bleeders; "$20 plug in bleeders" (10 Jul 2015); electronic set "additional $900" over Conroy (8 Jul 2015), "$1,200.00" (9 Jul 2015), "$1000" (25 May 2017).
- *Resolution:* none; split between "worth it for a short-handed team" and "good Conroy bleeders are close enough".
- *Repeats and objections:* not repeated in other threads found. Objections: "way over priced"; some fast teams do not use them; Conroy users within 1 lb; no problems with gold bleeders (May 2017); three posters distrusted the maker's comparison video. Defences: "paid for itself" in cleaning time (23 May 2017). Maker said remote adjustment would be illegal, so units are manual-adjust.
- *Inference (ours):* buyers pay for labour saved and confidence in the set point; the rival is a well-kept US$225–360 mechanical bleeder; fit is axle-diameter specific. Register: RD-016 / DEC-036–039; the gauge point relates to RD-003.

**HH-02 · [Torsion bar tester (2011)](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/torsion-bar-tester-841457) · D**
- *Dates / evidence:* started 21 Jan 2011; 13 replies, 9,262 views. Ten replies 21–23 Jan 2011; genuine follow-ups 5 Jan 2013 and 10 Jan 2015; empty/image post 11 Jan 2015. No spam bumps. Legacy ThreadID 50895 (legacy link now misdirects).
- *Who:* about 10 posters: racers, one hobbyist builder, and one promoter of AccuForce (same person fronts the 2012 promo HH-08; vendor/promoter).
- *Job and problem:* find who makes a manual torsion bar tester: a car-like fixture with standard bar bushings, a stop and an arm bearing on a load sensor, with a digital read-out. Not a tube the bar slides into.
- *Workaround / products named:* hobbyist's home-made mechanical-scale rig (worked "to check bar consistency"; offered to build one). DNK "Design & Knowledge" small-run tester (apparently discontinued; no website found). Intercomp ("a smaller unit now"; asker says tube type). Maxwell Industries. AccuForce dyno "mid $5000.00 range" (promotional post, 23 Jan 2011, US$).
- *Resolution:* suppliers named; nobody reports owning a commercial unit.
- *Repeats and objections:* 5 Jan 2013: "They cost a lot", wants to build one, asks for drawings; 10 Jan 2015: asks if anyone owns an Intercomp. Both unanswered. No "you don't need one" objection here (that appears in HH-21).
- *Inference (ours):* wanted item is a simple manual consistency checker, well below US$3,000–5,500 instruments; one existed and faded. Register: RD-017.

**HH-03 · [torsion bar tester (2009)](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/torsion-bar-tester-731127) · I**
- *Dates / evidence:* last reply 16 Apr 2009; 14 replies; 6,020 views. Legacy ThreadID 27849 (legacy link now misdirects). Replies not read; see HH-21.
- *Job and problem:* first post asks for "designs for a torsion bar tester" (DIY request).
- *Inference (ours):* Register: RD-017.

**HH-04 · [Maxim X-check torsion bar checker...anyone use them?](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/maxim-x-check-torsion-bar-checker-anyone-use-them-803401) · I**
- *Dates / evidence:* 10 Jun 2010; 0 replies; 1,115 views. Thread not opened.
- *Job and problem:* asks whether it gives a number or just compares, and what it costs. Unanswered.
- *Inference (ours):* Register: RD-017.

**HH-05 · [X-Check Torsion Bar Rater-need info](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/x-check-torsion-bar-rater-need-info-1114238) · I**
- *Dates / evidence:* 4 Apr 2020; 0 replies; 708 views. Thread not opened.
- *Job and problem:* seeks information or a contact for this unit. Unanswered.
- *Inference (ours):* Register: RD-017.

**HH-06 · [TORSION BAR DYNO WANTED](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/torsion-bar-dyno-wanted-1065891) · I**
- *Dates / evidence:* 3 Feb 2017; 0 replies; 1,317 views. Thread not opened.
- *Job and problem:* wants a used AccuForce or Maxwell torsion bar dyno.
- *Inference (ours):* Register: RD-017.

**HH-07 · [WANTED: Torsion Bar Dyno](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/wanted-torsion-bar-dyno-1134418) · I**
- *Dates / evidence:* last activity 12 Feb 2023; 1 reply; 2,237 views. Thread not opened.
- *Job and problem:* "Looking to buy an Accuforce or Maxwell torsion bar dyno. Cash in hand." A different poster from HH-06.
- *Inference (ours):* Register: RD-017.

**HH-08 · VIDEO: Quick Racing Products | Torsion Bar Dynamometer Demonstration · I**
- *Dates / evidence:* 15 Apr 2012; 0 replies. New-platform id 905788 (no full URL given). Thread not opened.
- *Who:* vendor promotion: an AccuForce torsion bar dyno service offered to micro, midget and sprint customers.

**HH-09 · Torsion Bar Dynoing · I**
- *Dates / evidence:* 8 Oct 2010; 0 replies. New-platform id 826731 (no full URL given). Thread not opened.
- *Who:* vendor post (Competition Suspension Inc.).

**HH-10 · TheTorsionBar.com · I**
- *Dates / evidence:* 21 Jul 2011; 0 replies. New-platform id 868804 (no full URL given). Thread not opened.
- *Who:* promotion for a then-new sprint tech forum; not a product need.

**HH-11 · [Torsion Bar Adjustment](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/torsion-bar-adjustment-1139285) · I**
- *Dates / evidence:* last reply 15 Aug 2023; 12 replies; 3,789 views; first post is a photo. Thread not opened; content not established.

**HH-12 · Other torsion-title rows (setup questions) · I**
- *Dates / evidence:* index rows only, no tool content in previews: "Coils vs. torsion bars?" (20 Jan 2021); "31 inch torsion bars" (23 Dec 2018; 13,827 views); "C R D TORSION BARS" (23 Jan 2017); "Angle broched right front torsion bar arm" (26 Oct 2015; newcomer, wingless car); "Torsion bar stop safety" (7 Oct 2013); "The New Torsion Bar Stop Retainer debuted at the Knoxville Nationals" (3 Aug 2013; vendor; 10 replies); "18" Titanium Torsion Bars Needed ASAP" (10 Jul 2013); "Coil Over vs Torsion Bar" (17 Jan 2013); "Sprint car torsion bars?" (legacy ThreadID 23715; 13 Sep 2011; 17 replies; 15,625 views; newcomer explainer); "TORSION BARS AND SHOCKS" (23 May 2010); "torsion bars" (26 Mar 2010). Threads not opened.

**HH-13 · [Air bleeders](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/air-bleeders-1096371) · I**
- *Dates / evidence:* 24 Jul 2018; 1 reply. Thread not opened.
- *Who / job:* a fan asks what bleeders do after a TV remark; explanatory, not a product need.

**HH-14 · big toob bleeders · I**
- *Dates / evidence:* 29 Jan 2008; 1 reply. New-platform id 654944 (no full URL given). Thread not opened.
- *Job and problem:* asks what happened to the maker's website and whether the bleeders are still available.

**HH-15 · [Wanting to purchase - Used - DSR leak down gauge w/hoses](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/wanting-to-purchase-used-dsr-leak-down-gauge-w-hoses-1064342) · I**
- *Dates / evidence:* 24 Dec 2016; 0 replies; 874 views. Thread not opened.
- *Job and problem:* wants a good used "DSR single gauge unit" with cylinder and jet-can hoses, sought second-hand before buying new. What "DSR" refers to was not established.
- *Inference (ours):* Register: RD-028.

**HH-16 · Open Wheel Gauge Panel · I**
- *Dates / evidence:* 11 May 2010; 0 replies; 298 views. New-platform id 798077 (no full URL given). Thread not opened.
- *Who:* vendor announcement (QuickCar): a Dzus-mounted sprint-car gauge panel that comes out with the engine.

**HH-17 · How to beat the ASCS G0-No-Go gauge! · I**
- *Dates / evidence:* 3 Jun 2008; 4 replies; 2,206 views; first post is a photo of a go/no-go gauge. New-platform id 673129 (no full URL given). Thread not opened; content not established (tech-inspection gauge topic).

**HH-18 · [KSE Steering Gears](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/kse-steering-gears-1175750) · I**
- *Dates / evidence:* last reply 8 Nov 2026; 3 replies. Only technical-sounding title among the 20 newest threads. Thread not opened; content not established.

**HH-19 · "Dumb Question of the Week, Barrel valve leakdown" · S**
- *Dates / evidence:* legacy ThreadID 41787 (legacy link now misdirects); approx. 2010 (inferred from ID order). Search summary, not read.
- *Job and problem:* mechanical-injection racer confused by the leak-down procedure (what the percentage is referenced to when the gauge drops on connection).
- *Resolution:* replies: re-set to 100 before the final adjustment; plug the secondary bypass. One replier has seen gauges "off as much as 10-12 psi"; another says only the difference matters but the pop-off gauge should be as accurate as possible.
- *Inference (ours):* Register: RD-028.

**HH-20 · "Hilborn Barrel Valve Help" · S**
- *Dates / evidence:* legacy ThreadID 89206 (legacy link now misdirects); approx. 2014. Search summary, not read.
- *Resolution:* confirm the valve pulls down to under 5%; worn or corroded ones cannot. Register: RD-028.

**HH-21 · Replies to "torsion bar tester" (2009; see HH-03) · S**
- *Dates / evidence:* legacy ThreadID 27849 (legacy link now misdirects); April 2009. Search summary, not read.
- *Workaround / products named (US$, 2009):* Intercomp purpose-built tester "three grand"; Roehrig and Maxwell "thousands of dollars". DIY: load cell plus a degree wheel about two feet across on the torsion arm; pull to the same angle both ways and compare ("should not vary by 10%"); poster estimate about US$100; used Intercomp coil-spring tester suggested as a load source.
- *Repeats and objections:* posters disagree on where to measure. Objection: pay a local speed shop to test bars at season start, mid-season and after any crash. Register: RD-017.

**HH-22 · "High Speed diaphram bypass help"; "ASCS pill and high speed setting" · S**
- *Dates / evidence:* legacy ThreadID 40237 (approx. 2010) and 10602 (approx. 2007) (legacy links now misdirect). Search summaries, not read.
- *Resolution:* settings cannot be advised without pump/nozzle sizes and an air-density reading; pay the "modest fee" for a flow-bench session; a builder urges buying a weather station. Register: RD-028.

**HH-23 · "Injection tuning"; "Take off issues"; "Under pressure" · S**
- *Dates / evidence:* legacy ThreadID 61043 (Tech Talk; approx. 2011–12), 55902 (approx. 2011), 108080 (4 pages; approx. 2017) (legacy links now misdirect). Search summaries, not read.
- *Workaround / products named:* chassis dyno with air/fuel and fuel-pressure read-outs recommended (also reveals a worn pump); shop tricks instead of instruments (half-closing the shut-off valve; a 1/8 in drill bit to set the barrel valve); a few pill sizes or psi on the high-speed can cause serious problems. Register: RD-028.

**HH-24 · "more 305 help please" · S**
- *Dates / evidence:* legacy ThreadID 63008 (legacy link now misdirects); approx. 2012. Search summary, not read.
- *Workaround:* a RaceSaver newcomer told to buy "the proper gauge" and have it checked when the engine is sealed, "so you know where you stand with the techs gauge and yours". Which gauge is uncertain (context suggests the valve-spring checker). Register: tech-inspection group (RD-033…037, RD-020).

**HH-25 · "Static Timing a Vertex Mag"; "Sprint Car Ignition Systems?" · S**
- *Dates / evidence:* legacy ThreadID 21862 (Tech Talk; approx. 2008) and 83995 (approx. 2013–14) (legacy links now misdirect). Search summaries, not read.
- *Job and problem:* can a beeping multimeter replace a magneto "buzz box"? One reply gives a hook-up; another never saw a buzz box. Not settled per the summary. Second thread: magnetos "checked and freshened up every year" by specialists. Register: RD-030.

**HH-26 · "tel tac repairs"; "Gearing Question" · S**
- *Dates / evidence:* legacy ThreadID 3330 (Tech Talk; 2007) and 76167 (approx. 2013) (legacy links now misdirect). Search summaries, not read.
- *Job and problem:* one-line request for a Tel-Tac repairer; no reply shown. Gearing thread: choose the gear from the memory tach's max rpm, not advertised track size. Register: RD-001.

**HH-27 · "Sprint Cars and Data Acquisition" · S**
- *Dates / evidence:* legacy ThreadID 107666 (legacy link now misdirects); 2017. Search summary, not read.
- *Repeats and objections:* hardware now "quite affordable" but needs laptop, software and analysis labour; sanctioning bodies restrict it on cost and competitive-gap grounds; some want it as a driver/setup tool. Register: RD-004/019.

**HH-28 · "TRANSPONDER DIFFERENCES???" · S**
- *Dates / evidence:* legacy ThreadID 86933 (legacy link now misdirects); approx. 2014. Search summary, not read.
- *Workaround / products named:* AMB/MyLaps (over US$400) versus Westhold (about US$230), approx. 2014; the MyLaps app gives crews immediate lap times. Register: RD-051.

**HH-29 · "sprint car and scales" · S**
- *Dates / evidence:* legacy ThreadID 28227 (legacy link now misdirects); approx. 2009. Search summary, not read.
- *Job and problem:* what scaling teaches and its limits; no complaint about scale cost or electronics.

**HH-30 · Rear-end squaring threads · S**
- *Dates / evidence:* legacy ThreadID 81864 and 83218 (approx. 2013–14) (legacy links now misdirect). Search summaries, not read.
- *Workaround / products named:* blocks-and-tape methods; the commercial Tru-Square tool praised (one endorsement reads as vendor/marketing-partner). Register: RD-042.

**HH-31 · Shock/bar dyno as a service · S**
- *Dates / evidence:* legacy ThreadID 36137 (vendor; Roehrig dynos), 75717 and 92055 (off-season checklist includes dyno-testing shocks and torsion bars) (legacy links now misdirect). Search summaries, not read; years not established. Register: RD-027.

**HH-32 · "Hot Shot Engine Heater"; "How Cold?" · S**
- *Dates / evidence:* legacy ThreadID 53266 (approx. 2011) and 117523 (approx. 2021) (legacy links now misdirect). Search summaries, not read.
- *Workaround:* heaters are universal; one needs a large generator.

**HH-33 · "Xtreme Fuel Stick" · S**
- *Dates / evidence:* legacy ThreadID 83602 (legacy link now misdirects); approx. 2013–14. Search summary, not read.
- *Workaround / products named:* users call the electronic fuel dipstick "very accurate"; one "would not go back" to a plain stick. Price not stated. Nearest register record: RD-048.

**HH-34 · "Driver Severely Burned" · S**
- *Dates / evidence:* legacy ThreadID 31102 (legacy link now misdirects); 2009. Search summary, not read.
- *Job and problem:* one poster notes 600 cc micros' electric fuel pumps keep running after a crash "unless the driver turns it off". A later thread (legacy ThreadID 121124, approx. 2022) shows a track banning electric pumps / requiring a tank shut-off. Single post; no register record.

**HH-35 · Traction-control detection threads · S**
- *Dates / evidence:* legacy ThreadID 31611, 22696, 25752, 6630 (approx. 2007–09) (legacy links now misdirect). Search summaries, not read.
- *Repeats and objections:* hidden devices in ignition boxes/tachs; officials would need to open or bench-test boxes; enforcement rare. Register: RD-033…037 group, RD-020.

**HH-36 · Wing-angle rule threads · S**
- *Dates / evidence:* legacy ThreadID 24331, 97908, 98115 (approx. 2008–2015) (legacy links now misdirect). Search summaries, not read.
- *Workaround:* wing angle "easily and quickly measured with a digital level" at the scales.

**HH-37 · Tyre threads · S**
- *Dates / evidence:* legacy ThreadID 113139 (approx. 2019) and 104623 (approx. 2016) (legacy links now misdirect). Search summaries, not read.
- *Job and problem:* start pressures 4.5–6.0 psi; 1–3 psi gain without bleeders; nitrogen in rears; durometer rules in a 305 class. Register: RD-003 (gauge trust).

**HH-38 · EGT (exhaust gas temperature) thread · S**
- *Dates / evidence:* legacy `forumDU.cfm?ThreadID=72496` (legacy link now misdirects); approx. 2012–13. Search summary, not read.
- *Repeats and objections:* an experienced tuner calls EGT "worthless" on constant-flow injection; dyno shops still read plugs.

#### Products and prices named

All forum prices are historical (dated at post). W figures are listing snapshots with unknown capture dates.

| Product | Price as stated | Date | Source type |
| --- | --- | --- | --- |
| Swindell electronic bleeders | "additional $900" over Conroy; "$1,200.00"; "$1000" (US$) | 8 Jul 2015; 9 Jul 2015; 25 May 2017 | forum post read (HH-01); current price not found in two off-site searches |
| Conroy diaphragm axle bleeder kit | US$350 per set | 8 Jul 2015 | forum post read (HH-01); off-site web-search summary: US$357.89–359.99 at three retailers, capture date unknown |
| Conroy Pneu bleeder kit | not stated in forum | not stated | off-site web-search summary: US$224.97–249.99, capture date unknown |
| Plug-in wheel bleeders | "$20" | 10 Jul 2015 | forum post read (HH-01); off-site web-search summary: Kwik Change large bleeder US$37.99 each, economy bleed kit US$260.99, capture date unknown |
| Kwik Change 713-300 hand pump for setting bleed-offs (0–30 psi); "bleeder setting tank" | not captured | not stated | off-site web-search summary (result titles only) |
| Willy Willy Tire Pressure Stabilizer | kit US$1,350 plus tax/shipping | promotional page referring to the 2025 season; capture date unknown | off-site web-search summary (promotional page; works with Conroy or Swindell bleeders per the maker) |
| AccuForce torsion bar dyno | "mid $5000.00 range" | 23 Jan 2011 | forum post read (HH-02, promotional); sought used in 2017 and 2023 (index rows HH-06, HH-07); off-site search found no current page |
| Intercomp torsion bar tester | "three grand" | 2009 | search summary of forum post (HH-21); tube type per HH-02; off-site search found none in current listings |
| Maxwell Industries torsion testers | "thousands of dollars" | 2009; named again Jan 2011 | search summary of forum post (HH-21); forum post read (HH-02) for the 2011 mention; off-site: 2013 trade piece only |
| DNK "Design & Knowledge" manual tester | not stated | Jan 2011 | forum post read (HH-02); small-run, apparently discontinued; off-site search found nothing |
| Maxim X-Check checker/rater | not stated ("how much" unanswered) | Jun 2010; Apr 2020 | index row only (HH-04, HH-05); off-site search found nothing |
| DIY load-cell plus degree-wheel rig | about US$100 (poster's estimate) | 2009 | search summary of forum post (HH-21) |
| Intercomp digital coil-spring tester, 5,000 lb | US$1,295 | not stated | off-site web-search summary (two retailer listings) |
| Leak-down testers sold for barrel-valve setting | US$73.59–154.99 | not stated | off-site web-search summary (JEGS, Total Seal, Good Vibrations, Longacre) |
| Longacre 52-73016 barrel-valve setting tool | US$144.99 | not stated | off-site web-search summary |
| King Racing Products high-speed checker, 0–160 psi / digital 0–300 psi | US$255.99 / US$331.97 | not stated | off-site web-search summary |
| Australian-listed high-speed tester | A$465.27–489.76 | not stated | off-site web-search summary (Australian retailer) |
| Magneto timing boxes / synchronisers | US$52–131; DIY about US$45 | not stated | off-site web-search summary (Speedway Motors box US$90.99) |
| Tel-Tac II; Oval Track Pro | US$324.99–359.81; about US$453–469 | not stated | off-site web-search summary (Australian listings A$652.80 and A$801.68, both shown sold out) |
| AMB/MyLaps vs Westhold transponders | over US$400 vs about US$230 | approx. 2014 | search summary of forum post (HH-28) |
| Xtreme Fuel Stick (Safety First USA) | not stated | approx. 2013–14 | search summary of forum post (HH-33); also off-site web-search summary |

Brands named that are not yet in the competitor lists: AccuForce, Maxwell Industries, Maxim X-Check, the DNK tester, Quick Racing Products, OC Shocks, Competition Suspension Inc., Tru-Square, Safety First USA / Xtreme Fuel Stick, Westhold, King Racing Products, Total Seal, Good Vibrations Motorsports, TI22, Hot Shot, Big Toob.

#### Low-yield searches and sections

- Live title searches: "tester" returned only the two torsion-bar threads in 60,760; "gauge" 4 (one name match, one wanted ad, one vendor panel, one go/no-go gauge); "bleeder" 3; "scaling" 5 news items; "pop off tester" 0.
- The newest 20 General-board threads contained no technical thread.
- **Not searched or read because of the access blocks:** title searches for tach, scale, inject, magneto, dyno, stagger, pill, leak, transponder, raceceiver, homemade, pressure, nozzle, data, tool, torque, ride height and barrel valve; thread reads of the 2009 torsion thread, "Torsion Bar Adjustment", both wanted ads and "Air bleeders", and everything those searches would have surfaced.
- Domain-filtered web searches with no relevant hits: raceceiver/radio problems; valve-spring tester; micro-sprint tach/shift light/logger; wing-slider position gauge; power-steering pressure testing; kill-switch/ignition wiring diagnosis; wideband/O2 on methanol; stopwatch/GPS lap timing; nitrogen/air tank/inflation tools; brake bleeding/pressure; "made my own"/"built my own"; "overpriced"/"too expensive" for tools (only general cost-of-racing complaints and the bleeder thread); "does anyone make" (returned the torsion threads again).
- Off-site searches that found nothing: current pages/prices for Swindell bleeders, AccuForce, Maxim X-Check, DNK and an Intercomp torsion tester; what "DSR" leak-down gauge refers to.
- Topics that looked already well served on this evidence: injection leak-down and high-speed checkers, magneto timing boxes, rear-end squaring, shock dyno services, transponders/lap times, engine heaters, wing-angle measurement, fuel dipstick, mechanical bleeders and bleeder setters.
- No micro-sprint or midget technical board exists on the new platform, so micro/midget-specific electronics could not be examined.

#### Unknowns

- **Thin direct evidence:** two threads read in full (HH-01, HH-02); the torsion-bar and bleeder evidence is reasonably grounded, while the injection, ignition, tach, fuel, logger and inspection topics rest on search-engine paraphrases and retailer snapshots.
- Whether a cheap torsion comparator already exists: the Maxim X-Check, the DNK unit and the current Intercomp offering could not be confirmed in or out of production, or priced.
- Whether racers would trust and pay for a comparative (not absolute) torsion reading: the forum shows the framing, not a purchase.
- Patent position around axle-mounted electronic bleeders (granted claims, expiry, Australian coverage): only database summaries were seen.
- Current prices of electronic bleeders, AccuForce/Maxwell torsion dynos and the fuel stick.
- Recency and venue: nothing technical after 2023 was seen; today's racer conversation has probably moved to social media or private groups (inference, unchecked). The evidence describes 2009–2017 US racers.
- Lost material: the legacy Tech Talk board (about 150 threads) and the 2009 thread's replies were not readable; register links need replacing with the new URLs given above.
- Selection bias: a popularity-weighted search-engine subset plus title-only site search, so absence of a topic is weak evidence of absence. US rules (bleeders, data acquisition, engine sealing) may not match Australian classes.

### KartPulse

#### Coverage and access
- Read anonymously on 2026-11-17 through the forum's public JSON endpoints (Discourse), with no login, posting or vendor contact. Eight categories had their topic listings crawled in full: 6,652 unique titles, created 2016-10-17 to 2026-11-16. About 1,850 titles were read by eye; the rest were screened by keyword only.
- 87 topics were fetched with their posts. About 72 were read end to end, with long posts truncated and key posts read in full. 15 long threads were read through keyword filters plus selected posts. The 28 ledger entries below cover about 75 of these threads.
- Posters are mostly US owner-driver club racers and karting parents (LO206, KA100, X30, Rotax, ROK, KZ). A minority post from Australia, the UK/Europe, Canada, Brazil, the UAE, Trinidad and China. Rental racers appear only in the timing threads. Professional teams are mentioned but rarely post. Vendors and makers are flagged in each entry.
- Search: 30 queries, first results page only. Free-text complaint phrases returned mostly off-topic matches. Title screening was far more productive.
- Access limits: the print-style export stopped working after the first few topics (an HTTP 422, apparently a rate limit), so later topics were fetched in chunks. No HTTP 429 was seen. Images, attachments and outbound links were not opened, so anything shown only in a photo is unknown. Six web-search queries were used to sanity-check current products and prices, and they are labelled as search summaries.
- Not read: very large megathreads (what-did-you-do, tyre diagnosis, the 743-post electric-karting thread, seat position, wheels, AiM software comparison, carb jetting). Software and app promotion threads were skipped as out of scope. Classifieds, Race Reports, Other Motorsports/Sim, Podcasts and Announcements were not crawled.
- The register's earlier KartPulse sample (the MyChron 6 thread page 14 and the race-day efficiency thread) was not re-read.
- Forum prices below are as stated in the post on the post date and are historical, not current. Poster identities are withheld.

#### Threads

**KP-01 · [Best tire Pressure Gauge for Karting](https://forums.kartpulse.com/t/best-tire-pressure-gauge-for-karting/4027)**
- *Dates / evidence:* started 2019-05-22, revived 2020-09-08, last reply 2020-09-14. 37 posts, 21 posters, about 10.8k views. Thread read.
- *Who:* mostly US owner-driver club racers, plus one forum founder. Customers, not vendors.
- *Job and problem:* set and check kart tyre pressures (about 5-15 psi) repeatably. Cheap gauges are called unreliable. Analogue Longacre needles creep or fail (about 3 users, 2019-07 and 2020-09). Gauges drift after drops and two team-mates' gauges disagree.
- *Workaround / products named:* Longacre analogue about US$30 and about US$60; Longacre Semi-Pro digital about US$80; Intercomp digital about US$300 (2019-05); Prisma about US$190, US$220 with stopwatch (2020-09); Unipro UniTire IR about US$300 (2020-09); Alfano gauges ("quite expensive", no figure); Motion Pro (maker spec ±0.6 psi).
- *Resolution:* no consensus.
- *Repeats and objections:* several moved to Prisma. Others say stay with the US$30 Longacre. One says $300 is a "hard pass". Repeatability may matter more than absolute accuracy.
- *Inference (ours):* the unmet need looks like trust in a gauge, not features. Register: RD-003, class 2.

**KP-02 · [Prisma Air Gauge Vs Longacre Digital Pro](https://forums.kartpulse.com/t/prisma-air-gauge-vs-longacre-digital-pro/12252)**
- *Dates / evidence:* 2024-04-29 to 2024-05-06. 8 posts, 7 posters. Thread read.
- *Who:* owner-drivers, one staff racer. Customers.
- *Job and problem:* decide whether a Prisma is worth about double a Longacre Digital Pro (no prices given).
- *Workaround / products named:* Prisma (about a decade old, still accurate, per one staff user); Longacre digital (10+ years, still fine, per another).
- *Resolution:* the original poster bought a Prisma and said he had already learned a lot about his pressures.
- *Repeats and objections:* one user found his new Prisma matched his 7-year-old Longacre "down to the tenth" and keeps it as a backup or benchmark.
- *Inference (ours):* the premium and mid slots look occupied and durable, which argues against a gap for another ordinary digital gauge. The benchmark habit shows a wish to verify gauges. Register: RD-003, class 2 / partly class 5.

**KP-03 · [Anyone using the new Prisma HiPreMa4 Tire Pressure/Temperature Gauges?](https://forums.kartpulse.com/t/anyone-using-the-new-prisma-hiprema4-tire-pressure-temperature-gauges/6142)**
- *Dates / evidence:* 2020-07-01 to 2020-08-17, 3 posts, 2 posters. Related thread [UniPro UniTire](https://forums.kartpulse.com/t/unipro-unitire/10487): 2023-04-19/20, 2 posters.
- *Who:* owner-drivers. Customers.
- *Job and problem:* use combined pressure and temperature gauges. HPM4 owner reported firmware and display bugs (hot pressures not shown, tyre temperatures not recordable). A UniTire owner said it randomly loses stored pressures. A second user had wrong readings and saving problems.
- *Workaround / products named:* Prisma HPM4 plus thermocouple pyrometer; UniPro UniTire. No prices given.
- *Resolution:* vendor suspected an EEPROM fault and replaced the HPM4 (outcome not reported). The second UniTire user returned it and bought a Prisma without timing, with no problems since.
- *Repeats and objections:* founder called the HPM4 not a common unit.
- *Inference (ours):* the reported faults sit in the memory and recording layer (2 products, 3 users), which supports keeping logging out of a first gauge. Register: DEC-013 (no class given in source).

**KP-04 · [Kart Tyre Temperature Data](https://forums.kartpulse.com/t/kart-tyre-temperature-data/3752)**
- *Dates / evidence:* started 2019-04-02; key posts 2021-04-03, 2021-05-11/17, 2023-01-18/20; last reply 2023-01-20. 50 posts, 23 posters, about 7.6k views. Thread read.
- *Who:* owner-drivers and parents; one data-savvy helper who dropped an e-box-input design when AiM launched its own.
- *Job and problem:* know tyre temperatures on track or quickly in the pits. AiM IR kit US$660 (2019-04) called "obscenely high"; real analysis needs three sensors per tyre.
- *Workaround / products named:* US$20 IR gun; Alfano Tyre Control V2 probe; US$34 K-type probe into the MyChron e-box (2023-01); DIY Arduino plus IR sensors (no finished build reported).
- *Resolution:* none commercial. The one AiM IR user (2021) saw no lap-time link to the tyre maker's temperature window.
- *Repeats and objections:* about 5 users want logged temperatures, about 5 are content with gun or probe. Objections: surface is not core temperature, mounting is hard, little to learn from the data.
- *Inference (ours):* real curiosity, weak willingness to pay. Register: RD-046, class 2; on-kart IR variant RD-086/RD-071, class 3.

**KP-05 · [DIY Tire Temp Monitoring with Arduino](https://forums.kartpulse.com/t/diy-tire-temp-monitoring-with-arduino/1792)**
- *Dates / evidence:* started 2018-03-14, outcome post 2019-02-27, last reply 2019-03-03. 15 posts, 7 posters, about 8.0k views. Thread read.
- *Who:* owner-driver hobbyist builder. Not a vendor.
- *Job and problem:* log tyre temperature cheaply because the AiM kit was out of his price range. His build (Arduino Uno, LCD, MLX90614 sensors at about US$12 each, 2018-03) was useful at one race, but the thin wires broke again.
- *Workaround / products named:* he then bought the AiM tyre-temperature kit. Stone Kart Company (Slovenia) in-rim wireless monitoring "around $300" (post 2019-03-03; poster not a vendor; unverified).
- *Resolution:* builder switched to the incumbent.
- *Repeats and objections:* one sensor per tyre misses camber and pressure gradient; three are needed.
- *Inference (ours):* the DIY route failed on wiring robustness and mounting rather than electronics. Register: RD-046 / RD-086 cluster, class 3 at best.

**KP-06 · [Kart Tire Temps](https://forums.kartpulse.com/t/kart-tire-temps/15367)**
- *Dates / evidence:* 2026-04-01 to 2026-04-04. 4 posts, 4 posters. Recent. Thread read.
- *Who:* experienced owner-driver and data coach; an AiM customer.
- *Job and problem:* fit AiM single-channel IR sensors to a MyChron 6 via an expansion unit. Needed an auxiliary lithium battery. The AiM bracket kit did not fit his chassis well, so he made a larger aluminium bracket. 3D-printed rear holders broke after two sessions.
- *Workaround / products named:* AiM IR sensors and brackets; no prices given.
- *Resolution:* working after his own fabrication; configuration took minutes.
- *Repeats and objections:* another user's kit order a year earlier was cancelled after a long delay. A third wants a simple per-tyre "in the window" colour light and suggests sidewall temperature may matter more.
- *Inference (ours):* the incumbent exists but fitting it is still a bracket and power problem, which is chassis-specific. Register: RD-046, class 2 (interesting data, no stated purchase need).

**KP-07 · [Simple laptimer and data logger](https://forums.kartpulse.com/t/simple-laptimer-and-data-logger/2944)**
- *Dates / evidence:* 2018-10-30 to 2018-11-10. 36 posts, 8 posters, about 5.9k views. Thread read.
- *Who:* ex-owner racing amateur team races in rental karts; a different venue and kart each time. Customer.
- *Job and problem:* a standalone GPS lap timer with live display, no wiring, moved between karts in seconds. Nothing mounts quickly to an arbitrary rental wheel.
- *Workaround / products named:* AiM Solo with magnetic bracket (about US$15) and zip tie; Velcro or dual-lock; pouch round the wheel boss. MyChron 5 cost GBP 200 more than a Solo 2 (2018). Phone GPS rejected.
- *Resolution:* none reported.
- *Repeats and objections:* one other rental-league racer and a staff remark that people ask about rental timing. Founder: nothing on the market suits the portability need.
- *Inference (ours):* the gap looks like a universal tool-less mount, not a new timer. Register: RD-094, class 5 (timer); RD-075, class 3 (mount).

**KP-08 · [Racing without a gauge](https://forums.kartpulse.com/t/racing-without-a-gauge/9622)**
- *Dates / evidence:* 2022-09-07 to 2022-09-09. 23 posts, 11 posters. Thread read.
- *Who:* owner-driver (KA100 and a shifter). Customer; one replying dealer.
- *Job and problem:* his out-of-warranty MyChron 5 2T failed (screen came loose and destroyed the board); replacements were unavailable in the 2022 shortage. He asked about rigging a voltmeter and 9V battery for EGT, and wished for an EGT-only MyChron.
- *Workaround / products named:* used Alfano Pro for about US$50-100 (2022-09, several users); a dealer said he had MyChron 5S in stock.
- *Resolution:* advice was to run without a gauge or buy used.
- *Repeats and objections:* you do not need a gauge on a KA100; Alfano battery life praised over MyChron's.
- *Inference (ours):* a single-function fallback was asked for once and the used market covers it. Register: RD-025, class 2 (weak); RD-095, class 5.

**KP-09 · [Ideas for a Quick Install/Release for Dataloggers: MyChron, Alfano etc](https://forums.kartpulse.com/t/ideas-for-a-quick-install-release-for-dataloggers-mychron-alfano-etc/10973)**
- *Dates / evidence:* 2023-07-26 to 2023-08-05, 10 posts, 7 posters. Related: [RaceBox MINI](https://forums.kartpulse.com/t/racebox-mini-new-datalogging-product/8756) (2022-02-15 to 2023-03-10, 24 posts); [Alfano vs mychron vs phone](https://forums.kartpulse.com/t/alfano-vs-mychron-vs-phone/12728) (2024-08-16/17, 5 posters).
- *Who:* forum founder (two karts, rental track operator), rental racers in Europe and the UAE. Customers.
- *Job and problem:* tool-less swap of a MyChron 5 between karts.
- *Workaround / products named:* wingnut, thumb-nut, hand nut; a rental wheel support (maker not established); a track in the UAE sells holders. RaceBox Mini about US$160 (crowdfunding, 2022-02).
- *Resolution:* solved with about US$12 of knurled nuts.
- *Repeats and objections:* staff say people ask about rental timing; MyChron battery called "a bit of a joke".
- *Inference (ours):* quick-release is solved by commodity hardware; rental mounting is a small unverified niche. Register: class 5 for owner karts (no RD number given).

**KP-10 · [Scaling. How important is cross weight?](https://forums.kartpulse.com/t/scaling-how-important-is-cross-weight/5173)**
- *Dates / evidence:* started 2020-02-09, main discussion to 2020-03-15, revived 2022-12-10/13. 60 posts, 23 posters, about 12.8k views. Companion thread [Best Scales to use?](https://forums.kartpulse.com/t/best-scales-to-use/5189) 2020-02-12, 4 posters.
- *Who:* owner-drivers, mostly LO206 (where scales are common); rare in 2-stroke paddocks.
- *Job and problem:* corner-weight a kart. Results are meaningless unless pads are level and co-planar; few have a level floor; some give up.
- *Workaround / products named:* floor shims, levelled painted rectangles, shop tables, KartBalance app (about US$3, 2020-03), used Tanner digital scales US$200, used Longacre set US$450 split between two racers (2020-02); an unbuilt levelling stand estimated US$1,500-2,000 (2020-02).
- *Resolution:* none.
- *Repeats and objections:* have a shop do it; many 2-stroke racers never scale.
- *Inference (ours):* the pain is levelling and reference, not indicator electronics. Register: RD-018, class 4; RD-049 no evidence of reader faults.

**KP-11 · [Anyway to test 2 stroke wiring harness?](https://forums.kartpulse.com/t/anyway-to-test-2-stroke-wiring-harness/12968)**
- *Dates / evidence:* 2024-10-03 to 2024-11-14, 17 posts, 7 posters. Also read: [IAME X30 Stator test](https://forums.kartpulse.com/t/iame-x30-stator-test/6400) (2020-08-24, revived 2024-10); [KA wouldn't start](https://forums.kartpulse.com/t/ka-wouldnt-start-and-now-wont-crank/12240) (2024-04 to 2024-07, 54 posts); [Rotax pick-up resistance](https://forums.kartpulse.com/t/rotax-max-pick-up-resistance-measurement-in-ohms/12147) (2024-04 to 2024-10, 32 posts).
- *Who:* owner-drivers and parents with electric-start TaG engines. Customers.
- *Job and problem:* locate an intermittent no-start (harness, switch, battery, starter, stator, pickup, coil). Stator resistance readings did not separate good from failed units.
- *Workaround / products named:* swap parts between karts, a KA100 harness with home-made adapter on a VLR, bypass the kill switch, multimeter; NOCO charger. No tester named. No prices given.
- *Resolution:* case by case; one Rotax thread's cause was the airbox.
- *Repeats and objections:* title screen only: 66 topic titles on starting/spark/starters/harnesses (28 since 2023), not individually read. A multimeter plus wiring print, or swapping parts, is seen as enough.
- *Inference (ours):* the most repeated electrical pain but engine-family-specific, with no explicit request for a product. Register: RD-029 and RD-083 nearest, class 3.

**KP-12 · [Rotax Battery Charger Alternatives](https://forums.kartpulse.com/t/rotax-battery-charger-alternatives/15838)**
- *Dates / evidence:* five threads, 2022-03 to 2026-08; this one 2026-08-26 to 08-29 (15 posts, 8 posters). Others: [Rotax killing batteries](https://forums.kartpulse.com/t/rotax-killing-batteries-in-half-a-session/8872) (2022); [Lipo battery on x30?](https://forums.kartpulse.com/t/lipo-battery-on-x30/11251) (2023-10 to 2025-01, 74 posts); [Rotax Max Voltage Display](https://forums.kartpulse.com/t/rotax-max-voltage-display-and-battery/11742) (2024-01); [Rotax Lithium Batteries?](https://forums.kartpulse.com/t/rotax-lithium-batteries/14180) (2025-05).
- *Who:* owner-drivers (Rotax, X30, ROK). Customers.
- *Job and problem:* keep starter batteries alive; charger seen as steep; batteries dying mid-session (vibration blamed); a wish for a live battery display; two first-hand LiPo fire reports.
- *Workaround / products named:* Rotax charger US$125 (2026-08); LiFePO4 packs US$35-69 (2023-12 to 2025-05); Shorai US$125, Banshee US$79 (2024-01); NOCO, Battery Tender; a kart-specific lithium unit reported discontinued (2025-01). Rotax Max Challenge requires the official battery (stated 2025-05).
- *Resolution:* yes, with commodity items.
- *Repeats and objections:* a US$10 voltmeter answers the low-voltage wish.
- *Inference (ours):* no electronics lead. Register: RD-083, class 5.

**KP-13 · [Mychron + EGT: which sensor to buy, and how to install](https://forums.kartpulse.com/t/mychron-egt-which-sensor-to-buy-and-how-to-install/8617)**
- *Dates / evidence:* 2022-01-25 to 2022-02-05, later question 2025-02-09; 20 posts, 11 posters, about 8.6k views. Related: [EGT sensors AIM vs Unipro](https://forums.kartpulse.com/t/egt-sensors-aim-vs-unipro/14697) (2025-09-20); [MyChron 5 EGT on Alfano 7?](https://forums.kartpulse.com/t/mychron-5-egt-sensor-on-alfano-7/12630) (2024-07); [Sensor and IR Receiver Compatibility](https://forums.kartpulse.com/t/mychron-alfano-sensor-and-ir-receiver-compatibility/7375) (2021-05); [EGT sensor repair](https://forums.kartpulse.com/t/mychron-egt-sensor-repair/11573) (2023-12, unanswered).
- *Who:* owner-drivers adding EGT to a MyChron. Customers.
- *Job and problem:* confusing sensor range, bung thread mismatch (the OP welded one nut onto another), probe styles reading 100-150 °F apart, unclear cross-brand reuse.
- *Workaround / products named:* forum guidance; no prices given.
- *Resolution:* OP installed it with forum help.
- *Repeats and objections:* about 5 users hit fitment issues. One long-time user saw no difference between cheap and expensive probes.
- *Inference (ours):* friction is fitment and documentation; dealers already sell adapters. Register: RD-025, class 2 (accessories); overlaps RD-072/073-type suggestions.

**KP-14 · [How crucial is a lambda sensor?](https://forums.kartpulse.com/t/how-crucial-is-a-lambda-sensor/11986)**
- *Dates / evidence:* 2024-03-03 to 2025-11-27, 16 posts, 10 posters. Also [Lambda sensors in karting?](https://forums.kartpulse.com/t/lambda-sensors-in-karting/620) (2017-05 to 2021-04, 27 posts, about 13.9k views) and [LCU1S install on Mini Max](https://forums.kartpulse.com/t/tips-for-installing-lcu1s-afr-lambda-sensor-on-rotax-mini-max-exhaust/13915) (2025-03, unanswered).
- *Who:* owner-drivers, one AiM dealer (2017), a coach.
- *Job and problem:* tune carburation with weather. An Australian X30 racer (2024-03) said everyone in his class has one. Target numbers are disputed and partial-throttle readings on a piped 2-stroke are unreliable.
- *Workaround / products named:* AiM lambda controller US$400 (AiM dealer, 2017-05), called a tough sell; narrowband gauge US$20-60 (2017-05); heater needs a full-size battery.
- *Resolution:* buyers pointed to AiM LCU-One via MyChron (2025-11); pipe-specific install help missing.
- *Repeats and objections:* "not crucial on a hobby level"; a champion coach says people over-watch the dash.
- *Inference (ours):* a light-bar AFR indicator is conceivable but rests on a disputed measurement. Register: RD-082/RD-084, class 2; class 5 for MyChron owners.

**KP-15 · [Front End Alignment without Snipers?](https://forums.kartpulse.com/t/front-end-alignment-without-snipers/8965)**
- *Dates / evidence:* six threads, 2018-12 to 2026-03; this one 2022-04-06 to 04-13 (15 posts, 8 posters). Others: [When to buy snipers](https://forums.kartpulse.com/t/when-to-buy-snipers/5108) (2020-01); [Gyraline alignment tool](https://forums.kartpulse.com/t/anyone-tried-the-gyraline-alignment-tool-on-a-kart/15321) (2026-03); [Sniper works only after sun](https://forums.kartpulse.com/t/sniper-alignment-lasers-only-works-after-sitting-in-sun/3195) (2018-12); [Broken sniper](https://forums.kartpulse.com/t/broken-sniper/7993) (2021-09); [Sniper battery cap](https://forums.kartpulse.com/t/sniper-battery-cap-where/9234) (2022-06).
- *Who:* owner-drivers. Customers.
- *Job and problem:* set toe, camber and caster. Sniper called "way beyond my budget" for casual use. Weak or dead lasers revived by warming (at least 5 owners); a cracked cap was unobtainable.
- *Workaround / products named:* Sniper US$300 (2022-04); borrow a set; tape measure; DIY angle-iron plates about US$15 (2022-04, two builders).
- *Resolution:* none needed; owners rate Snipers highly.
- *Repeats and objections:* a 2026 post dismisses Gyraline as less kart-suited.
- *Inference (ours):* entrenched, liked incumbent. Register: RD-042/RD-043, class 2 (reinforces the recorded blocker).

**KP-16 · [Measuring rear track width - Ideas for a non PITA method?](https://forums.kartpulse.com/t/measuring-rear-track-width-ideas-for-a-non-pita-method/11198)**
- *Dates / evidence:* 2023-09-17 to 2024-03-01, 29 posts, 22 posters, about 1.8k views. Also [Rear Track Width Adjustment Tool](https://forums.kartpulse.com/t/rear-track-width-adjustment-tool/15589) (2026-06-03 to 07-22, 14 posts, 10 posters).
- *Who:* owner-drivers working alone. Customers; one commercial gauge linked by the founder.
- *Job and problem:* set and measure rear width (legal maximum 1400 mm) solo at the track; a chore alone.
- *Workaround / products named:* tape through the axle, KartMaster spacer rings (most popular), marks on axle, trammel bar, US$17 bar clamp, a New Zealand-made T-square gauge, AMK Karting (Belgium) gauge linked 2024-02-27 (price not captured).
- *Resolution:* comprehensively solved with cheap methods.
- *Repeats and objections:* "no need to complicate it"; one racer only wants wider or narrower.
- *Inference (ours):* frequent but solved, and mechanical rather than electronic. Register: RD-042, class 5.

**KP-17 · [Open source, affordable, portable small engine dyno](https://forums.kartpulse.com/t/open-source-affordable-portable-small-engine-dyno/14978)**
- *Dates / evidence:* 2025-12-04 to 2026-01-29, 37 posts, 12 posters, about 1.5k views. Also [DIY Kart Dyno Using a Mychron](https://forums.kartpulse.com/t/diy-kart-dyno-using-a-mychron-rear-axle-mounted/7444) (2021-05, about 11.1k views) and [Kart Dyno Talk](https://forums.kartpulse.com/t/kart-dyno-talk/10964) (2023-07). Two more seen by title only.
- *Who:* the OP is a maker/vendor (Pit Row Dyno) selling small 4-stroke dynos and an electronics-only package. Others are builders and tuners.
- *Job and problem:* low-cost dyno data capture. Maker's parts list (post 2025-12-04) included ESP32 touchscreen US$34, load-cell amplifier US$3, 50 kg load cell US$30, hall sensor US$4, hydraulic brake US$25. By 2026-01-28 he had shipped "a few" units.
- *Workaround / products named:* Pit Row Dyno; own prices not found.
- *Resolution:* a small vendor now supplies it; no independent user review yet.
- *Repeats and objections:* about 6 users want to build or buy. Objections: manual load control hurts repeatability; a 2-stroke needs a bigger absorber.
- *Inference (ours):* a small audience of builders and tuners, with probable high support burden. Register: not present, class 1 against the register; partly class 5 in the market.

**KP-18 · [Using leakdown to diagnose valve life?](https://forums.kartpulse.com/t/using-leakdown-to-diagnose-valve-life/11308)**
- *Dates / evidence:* 2023-10-08 to 2024-01-10, 62 posts, 14 posters, about 2.6k views. Also [LO206 head leakdown fixture](https://forums.kartpulse.com/t/lo206-cylinder-head-leakdown-test-fixture/15781) (classified, 2026-08-03) and [Clutch engagement RPM for 206](https://forums.kartpulse.com/t/technique-for-checking-clutch-engagment-rpm-for-206/9557) (2022-08 to 2023-02, 14 posts).
- *Who:* LO206 racers and parents; one hobbyist maker selling a mechanical fixture.
- *Job and problem:* judge when to re-cut valves by leak-down; separately, check clutch engagement RPM (users were reading lock-up).
- *Workaround / products named:* OTC 5609 tester ("very reasonable", no figure, 2024-01); hobbyist head fixture, last one US$150 shipped (2026-08, classified).
- *Resolution:* clutch question resolved by forum explanation; no tool requested.
- *Repeats and objections:* two users happy with the OTC tester.
- *Inference (ours):* adequately solved by an automotive tester; the fixture is machining, not electronics. Register: RD-099, class 5.

**KP-19 · [Measuring Jets/Atomizers](https://forums.kartpulse.com/t/measuring-jets-atomizers/12205)**
- *Dates / evidence:* 2024-04-21 to 2024-04-29, 23 posts, 9 posters, about 1.5k views. Thread read.
- *Who:* owner-drivers with Dell'Orto carburettors. Customers.
- *Job and problem:* check jet sizes; users report stamped main jets measure larger than stamped (pin-gauge kits, typically 4-13 points) while atomisers are near exact.
- *Workaround / products named:* pin gauge kits; Black Racing Engines flow-tested relabelled jet kits. No prices given.
- *Resolution:* OP bought pin kits and confirmed the findings.
- *Repeats and objections:* jets are calibrated by flow, not diameter; own jets make variance irrelevant; one user says it never cost a race win.
- *Inference (ours):* the problem is real among about 9 karters but already served. Register: RD-039, class 4.

**KP-20 · [Weather Station](https://forums.kartpulse.com/t/weather-station/11999)**
- *Dates / evidence:* 2024-03-05, 2 posters. Also [Any Weather Experts?](https://forums.kartpulse.com/t/any-weather-experts/12219) (2024-04-23/24, 10 posters) and [AF Radiator Curtain for IAME X30](https://forums.kartpulse.com/t/af-radiator-curtain-for-iame-x-30/9943) (2022-11 to 2025-06, 21 posts, 11 posters).
- *Who:* owner-drivers, one in the UK/Europe.
- *Job and problem:* find a radiator-temperature or air-density gauge (poor EU availability); predict rain; manage radiator temperature without taping the radiator.
- *Workaround / products named:* Kestrel 5100 Motorsport (no price stated, 2024-03); density altitude from an online station; radar apps; roller curtains, Y-type thermostats, MyChron alarm LEDs. An electric curtain brand was asked about in a 2020 thread (title only, not read).
- *Resolution:* each user settled on an existing option.
- *Repeats and objections:* one user's EU availability complaint only.
- *Inference (ours):* water temperature is solved mechanically and there is no electronics lead. Register: RD-085, class 5.

**KP-21 · [One way radios in sprint racing](https://forums.kartpulse.com/t/one-way-radios-in-sprint-racing/13565)**
- *Dates / evidence:* 2025-01-19 to 01-23, 9 posts, 5 posters. Also [Racing Radios/Communication](https://forums.kartpulse.com/t/racing-radios-communication/15274) (2026-03); [What's the best 2 way comms](https://forums.kartpulse.com/t/whats-the-best-2-way-comms/11088) (2023-08/09, 18 posts); [Helmet Comms: arai sk6](https://forums.kartpulse.com/t/helmet-comms-arai-sk6/9259) (2022-06 to 07, 29 posts).
- *Who:* owner-drivers, parents, staff racers. Customers.
- *Job and problem:* hear race control (one US sprint track mandated one-way radios for 2025; another track uses Raceceiver); separately, practice coaching comms (banned in sprint races). Cheap handhelds and earbuds were unsatisfactory (2 users); Nitro Bee earbuds criticised.
- *Workaround / products named:* Raceceiver, Nitro Bee, used Raceceiver units "100 & up" (US$, classified 2022); Trac-Com, Rugged Radios, Sena/Cardo recommended or tried.
- *Resolution:* one-way receivers are served by existing brands.
- *Repeats and objections:* at least 5 users dissatisfied with cheap two-way options (2022-2026).
- *Inference (ours):* adjacent-market evidence for the same product class as RD-002; practical issues are channel compatibility and earpiece fit. Register: RD-002, class 2; RD-110, class 2 (weak fit).

**KP-22 · [MyChron 6 Discussion megathread](https://forums.kartpulse.com/t/mychron-6-discussion-comparison-reviews-etc/13272)**
- *Dates / evidence:* started 2024-12-13; posts relied on 2024-12-14, 2025-01-17, 2025-04-17, 2025-06-05, 2025-12-11; last reply 2026-07-20. 274 posts, 52 posters, about 15.3k views. Keyword-filtered plus selected posts; NOT every post read.
- *Who:* owner-drivers, parents, coaches, an AiM-affiliated trainer.
- *Job and problem:* price (about US$550 expected at launch, 2024-12; "not enough to drop another $600-$700"). One coach wished for a stripped-down "dumb dash" (2024-12-14). Wishes for analogue inputs (2025-01-17) and user CAN (AiM-affiliated reply 2025-12-11: no CAN2 configuration). Missing app, sleeping unit with no RPM signal (2025-06).
- *Workaround / products named:* hobbyist DIY logger parts about EUR 205; Unipro package about US$700 (2024-12).
- *Resolution:* none.
- *Repeats and objections:* three users defend value (20+ year units, support).
- *Inference (ours):* weaknesses are casual-user price, accessory sprawl and closed integration, though owners value longevity. Register: RD-095, class 2; third-party sensors RD-072/RD-070-style, blocked by closed CAN.

**KP-23 · [Cheap timing solutions](https://forums.kartpulse.com/t/cheap-timing-solutions/13252)**
- *Dates / evidence:* 2024-12-07 to 2025-01-11, 22 posts, 8 posters. Also [Lap timer options](https://forums.kartpulse.com/t/lap-timer-options/10277) (2023-02/03, 21 posts, 15 posters, about 6.0k views); [How "Required" is a Mychron](https://forums.kartpulse.com/t/how-required-is-a-mychron-or-similar/13148) (2024-11); [Need a MyChron](https://forums.kartpulse.com/t/need-a-mychron-any-recommendations/14763) (2025-10); [Custom made data logger](https://forums.kartpulse.com/t/custom-made-data-logger/12993) (build updates 2026-06 to 2026-09).
- *Who:* new owner-drivers, a rental-league racer, hobbyist builders; one app developer (maker).
- *Job and problem:* affordable lap timing; "can't justify a 500 dollar mychron 5" (2024-12). Staff (2023): no basic timer that works with beacons.
- *Workaround / products named:* used MyChron 4 US$200+ (2023-02); MC5+MC4 pair US$450 (2024-11); RaceBox Mini US$199 sale (2024-12) plus phone; Amazon IR timers US$44 and US$72 (2023-03); Alfano 6 1T US$390 new (2023-03).
- *Resolution:* mostly met by used units or RaceBox plus phone.
- *Repeats and objections:* at least 6 independent askers (2018-2025). Objections: RPM matters even on a 206; phone on the wheel may be unsafe or banned.
- *Inference (ours):* unserved gap is a phone-free cheap dash with RPM, one temperature and lap time. Register: RD-095/RD-094, class 2; timing-only class 5.

**KP-24 · [TPMS in karting](https://forums.kartpulse.com/t/tpms-in-karting/8347)**
- *Dates / evidence:* 2021-11-29 to 2023-10-03, 16 posts, 10 posters, about 3.9k views. Also [New Tachs - Alfano 7, Mychron XX?](https://forums.kartpulse.com/t/new-tachs-alfano-7-mychron-xx-next-gen/12435) (2024-06-12 to 08-20, 25 posts, 13 posters).
- *Who:* owner-drivers. Customers.
- *Job and problem:* see pressure and temperature build, or capture hot pressures the moment the kart stops. 2021 replies: "cost prohibitive for 99% of us". A 2023 user asked about cheap Bluetooth valve-cap sensors; founder: workable only if accurate to 0.25 psi.
- *Workaround / products named:* Alfano 7 in-tyre sensor EUR 129 each (2024-06); Stone Kart Company about US$300 (2019 mention, unverified); a kart KTPMS with a fixed 0.84 bar alarm.
- *Resolution:* none.
- *Repeats and objections:* pressure rise just tracks temperature; sensor batteries; per-sensor cost.
- *Inference (ours):* an affordable brand-independent version does not appear on the forum's evidence, with high development burden. Register: RD-003 and DEC-036 relative, class 3.

**KP-25 · [Brake Pressure Sensor for Mychron](https://forums.kartpulse.com/t/brake-pressure-sensor-for-mychron/13651)**
- *Dates / evidence:* 2025-02-02 to 02-05, 9 posts, 6 posters. Also [OTK Brake pressure sensor leaking](https://forums.kartpulse.com/t/otk-brake-pressure-sensor-leaking/13815) (2025-03 to 2025-11); [MyChron5 + Coil-on-Plug](https://forums.kartpulse.com/t/mychron5-coil-on-plug/12687) (2024-08 to 11, 23 posts); [False Low RPM on Alfano 6 ADA](https://forums.kartpulse.com/t/false-low-rpm-reading-in-alfano-6-ada-when-on-throttle-lo206/10102) (2023-01 to 05). Four more seen by title only.
- *Who:* owner-drivers (KZ, OTK, LO206). Customers.
- *Job and problem:* fit AiM sensors. Brake kit is single-circuit; an OTK fitting leaked even with the supplied washer (AiM support suggested thread locker); brake lines too short for the adapter; the inductive RPM lead reads half RPM on LO206 with Alfano 6 (2 users).
- *Workaround / products named:* more wraps and a trimmed lead; moving the sender to the caliper. No prices given.
- *Resolution:* case by case.
- *Repeats and objections:* one doubter says OTK masters draw air, so readings would be inconsistent.
- *Inference (ours):* friction is adapters, seals and leads, with brake liability. Register: RD-073/RD-072, class 2 (low value); not RD-047.

**KP-26 · [Fuel tester](https://forums.kartpulse.com/t/fuel-tester/5169)**
- *Dates / evidence:* 2020-02-07 to 02-10, 3 posters. Also [Want to buy fuel testers](https://forums.kartpulse.com/t/want-to-buy-fuel-testers/14877) (2025-11-09, 1 post); [Testing for control fuel](https://forums.kartpulse.com/t/testing-for-control-fuel/12448) (2024-06 to 07, 4 posters); [Digatron reading leaded vs unleaded](https://forums.kartpulse.com/t/digatron-reading-on-leaded-vs-unleaded-fuel/14851) (2025-11-04, unanswered).
- *Who:* a club volunteer, club racers, a buyer. Customers.
- *Job and problem:* check fuel legality cheaply. Digatron fuel tester about US$700 (2020-02) seen as costly. A 2025-11 poster wants DT-47 units "even if they do not work" (reason not stated).
- *Workaround / products named:* specific-gravity kits, water (ethanol) tests.
- *Resolution:* none.
- *Repeats and objections:* an Australian racer (2024) calls control fuel an open secret nobody uses.
- *Inference (ours):* the buyer is the club or tech official. The only point touching the recorded blocker is a possible incumbent supply shortage, unconfirmed. Register: RD-035, class 4.

**KP-27 · [Tire Pressure Gauge Reading](https://forums.kartpulse.com/t/tire-pressure-gauge-reading/14240)**
- *Dates / evidence:* 2025-05-28, 13 posts, 8 posters. Also [Tools you swear by?](https://forums.kartpulse.com/t/tools-you-swear-by/11178) (2023-09 to 10, 93 posts, 40 posters, keyword-read) and [Best tyre inflator?](https://forums.kartpulse.com/t/best-tyre-inflator/13339) (2024-12, 7 posters).
- *Who:* owner-drivers; one staff Prisma owner. Customers.
- *Job and problem:* get a stable reading on a small tyre; the OP's gauge took about 30 s to settle. Replies: gauges are only a consistent reference and can differ by a couple of psi.
- *Workaround / products named:* Prisma, Longacre digital, Vega analogue (named 2025); Blue Point digital inflator praised for tenths; cordless preset inflators popular. No prices given.
- *Resolution:* none; glycerine-filled gauges are slow by design.
- *Repeats and objections:* a Prisma owner still waits about 10 s; gauge theft or loss mentioned by 3 users across threads. No electronic instrument is championed in the tools thread.
- *Inference (ours):* settle time is a concrete 2025 annoyance matching the RD-003 brief. Register: RD-003, class 2.

**KP-28 · [3d printed items useful for go karting](https://forums.kartpulse.com/t/3d-printed-items-useful-for-go-karting/7509)**
- *Dates / evidence:* skimmed with keyword filters only; no lead found. This thread 2021-05-31 to 2026-07-20, 149 posts. Others, each by title and partial read: [KA pop off (carb)](https://forums.kartpulse.com/t/ka-pop-off-carb/15572) (2026-05/06); [Hour meters](https://forums.kartpulse.com/t/hour-meters-difference-between-cheap-vs-expensive/8618) (2022-01); [Sprocket and Hub alignment](https://forums.kartpulse.com/t/sprocket-and-hub-alignment/15845) (2026-09, 28 posts); [Chassis straightness](https://forums.kartpulse.com/t/chassis-straightness-without-a-straightening-table/8915) (2022-03, 17 posts); [MyLaps transponder](https://forums.kartpulse.com/t/how-to-tell-if-your-mylaps-transponder-is-fubar/9315) (2022-06 to 2023-06); [Charging cradle contacts](https://forums.kartpulse.com/t/charging-cradle-contacts-for-transponder-cradle/13058) (2024-10, unanswered).
- *Who:* owner-drivers and hobbyists. Customers.
- *Job and problem:* 3D prints are brackets and covers, with nothing electronic beyond one unfinished Arduino project. A user mis-read a shock pump as a pop-off gauge. Transponder faults were battery or cable and were replaced by MyLaps.
- *Workaround / products named:* Oppama PET-3200R hour meter about US$60 vs generic under US$10-13 (2022-01); Kelgate R3 Magtronic laser kit US$750 paid (2022-03; link preview GBP 598.80).
- *Resolution:* proper pop-off gauge bought; cheap hour meters judged fine.
- *Repeats and objections:* MyChron already counts hours.
- *Inference (ours):* no product-sized gap in any of these. Register: hour meters class 5 (no RD number given).

#### Products and prices named
| Product | Price as stated | Date | Source type (forum post / web-search summary) |
|---|---|---|---|
| Longacre analogue 0-15 psi gauge | ~US$30; another analogue ~US$60 | 2019-05; 2020-09 | Forum post |
| Longacre Semi-Pro digital 0-60 psi | ~US$80 | 2020-09 | Forum post |
| Longacre Semi-Pro digital; Basic; Pro | US$86.96-111.99; US$54.99; US$179.99 | 2026-11 | Web-search summary |
| Intercomp digital tyre gauge | ~US$300 | 2019-05 | Forum post |
| Prisma tyre gauge (basic / with stopwatch) | ~US$190 / ~US$220 | 2020-09 | Forum post (current price not found) |
| Unipro UniTire IR | ~US$300 | 2020-09 | Forum post |
| AiM kart tyre-temperature IR kit | US$660 | 2019-04 | Forum post |
| AiM kart tyre-temperature IR kit | ~US$600-660; EUR 650 list (ex VAT, Jan-2025 list); bracket kit ~US$185-191; single sensor ~EUR 115 | 2026-11 | Web-search summary |
| Alfano 7 wireless in-tyre sensor | EUR 129 each | 2024-06 | Forum post |
| Stone Kart Company in-rim tyre monitoring | ~US$300 (unverified) | 2019-03 | Forum post |
| MLX90614 IR sensor (DIY) | ~US$12 each; later "$20+" | 2018-03; 2021-05 | Forum post |
| IR temp gun; K-type probe | ~US$20; US$34 | 2019-04; 2023-01 | Forum post |
| AiM MyChron 5 | ~US$500-550 | 2024-12 | Forum post |
| AiM MyChron 6 (1T / 2T) | US$649.95-714.99 / ~US$759-769; UK GBP 430-470 | 2026-11 | Web-search summary |
| Used MyChron 4 | US$200+ | 2023-02 | Forum post |
| Used MyChron 5 + MyChron 4 pair | US$450 | 2024-11 | Forum post |
| Used Alfano Pro / Pro 3 Evo | ~US$50; ~US$100 with sensors | 2022-09 | Forum post |
| Alfano 6 1T new; Alfano 6 2T used | US$390; ~US$500 | 2023-03 | Forum post |
| Unipro logger with extension/splitter/sensors | ~US$700 | 2024-12 | Forum post |
| RaceBox Mini | ~US$160 (crowdfund); US$199 sale | 2022-02; 2024-12 | Forum post |
| Amazon IR lap-timer sets | US$44; US$72 | 2023-03 | Forum post |
| AiM Solo 2 vs MyChron 5; Solo bracket | Solo 2 GBP 200 cheaper; bracket ~US$15 | 2018-10/11 | Forum post |
| AiM SmartyCam | ~US$900 | 2024-08 | Forum post |
| AiM replacement MyChron battery | US$65 | 2024-08 | Forum post |
| AiM lambda controller (LCU-One) | US$400 (AiM dealer) | 2017-05 | Forum post |
| AiM LCU1S lambda | ~US$450-499; AU$698.95 inc. tax | 2026-11 | Web-search summary |
| Narrowband O2 gauge | US$20-60 | 2017-05 | Forum post |
| Sniper laser alignment | US$300 | 2022-04 | Forum post |
| Sniper V2 Inox | US$315-400; GBP 225; EUR 290-321 | 2026-11 | Web-search summary |
| Kelgate R3 Magtronic laser master kit | US$750 paid; GBP 598.80 in link preview | 2022-03 | Forum post |
| DIY angle-iron alignment plates | US$15 | 2022-04 | Forum post |
| Used Tanner digital scales; used Longacre scales + pad | US$200; US$450 | 2020-02 | Forum post |
| KartBalance phone app | ~US$3 | 2020-03 | Forum post |
| Proposed scale levelling stand (not built) | est. US$1,500-2,000 | 2020-02 | Forum post |
| Rotax battery charger | US$125 | 2026-08 | Forum post |
| LiFePO4 12 V 6-10 Ah packs | US$35-69 | 2023-12 to 2025-05 | Forum post |
| Shorai LFX09 / Banshee lithium | US$125 / US$79 | 2024-01 | Forum post |
| LO206 head leak-down fixture (hobbyist batch) | US$150 shipped | 2026-08 | Forum post (classified) |
| Digatron fuel tester | ~US$700 | 2020-02 | Forum post |
| Oppama PET-3200R hour meter; generic | ~US$60; under US$10-13 | 2022-01 | Forum post |
| Raceceiver Fusion/Element (used) | "100 & up" (US$) | 2022-03 | Forum post (classified) |
| Rugged Radios Nitro Bee UHF receiver | US$84.15-99 | 2026-11 | Web-search summary |
| Karting coaching radio kit with Nitro Bee Xtreme | US$319 | 2026-11 | Web-search summary |
| Pit Row Dyno parts: ESP32 7" touch, HX711, 50 kg load cell, hall sensor, hydraulic brake | US$34, US$3, US$30, US$4, US$25 (component costs) | 2025-12 | Forum post (maker) |
| Performance Trends DataMite Mini inertia dyno package | US$399 | undated listing | Web-search summary |
| YourDyno eddy / water-brake engine dyno kits | US$3,680 / US$4,925 | undated listing | Web-search summary |
| Manual kart starters (Rotax) | ~US$400 | 2022-08 | Forum search blurb (thread not read) |
| Stationary vs rolling kart stand (Streeter) | US$103 vs US$320 | 2022-11 | Forum search blurb (thread not read) |

Brands named without a price: Alfano Tyre Control 2 / P-T (described as "quite expensive"), Motion Pro digital gauge (spec only), Vega analogue gauge, Blue Point inflator, OTC 5609 leak-down tester, Kestrel 5100 Motorsport, AMK Karting track-width gauge, KartMaster spacer rings, Black Racing Engines jet kits, Trac-Com, Sena, Cardo, NOCO, Battery Tender, Pit Row Dyno's own units, MyLaps, RaceChrono.

#### Low-yield searches and sections
- Free-text complaint searches ("nobody makes", "wish someone would make", "overpriced sensor", "homemade tester", "discontinued sensor", "tach hour meter") gave zero or off-topic results. Members rarely phrase product gaps this way.
- "Rain light" returned only tyre and weather chatter. Track-operator lighting and flag topics were not read.
- "esp32" returned nothing; "arduino" and "raspberry pi" returned only projects already in the ledger, so the maker population looks small.
- "Durometer" and "pyrometer": one durometer purchase for tyre ageing; no complaint about availability or price of either.
- "Timing light", "dial indicator timing", "spark tester", "crank seal pressure test": scattered how-to replies and no tool gap.
- Already well served by cheap established products: pop-off testers, hour meters, leak-down testers, weather meters, battery chargers and testers.
- Tools megathreads: hand tools, cordless inflators, compressors, tyre changers; electronic measuring instruments almost absent from favourites.
- 3D-printing threads: brackets and covers, no electronics. Transponder threads: purchase and charging questions, with MyLaps replacing faulty units.
- Radiator curtain and thermostat threads: mechanical solutions exist; no control-electronics request.
- Chassis category (straightness, frame tables, ride height, caster/camber): mostly set-up theory; three sampled, no instrument gap.
- 4-stroke category: clutch, valves, oil, fuel rules. Tech-inspection tools appear by title only (the already-rejected group RD-033 to RD-037) and were not read.
- Getting Started category: cost-of-entry threads; the only relevant item was the cheap timing thread (KP-23).
- Rental karting appears only as a timer mounting and portability problem; no rental-operator instrumentation needs were found. Driver radios are banned in sprint racing, so use is practice and endurance only.

#### Unknowns
- Sampling bias: the forum skews to US circuit karting, LO206/KA100/X30 and engaged users. Australian class rules, lap-trigger infrastructure and prices differ, and only a handful of Australian posters were identified. Dirt-oval karting is discussed elsewhere.
- Purchase intent is not shown: almost every lead is a complaint, question or wish. Only two posts say "I would buy" (a hobbyist logger; interest in the maker's dyno). View counts show readership, not demand.
- Current prices and availability are unconfirmed. Forum prices are 2017-2026 snapshots and search figures are unverified summaries. Current Prisma and Alfano tyre-gauge prices, Pit Row Dyno prices, and whether the Stone Kart and KTPMS products still exist were not confirmed.
- Digatron fuel tester status: the November 2025 wanted-to-buy post hints at scarcity, but a search could not confirm whether the DT-47 is still made. This is the only fact that could bear on RD-035's recorded blocker.
- Race-control receiver mandates rest on two anecdotal tracks plus "common in dirt karting". Which clubs or series mandate them, on what bands, and whether any Australian kart or speedway-kart body does, is unknown.
- TaG diagnostic tester feasibility: unknown how many no-start cases are electrical rather than mechanical, how many loom variants exist per engine family, and whether a simple tester could give a trustworthy verdict (stator resistance evidently cannot).
- Gauge accuracy: posters quote maker specs (0.1 %, 0.5 %, ±0.6 psi) but nobody reports a calibration check against a reference. Field accuracy of Longacre and Prisma at 5-15 psi is unknown.
- Unread material: tyre megathreads, the electric-karting megathread, app-promotion threads, classifieds, and all images and outbound links. A relevant complaint could sit there. The MyChron 6 thread was keyword-sampled, not fully read.
- The decision value of tyre temperature and TPMS data is contested within the forum; the single owner who published analysis found no lap-time link.
- Alfano and Unipro-side evidence is thin: most accessory friction recorded is around AiM, so gaps on the other brands are not established.

### Grassroots Motorsports

#### Coverage and access
- **Access limitation:** one direct test (the Tech Tips index) returned HTTP 403 (Cloudflare challenge). It was not retried and no bypass was attempted. **No GRM thread page was read directly.** Every entry below comes from web-search summaries that paraphrase indexed post text. Reply order, agreement levels, edit history and later pages are mostly invisible, and a summary can blend two threads.
- **Searches:** about 138 web-search calls, roughly 129 restricted to the forum (grassrootsmotorsports.com and its classicmotorsports.com mirror) and 9 general-web product/price checks. Query families covered tyre/brake/corner-weight measurement, alignment, spring and shock testing, loggers and CAN, engine-protection warnings and gauges, fuel, electrical (kill switches, PDMs), driver comfort and radios, and phrase and recency probes.
- **Evidence levels used here:** **S2** = substantive, cross-confirmed in two or more searches; **S** = substantive from one focused search; **P** = partial (first post or snippet only). A fourth level, T, is title or index only.
- **Counts from the research notes:** 19 S2, 17 S (including sub-threads inside larger entries), about 28 P, about 70 T. The ledger below has 31 substantive entries (some bundle related threads). Zero threads were read in full, so the depth target is met only in the "search-summary" sense.
- **Dates:** about 2009 to February 2026. Most technical threads are 2012–2021. The most recent directly relevant maker thread is December 2025 (brake temperature logger). "≈" dates are derived from the search tool's age metadata (±a few months) and are not confirmed. Prices are historical, as stated in the post on its date.
- **Not verified:** full reply lists for the two newest maker threads, several thread start dates, how many people agreed with any point, and usernames (none recorded). Short quoted fragments were not checked against the page. Search for "sold it / went back to simpler" posts found no clean data-logging example; one clear fuel-system example exists (GRM-16).
- **Prices marked `[web]`** come from a general web search of retailer listings on 2026-11-17, not from the forum, and are unverified.

#### Threads

**GRM-01 · [Plug-n-Play CAN Bus converter for telemetry?](https://grassrootsmotorsports.com/forum/grm/plug-n-play-can-bus-converter-for-telemetry/128988/page1/) · S2**
- *Dates / evidence:* start ≈2017 (summary says about a decade old); latest reply unknown.
- *Who:* racer, analogue (non-OBD) car, bought an OBD-oriented logger. Customer.
- *Job and problem:* get oil pressure and other analogue sensors into the logger over CAN; would pay under US$100; saw no simple prepackaged box.
- *Workaround / products named:* MRS Electronic CAN I/O from US$133 (≈2017, needs programming); used Megasquirt MS2 as sensor box; DIY Arduino Nano + CAN board + ADC "sub $10" with coding; RaceCapture/Pro analogue inputs. One reply doubted a one-board solution given varied voltages.
- *Resolution:* none seen.
- *Repeats and objections:* threads 117705, 270641 and 274870 repeat the no-easy-data-without-OBD-II complaint.
- *Inference (ours):* the 2017 gap was price and zero-programming, not function; `[web]` 2026 listings (AnalogX US$149.95, AEM about US$175–215) suggest it is mostly solved above US$100. Register: RD-072 / RD-019, class 3 tending to 5 (already sold at about US$150).

**GRM-02 · [DIY brake temperature logging tool, take 2](https://grassrootsmotorsports.com/forum/grm/diy-brake-temperature-logging-tool-take-2/283478/page1/) · S2**
- *Dates / evidence:* December 2025 (explicit); later replies not recovered. Stub thread 283450.
- *Who:* experienced builder testing brake cooling; maker/hobbyist, not selling.
- *Job and problem:* compare left/right pad temperature behaviour; temperature paint shows only peaks.
- *Workaround / products named:* RP2040 Feather, two thermocouple amplifiers, accelerometer, SD/RTC, display; K-type probes in a tapped hole in the pad backing plate; 10 Hz CSV; parts about US$85 (Dec 2025). `[web]` comparators: RS PRO/Labfacility pad thermocouples about €30/£28 each; Izze-Racing IR sensor US$385 each; CANchecked set about US$1,639; AvioRace kit US$2,750 (all 2026).
- *Resolution:* works for the author; venting-test result not seen.
- *Repeats and objections:* thread 271374 shows rotor-temperature difficulty when alone. Paint/strips, IR guns and published pad ranges were offered as alternatives; IR raises emissivity questions.
- *Inference (ours):* a real "one function" build at about US$85 against US$1,600+ kits, but one skilled maker and demand is unproven. Register: RD-086 / RD-025 / RD-071, class 3 (narrower version).

**GRM-03 · [How useful are oil pressure gauges?](https://grassrootsmotorsports.com/forum/grm/how-useful-are-oil-pressure-gauges/151781/page1/) · S2**
- *Dates / evidence:* 2019 (year explicit); exact dates unknown; two pages.
- *Who:* mixed track-day, endurance and street owners. Customers.
- *Job and problem:* know about low oil pressure in time; stock lights trip very low (Subaru 2.1 psi; BMW about 7 psi in a 2016 thread).
- *Workaround / products named:* run gauge plus light; higher-pressure switch; large bright LEDs mounted high; Longacre three-level "blinker" gauge; rule of thumb 10 psi per 1000 rpm.
- *Resolution:* consensus is light for sudden loss, gauge/log for trend.
- *Repeats and objections:* one poster wants a light that trips at varying pressure by rpm (also asked in GRM-06); one view: a gauge is almost useless on track without an in-car camera.
- *Inference (ours):* wanted behaviour is a higher, sensible threshold and an unmissable light; the rpm-scaled threshold was asked for by at least two posters. Register: RD-089 / RD-090, class 2; does not address why RD-032 was dropped.

**GRM-04 · [What gauges do you really need?](https://grassrootsmotorsports.com/forum/grm/what-gauges-do-you-really-need/178621/page1/) · S2**
- *Dates / evidence:* replies from 16 Nov 2020 (explicit); start unknown.
- *Who:* club racers and track drivers. Customers.
- *Job and problem:* notice engine trouble without watching gauges.
- *Workaround / products named:* idiot lights with configurable thresholds; shift light plus lights for low oil pressure, low coolant pressure, high water temperature; keep tach and fuel level.
- *Resolution:* none; views split.
- *Repeats and objections:* same message in 57051 (2012; programmable-threshold gauges "very expensive"), 159068 (2019), 118257 (≈2016), 125825, 122691. Counter-view: lights say back off, gauges show trends.
- *Register:* RD-089 / RD-090, class 2; does not address why RD-032 was dropped.

**GRM-05 · [Digital Dash-any experience?](https://grassrootsmotorsports.com/forum/grm/digital-dash-any-experience/108798/page1/) / [Lern me: Digital dash in an analog car?](https://grassrootsmotorsports.com/forum/grm/lern-me-digital-dash-in-an-analog-car/178890/page1/) · S (attribution between the two threads uncertain)**
- *Dates / evidence:* unknown (178890 ≈2020 by ID proximity only, an inference).
- *Who:* racers with analogue cars. Customers.
- *Job and problem:* a digital dash mainly for alarms; one account of two experienced drivers missing an engine slowly failing.
- *Workaround / products named:* very bright red LED lamp at dash top. Prices quoted, dates unknown: Raspberry Pi build about US$175; Amazon OBD2/CAN display about US$45; AceWell US$309; 4.5" display US$400; Haltech about US$1,000; AiM MXP US$2,299 (GRM review).
- *Resolution:* none seen.
- *Repeats and objections:* none recorded.
- *Inference (ours):* for some buyers the alarm function is the reason for a US$400–2,300 dash. Register: RD-089 / RD-090, class 2; does not address why RD-032 was dropped.

**GRM-06 · [Can anyone recommend a combined oil temp/analog pressure sensor?](https://grassrootsmotorsports.com/forum/grm/can-anyone-recommend-a-combined-oil-tempanalog-pressure-sensor/136384/page1/) · S2**
- *Dates / evidence:* ≈2018 (by reply dates per summary).
- *Who:* builder with standalone ECU. Customer.
- *Job and problem:* one sensor for logging, with the ECU driving an idiot light from a minimum-pressure-versus-rpm curve and a temperature-based rev limit; budget up to US$150.
- *Workaround / products named:* Speedhut dual gauge; Motion Raceworks sensor; KA Sensors ASMC (price on request); VDO double-pole sender.
- *Resolution:* none seen; a later "reliable cheap-ish option?" question went unanswered in the summary.
- *Repeats and objections:* rpm-scaled warning also wanted in GRM-03.
- *Register:* RD-089 / RD-090, class 2; does not address why RD-032 was dropped.

**GRM-07 · [Recommendation for good quality gauges with peak recall?](https://grassrootsmotorsports.com/forum/grm/recommendation-for-good-quality-gauges-with-peak-recall/52775/page1/) · S**
- *Dates / evidence:* ≈2012.
- *Who:* track-day driver. Customer.
- *Job and problem:* 52 mm gauges with peak recall, avoiding expensive Japanese brands, because watching gauges at speed is frowned upon.
- *Workaround / products named:* AutoMeter Elite; ProSport (cheapest, durability doubts); GReddy/A'PEXi; Stack about US$220 each, 3-gauge set about US$270 (≈2012); Summit digital gauges; temperature labels, filming gauges, logging.
- *Resolution:* served by existing gauges for those paying US$60–270 per gauge.
- *Repeats and objections:* build-thread anecdotes of engine at about 260 °F for about 20 min unnoticed, and a low-coolant buzzer sounding while the stock gauge looked normal.
- *Register:* RD-089 / RD-090, class 2; does not address why RD-032 was dropped.

**GRM-08 · ['All-in-One' Gauges, what do ya know?](https://grassrootsmotorsports.com/forum/off-topic-discussion/all-in-one-gauges-what-do-ya-know-who-has-what-im-looking-for/184197/page1/) · S2**
- *Dates / evidence:* ≈mid-2021.
- *Who:* individual car owner. Customer.
- *Job and problem:* one sub-3" gauge for rpm, boost and EGT from individual sensors; found they "all require an ECU".
- *Workaround / products named:* PLX SM-PRO, Westach multi-needle, AiM/Dakota/Stack ("none are going to be cheap"), DIY Arduino + LCD.
- *Resolution:* none seen.
- *Repeats and objections:* caution about loading ECU sensors.
- *Register:* RD-089 / RD-090 and RD-015, class 2 / 5.

**GRM-09 · [The state of OBD2 gauges in 2022?](https://grassrootsmotorsports.com/forum/grm/the-state-of-obd2-gauges-in-2022/228300/page1/) · S2**
- *Dates / evidence:* 2022; exact date not stated.
- *Who:* rallycross owner among others. Customers.
- *Job and problem:* hardwired, install-once, no phone app; ScanGauge E discontinued.
- *Workaround / products named:* ScanGauge 2 about US$160 (2022); UltraGauge cheaper but less reliable per one reply; Torque on an old Android with Bluetooth dropouts; Edge CTS, Banks iDash, RaceCapture.
- *Resolution:* existing products adequate.
- *Repeats and objections:* none recorded.
- *Register:* RD-089 / RD-090 and RD-015, class 2 / 5.

**GRM-10 · [Budget digital dash (non obd)](https://grassrootsmotorsports.com/forum/advertiser-playground/budget-digital-dash-non-obd/118568/page1/) · S**
- *Dates / evidence:* 2016 (explicit).
- *Who:* Locost builder, carburetted Datsun 1200. Customer.
- *Job and problem:* tach, speedo, oil pressure and temperature on US$300–500.
- *Workaround / products named:* Summit digital dash (tach too small); used MyChron 4 about US$200–250 and MyChron5 GPS US$500 new (2016); Proform shift light; Sunpro gauges; "cheapest off the shelf" from Autosport Labs. Senders are variable resistors needing pull-ups.
- *Resolution:* none stated.
- *Repeats and objections:* none recorded.
- *Register:* RD-089 / RD-090 and RD-015, class 2 / 5.

**GRM-11 · [Cheap generic stainless pressure senders, do we trust them?](https://grassrootsmotorsports.com/forum/grm/cheap-generic-stainless-pressure-senders-do-we-trust-them/204334/page1/) · S**
- *Dates / evidence:* unknown (≈2022 by ID, an inference). Related thread 33888 (S2); 280735 August 2025 (explicit).
- *Who:* track-car owners and racers. Customers.
- *Job and problem:* trust in cheap pressure senders: one fine on a fuel rail, one a year on oil; one brake-pressure sender gave a spongy pedal; one oil sender cracked and sprayed oil.
- *Workaround / products named:* check a sender against 10–20 psi compressed air; short braided line to a chassis bracket rather than engine-mounting (33888); Bosch mechanical gauge to verify an intermittent oil light (280735).
- *Resolution:* none overall; 280735 diagnosed with a mechanical gauge.
- *Repeats and objections:* senders leaking or reading 50 psi against 85–90 on a mechanical gauge (33888); one reply: "a cheap gauge is fine".
- *Register:* RD-088 / RD-087 / RD-019, class 2.

**GRM-12 · [Are brake pressure gauges a waste of time](https://grassrootsmotorsports.com/forum/grm/are-brake-pressure-gauges-a-waste-of-time/128673/page1/) · S2**
- *Dates / evidence:* ≈2017. Related 70215 (old, S), 278128.
- *Who:* club racers and builders. Customers/makers.
- *Job and problem:* set brake bias; mostly sceptical of gauges.
- *Workaround / products named:* tune by feel on a balance bar; Longacre manual gauges about US$60 (≈2013, with tees); Bosch sensor via Race Technology US$290 balked at; AiM MSI/AEM about US$150 (old); salvage-yard Bosch sensor "a few dollars".
- *Resolution:* none; value seen only for logging or a setup baseline.
- *Repeats and objections:* numbers do not transfer between cars; extra fittings add failure points (one cracked fitting failed in a race); gauges are a pain to bleed.
- *Register:* RD-047, class 4 (evidence leans against).

**GRM-13 · [Race car TPMS for less than a new game console?](https://grassrootsmotorsports.com/forum/grm/race-car-tpms-for-less-than-a-new-game-console/101716/page1/) · S2**
- *Dates / evidence:* 2015 (explicit).
- *Who:* racer wanting CAN output to a logger. Customer.
- *Job and problem:* TPMS under US$300 with valve-stem sensors and CAN output.
- *Workaround / products named:* 4-sensor display kit US$270 (2015); junkyard OEM receiver reverse-engineering; cheap valve-cap sensors "display only". `[web]` 2026: AiM kit £425 / CAN receiver £160; WHP/ECUMaster TPMS-to-CAN US$329; a Rennlist thread claims US$225.
- *Resolution:* hard at that price in 2015; `[web]` suggests largely solved since.
- *Repeats and objections:* Bluetooth/trailer units ruled out (no CAN).
- *Inference (ours):* largely solved since 2015. Register: no exact record; class 5 (now sold by AiM and others).

**GRM-14 · [Lap Timers – Am I asking too much?](https://grassrootsmotorsports.com/forum/grm/lap-timers-am-i-asking-too-much-is-there-a-setup-that-meets-my-requirements/272013/page1/) (S2) and [Lap Timers for Beginners and DIYers, OBD1](https://grassrootsmotorsports.com/forum/grm/lap-timers-for-beginners-and-diyers-obd1/270641/page1/) (S) · S2**
- *Dates / evidence:* both ≈mid-2024.
- *Who:* beginner track drivers (one with an MR2 Turbo, OBD-1). Customers.
- *Job and problem:* video + OBD-II + display + easy start in one unit; OBD-less cars lack easy data.
- *Workaround / products named:* split jobs (cheap predictive timer plus logger); RaceChrono Pro about US$20 and GPS; RoadKeeper about US$400 (≈2024); AiM Solo 2 US$400 (older) / "$700" (newer); Solo 1 "a couple hundred"; Racepak CL2 about US$250 (≈2020); RaceBox Mini US$160–200 (≈2025, thread 280175); Garmin Glo about US$100.
- *Resolution:* well served.
- *Repeats and objections:* one switched Harry's to RaceChrono over OBD-II dropouts; one called external GPS "a waste" for lap timing.
- *Inference (ours):* negative for a new timer/logger. Register: RD-094 / RD-087 / RD-072, class 5.

**GRM-15 · [Is There A Hack For Budget Race Radios?](https://grassrootsmotorsports.com/forum/grm/is-there-a-hack-for-budget-race-radios/279449/page1/) · S2**
- *Dates / evidence:* ≈2025 (279449, 276129); related threads older.
- *Who:* budget endurance teams (ChampCar/Lemons). Customers.
- *Job and problem:* clear driver–pit comms; cheap kits too quiet, noisy and fragile at driver changes.
- *Workaround / products named:* Baofeng + IMSA car kit US$250–300 (≈2020–2025); GMRS licence US$35; Rapid Radios US$400/pair + US$50/yr (≈2025); Racing Radios "figure $2K"; a pit board as backup. A GRM article says budget sets are "nearly useless" without noise isolation.
- *Resolution:* none; cost is headsets, wiring and antennas.
- *Repeats and objections:* a Lemons incident of Baofengs on police frequencies.
- *Inference (ours):* the pain is audio isolation, harness robustness and licensing, not a missing electronic box. Register: RD-110 (name only); class 1 / 5.

**GRM-16 · [22 gallon cell starving at ~12 gallons even with giant Hydramat](https://grassrootsmotorsports.com/forum/grm/22-gallon-cell-starving-at-12-gallons-even-with-giant-hydramat-what-am-i-missing/258775/page1/) · S**
- *Dates / evidence:* start unknown (≈2023–24 by ID); resolution post references a September 2025 race; 3+ pages.
- *Who:* budget endurance team (V8, Holley Sniper EFI). Customer.
- *Job and problem:* fuel starvation with about 10 gal left; theories of foam, tilt, hot return fuel and EFI sensitivity.
- *Workaround / products named:* temporary fuel-pressure gauge visible under the wiper (related threads 54139, 130674, 38990); logging an electric sender through the ECU.
- *Resolution:* went back to simpler: replaced EFI with a four-barrel carburettor, now about 20 gallons usable of 22.
- *Repeats and objections:* another team got 45 min, then 75 min after adding a return-line cooler.
- *Inference (ours):* track-only fuel-pressure faults are diagnosed with improvised visible gauges; nobody in these snippets asks for a recorder. Register: RD-088 / RD-087 / RD-019, class 2.

**GRM-17 · [Making old discontinued race scales useful again?](https://grassrootsmotorsports.com/forum/shop-talk/making-old-discontinued-race-scales-useful-again/271888/page1/) · S2**
- *Dates / evidence:* ≈2024–25 (by ID); exact date unknown.
- *Who:* home racer with an inherited unbranded electronic set. Customer.
- *Job and problem:* display would not power up; no specs findable.
- *Workaround / products named:* replaced the board's voltage regulator ("$6 for a 20 pack"); suggestion that pads hold the load-cell amplifiers.
- *Resolution:* scales functional; calibration check not reported.
- *Repeats and objections:* calibration is the hard part.
- *Register:* RD-049, class 2 (speaks to part of its installed-base blocker).

**GRM-18 · [Connectors/pins for Intercomp Scales?](https://grassrootsmotorsports.com/forum/grm/connectorspins-for-intercomp-scales/256324/page1/) · S2**
- *Dates / evidence:* ≈mid-2023.
- *Who:* scale owner. Customer.
- *Job and problem:* broken wire at a pad connector; previous fix was a whole cable at about US$85–100 shipped (≈2023).
- *Workaround / products named:* Amphenol MS-series connector (MS3106A14S-6P) about US$9, about 30 min repair.
- *Resolution:* identified the connector and repaired.
- *Repeats and objections:* none recorded.
- *Register:* RD-049, class 2 (speaks to part of its installed-base blocker).

**GRM-19 · [Scales- best value?](https://grassrootsmotorsports.com/forum/grm/scales-best-value/192553/page1/) · S**
- *Dates / evidence:* March 2022 (explicit); related threads 127520, 136444, 66847, 39784, 135487 ≈2013–2018.
- *Who:* club racers and home builders. Customers/makers.
- *Job and problem:* corner weights affordably; DIY rigs "a pain to set up" with poor repeatability.
- *Workaround / products named:* borrow/rent; new set about US$600 plus shipping (≈2016); used Intercomp with cart US$350; used sets US$350–1,000 (≈2014–2018); Proform about US$685–800, classified US$699; Rebco 20–30% below Intercomp; 2013 wired over US$1,000, wireless over US$1,500.
- *Resolution:* buy a used or new complete set, or borrow.
- *Repeats and objections:* load cells "cost more than buying a real set"; uncalibrated scales offer no value.
- *Register:* RD-018, class 4 (reinforces the rejection).

**GRM-20 · [4 pole vs. 6 pole kill switch](https://grassrootsmotorsports.com/forum/grm/4-pole-vs-6-pole-kill-switch/282746/page1/) · S2**
- *Dates / evidence:* ≈November 2025.
- *Who:* ChampCar team rewiring with a PDM. Customer/builder.
- *Job and problem:* whether to move to a 6-pole switch and how the resistor is wired.
- *Workaround / products named:* bleed resistor between B+ and field; PDM ground-wire kill input; solid-state relay or solenoid redundancy; Cartek isolator seen as premium. Rules differ by body.
- *Resolution:* none single; one team "killed an alternator in 2000 miles" (cause unsure).
- *Repeats and objections:* same confusion in 275829 (≈Jan 2025), 187015, 41092, 142874, 153563, 142610, 128219, 143501; one Spec Miata failed tech when the car ran on the alternator at 2,000 rpm.
- *Inference (ours):* a recurring wiring-knowledge problem with scrutineering consequences, with existing answers (correctly wired switch, Cartek, PDM logic). Register: no exact record (adjacent RD-011, RD-077, RD-022); class 1, largely 5.

**GRM-21 · [Spring rate tester, opinions?](https://grassrootsmotorsports.com/forum/grm/spring-rate-tester-opinions/163020/page1/) · S**
- *Dates / evidence:* unknown (≈2019–20 by ID).
- *Who:* hobbyist racers/builders.
- *Job and problem:* measure spring rates cheaply.
- *Workaround / products named:* press plus bathroom or corner-weight scale; valve-spring testers about US$75 (undated) adaptable; one commercial tester disappointing (a 180 lb/in spring read 150).
- *Resolution:* none stated.
- *Repeats and objections:* bathroom scales max about 300 lb and time out.
- *Register:* adjacent to RD-017 validation theme; class 1, mechanical.

**GRM-22 · [Digital alignment tools – recommendation](https://grassrootsmotorsports.com/forum/grm/digital-alignment-tools-recommendation/184710/page1/) · S**
- *Dates / evidence:* unknown (≈2021). Related 285036 February 2026 (explicit, P).
- *Who:* home alignment DIYers. Customers/makers.
- *Job and problem:* quality digital caster/camber tool at reasonable price.
- *Workaround / products named:* Amazon angle boxes within about 0.2 degrees; SmartCamber; Longacre digital gauge "died early"; phone app; Harbor Freight finder US$29.95 (undated). 285036: shops quote about US$200 per alignment; hub stands about US$900 considered (Feb 2026); PACO US$849 per set of four (2018); Flyin' Miata US$395/pair (old); bump-steer DIY about US$125 vs over US$400 kit (≈2022).
- *Resolution:* none single; one DIY alignment compared to a shop machine was within "noise".
- *Repeats and objections:* none recorded.
- *Register:* RD-043 / RD-042 / RD-061, class 4 / 5.

**GRM-23 · [Did we reach a consensus on tire pressure gauges?](https://grassrootsmotorsports.com/forum/grm/did-we-reach-a-consensus-on-tire-pressure-gauges/181353/page1/) · S2**
- *Dates / evidence:* ≈2021; related 258492 ≈2023–24; test-article thread 194671 date unknown.
- *Who:* autocrossers and track drivers. Customers.
- *Job and problem:* trust a tyre gauge; digital gauges drift.
- *Workaround / products named:* Longacre most named; Intercomp digital "stupid expensive"; three-gauge voting; US$20–30 gauges "practical". GRM test against a reference: low-cost digital within about 1%, US$50 dial about 2%, pencil about 14%, pocket digital about 16%.
- *Resolution:* none; users cannot tell which gauge is right without a reference.
- *Repeats and objections:* "repeatability matters, not the number".
- *Register:* RD-003 / RD-046 / RD-092, class 2.

**GRM-24 · [Does the world really need a tire gauge app?](https://grassrootsmotorsports.com/forum/grm/does-the-world-really-need-a-t/184363/page1/) · S2**
- *Dates / evidence:* article 16 June 2021 (explicit).
- *Who:* GRM review of a vendor product (Fastmate RaceSense); commenters are customers/hobbyists.
- *Job and problem:* fast guided tyre temperature and pressure capture; "16 measurements… in less than 30 seconds".
- *Workaround / products named:* RaceSense list US$449 (16 Jun 2021); Longacre competitor US$499 without phone pairing (Jun 2021). `[web]` 2026: about US$449–490, pocket US$315–420, UK £275–325 (one listing April 2026).
- *Resolution:* none.
- *Repeats and objections:* price scepticism; one would spend it on TPMS feeding an AiM instead.
- *Register:* RD-003 / RD-046 / RD-092, class 2.

**GRM-25 · [DIY stupidly cheap tire temp logger](https://grassrootsmotorsports.com/forum/grm/diy-stupidly-cheap-tire-temp-logger-16-meas-points-ir-array-per-wheel/146207/page1/) · S2** (already in the R&D sources)
- *Dates / evidence:* December 2018 (explicit); replication ≈mid-2019; no later status found; 3+ pages.
- *Who:* maker/hobbyist; replicator also a maker.
- *Job and problem:* cheap multi-point tyre temperatures into lap-timer apps.
- *Workaround / products named:* 16-point IR array, BLE to phone apps, about US$170 per wheel in parts (Dec 2018); M5Stick + MLX90640 replication about US$130 (≈2019). Related: K-type probe C$44 (undated); Harbor Freight IR gun US$16–30 reads 5–10 °F low.
- *Resolution:* none seen.
- *Repeats and objections:* BLE confusion; WiFi/CAN suggested; one comparison to US$20K–40K systems (context unclear).
- *Register:* RD-003 / RD-046 / RD-092, class 2.

**GRM-26 · [How do you record your track day data?](https://grassrootsmotorsports.com/forum/grm/how-do-you-record-your-track-day-data/262354/page1/) · S2** (already in the R&D sources)
- *Dates / evidence:* 19–22 Feb 2024 (per existing R&D record).
- *Who:* track-day drivers. Customers.
- *Job and problem:* record temperatures and pressures while busy with gauges.
- *Workaround / products named:* paper clipboard (easier than a phone), phone screenshots, Stock Car Stats Pro, TrackAddict, memory probe pyrometer over IR for some.
- *Resolution:* none.
- *Repeats and objections:* none recorded.
- *Register:* RD-003 / RD-046 / RD-092, class 2.

**GRM-27 · [Data logging ride height on the cheap](https://grassrootsmotorsports.com/forum/grm/data-logging-ride-height-on-the-cheap/139784/page1/) · S**
- *Dates / evidence:* ≈2018.
- *Who:* hobbyist builders.
- *Job and problem:* log ride height cheaply.
- *Workaround / products named:* junkyard headlight-levelling sensors; GM OE sensors about US$30 on eBay (undated); pots; used RaceCapture Pro; DataQ pricier.
- *Resolution:* none stated.
- *Repeats and objections:* needs 50–100+ Hz and filtering; doubts it shows downforce; load cells costly.
- *Register:* no exact record (adjacent RD-087); single maker lead.

**GRM-28 · [Anyone ever tried Race Technology DL1 data logger or Dash2 display?](https://grassrootsmotorsports.com/forum/grm/anyone-ever-tried-race-technology-dl1-data-logger-or-dash2-display/275778/page1/) · S**
- *Dates / evidence:* ≈2025.
- *Who:* Locost builder who inherited unused units; long-time owner replying.
- *Job and problem:* is the old logger worth using; owner says time has passed it by (analogue, no native CAN, slow RS232, clunky software, no camera integration).
- *Workaround / products named:* none stated.
- *Resolution:* none.
- *Repeats and objections:* others praise analysis depth.
- *Register:* RD-094 / RD-113, class 5.

**GRM-29 · [Reduced Alternator Charging Over 12 Autocross Runs](https://grassrootsmotorsports.com/forum/grm/reduced-alternator-charging-over-12-autocross-runs/252530/page1/) · S**
- *Dates / evidence:* ≈2023.
- *Who:* Camaro autocrosser, Powermaster alternator. Customer.
- *Job and problem:* voltage fell from 13.7 V to 12.0 V at the same rpm over a weekend (from engine logs); heat suspected.
- *Workaround / products named:* shop bench test found nothing; grounds and belt suggested.
- *Resolution:* not seen.
- *Repeats and objections:* none recorded.
- *Register:* RD-088 / RD-087 / RD-019, class 2.

**GRM-30 · [Modern digital gauges: A better way to monitor our Mustang?](https://grassrootsmotorsports.com/forum/grm/modern-digital-gauges-a-bette/262361/page1/) · S**
- *Dates / evidence:* 2024 (article).
- *Who:* GRM article; commenters are customers.
- *Job and problem:* monitoring engine vitals; digits hard to read in a race car.
- *Workaround / products named:* ProSport digital gauges about US$60 each (2024).
- *Resolution:* none.
- *Repeats and objections:* commenters want a separate warning light plus a recorder; liquid-filled gauges read low when hot.
- *Register:* RD-090 / RD-096 / RD-097, class 2 / 5.

**GRM-31 · [Good quality fuse/relay box for motorsports?](https://grassrootsmotorsports.com/forum/grm/good-quality-fuserelay-box-for-motorsports/257795/page1/) · S**
- *Dates / evidence:* ≈2023; related 193227 and 149441 (P) ≈2018–2022.
- *Who:* builders. Customers/makers.
- *Job and problem:* a reliable fuse/relay panel or PDM at modest cost.
- *Workaround / products named:* Eaton Bussmann, Littelfuse MiniFlex, Blue Sea; Eaton SSVEC hub about US$156 (≈2023); panel about US$150 all-in; Rowe PDM-60 about US$200 (≈2018); open-source dingoPDM/Synapse.
- *Resolution:* none single.
- *Repeats and objections:* avoid no-name imports; solid-state units can fail closed, so keep a master relay.
- *Register:* RD-011, class 2 (evidence makes the commercial case harder).

**Partial threads (P)**
- "Learn Me: Cool Suits" (273606; URL not in source) — ≈2024–25 — a CoolShirt-branded unit lasted 1.5 hours; home-built cooler and bilge pump preferred.
- Tech Tips "DIY Cool Shirt Cooler Setup" (279399; URL not in source) — ≈2025 — US$29 Igloo cooler, 12 V pump, fittings.
- "DIY ways of keeping cool in the race car" (37937; URL not in source) — old — US$80–100 all-in; shirt US$155 and cold unit US$60 (old).
- "Dead Longacre Scales. Repair options?" (267943; URL not in source) — ≈2024 — quote "usually $300 or so" for a battery box; a US$15 part fitted; still dead; outcome unknown.
- "DIY Arduino Corner Weights" (186240; URL not in source) — ≈2021 — HX711 + Arduino retrofit about €335/US$400; accuracy not stated.
- "Hub stands/home alignment" (285036; URL not in source) — Feb 2026 — see GRM-22.
- "Pegasus Kill Switch" (275829; URL not in source) — ≈Jan 2025 — see GRM-20.
- "Building an analog race dash" (builds 181498; URL not in source) — unknown — Feather-based analogue dash with CAN input and LED ring for warnings; reading analogue inputs was the hard part.
- "Autocross Telemetry/Data Recording DIY/Budget options" (280175; URL not in source) — ≈2025 — see GRM-14.
- "Tire temp probe on the cheap" (182067; URL not in source) — unknown — K-type probe C$44 into a multimeter.
- "Learn Me Transponders." (195322; URL not in source) — ≈2022 — MyLaps lifetime US$600; rent US$40–50 per race.
- "Never Miss a Flag" Flagger article thread (180084; URL not in source) — ≈2021 — subscription lock-in objections; Flagtronics FT200 from about US$250.
- "Programmable fuel gauge – … using resistor?" (97367; URL not in source) — old — sender/gauge ohm mismatch; resistor hacks "not perfect".
- "Electric fan controllers" (142383; URL not in source) — old — PWM controller praised; one control melted.
- "DIY Shock Dyno?" (158874; URL not in source) — unknown — load cell + linear pot idea; no finished build seen.
- "Cheap Simple NVH tool and write up" (117396) and "DIY chassis ear???" (8466; URLs not in source) — old — Sirometer about US$21; piezo chassis ear about US$40.
- "Torque Wrench Calibration" (81284; URL not in source) — old — beam wrench as reference.
- "Tongue weight scale…" (256837; URL not in source) — ≈2023 — bathroom-scale lever reads low; real scale about US$100–150.
- "Let's talk autocross timing" (194918) and "Where do I find timing equipment?" (24928; URLs not in source) — mixed — Race America/Tag Heuer "a few thousand".
- "Who's Running a Diff Oil Cooler?" (285286; URL not in source) — 2026 — diff 320 °F+ in one-hour sessions.
- "Recommend me a wideband" and related (180027, 161340; URLs not in source) — mixed — 14point7 Spartan about US$125; mixed support reports.
- "Good compression tester?" (275037; URL not in source) — ≈2024 — cheap testers judged adequate.
- "How do 'Portable Dyno' products work?" (178344; URL not in source) — ≈2020 — accelerometer/GPS estimates limited, fine for back-to-back.
- "Blue Bayou 240SX" build (178841; URL not in source) — multi-year — overheating anecdote (see GRM-07); one rule-of-thumb anecdote may belong to a different thread (attribution uncertain).
- "Gas tank issues/Racecar – HELP" (256316; URL not in source) — ≈2023 — gauge read 3/4 after an hour and was assumed failed.
- "1988 Nissan 200sx SE V6 Endurance Race Car" (builds 179200; URL not in source) — multi-year — surge tank fix; wall clock for stint timing.
- "Budget electric gauges"/"What Cheap Gauges Work?" (151898; URL not in source) — ≈2019 — AutoMeter and Sunpro called most dependable.

About 70 further threads were seen by title or index only (T-level, source section 2C) and are not listed here. Source ledger item L32 (a cluster of spring/shock, torque, NVH and tongue-weight DIY threads) is covered by the P lines above.

#### Products and prices named
Forum prices are historical, as quoted on the date shown. `[web]` rows are unverified retailer-listing summaries dated 2026-11-17 unless a date is shown.

| Product | Price as stated | Date | Source type |
|---|---|---|---|
| Fastmate RaceSense gauge + probe pyrometer | US$449 list | 16 Jun 2021 | forum post via search summary |
| Fastmate RaceSense (current listings) | ~US$449–490; pocket ~US$315–420; UK £275–325 | 2026 (one UK listing Apr 2026) | general web-search summary |
| Longacre combined gauge/pyrometer | US$499 | Jun 2021 | forum post via search summary |
| Longacre manual brake-pressure gauges | US$60 | old (≈2013) | forum post via search summary |
| Longacre Gagelite warning-light kit | US$25.99 | 2024-dated listing | general web-search summary |
| Pegasus 20 psi oil-pressure switch | US$29.99 | undated | general web-search summary |
| Auber 2-in-1 gauge with alarm outputs | ~US$70 | old (thread attribution uncertain) | forum post via search summary |
| ProSport digital gauges | ~US$60 each | 2024 | forum post via search summary |
| Stack stepper gauges | ~US$220 each; 3-gauge set ~US$270 | ≈2012 | forum post via search summary |
| AiM MXP dash | US$2,299 | review date unknown | forum post via search summary |
| Haltech dash / AceWell dash / generic OBD2 display | ~US$1,000 / US$309 / ~US$45 | unknown | forum post via search summary |
| ScanGauge 2 | ~US$160 | 2022 | forum post via search summary |
| MyChron 4 used / MyChron5 GPS new | US$200–250 / US$500 | 2016 | forum post via search summary |
| AiM Solo 1 used / Solo 2 | "couple hundred" / US$400 (older), US$700 (newer) | ≈2020–2024 | forum post via search summary |
| Racepak CL2 | ~US$250 | ≈2020 | forum post via search summary |
| RoadKeeper | ~US$400 | ≈2024 | forum post via search summary |
| RaceBox Mini | US$160–200 | ≈2025 | forum post via search summary |
| RaceChrono Pro app | US$20 | ≈2025 | forum post via search summary |
| Garmin Glo / Dual XGPS150A | ~US$100 / under US$100 | ≈2020 | forum post via search summary |
| Race Technology DL1 kit | ~US$1,090 | article date unknown | forum post via search summary |
| MRS Electronic CAN I/O module | from US$133 | ≈2017 | forum post via search summary |
| Autosport Labs AnalogX/AnalogX2 | US$149.95 | 2026 | general web-search summary |
| AEM 6-ch / 22-ch CAN sensor module | ~US$175–215 / ~US$380–425 | 2026 | general web-search summary |
| CSS Electronics CANmod.input | ~£444 ex VAT | 2026 | general web-search summary |
| Racepak sensor module (adds oil pressure to IQ3) | US$383 | GRM project article, date unknown | forum post via search summary |
| Bosch brake-pressure sensor via Race Technology / AiM-AEM sensors | US$290 / ~US$150 | old | forum post via search summary |
| DIY pad-thermocouple logger (parts) | ~US$85 | Dec 2025 | forum post via search summary |
| RS PRO / Labfacility pad thermocouple | ~€30 / ~£28 ex VAT | 2026 | general web-search summary |
| Izze-Racing IRTS-B-V2 IR brake sensor | US$385 each | 2026 | general web-search summary |
| CANchecked BMC04 wired brake-temp set / BLE set | ~US$1,639 / ~US$2,050–2,460 | 2026 | general web-search summary |
| AvioRace 4× IR + analogue-CAN kit | US$2,750 | 2026 | general web-search summary |
| DIY IR-array tyre sensor (parts) | ~US$170 per wheel; replication ~US$130 | Dec 2018 / ≈2019 | forum post via search summary |
| Harbor Freight IR thermometer | US$24 (US$16 with coupon); "$29.95 pyrometer" | ≈2009–2013 | forum post via search summary |
| K-type probe for multimeter | C$44 | unknown | forum post via search summary |
| Proform scale kit 67650 | US$685–800; classified US$699 | ≈2015–2023 | forum post via search summary |
| New entry scale set | ~US$600 + shipping | ≈2016 | forum post via search summary |
| Used Intercomp with cart / used sets | US$350 / US$350–1,000 | ≈2014–2018 | forum post via search summary |
| Longacre battery-box repair quote | "usually 300 or so" (US$) | ≈2024 | forum post via search summary |
| Intercomp replacement pad cable | US$85–100 shipped | ≈2023 | forum post via search summary |
| DIY HX711/Arduino scale retrofit | ~€335 / ~US$400 | ≈2021 | forum post via search summary |
| PACO hub stands (set of 4) / Flyin' Miata (pair) / hub stands considered | US$849 / US$395 / ~US$900 | 2018 / old / Feb 2026 | forum post via search summary |
| Complete bump-steer kit vs DIY | over US$400 vs ~US$125 | ≈2022 | forum post via search summary |
| Rowe PDM-60 | ~US$200 | ≈2018 | forum post via search summary |
| Eaton SSVEC fused relay hub | ~US$156 | ≈2023 | forum post via search summary |
| Baofeng-based 2-radio car kit | US$250–300; another "around 500" | ≈2020–2025 | forum post via search summary |
| Rapid Radios (cellular) | US$400 per pair + US$50/yr | ≈2025 | forum post via search summary |
| Racing Radios basic pro set | ~US$2,000 | ≈2025 | forum post via search summary |
| Flagtronics in-car unit | from ~US$250 | article date unknown | forum post via search summary |
| MyLaps transponder | lifetime US$600; X2 lease from US$160/yr; rent US$40–50/race | ≈2022 | forum post via search summary (lease figure also in a web-search summary) |
| TPMS 4-sensor display kit | US$270 | 2015 | forum post via search summary |
| AiM TPMS kit / CAN receiver | £425 / £160 | 2026 | general web-search summary |
| WHP/ECUMaster TPMS-to-CAN | US$329 | 2026 | general web-search summary |
| CoolShirt-type shirt; DIY cooler system | US$155; US$80–100 | old | forum post via search summary |
| 14point7 Spartan 2 | ~US$125 | ≈2019–2022 | forum post via search summary |
| Commercial tongue-weight scale | ~US$100–150 | ≈2023 | forum post via search summary |
| Commercial autocross timing (Race America/Tag Heuer) | "a few thousand", double for wireless | old | forum post via search summary |

Brands named without prices (as seen in the ledger): Dakota Digital, RaceCapture, Motion Raceworks, KA Sensors, Speedhut, VDO, GReddy, A'PEXi, AutoMeter, Marshall Blueline, Summit, PLX, Westach, UltraGauge, Edge CTS, Banks iDash, Sunpro, Proform shift light, Joe's, Intercomp, Rebco, SmartCamber, FasTrax, Cartek, Littelfuse, Blue Sea, Eaton Bussmann, Healtech, Shift-I, Innovate, Hyperco.

Mentioned brands found **absent** from the competitor lists (forum/web mentions only; nothing here classifies their business role): Auber, AutoMeter, Cartek, PLX, Izze-Racing, CANchecked, Fastmate/RaceSense, ProSport, ScanGauge, UltraGauge, Flagtronics, Speedhut, Lifeline, Waytek, Blue Sea, Bussmann/Eaton, CoolShirt, PACO, SmartCamber, AvioRace, MRS Electronic, Ballenger, Westach, VDO, KA Sensors, Steelman, Farmtek, Race America, Traqmate, CSS Electronics, Tulay's Wire Werks.

#### Low-yield searches and sections
- Sound/dB meters for track noise limits: only venue policy threads; negative.
- Fuel-used/fuel-flow totalisers for endurance: no request found; teams use stint time and measured fills; negative on GRM.
- Pit/stint timers and boards: only build-thread asides; thin.
- "Went back to" / "sold it" / "overkill" for data systems: no clean example; closest were the DL1 "time has passed it by" comment, a phone-plus-OBD "80% of the functions for 20% of the money" remark and the EFI-to-carburettor reversal (GRM-16).
- "Does anyone make / wish someone made": surfaced only the all-in-one gauge and no-app OBD gauge asks.
- Knock detection, shock dyno/damper pots, weather/density altitude: old, generic or idea-level; no new evidence (one racer still uses an air-density gauge).
- Flow bench/injector testing, compression/leak-down/smoke: adequately served by cheap tools and services.
- Shift lights, tach/speedo converters, wideband/AFR, fan controllers, rain lights, transponders, flag systems: commodity products, closed ecosystems or vehicle-specific; anecdotes only.
- Tyre durometer, heat cycling, warmers, nitrogen, inflators: general advice only.
- Bearing/diff temperature: IR-gun anecdotes, mixed; no stick-on sensor discussion.
- TPMS for track: mostly OEM-sensor replacement talk; the one 2015 CAN-output ask now looks solved.
- Intermittent/track-only misfire: mostly street-car threads; fuel starvation dominated track-only faults.
- Cool suits: plenty of DIY, no electronics ask.
- Recency probe (2026 electronics threads): returned mainly older threads; 2026 items seen by title only.

#### Unknowns
- No thread was read directly. Reply counts, agreement levels, later pages and exact wording are unverified; every "several users" statement is a judgement from summaries. It is recommended that a person open at least GRM-02, GRM-03, GRM-04, GRM-17, GRM-20 and the dead-Longacre thread (267943) before relying on any of it.
- "≈" dates are derived from age metadata. Start dates for GRM-03, -04, -05, -11, -16, -17, -21 and -22 are not confirmed.
- GRM-02 follow-up (parts list or code published, whether others wanted one, track result) was not recovered, so whether it is one person's project or a wider want is unknown.
- Whether a current low-cost standalone warning module with its own sensors and adjustable thresholds exists was not established from search; the owner's reason for dropping RD-032 is also not recovered in the register.
- Outcome of the dead-Longacre thread, which pad families share electronics/connectors, and any Australian installed base are unknown (the evidence is US).
- GRM gauge-accuracy test date and models, and RaceSense real-world sales or adoption, are unknown.
- `[web]` prices are unverified retailer-listing summaries in mixed currencies, several undated.
- Attribution risks: the "foam broke the gauge / 90 minutes–12 gallons" and "3/4 tank after an hour" anecdotes come from build/help threads the search blended; the digital-dash alarm quotes may belong to either GRM-05 thread.
- Selection bias: search indexing favours older, long threads; GRM skews US, Miata/E30/budget-endurance and DIY-capable, which probably understates willingness to pay and overstates DIY adequacy.
- The forum's own search and the Tech Tips index could not be browsed; Tech Tips coverage is about 15 titles surfaced by search.

### Speed-Talk

#### Coverage and access

- Research pass on 2026-11-17, guest access only (phpBB board at speed-talk.com): no registration, login, posting, messaging or vendor contact; member profiles and private messages not accessed. Vendor sites linked in posts were not visited.
- Sub-forums on the index (topic counts on 2026-11-17): Engine Tech f=1 (43,236), Advanced Engine Tech f=15 (3,502), Vintage/Classic f=84 (252), Shop & Garage Tech f=32 (2,592), General Tech f=20 (855), Vendor Marketplace f=43 (84), Industry/Business f=18 (817), Shop Equipment For Sale/Wanted f=35 (1,365), plus Driveline f=19, Chassis f=11, Electric & Hybrid f=41, Race Cars & Parts f=31 and two paid HotPass forums (f=70, f=47). Vendor Marketplace, Driveline, Chassis and Electric were not reviewed.
- Registration-labelled sections were in fact readable: f=32, f=15 and f=18 are described as "Must be Registered and Logged In to view", yet on this date a guest saw full topic lists and full post text in all three (for example t=62492, t=71472, t=64301, t=45929). The existing directory note is accurate about the label but not about actual guest visibility on this date. Attachments (photos, scans, dyno sheets, schematics, PDFs) were withheld from guests everywhere, so any claim resting on a picture is unverified. HotPass forums showed names only, zero topics; not reviewed.
- Guest-search gap: topics started roughly mid-2009 to late-2019 (topic ids about 17,000–59,000) are not returned by title or content search unless bumped later. Checked: title search "load cell" gave 0 hits although f=32 has four such titles from 2012–2019. Content search is valid only for mid-2009 and earlier, and Dec-2019 onward; the gap was covered by title lists only.
- Title lists downloaded and filtered: f=32 complete (2,595 titles, 2003–2026), f=15 complete (3,505), f=20 complete (858), f=1 645 of 865 pages (32,253 titles back to 2009-05-16). Not listed, reached only through search hits: f=18, f=35, f=84, f=19, f=11, f=31. About 39,200 titles machine-filtered and about 1,400 read by eye.
- Search behaviour: a global flood interval of about 15 s shared by all guests (roughly one query per 20–60 s); whole-word AND matching with a stop list ("DIY" and "EGT" rejected as too common); no phrase search, so multi-word complaint phrases returned mostly noise. 113 queries logged (58 title-only, 25 first-post, 30 all-posts); about 1,800 result rows skimmed.
- Topics opened: 126 (224 topic pages). About 105 read with every reply displayed, but long posts were shown truncated at 200–1,500 characters, so detail deep in very long posts may be missed. About 20 larger threads read partially (first page only, or replies filtered by keywords) and marked "partial" below. Posts read span 2004-12 to 2026-11-15; 33 opened topics contain a post from 2024 or later, 70 from 2020 or later.
- Web-search validation: 8 queries completed, then the shared search budget ran out; three planned checks (DEPAC status, Spintron support, Performance Trends spring-tester price) were not performed. Web-search facts are labelled "search summary, not directly read". Two searches (Audie Cam Pro Plus price; Buxton Bench Pro price) returned nothing relevant. No other website was opened.

#### Threads

Codes in the Register lines: (1) new to the register, (2) new evidence for an existing idea, (3) narrower or materially different version, (4) repeat of something rejected, (5) already adequately solved. Prices are the poster's figure at the post date.

**ST-01 · [Recommend me a valve spring tester](https://www.speed-talk.com/forum/viewtopic.php?t=71535)** — Shop & Garage Tech
- *Dates / evidence:* 2026-02-05 → 2026-02-06; one reply.
- *Who:* low-volume builder; customer.
- *Job and problem:* wants a bench valve spring tester; says occasional use does not justify "$1000.00 Rimac or Intercomp" (2026-02), dislikes vise-mounted units.
- *Workaround / products named:* shortlist LSM bench-top, Proform 66776/66774; reply suggests the cheaper Proform.
- *Resolution:* none.
- *Repeats and objections:* none stated beyond the cheaper-Proform reply.
- *Inference (ours):* the price step between roughly US$100–300 vise/hydraulic testers and US$900+ bench testers is still felt in 2026. Register: adjacent to RD-020 (rejected on-engine checker), class 3; verification sub-need touches RD-092.

**ST-02 · [Inexpensive valve spring tester](https://www.speed-talk.com/forum/viewtopic.php?t=68722)** — Shop & Garage Tech
- *Dates / evidence:* 2024-07-05 → 2024-07-08.
- *Who:* hobby/semi-pro asker; repliers are customers and makers, plus a head porter (vendor of head services).
- *Job and problem:* asks whether any cheap tester is any good.
- *Workaround / products named:* head porter began with a sub-US$100 mini vise tester plus calibration spring (2024-07), moved to a Performance Trends tester ("not inexpensive"), found portable track-tech testers disagreed with bench values; bathroom scale on a drill press; hydraulic tongue-weight scales; one user made a hydraulic tester (1 sq-in piston, gauge); suggestion of a ~US$40 drill-press DRO plus digital scale.
- *Resolution:* no single resolution.
- *Repeats and objections:* 4 distinct users.
- *Register:* adjacent to RD-020 (rejected on-engine checker), class 3; verification sub-need touches RD-092.

**ST-03 · [spring tester brands and recommendation](https://www.speed-talk.com/forum/viewtopic.php?t=70781)** — Engine Tech
- *Dates / evidence:* 2025-05-14 → 2025-05-17.
- *Who:* customers plus one professional porting vendor.
- *Job and problem:* wants a 1,000 lb+ tester; liquid versus digital.
- *Workaround / products named:* on-head testers described as consistency checks, not very accurate; LSM on-head and bench liked (2 users); head porter says off-head "begins and ends with a digital Buxton", Rimac fine until his eyesight failed; Performance Trends set-up praised for speed; a 20-year-old Intercomp still fine. No prices.
- *Resolution:* none stated.
- *Repeats and objections:* objection implied: adequate products exist at every level.
- *Register:* adjacent to RD-020 (rejected on-engine checker), class 3; verification sub-need touches RD-092.

**ST-04 · [Valve Spring Tester/Checker DANG!](https://www.speed-talk.com/forum/viewtopic.php?t=60160)** — Engine Tech
- *Dates / evidence:* 2020-02-19 → 2020-02-21.
- *Who:* enthusiast owning a used 0–500 lb Rimac; replies from a machinist and a volume rebuilder.
- *Job and problem:* admires the Buxton Bench Pro (one pull to coil bind, computed results).
- *Workaround / products named:* Buxton US$1,595 + US$189 PC firmware (poster's site price, 2020-02); machinist calls it "$1800"; Intercomp "over $1,000"; used Rimac ~US$600; cheap hydraulic tester described as non-repeatable; Rimac name reported bought by Proform.
- *Resolution:* none.
- *Repeats and objections:* one user asks about building one with a load cell and digital readout (already has a homemade checker); volume rebuilder finds Buxton too delicate for production.
- *Register:* adjacent to RD-020 (rejected on-engine checker), class 3; verification sub-need touches RD-092.

**ST-05 · [Valve Spring Tester](https://www.speed-talk.com/forum/viewtopic.php?t=59918)** — Engine Tech
- *Dates / evidence:* 2020-01-30 → 2021-07-02.
- *Who:* enthusiast; a South Australian shop owner; an engineer; a Queensland user.
- *Job and problem:* wants a good analog tester; distrusts digital (batteries, failing parts) and calls cheap hydraulic ones inaccurate.
- *Workaround / products named:* shop owner's Rimac digital 1700 (bought 2006) checked weekly against a Crane calibration spring, would buy Performance Trends next; engineer built own (arbor press, linear position transducer, small load cell, 0.1 lb resolution, force-vs-position graphs). Proform relaunch of Rimac noted (2021) with quality doubts.
- *Resolution:* OP bought a used Rimac.
- *Repeats and objections:* Queensland user asks for the load-cell and transducer part numbers; no public answer.
- *Register:* adjacent to RD-020 (rejected on-engine checker), class 3; verification sub-need touches RD-092.

**ST-06 · [Spring Tester that made life easier](https://www.speed-talk.com/forum/viewtopic.php?t=57365)** (partial) — Engine Tech
- *Dates / evidence:* 2019-06-26 → 2019-07-02; 15 authors; partial read.
- *Who:* head porter (vendor), two Australians, a Canadian shop; professionals.
- *Job and problem:* checking boxed valve springs quickly.
- *Workaround / products named:* head porter shows Buxton, "$1800", all 16 springs in 5 minutes (2019-06); Australians say Rimac cost "$1200 au" about 10 years earlier; interest in PC printout as a customer report card; Canadian shop tested every spring twice when buying boxes of 500.
- *Resolution:* none needed; satisfied users.
- *Repeats and objections:* none stated.
- *Inference (ours):* professionals pay happily for speed and reporting; the unmet need is not at the professional end. Register: adjacent to RD-020 (rejected on-engine checker), class 3; verification sub-need touches RD-092.

**ST-07 · [Valve spring tester ????](https://www.speed-talk.com/forum/viewtopic.php?t=21020)** (partial) — Engine Tech
- *Dates / evidence:* 2010-03-25 → 2019-12-11; 19 authors; partial read.
- *Who:* owner of a failed tester wanting 1,000 lb+; later an engineer and others.
- *Job and problem:* replace a broken tester; 2019 exchange on whether a tester is needed and how its accuracy is known.
- *Workaround / products named:* Performance Trends tester; Roehrig lab unit "around $12,000" (2010-03); bathroom scale plus drill press "as accurate as any"; Buxton with 2" dial indicator added.
- *Resolution:* none.
- *Repeats and objections:* 2019: engineer says caliper plus spreadsheet suffices; others reply boxed springs still need checking and ask how any tester is calibrated.
- *Register:* adjacent to RD-020 (rejected on-engine checker), class 3; verification sub-need touches RD-092.

**ST-08 · [Mini Valve spring tester](https://www.speed-talk.com/forum/viewtopic.php?t=51845)** — Engine Tech
- *Dates / evidence:* 2017-12-23 → 2018-01-16; 13 authors.
- *Who:* one-build-a-year hobbyist; South Australian user and others.
- *Job and problem:* cannot justify a Rimac; asks about Proform 700 lb mini versus Speedway.
- *Workaround / products named:* old vise tester "plus or minus whatever it felt like" until checked with a calibration spring; Goodson bench testers "from $899.00 on up" (2017-12); "have a local shop test"; Tavia mini read 160 versus 162 lb on a calibration spring; advice to average five readings.
- *Resolution:* none; mixed verdict on cheap units.
- *Repeats and objections:* objection: pay a local shop instead.
- *Register:* adjacent to RD-020 (rejected on-engine checker), class 3; verification sub-need touches RD-092.

**ST-09 · [Calibrated Checking Valve Spring](https://www.speed-talk.com/forum/viewtopic.php?t=47010)** (partial) — Engine Tech
- *Dates / evidence:* 2016-07-12 → 2016-07-21; partial read.
- *Who:* design engineer with a Proform 700 lb mini in a drill press; other owners.
- *Job and problem:* checks a Comp calibration spring (~US$35, 2016-07); tester read 7–9% low.
- *Workaround / products named:* another user's Proform leaks oil, drifts with temperature, first unit arrived empty; adjusts via bottom plug against a Crane spring; a third had a lab calibrate a spring for his Rimac.
- *Resolution:* none stated.
- *Repeats and objections:* three users report cheap-tester accuracy or calibration problems.
- *Register:* adjacent to RD-020 (rejected on-engine checker), class 3; verification sub-need touches RD-092.

**ST-10 · [PAC calibration spring and Rimac tester](https://www.speed-talk.com/forum/viewtopic.php?t=61214)** — Shop & Garage Tech
- *Dates / evidence:* 2020-05-21 → 2020-07-06.
- *Who:* rural builder; customer.
- *Job and problem:* new Intercomp 1,000 lb and old Rimac 500 lb disagree; asks who calibrates Rimacs (nobody named).
- *Workaround / products named:* calibration springs: Larson US$182 (2020-05), PAC T900 (8 points, 105 lb to 571 lb), Goodson 100–285 lb.
- *Resolution:* none; OP worries a ~570 lb spring checks only half of a 1,000 lb tester.
- *Repeats and objections:* one user returned three Intercomps before finding the digital height gauge mount was the error source (fixed with a dial gauge).
- *Register:* adjacent to RD-020 (rejected on-engine checker), class 3; verification sub-need touches RD-092.

**ST-11 · [rimac spring tester calibration instructions](https://www.speed-talk.com/forum/viewtopic.php?t=45929)** — Industry/Business
- *Dates / evidence:* 2016-03-10 → 2025-03-05.
- *Who:* shops, including a vintage-engine shop.
- *Job and problem:* shops share a faxed Rimac adjustment procedure; 2025-01 a vintage-engine shop cannot get a new-looking 500 lb unit right at both ends of the scale.
- *Workaround / products named:* Rimac-branded dual calibration spring bought from a retailer for "around 75.00" (2025-03).
- *Resolution:* none stated.
- *Repeats and objections:* none stated.
- *Register:* adjacent to RD-020 (rejected on-engine checker), class 3; verification sub-need touches RD-092.

**ST-12 · [Proform Spring Tester](https://www.speed-talk.com/forum/viewtopic.php?t=40008)** — Shop & Garage Tech
- *Dates / evidence:* 2014-05-24 → 2014-07-21.
- *Who:* buyer of a Proform 66776; customer.
- *Job and problem:* digital height scale mounted sideways, flexing handwheel, fixed gauge.
- *Workaround / products named:* refitted a US$50 eBay vertical DRO (2014) and steel handle; Proform reportedly adopted two changes.
- *Resolution:* owner's own fix.
- *Repeats and objections:* same sideways gauge on Intercomp; Intercomp height bracket gave wrong readings (same user as ST-10, six years earlier).
- *Register:* adjacent to RD-020 (rejected on-engine checker), class 3; verification sub-need touches RD-092.

**ST-13 · [Bench Pro Valve Spring Tester](https://www.speed-talk.com/forum/viewtopic.php?t=60123)** — Shop & Garage Tech
- *Dates / evidence:* 2020-02-16 → 2020-03-11.
- *Who:* two professional shops; customers.
- *Job and problem:* ordering Buxton testers (3-week lead).
- *Workaround / products named:* one shop sells a 2-year-old Intercomp for US$700 (2020).
- *Resolution:* satisfied customers.
- *Repeats and objections:* none stated.
- *Register:* adjacent to RD-020 (rejected on-engine checker), class 3; verification sub-need touches RD-092.

**ST-14 · [OK, engineers, let's design a valve spring tester](https://www.speed-talk.com/forum/viewtopic.php?t=37769)** — Shop & Garage Tech
- *Dates / evidence:* 2013-11-07 → 2013-11-11.
- *Who:* vintage-engine shop; other shops.
- *Job and problem:* old Rimac read 140 lb versus maker's 120 lb, calibration spring lost; proposes a press plus gauge.
- *Workaround / products named:* one shop already uses Omega load cells with digital readout; another points to a spring-maker's load checker ("expensive but wonderful"). No prices.
- *Resolution:* none.
- *Repeats and objections:* load-cell approach already in use by one shop.
- *Register:* adjacent to RD-020 (rejected on-engine checker), class 3; verification sub-need touches RD-092.

**ST-15 · [Valve spring tester (on head)](https://www.speed-talk.com/forum/viewtopic.php?t=60675)** — Engine Tech
- *Dates / evidence:* 2020-04-03 → 2020-04-04.
- *Who:* racer (SB2.2 heads, shaft rockers).
- *Job and problem:* wants an on-head tester; LSM not answering; Buxton on-head judged "Big $$$$".
- *Workaround / products named:* none beyond the above.
- *Resolution:* none.
- *Repeats and objections:* repeat only.
- *Inference (ours):* relevant to RD-020 only as a repeat. Register: RD-020.

**ST-16 · [Cam Doctor costs](https://www.speed-talk.com/forum/viewtopic.php?t=71472)** — Shop & Garage Tech
- *Dates / evidence:* 2026-01-17; one reply.
- *Who:* customer.
- *Job and problem:* asks the cost of a basic Audie Cam Pro.
- *Workaround / products named:* reply says Audie's base set-up was "around $4,700" when last checked (2026-01-17).
- *Resolution:* price answer only.
- *Repeats and objections:* none stated.
- *Register:* RD-026, class 2 (class 3 if scoped as interface electronics only).

**ST-17 · [Camshaft measuring](https://www.speed-talk.com/forum/viewtopic.php?t=69294)** — Engine Tech
- *Dates / evidence:* 2024-10-12 → 2024-10-20.
- *Who:* machine shop (tractor cams); a cam designer (vendor); another machinist; maker/hobby-level commercial users.
- *Job and problem:* commercial equipment "rather pricey for the occasional user".
- *Workaround / products named:* built an Arduino, stepper and digital indicator rig logging each degree to a spreadsheet; build cost "very minimal"; cam designer notes first Cam Doctors were DOS, half-degree steps.
- *Resolution:* self-built.
- *Repeats and objections:* objection: use the actual lifter, not a ball; another machinist has building one on his bucket list.
- *Register:* RD-026, class 2 (class 3 if scoped as interface electronics only).

**ST-18 · [Cam Analyser](https://www.speed-talk.com/forum/viewtopic.php?t=60307)** — Shop & Garage Tech
- *Dates / evidence:* 2020-03-02 → 2020-03-17.
- *Who:* UK race-engine builder (maker/promoter); Danish developer (MJP, vendor) present; cam designer; Swedish and Finnish users.
- *Job and problem:* identifying ageing cams of unknown origin.
- *Workaround / products named:* built a stepper/Arduino analyser, "around $800 in parts" (2020-03); US analysers "around $3500" landed in Europe (2020-03-03); intends to sell built stands in Europe. Software, circuit, parts list and firmware belong to MJP, sold separately.
- *Resolution:* self-built; a Finn already runs the MJP set-up.
- *Repeats and objections:* cam designer says software is the expensive part; a Swede says he would buy one; vintage-engine shop wants faster swap-meet cam identification.
- *Register:* RD-026, class 2 (class 3 if scoped as interface electronics only).

**ST-19 · [Encoder reading box and graphing software](https://www.speed-talk.com/forum/viewtopic.php?t=37958)** — Advanced Engine Tech
- *Dates / evidence:* 2013-11-20 → 2015-04-21; 39 posts.
- *Who:* software developer, maker.
- *Job and problem:* sought a ~US$600 commercial box reading two encoders; none identified beyond Audie, Andrews, Performance Trends, Sportdevices.
- *Workaround / products named:* built an Arduino and rotary-table/stepper rig, "roughly $600" versus "$3500" commercial (2014-03); later posted Arduino and VB code; others pointed to MJP build instructions.
- *Resolution:* self-built.
- *Repeats and objections:* at least five different users asked for plans or a parts list over 18 months; caveat: encoder pulses over serial miss counts at speed, so a hardware counter is needed.
- *Register:* RD-026, class 2 (class 3 if scoped as interface electronics only).

**ST-20 · [Cam Doctor or other brands??](https://www.speed-talk.com/forum/viewtopic.php?t=23523)** (partial) — Engine Tech
- *Dates / evidence:* 2010-10-08 → 2010-10-19; 12 authors; partial read.
- *Who:* buyer comparing Audie, Performance Trends, Andrews; the same developer as ST-19.
- *Job and problem:* choosing a cam analyser.
- *Workaround / products named:* developer had built his own (card US$49, 2010-10); cam designer prefers Audie "for the money".
- *Resolution:* none.
- *Repeats and objections:* three users immediately offered to pay for a parts list plus programmed card/software; one said it could be a cam-related product with a market.
- *Register:* RD-026, class 2 (class 3 if scoped as interface electronics only).

**ST-21 · [Camshaft measuring stand recommendations](https://www.speed-talk.com/forum/viewtopic.php?t=51002)** — Engine Tech
- *Dates / evidence:* 2017-09-26 → 2017-10-02.
- *Who:* professional engine shop; a cam designer.
- *Job and problem:* about to buy an Audie or Performance Trends stand.
- *Workaround / products named:* cam designer says Audie is more accurate; PT stand not rigid enough, follower not exactly tangent. Cam checks charged at US$25 per cylinder, US$100 for eight, or US$50 with printed card (2017-09); owning one "builds traffic".
- *Resolution:* none stated.
- *Repeats and objections:* the PT rigidity objection above.
- *Register:* RD-026, class 2 (class 3 if scoped as interface electronics only).

**ST-22 · [Cam profile measuring/mapping equipment](https://www.speed-talk.com/forum/viewtopic.php?t=36532)** — Advanced Engine Tech
- *Dates / evidence:* 2013-07-18 → 2013-08-15.
- *Who:* Irish builder mapping cams by hand with degree wheel and indicator.
- *Job and problem:* wants an encoder stand.
- *Workaround / products named:* Audie (new interface needs no serial port), Andrews EZCam (dearer, better analysis), Performance Trends plus motorised stand, own stand on a reground lathe bed; original Cam Doctor no longer available. No prices.
- *Resolution:* options offered.
- *Repeats and objections:* adequate commercial options listed.
- *Register:* RD-026, class 2 (class 3 if scoped as interface electronics only).

**ST-23 · [Audies Cam Pro Plus](https://www.speed-talk.com/forum/viewtopic.php?t=64301)** — Advanced Engine Tech
- *Dates / evidence:* 2021-11-04 → 2021-11-23.
- *Who:* long-time owner; a cam designer replied.
- *Job and problem:* five years of wrong readings; three phone sessions with the vendor without a fix.
- *Workaround / products named:* Audie Cam Pro Plus.
- *Resolution:* resolved in two forum posts (lifter-bank angle left at a small-block Chevy setting; report fields zeroed).
- *Repeats and objections:* none stated.
- *Inference (ours):* support burden for this class is software configuration, not hardware. Register: RD-026, class 2 (class 3 if scoped as interface electronics only).

**ST-24 · [Quadrant Scientific Cam Doctor](https://www.speed-talk.com/forum/viewtopic.php?t=72099)** — Engine Tech
- *Dates / evidence:* 2026-10-23 → 2026-11-01.
- *Who:* owner of an inherited 1990s Cam Doctor (Rev E board, 1997).
- *Job and problem:* original linear sensor broke about 20 years ago, replacement Ono Sokki gauge never worked, software sits on a Windows 98 PC that also runs a PR200 spring tester; maker "gone for decades".
- *Workaround / products named:* none.
- *Resolution:* none.
- *Repeats and objections:* none stated.
- *Register:* RD-026, class 2 (class 3 if scoped as interface electronics only).

**ST-25 · Local cam-measuring service requests — [t=38495](https://www.speed-talk.com/forum/viewtopic.php?t=38495), [t=41760](https://www.speed-talk.com/forum/viewtopic.php?t=41760), [t=44148](https://www.speed-talk.com/forum/viewtopic.php?t=44148)** — sub-forum not stated
- *Dates / evidence:* t=38495 2014-01 (how fixtures place the lifter), t=41760 2014-11, t=44148 2015-08; titles not recorded in source; opened.
- *Who:* people seeking a local owner of a Cam Doctor.
- *Job and problem:* get one cam measured as a service.
- *Workaround / products named:* none.
- *Resolution:* none stated.
- *Repeats and objections:* three threads, 2014–2015.
- *Register:* RD-026, class 2 (class 3 if scoped as interface electronics only).

**ST-26 · [Upgrading a Superflow 901](https://www.speed-talk.com/forum/viewtopic.php?t=52878)** — Shop & Garage Tech
- *Dates / evidence:* 2018-04-03 → 2019-05-18; OP outcome 2019-03.
- *Who:* professional shop with a 2,000 lb-ft absorber.
- *Job and problem:* modernise the dyno electronics.
- *Workaround / products named:* SuperFlow quoted US$22,500 (902 electronics, servo), other quotes US$15–23k (2018-04); Land & Sea rep reportedly offered a console/speed-sensor update for US$7,500; one shop paid ~US$9k for a Land & Sea DAQ upgrade and rates its support above SuperFlow's; a 902-conversion owner reports better repeatability and 3–4% lower numbers.
- *Resolution:* OP kept the DOS software, built a PC to run it and added an external logger.
- *Repeats and objections:* OEM price judged out of reach.
- *Register:* RD-026, class 2 (class 3 if scoped as interface electronics only).

**ST-27 · [SF901 software/console problem](https://www.speed-talk.com/forum/viewtopic.php?t=32734)** — Shop & Garage Tech
- *Dates / evidence:* 2012-09-25 → 2017-10-25; 44 posts; resolved 2013-04.
- *Who:* Australian buyer of an imported 901.
- *Job and problem:* WinDyn 1.16 would not talk to the console; maker's support suggested upgrading.
- *Workaround / products named:* weeks of serial-cable/COM experiments with a dozen helpers.
- *Resolution:* only the genuine SuperFlow comm cable (non-standard wiring) works, found by taking the PC to another Australian owner.
- *Repeats and objections:* 2017: another owner seeks Win98 WinDyn 1.2.1, told it no longer exists; a flow-bench owner had to rename COM5 to COM1 after a lightning-killed serial port.
- *Register:* no matching record, class 1 (class 5 for whole-system retrofit).

**ST-28 · [SF 901 Load Sensor Cable from Cart to Console](https://www.speed-talk.com/forum/viewtopic.php?t=62492)** — Shop & Garage Tech
- *Dates / evidence:* 2020-11-19 → 2026-11-06; a new owner posted 2026-10-17.
- *Who:* professional shop; later a new 901 owner.
- *Job and problem:* torque reads "1000", cable wires pulled from plug; SuperFlow no longer makes the cable.
- *Workaround / products named:* generic connectors; spares from a dead 901.
- *Resolution:* no documented fix.
- *Repeats and objections:* the 2026 owner needs the same cable/pinout.
- *Register:* no matching record, class 1 (class 5 for whole-system retrofit).

**ST-29 · SuperFlow 901 and other orphaned-software cases** — mixed sub-forums
- *Dates / evidence:* [t=66808](https://www.speed-talk.com/forum/viewtopic.php?t=66808) 2023-04; [t=67283](https://www.speed-talk.com/forum/viewtopic.php?t=67283) 2023-07-27 → 2023-09-18; [t=66634](https://www.speed-talk.com/forum/viewtopic.php?t=66634) 2023; [t=58528](https://www.speed-talk.com/forum/viewtopic.php?t=58528) 2019 (no replies); [t=69520](https://www.speed-talk.com/forum/viewtopic.php?t=69520) 2024-11 (no replies); [t=56216](https://www.speed-talk.com/forum/viewtopic.php?t=56216) 2019; [t=62802](https://www.speed-talk.com/forum/viewtopic.php?t=62802) 2021; [t=47668](https://www.speed-talk.com/forum/viewtopic.php?t=47668) 2016; [t=71891](https://www.speed-talk.com/forum/viewtopic.php?t=71891) 2026-06-30 → 2026-10-28; [t=62533](https://www.speed-talk.com/forum/viewtopic.php?t=62533) 2020-11 (no replies).
- *Who:* dyno owners, US, Australia, Sweden; customers.
- *Job and problem:* old 901 electronics drifted 4–5% high; burnt choke in sensor box; unknown 0–5 V scaling for widebands; 3,000 lb load cell with display stopping at 1,000; blown isolation-board resistor; dead 486SX drive; EPROM-tied WinDyn/DOS versions; 1980s `.SD9` files unopenable on Windows 11; budget water-brake control now DEPAC is gone.
- *Workaround / products named:* a Texas owner converted to YourDyno at "about 20%" of OEM cost (2023); viewer 5.2.0 runs on Win 7, file is concatenated text.
- *Resolution:* only the `.SD9` and YourDyno cases; the no-reply threads none.
- *Repeats and objections:* ten threads; five of the dyno threads had no reply.
- *Register:* no matching record, class 1 (class 5 for whole-system retrofit).

**ST-30 · [DTS dyno problems again](https://www.speed-talk.com/forum/viewtopic.php?t=54534)** and related — Shop & Garage Tech
- *Dates / evidence:* t=54534 2018-09-07 → 2022-06-28, 32 posts; [t=44205](https://www.speed-talk.com/forum/viewtopic.php?t=44205) 2015; [t=68517](https://www.speed-talk.com/forum/viewtopic.php?t=68517) General Tech 2024-05 (no replies); [t=70571](https://www.speed-talk.com/forum/viewtopic.php?t=70571) 2025-03.
- *Who:* DTS owners; Power Test/SuperFlow vice-president (vendor) and a DTS founder (ex-vendor) replied.
- *Job and problem:* console faults; acquisition needs a PC with an ISA slot; 2022 three more owners seek a computer, fuel-flow sensor, servo-drive documentation; DTS4000 drive died with one executable unrecoverable.
- *Workaround / products named:* vendor says repairs possible and WinDyn 4.0 runs on Windows 10; upgrade "at 28k and 4 months lead time" (2015); misfire traced to shop earth noise (2025-03).
- *Resolution:* partial; referral to an ex-employee.
- *Repeats and objections:* no schematics; fear for the old computer.
- *Register:* no matching record, class 1 (class 5 for whole-system retrofit).

**ST-31 · [Depac Software ?](https://www.speed-talk.com/forum/viewtopic.php?t=63017)** and related — Shop & Garage Tech
- *Dates / evidence:* t=63017 2021-02-19 → 2025-08-08; [t=61702](https://www.speed-talk.com/forum/viewtopic.php?t=61702) 2020-07; [t=66076](https://www.speed-talk.com/forum/viewtopic.php?t=66076) 2022-12 (no replies); [t=71670](https://www.speed-talk.com/forum/viewtopic.php?t=71670) Engine Tech 2026-03-30 → 2026-04-07; [t=34087](https://www.speed-talk.com/forum/viewtopic.php?t=34087) 2013.
- *Who:* DEPAC owners (US, Argentina, UK).
- *Job and problem:* five separate owners lost the PC holding DEPAC DOS software after the principal died; erratic torque after 14 years; Stuska XS-211 reading a fixed torque; 2013 owner lost channel formulas (vendor then alive, fixed it).
- *Workaround / products named:* runs on a Win95 partition; referral to DynoHelp.
- *Resolution:* diagnosis by forum in the 2026 thread; others none.
- *Repeats and objections:* one poster calls for a "Depac orphan support group".
- *Register:* no matching record, class 1 (class 5 for whole-system retrofit).

**ST-32 · [Stuska Dyno question](https://www.speed-talk.com/forum/viewtopic.php?t=70061)** and [t=72139](https://www.speed-talk.com/forum/viewtopic.php?t=72139) (partial) — Shop & Garage Tech / Engine Tech
- *Dates / evidence:* t=70061 2025-03-14 → 2025-04-26; t=72139 2026-11-09 → 2026-11-15, partial.
- *Who:* engine builder; contest dyno owner.
- *Job and problem:* computer-controlled Stuska reads 10–13% low, calibration-order confusion; same engine 437 hp there versus 496 hp elsewhere; contest dyno "about 7 percent low", second event running out of calibration.
- *Workaround / products named:* parent company "didn't have much"; one owner plans to replace a temperature-drifting SuperFlow load cell.
- *Resolution:* none stated.
- *Repeats and objections:* two threads, 2025–2026.
- *Register:* no matching record, class 1 (class 5 for whole-system retrofit).

**ST-33 · [Spintron Operating Software](https://www.speed-talk.com/forum/viewtopic.php?t=58094)** — Advanced Engine Tech
- *Dates / evidence:* 2019-08-14 → 2019-12-15.
- *Who:* Spintron owner on Windows XP with 2004 software; a well-known induction specialist; another owner with two machines.
- *Job and problem:* maker no longer updates the software.
- *Workaround / products named:* reply: ask Performance Trends. No product named.
- *Resolution:* none.
- *Repeats and objections:* specialist says three other individuals approached him and "someone needs to come up with a low cost plug and play system".
- *Register:* no matching record, class 1 (class 5 for whole-system retrofit).

**ST-34 · Engine balancers** — mixed sub-forums
- *Dates / evidence:* [t=46365](https://www.speed-talk.com/forum/viewtopic.php?t=46365) 2016-04; [t=54386](https://www.speed-talk.com/forum/viewtopic.php?t=54386) 2018; [t=67634](https://www.speed-talk.com/forum/viewtopic.php?t=67634) 2023; [t=58657](https://www.speed-talk.com/forum/viewtopic.php?t=58657) 2019 (no replies); [t=68255](https://www.speed-talk.com/forum/viewtopic.php?t=68255) 2024; [t=69644](https://www.speed-talk.com/forum/viewtopic.php?t=69644) General Tech 2024-12; [t=35373](https://www.speed-talk.com/forum/viewtopic.php?t=35373) partial, 2013–14, 53 posts.
- *Who:* balancer owners; one vendor post (Turner Technology).
- *Job and problem:* analog-to-digital retrofit; Hines HC-500 drive crash, no software for a 1999 machine; Hines calibration (maker "just want to sell a new one"); encoder part unobtainable; tach pickup.
- *Workaround / products named:* Turner ~US$5,000 + computer, T&S US$7,500–10,000, new ~US$20k (2016-04); Turner now makes replacement SW/Baltech/Hines sensors; homemade balancer debate ended "buy an old Stewart-Warner".
- *Resolution:* vendor sensor supply; others none.
- *Repeats and objections:* caution that conversions do not guarantee correct readings (stanchion stiffness).
- *Register:* no matching record, class 1 (class 5 for whole-system retrofit).

**ST-35 · Other legacy electronics** — mixed sub-forums
- *Dates / evidence:* [t=65433](https://www.speed-talk.com/forum/viewtopic.php?t=65433) 2022; [t=55118](https://www.speed-talk.com/forum/viewtopic.php?t=55118) 2018; [t=68996](https://www.speed-talk.com/forum/viewtopic.php?t=68996) 2024-09 (see ST-39); [t=67040](https://www.speed-talk.com/forum/viewtopic.php?t=67040) 2023; [t=66577](https://www.speed-talk.com/forum/viewtopic.php?t=66577) 2023; [t=62446](https://www.speed-talk.com/forum/viewtopic.php?t=62446) 2020; [t=56622](https://www.speed-talk.com/forum/viewtopic.php?t=56622) 2019; [t=53140](https://www.speed-talk.com/forum/viewtopic.php?t=53140) 2018. Low-budget dyno builders: [t=32877](https://www.speed-talk.com/forum/viewtopic.php?t=32877) 2012; [t=61596](https://www.speed-talk.com/forum/viewtopic.php?t=61596) 2020, partial, 21 authors.
- *Who:* owners of flow benches, loggers, meters; home dyno builders.
- *Job and problem:* SF-600 with FlowCom and Win95 laptop, serial settings unknown; Innovate ST-12 no longer supported; RPM Performance logger lost its serial port on a new laptop; G-Tech Pro unobtainable; dead Snap-on meter LCD; ignition and VFD noise upsetting consoles.
- *Workaround / products named:* referral to Performance Trends; logger fixed after hours; bought Dragy at "less than half the price"; replace the meter; shielding and earthing; DEPAC "too far out of our budget"; home-built cart with Land & Sea brake and Performance Trends data/control.
- *Resolution:* several fixed or replaced; others none stated.
- *Repeats and objections:* none stated.
- *Register:* no matching record, class 1 (class 5 for whole-system retrofit).

**ST-36 · [Need parts for a Marquette distributor tester](https://www.speed-talk.com/forum/viewtopic.php?t=63548)** — Shop Equipment For Sale/Wanted
- *Dates / evidence:* 2021-05-23 → 2025-05-31; 31 posts.
- *Who:* at least 8 owners of Marquette, King and Allen machines (one in Australia under the Blackhawk name); a US software vendor and dyno owner.
- *Job and problem:* missing degree wheel/chuck, strobe tubes with no part number, lost manuals, incomplete schematics.
- *Workaround / products named:* owners fabricate parts; one converted his machine to an LED light source and digital tach and published a rebuilt manual; vendor describes a homemade adjustable spark-gap load board.
- *Resolution:* owner-made conversions.
- *Repeats and objections:* at least 8 machine owners in this thread.
- *Register:* RD-041, class 2 / 3.

**ST-37 · [Sun Distributor Tester – Ignition Simulation Plate](https://www.speed-talk.com/forum/viewtopic.php?t=70021)** — Shop & Garage Tech
- *Dates / evidence:* 2025-03-08 → 2025-05-08.
- *Who:* restorer of a Sun 504; a specialist parts supplier (Paramount); a long-time owner.
- *Job and problem:* parts and an ignition-simulation plate.
- *Workaround / products named:* Paramount supplies parts, strobes and a converter box for electronic ignitions.
- *Resolution:* supplier route exists.
- *Repeats and objections:* long-time owner says machines are "making a serious come back" with points-ignition hot rods; also used for aircraft magnetos.
- *Register:* RD-041, class 2 / 3.

**ST-38 · [Need help with a Sun EDT-5001](https://www.speed-talk.com/forum/viewtopic.php?t=36464)** — Shop & Garage Tech
- *Dates / evidence:* 2013-07-11 → 2016-11-08.
- *Who:* owners of a military-surplus electronic distributor tester.
- *Job and problem:* d'Arsonval meters fail (zinc castings); machine reportedly ~US$8k each new (reported 2013).
- *Workaround / products named:* suggestion to bypass with an Innovate logger; the user says it "costs more than double" what he paid for the tester.
- *Resolution:* none.
- *Repeats and objections:* two later owners need the test lead or manual.
- *Register:* RD-041, class 2 / 3.

**ST-39 · [Innovate LMA-3 problems](https://www.speed-talk.com/forum/viewtopic.php?t=68996)** — Engine Tech
- *Dates / evidence:* 2024-09-11 → 2024-09-16.
- *Who:* carburetted street-engine owner; a carb/ignition tuner.
- *Job and problem:* wants manifold vacuum and ignition timing in his LM-2 logs.
- *Workaround / products named:* tuner says only pre-2008 LMA-3 units with old software record spark advance, "as far as I know" the only way to log it; believes it was dropped because users ignored set-up instructions; he runs a pre-2008 unit on a Sun machine to plot curves. USB-serial chipset trouble (2 users).
- *Resolution:* none for OP.
- *Repeats and objections:* one explicit statement of the logging gap.
- *Register:* RD-041, class 2 / 3.

**ST-40 · Timing lights** — Engine Tech and other
- *Dates / evidence:* [t=46619](https://www.speed-talk.com/forum/viewtopic.php?t=46619) partial, 2016-05-25 → 2018-02-18, 50 posts, 23 authors; [t=33249](https://www.speed-talk.com/forum/viewtopic.php?t=33249) partial, 2012-11, 13 authors; [t=61078](https://www.speed-talk.com/forum/viewtopic.php?t=61078) 2020.
- *Who:* tuners and owners.
- *Job and problem:* lights disagree and show progressive retard with rpm; an MSD light (US$200+, 2016-05) worked on one of four cars; three lights give unreadable marks with MSD multi-spark (MSD tech had no answer); a new Innova dial-back light dead on arrival.
- *Workaround / products named:* solid-core wire on #1; Ferret lights; verify with a scope.
- *Resolution:* none stated.
- *Repeats and objections:* three threads; five more titles seen, not opened (t=25379, t=44221, t=7489, t=61096, t=72081).
- *Register:* no matching record, class 1 (commodity category).

**ST-41 · [Carb guys use a knock sensor?](https://www.speed-talk.com/forum/viewtopic.php?t=44489)** — Engine Tech
- *Dates / evidence:* 2015-09-30 → 2015-10-01.
- *Who:* carb 383 solid-roller owner.
- *Job and problem:* cannot hear ping over the car; asks for a sensor or gauge.
- *Workaround / products named:* MSD Knock Alert 8964 (used on solid cams by an Australian); J&S stand-alone knock control (4 years on a carb LS); kit-electronics retailer's op-amp and bar-graph kit "real cheap".
- *Resolution:* options offered.
- *Repeats and objections:* objection that block-sensor knock detection is "virtually useless with a solid roller, headers".
- *Inference (ours):* source treats this as the only request for a stand-alone indicator. Register: RD-012 Portable Knock Meter (parked, not rejected), class 2.

**ST-42 · Knock detection, further threads** — Engine Tech and other
- *Dates / evidence:* [t=23209](https://www.speed-talk.com/forum/viewtopic.php?t=23209) partial, 2010-09; [t=70801](https://www.speed-talk.com/forum/viewtopic.php?t=70801) partial, 2025-05/06, 83 posts; [t=71216](https://www.speed-talk.com/forum/viewtopic.php?t=71216) 2025-10 → 2025-11-17; [t=65055](https://www.speed-talk.com/forum/viewtopic.php?t=65055) 2022 and [t=71864](https://www.speed-talk.com/forum/viewtopic.php?t=71864) 2026, ancillary.
- *Who:* hobbyists; J&S principal (vendor).
- *Job and problem:* only MSD found for detonation control; hobbyist wants to know which cylinder detonates; vendor says piston noise is the main interference.
- *Workaround / products named:* scope plus knock sensor against #1 plug wire, or J&S (individual-cylinder retard); J&S lists three current versions and an ion-sensing research project that "will be very expensive". No prices.
- *Resolution:* none stated.
- *Repeats and objections:* nothing found asking for a hand-held knock listening meter; "det cans"/headphones searches gave only two passing mentions (2006, 2009).
- *Inference (ours):* source rates this as a technical caution plus one supportive use case, not new demand. Register: RD-012, class 2.

**ST-43 · Flow-bench electronics** — mixed sub-forums
- *Dates / evidence:* [t=47193](https://www.speed-talk.com/forum/viewtopic.php?t=47193) 2016; [t=54639](https://www.speed-talk.com/forum/viewtopic.php?t=54639) 2018; [t=58977](https://www.speed-talk.com/forum/viewtopic.php?t=58977) 2019; [t=63356](https://www.speed-talk.com/forum/viewtopic.php?t=63356) 2021; [t=41818](https://www.speed-talk.com/forum/viewtopic.php?t=41818) 2014; [t=69376](https://www.speed-talk.com/forum/viewtopic.php?t=69376) 2024 (no replies).
- *Who:* flow-bench users.
- *Job and problem:* one open wish: an SF-110 owner "drumming up ways to get an air speed".
- *Workaround / products named:* Audie Flow Quik/FlowPro, PTS digital manometer, C&D "Blue Box" (developer active on forum), Performance Trends, FP1; DIY community at a separate flow-bench forum.
- *Resolution:* served by existing products.
- *Repeats and objections:* adequate alternatives. Register: RD-023, class 5.

**ST-44 · Blow-by meters** — [t=15556](https://www.speed-talk.com/forum/viewtopic.php?t=15556) — sub-forum not stated
- *Dates / evidence:* 2009.
- *Who:* users; not further stated.
- *Job and problem:* measuring blow-by.
- *Workaround / products named:* J-Tec ("a little pricey"), Dwyer rotameter ~US$70 (2009-03), Performance Trends 0–5 V sensor, DEPAC sensor, King Instrument.
- *Resolution:* adequate cheap options.
- *Repeats and objections:* alternatives listed. Register: RD-037, class 4 / 5.

**ST-45 · Leak-down and compression testers** — [t=70207](https://www.speed-talk.com/forum/viewtopic.php?t=70207) 2025; [t=67470](https://www.speed-talk.com/forum/viewtopic.php?t=67470) 2023; [t=16132](https://www.speed-talk.com/forum/viewtopic.php?t=16132) 2009; [t=35895](https://www.speed-talk.com/forum/viewtopic.php?t=35895) 2013
- *Dates / evidence:* as listed; [t=66002](https://www.speed-talk.com/forum/viewtopic.php?t=66002) and [t=65861](https://www.speed-talk.com/forum/viewtopic.php?t=65861) seen in search excerpts only.
- *Who:* commodity-tool users; a carb/MFI specialist (2009).
- *Job and problem:* commodity tools; the specialist found 5–8% differences between brands (no orifice standard); failures are Schrader valves.
- *Workaround / products named:* a digital Mityvac storing 12 cylinders is liked; several point to pressure transducer plus scope for running compression.
- *Resolution:* commodity tools adequate.
- *Repeats and objections:* alternatives. Register: RD-099, class 5.

**ST-46 · Whistler / cubic-inch checking** — [t=64600](https://www.speed-talk.com/forum/viewtopic.php?t=64600) — sub-forum not stated
- *Dates / evidence:* 2022.
- *Who:* buyer-inspection use case.
- *Job and problem:* checking an engine's capacity before purchase.
- *Workaround / products named:* acrylic "bubble checker", borescope.
- *Resolution:* alternatives suggested.
- *Repeats and objections:* two posters say a whistler is easily fooled (one reports an over ~15 to 1 engine whistling 9.5). Register: RD-033 / RD-034, class 4.

**ST-47 · Rod-bolt stretch gauges** — [t=567](https://www.speed-talk.com/forum/viewtopic.php?t=567) (2004–06, 12 authors); [t=2648](https://www.speed-talk.com/forum/viewtopic.php?t=2648) (2006)
- *Dates / evidence:* as listed.
- *Who:* engine builders; not further stated.
- *Job and problem:* wishes limited to finer resolution, stiff spring, in-engine access.
- *Workaround / products named:* ARP, BHJ, Proform, JEGS gauges judged adequate. No prices.
- *Resolution:* existing gauges adequate.
- *Repeats and objections:* adequate alternatives. Register: RD-021, class 5.

**ST-48 · Sonic thickness testers** — [t=64850](https://www.speed-talk.com/forum/viewtopic.php?t=64850) (2022); [t=61283](https://www.speed-talk.com/forum/viewtopic.php?t=61283) (2020)
- *Dates / evidence:* as listed.
- *Who:* users; not further stated.
- *Job and problem:* unmet detail is small curved probes and holders for ports; users grind probes to a radius.
- *Workaround / products named:* US$75–200 imports within 0.005" of a Dakota unit (2022-03).
- *Resolution:* imports accepted.
- *Repeats and objections:* two threads. Register: RD-024, class 5.

**ST-49 · Profilometers** — [t=33856](https://www.speed-talk.com/forum/viewtopic.php?t=33856) (2012); [t=49419](https://www.speed-talk.com/forum/viewtopic.php?t=49419) (2017); [t=71561](https://www.speed-talk.com/forum/viewtopic.php?t=71561) (2026); [t=67524](https://www.speed-talk.com/forum/viewtopic.php?t=67524) (2023)
- *Dates / evidence:* as listed.
- *Who:* shops; not further stated.
- *Job and problem:* surface roughness measurement.
- *Workaround / products named:* Mitutoyo US$2,000 new, US$900 used (2012-12); used US$570 (2017-03).
- *Resolution:* served by used Mitutoyo.
- *Repeats and objections:* most shops "don't care about Ra" (2023). Register: no matching record, class 5.

**ST-50 · Valve-seat run-out gauges** — [t=62440](https://www.speed-talk.com/forum/viewtopic.php?t=62440) — sub-forum not stated
- *Dates / evidence:* 2020.
- *Who:* users; a one-man maker whose web domain was for sale.
- *Job and problem:* gauges for seat run-out.
- *Workaround / products named:* Goodson.
- *Resolution:* existing supply.
- *Repeats and objections:* source reads this as small supply and small demand. Register: RD-040, class 4.

**ST-51 · Torque-wrench checking, deck height, piston measuring centre** — mixed
- *Dates / evidence:* [t=33156](https://www.speed-talk.com/forum/viewtopic.php?t=33156) 2012; [t=71758](https://www.speed-talk.com/forum/viewtopic.php?t=71758) 2026; [t=71453](https://www.speed-talk.com/forum/viewtopic.php?t=71453) 2026 (QMP price dated 2026-01).
- *Who:* shops and builders.
- *Job and problem:* checking torque wrenches, deck height, piston dimensions.
- *Workaround / products named:* spring tester, beam wrench, tool truck; 12" dial caliper; QMP MC-1 ~US$3,000 (show price) to "$4000+ complete", "not yet ready to make" the investment.
- *Resolution:* existing methods adequate.
- *Repeats and objections:* investment hesitation only. Register: no matching record, class 5.

**ST-52 · Wideband sensors** — [t=55682](https://www.speed-talk.com/forum/viewtopic.php?t=55682) (partial; 2019, 13 authors); [t=66634](https://www.speed-talk.com/forum/viewtopic.php?t=66634)
- *Dates / evidence:* t=55682 2019, partial; t=66634 scaling on old dyno software (see ST-29). Titles [t=53594](https://www.speed-talk.com/forum/viewtopic.php?t=53594) (42 replies), [t=51265](https://www.speed-talk.com/forum/viewtopic.php?t=51265) (58), [t=50822](https://www.speed-talk.com/forum/viewtopic.php?t=50822) (88) not opened.
- *Who:* users running per-cylinder sensors.
- *Job and problem:* eight per-cylinder sensors dying each winter (condensation/rust, controller differences).
- *Workaround / products named:* none stated.
- *Resolution:* none stated.
- *Repeats and objections:* the long threads concern sensor placement and trust, not a missing instrument. Register: RD-082 / RD-084, class 5.

**ST-53 · Data loggers and EGT** — [t=45313](https://www.speed-talk.com/forum/viewtopic.php?t=45313) (2016); [t=48022](https://www.speed-talk.com/forum/viewtopic.php?t=48022) (2016); [t=48905](https://www.speed-talk.com/forum/viewtopic.php?t=48905) (2017)
- *Dates / evidence:* as listed; all partial reads.
- *Who:* hobbyists and builders.
- *Job and problem:* "affordable and 8 EGTs probably won't mix".
- *Workaround / products named:* AiM, AEM, Dataq, Innovate TC-4, ECU logging; Racepak default; hobby scope suggestions Rigol US$399 (2017-02), used Tektronix, Snap-on Modis.
- *Resolution:* answered with existing brands.
- *Repeats and objections:* adequate alternatives. Register: RD-025 / RD-019, class 5.

**ST-54 · Fuel-pressure gauges** — [t=64986](https://www.speed-talk.com/forum/viewtopic.php?t=64986) (Engine Tech, 2022-04-08/09, Australia); [t=14568](https://www.speed-talk.com/forum/viewtopic.php?t=14568) (2009); [t=50013](https://www.speed-talk.com/forum/viewtopic.php?t=50013) (2017)
- *Dates / evidence:* as listed.
- *Who:* carb and nitrous users; a machinist.
- *Job and problem:* liquid-filled gauge on the fuel log read ~2–3 psi different at ~5.5 psi until drained/vented; machinist "never" gets small gauges to read right.
- *Workaround / products named:* 2½" industrial gauge; cheap 4½" 0–15 psi gauge plus calibration; digital 0.1 psi with aerospace-grade sensors "expensive" (2009); AutoMeter/Speedhut electric trusted, cheap imports "crazy".
- *Resolution:* resolved by workaround in each thread.
- *Repeats and objections:* three threads. Register: RD-065 / RD-088 / RD-092, class 3 (weak).

**ST-55 · Crankcase vacuum** — [t=47544](https://www.speed-talk.com/forum/viewtopic.php?t=47544) (2016); [t=68698](https://www.speed-talk.com/forum/viewtopic.php?t=68698) (2024)
- *Dates / evidence:* as listed.
- *Who:* builders; not further stated.
- *Job and problem:* measuring pan pressure/vacuum; no instrument gap voiced.
- *Workaround / products named:* Bosch MAP sensor in the valve cover; advice to buy an accurate vacuum gauge; smoke machine ~US$550 (2024-06).
- *Resolution:* existing tools adequate.
- *Repeats and objections:* none. Register: RD-037 adjacent, class 5.

**ST-56 · Miscellaneous single-user items** — [t=71572](https://www.speed-talk.com/forum/viewtopic.php?t=71572) (Shop & Garage Tech, 2026-02); [t=65259](https://www.speed-talk.com/forum/viewtopic.php?t=65259) (2022)
- *Dates / evidence:* as listed.
- *Who:* single users.
- *Job and problem:* Moroso/Smokey Yunick small-block compression-ratio (clear cc) plate "unavailable everywhere… extinct"; an indexed-inner-ring degree wheel shown in a video is sold by no one (two users looked).
- *Workaround / products named:* the plate was found second-hand.
- *Resolution:* plate found second-hand; degree wheel none.
- *Repeats and objections:* single user each. Register: no matching record.

#### Products and prices named

Forum prices are the poster's figure at the date shown, not current prices. "Current" in the date column marks a web-search summary seen on 17 November 2026.

| Product | Price as stated | Date | Source type |
|---|---|---|---|
| Audie Technology Cam Pro Plus, base set-up | "around $4,700" | 2026-01-17 | forum post (t=71472) |
| US cam analysers landed in Europe | "around $3500" | 2020-03-03 | forum post (t=60307) |
| DIY Arduino/stepper cam analyser parts | ~US$800; ~US$600 | 2020-03; 2014-03 | forum post (t=60307; t=37958) |
| Performance Trends Cam Test Stand: complete / electronics-only / motorised retrofit | US$2,499 / US$1,799 / US$1,475 | undated price list | web-search summary, not directly read |
| Cam check as a service | US$25 per cylinder, US$100 for eight; US$50 | 2017-09 | forum post (t=51002) |
| Buxton Engineering Bench Pro spring tester | US$1,595 + US$189 PC firmware; "$1800" | 2020-02; 2019-06 | forum post (t=60160; t=57365) |
| Rimac spring tester (new) | "$1000.00"; A$1,200 (~2009) | 2026-02; 2019-06 | forum post (t=71535; t=57365) |
| Rimac 500 lb (used) | ~US$600 | 2020-02 | forum post (t=60160) |
| Intercomp spring tester | "over $1,000"; used US$700; US$895 | 2020-02; 2020-03; current | forum post (t=60160, t=60123); US$895 web-search summary, not directly read |
| Goodson bench spring testers | "from $899.00 on up" | 2017-12 | forum post (t=51845) |
| Proform 66776 1,000 lb digital bench tester | ~US$621–684 | current | web-search summary, not directly read |
| Proform 66842 digital mini (0–1,000 lb) | ~US$602 | current | web-search summary, not directly read |
| LSM bench-top tester | ~US$500 (NZ retailer NZ$1,343 + GST for 1,000 lb) | current | web-search summary, not directly read |
| Comp Cams mini tester; generic mini | ~US$248; "less than $100" | current; 2024-07 | web-search summary, not directly read; forum post (t=68722) |
| Roehrig lab spring tester | "around $12,000" | 2010-03 | forum post (t=21020) |
| Calibration springs: Larson / Rimac-branded / Comp | US$182 / ~US$75 / ~US$35 | 2020-05 / 2025-03 / 2016-07 | forum post (t=61214, t=45929, t=47010) |
| SuperFlow 901 to 902 electronics upgrade | US$22,500; other quotes US$15–23k | 2018-04 | forum post (t=52878) |
| DTS to WinDyn upgrade | "28k and 4 months lead time" | 2015-08 | forum post (t=44205) |
| Land & Sea 901 retrofit | US$7,500 (verbal, show); ~US$9k as optioned | 2018-04 | forum post (t=52878) |
| YourDyno SuperFlow water-brake kit (901/902) | from US$5,295 ex tax | current | web-search summary, not directly read |
| Balancer digital retrofits: Turner / T&S / new machine | ~US$5,000 + PC / US$7,500–10,000 / ~US$20k | 2016-04 | forum post (t=46365) |
| Mitutoyo surface tester | US$2,000 new; US$900, US$570 used | 2012-12; 2017-03 | forum post (t=33856, t=49419) |
| QMP Racing MC-1 piston measuring centre | ~US$3,000 (show) to "$4000+ complete" | 2026-01 | forum post (t=71453) |
| Ultrasonic thickness testers (imports) | US$75–200 | 2022-03 | forum post (t=64850) |
| Dwyer rotameter as blow-by meter | ~US$70 | 2009-03 | forum post (t=15556) |
| MSD timing light | "$200+" | 2016-05 | forum post (t=46619) |
| Rigol DS1054Z scope | US$399 | 2017-02 | forum post (t=48905) |
| Smoke leak tester (discount tool chain) | ~US$550 | 2024-06 | forum post (t=68698) |
| Sun EDT-5001 distributor tester (military purchase) | ~US$8,000 each | reported 2013 | forum post (t=36464) |

Other brands named without prices: Andrews EZCam, MJP (Denmark), Sportdevices, Adcole; Performance Trends (spring tester, DataMite, blow-by sensor, flow-bench electronics); Audie Flow Quik/FlowPro, PTS, C&D "Blue Box", FP1; DEPAC, DTS, Stuska/Power Test, DynoHelp; Turner Technology, T&S, ProBal, G&H; J&S SafeGuard, MSD Knock Alert; Innovate (LM-2, LMA-3, ST-12, LC-2, TC-4), AEM, 14point7, AiM, Racepak, Dataq; Computech EGT probes; J-Tec; Mityvac MV5532, Lang, OTC, Snap-on; Dakota/Phase II sonic testers; Paramount (distributor-machine parts); Dragy; LSM; Tavia; Larson Systems; Crane/PAC/Goodson calibration springs.

Brands found absent from the existing competitor lists: Audie, Buxton, Rimac, LSM, SuperFlow, YourDyno, DEPAC, Land & Sea, J&S, Turner, Andrews, MJP, Paramount, Mityvac, Goodson.

#### Low-yield searches and sections

- Searches returning zero hits or noise: "arduino" in titles (0; 14 content posts, three of them cam-measuring threads), "transducer", "encoder", "load cell" (0 in titles, because of the search gap), "torque wrench calibration" (0), "wideband accuracy" (0), "overpriced gauge" (0), "pressure transducer arduino" (0), "discontinued tester" (1 irrelevant), "obsolete software" (10, one relevant), "bleed down tester" (1 irrelevant), "ring tension gauge" (4 irrelevant), "digital degree wheel" (2).
- Phrase-style searches were noisy: "wish someone made" (187 hits, none relevant on the first page), "nobody makes" (137, parts not instruments), "discontinued" first-post (30, parts not instruments); "windows 98" and "serial port" matched on stop-words and yielded only t=72099, t=71891 and t=68996. "det cans" and "knock headphones" found no tool discussion. "oil pump test", "fuel flow meter" and "weather station" (8 hits, none about an instrument gap) gave broad noise. "DIY" and "EGT" were rejected by the stop list.
- Well-served areas (section 2F): flow-bench electronics, leak-down/compression, blow-by, rod-bolt stretch, sonic testers, profilometers, data loggers, wideband controllers, torque-wrench checking, deck-height/piston measuring.
- Not found at all: complaints about lifter bleed-down testers, pushrod-deflection tools, ring-tension gauges, oil-pump test stands, regulator/fuel-pump flow benches, injector flow benches (nothing bearing on RD-008), cooling-system flow tools, carb float-level or jet-measuring tools (nothing bearing on RD-039), torsion-bar or shock-dyno electronics (off-topic here).
- In-cylinder pressure: threads are vendor tutorials or OEM/professional lab descriptions (t=63167, t=68333); no price complaint or DIY attempt read.
- Vendor Marketplace (f=43), Driveline, Chassis and Electric not reviewed; HotPass inaccessible.

#### Unknowns

- Volume: forum posts show a problem recurs, not how many units would sell; no thread gives installed-base numbers for SF-901, DTS or DEPAC dynos, Rimac testers or distributor machines.
- Current prices and availability of Audie Cam Pro Plus, Buxton Bench Pro, the Performance Trends spring tester, MJP software, Turner/T&S retrofits and J&S SafeGuard are not validated (search budget exhausted; two searches returned nothing).
- Whether Proform digital testers, or import digital load-cell testers, already satisfy the cheap-but-trustworthy spring-tester need is unknown; only one owner post (untested unit, 2021).
- DEPAC and Spintron support status in 2026 not independently checked; forum evidence ends with referrals to third parties.
- Attachments were unseen, so build complexity of home-built testers, cam stands, LED distributor conversions and SF-901 cable/board photos is inferred from text only.
- The 2009–2019 search gap was covered by titles, not content; complaint phrases inside threads of that decade were found only when the title suggested them.
- Australian relevance: Australians appear in many threads (spring testers, SF-901, DEPAC, distributor machines, fuel gauges), but numbers are anecdotal.
- Many advisers are vendors or professionals with products or services to sell (cam designers, head porters, software sellers, dyno-service firms); their commercial interest in specific brands is not always visible.

## 4. Candidate validations

Four forum findings were each given an independent validation, briefed to refute the idea if the facts allowed. Each subsection gives the validator's verdict, current competitor sources and prices, cost inputs with their basis, and kill criteria. A fifth subsection gives the coordinator's own checks for the torsion-bar candidate, which was not independently validated. Web prices are search-result summaries seen on 17 November 2026 unless a row says otherwise.

### V1 — Stand-alone configurable engine-protection warning module

**Validator's verdict:** Do not advance. The need is real (drivers miss gauges; stock switches trip too low), but the minimum job is already done by US$16–63 switch-and-lamp kits, and the "configurable plus recall" tier is occupied by US$125–330 gauges that include the sender and a live reading. The validator estimates a complete SkidLabz kit at A$190–350 (generic senders) or A$300–500 (branded senders at retail) before development recovery, so it cannot undercut either tier. No recorded register blocker is addressed; the evidence is "more people mentioned it" (search summaries of US, DIY-heavy threads, mostly 2012–2021), not an owner-selected requirement.

**What the customer actually needs:** The strongest, repeated ask is a light that trips at a sensible oil pressure (not 2–7 psi) and cannot be missed, with the same for high coolant or oil temperature. Adjustable thresholds were asked for by a few posters; peak/minimum recall by one; RPM-scaled pressure thresholds by two (one of whom wanted their stand-alone ECU to do it). The smallest product that does the job is a pressure switch (about 20–30 psi, or adjustable) and a temperature switch, each driving a very bright lamp, which is a parts kit rather than an electronic module. The validator's inference for the smallest candidate that adds anything: 1 pressure plus 1 temperature input with supplied senders, button-set thresholds, start-up inhibit and filter, one lamp output and one buzzer/relay output, and a non-volatile record of the channel tripped, worst value and time beyond threshold. The kart, speedway-forum and engine-builder notes did not corroborate the need (a karter low-voltage warning request was answered by a US$10 voltmeter), so the speedway/dirt-oval buyer is not evidenced.

**Competing products and prices**

Evidence type for every web row is a search-result summary, not a directly read page (retail pages could not be opened). Listing dates are mostly unknown, and prices may be stale or sale prices.

| Product | What it does | Price as found | Date seen | Source | Evidence type |
|---|---|---|---|---|---|
| Longacre Gagelite oil-pressure kit 52-40000 | Fixed 20 psi switch, red light, wire; complete | US$33.99–37.99 (UK £39.16 at Merlin; an older 2024-dated forum figure was US$25.99) | 2026-11-17 | [90racing](https://90racing.com/products/longacre-gagelites-oil-pressure-warning-light-kit-40000), [Keyser](https://keysermanufacturing.com/?p=2540), [GGC](https://ggcracing.com/products/longacre-gagelite-kit-o-p-1-8in-npt-20psi) | Search-result summary |
| Longacre Gagelite adjustable kit 52-40100 | Sender adjustable 15–50 psi plus light, tee, wiring | US$55.99–62.99 | 2026-11-17 | [OG Racing](https://www.ogracing.com/products/longacre-oil-pressure-warning-light-kit-15-50-psi), [Drift HQ](https://drifthq.com/products/long-acre-racing-oil-pressure-warning-light-kit-15-50-psi-adjustable-40100) | Search-result summary |
| Longacre water-pressure warning kit | Low coolant-pressure switch plus light | US$43.99–45.99 (3 psi switch alone US$27.99 at Pegasus) | 2026-11-17 | [OG Racing](https://www.ogracing.com/products/longacre-water-pressure-warning-light-kit), [Pegasus](https://www.pegasusautoracing.com/productdetails.asp?RecID=9749) | Search-result summary |
| Longacre sprint-car battery-pack kits 52-45620 / 52-45624 | 20 psi switch, light, 9 V battery holder for cars without a 12 V system | US$51.99–53.95 / US$59.99; NZ$110 + GST at Fast Lane Spares; AUD price not shown at Speedway Spares | 2026-11-17 | [90racing](https://90racing.com/products/longacre-sprint-car-battery-pack-kit-52-45620), [Speedway Spares](https://speedwayspares.com.au/products/longacre-oil-pressure-warning-light-battery-pack-kit) | Search-result summary |
| QuickCar Quick-Light kits 61-711 (oil pressure) / 61-712 (water temperature 235 °F) | Pre-set switch plus light | US$30.59 / US$15.99 | 2026-11-17 | [61-711](https://appletreeauto.com/VW-OIL-SYSTEMS/temperature-safety-switch/quick-light-oil-pressure-kit-61-711), [61-712](https://www.appletreeauto.com/quick-light-water-temperature-kit-61-712) | Search-result summary |
| QuickCar sprint oil-pressure kits 61-717 / deluxe 61-718 | Light, switch, tee, 9 V battery; speedway-specific | US$54.95–59.99 / US$73.67–79.95 | 2026-11-17 | [61-717](https://appletreeauto.com/sprint-oil-pressure-warning-light-kit-61-717), [deluxe](https://ggcracing.com/products/oil-pressure-warning-kit-deluxe) | Search-result summary |
| Longacre Gagelites water-temperature kit, 230 °F | Temperature switch plus light; the only Australian shelf price found for a complete kit | A$39.78 | 2026-11-17 | [Speedway Spares](https://www.speedwayspares.com.au/products/longacre-gagelites-warning-light-kit-230%C2%BA-water-temp-3-8-npt) | Search-result summary |
| AutoMeter Pro-Lite 3239 lamp + 3241 switch | "Extremely bright" lamp plus 15-on/18-off psi switch | US$62.17 + US$34.93–46.50 (pair about US$97–109) | 2026-11-17 | [lamp](https://autometer.com/mini-pro-lite-warning-lite-black.html), [switch](https://autometer.com/pressure-switch-15-psi.html) | Search-result summary |
| GlowShift Elite 10-colour oil pressure | Peak recall, user-programmable high/low warnings | US$143.85 | 2026-11-17 | [MA Performance](https://www.maperformance.com/products/glowshift-elite-10-color-oil-pressure-gauge) | Search-result summary |
| ProSport Premium EVO oil pressure with sender | Peak recall plus programmable warning | US$122.54–167.50 (NZ$159.10 + GST at Fast Lane Spares) | 2026-11-17 | [Rally Sport Direct](https://www.rallysportdirect.com/products/216evoop-pk-r-psi-prosport-premium-evo-digital-oil-pressure-gauge-w-sender), [American Muscle](https://www.americanmuscle.com/prosport-camaro-oil-pressure-gauge-238evoop-pk-psi.html) | Search-result summary |
| Longacre SMi Elite waterproof oil pressure 52-46741 | Sender included; warning stages set on the gauge (LED, flashing, backlight flash); speedway-oriented | US$169.99–209.99 | 2026-11-17 | [OG Racing](https://www.ogracing.com/products/longacre-smi-elite-waterproof-oil-pressure-gauge-0-120-psi), [90racing](https://90racing.com/products/longacre-oil-pressure-gauge-52-46741) | Search-result summary |
| Innovate MTX-D 3913 | Oil pressure plus oil temperature, both sensors in kit, warnings set on the gauge; remote output not confirmed | US$190.52–271 street (MSRP US$245.98); C$330 at a Canadian seller | 2026-11-17 | [Fidanza](https://fidanza.com/innovate-mtx-digital-oil-temperature-pressure-gauge-kit-0-150psi-3913), [CSP Racing](https://www.cspracing.com/innovate-3913-mtx-digital-oil-temperature-pressure-gauge-kit-0-150psi/inv-3913) | Search-result summary |
| **SPA Design / Racetech DG200** (dual oil pressure + water temperature; DG208 oil pressure/volts) | Closest existing match to the whole candidate: sold with sensors and harness; alarm thresholds set on the unit for both channels; peak recall of maximum values; programmable outputs for an external LED or relay | DG200-B £202.25 ex VAT (£242.70 inc.) on one Rallynuts page, "from £134.47" on another (conflict, possibly with/without sensors, unresolved); DG208 £178.75 at Merlin | 2026-11-17 | [Rallynuts](https://www.rallynuts.com/racetech/DG200-B.html), [Rallynuts 2](https://rallynuts.com/gauges/DG200-B.html), [Merlin DG208](https://merlinmotorsport.co.uk/p/badekurort-oeldruck-volt-lehren-spa-dg208) | Search-result summary; no maker spec sheet seen |
| AutoMeter Spek-Pro oil pressure 0–120 psi | Sender and harness; peak recall; warn point on the gauge; Pro-Control output switches a 1.5 A load | US$240.33–326.86 (one retailer notes a 2–3 month special-order wait) | 2026-11-17 | [AutoMeter](https://www.autometer.com/2-1-16-oil-pressure-0-120-psi-spek-pro-black-black-6473.html), [Speedway Motors](https://www.speedwaymotors.com/AutoMeter-P32552-Spek-Pro-Oil-Press-Gauge-2-1-16-0-120-PSI-Domed,308557.html) | Search-result summary |
| Stack Pro-Control ST3501 / ST3502 | Peak "tell-tale" memory plus configurable output | US$259.95 (sold out) / US$337–387 | 2026-11-17 | [ST3501](https://frsport.com/products/stack-st3501-oil-press-pro-control-52mm-blk-0-7-bar-m10-male), [ST3502](https://frsport.com/products/autometer-st3502-gauge-oil-press-pro-control-52mm-blk-0-100psi-1-8-nptf-male) | Search-result summary |
| Scintex fuel/oil pressure gauge + sensor (Australian) | Digital controller with set points triggering an internal relay | A$299.00 (currency assumed) | 2026-11-17 | [Scintex](https://www.scintex.com.au/collections/all/products/oil-fuel-pressure-gauge) | Search-result summary |
| Engine Watchdog TM2 / TM4 (Australian) | Bolt-on temperature alarm; a retailer document says the TM4 also alarms on low oil pressure | No list price found; owner reports about A$149–189 (TM4), TM2 A$110 delivered (old) | 2026-11-17 (forum recollections 2009–2025) | [Vehikool document](https://s0.yellowpages.com.au/d1072046-3f46-4350-aabf-e4ede258cb19/vehikool-automotive-port-adelaide-5015-document.pdf), [AULRO](https://www.aulro.com/afvb/archive/index.php/t-177774.html) | Search-result summary; a 2025 forum post says "only does temp", so sources conflict |
| Muirhead / RCT light-vehicle engine warning kits (Australian) | Oil pressure, coolant temperature and coolant level; audible and visual alarm; optional idle-down or shutdown | Quote only; no price published | 2026-11-17 | [RCT datasheet](https://rct-global.com/datasheet/light-vehicle-engine-warning-kits/), [RCT part](https://rct-global.com/part/engine-protection-system-12-24v-energised-to-run-to-suit-light-vehicles) | Search-result summary; adjustability not stated |
| Engine Guard EG01-1 / EG01-2 | Digital temperature gauge, bolt-on sensor, adjustable audible alarm | £89.99 / £109.99 (AUD price not captured) | 2026-11-17 | [engineguard.eu.com](https://engineguard.eu.com), [Patrol Apart](https://patrolapart.com.au/product/engine-guard-single-temperature-sensor-kit) | Search-result summary; the name is close to the dropped RD-032 "EngineGuard" |
| CANchecked MFD15 Gen2 (52 mm) | 6 analogue inputs, stand-alone, preset alarms; display unit | US$309.99–341.03 (EUR 309.65–329 with OBD cable), plus senders | 2026-11-17 | [Uro Tuning](https://www.urotuning.com/products/canchecked-mfd15-multi-function-universal-display-1-5-gen2), [Bimmerworld](https://bimmerworld.com/Gauges-Data-Acquisition/Data-Acquisition-Systems/CANchecked-MFD15-52mm-Round-Display-Analog-CAN.html) | Search-result summary; whether thresholds can be set without a PC is unresolved |
| AiM MXm / MXS dashes | Logging dashes with alarm LEDs | MXm US$1,299–1,449; MXS US$1,299–1,499 (Light £875) | 2026-11-17 | [MXm](https://dfusermotorsports.com/products/aim-sports-mxm-compact-dash-logger), [MXS](https://competitionmotorsport.com/products/aim-sports-mxs-1-2-strada-compact-color-tft-dash) | Search-result summary |

Other items seen with no price captured: Longacre fuel-pressure and oil-temperature kits, Moroso 49500, Allstar ALL80250, QuickCar 61-751, PLEX µSDM (three searches, no price), GaugePilot. A Pegasus 20 psi switch (US$29.99) and Autosport Labs AnalogX (US$149.95) were carried from earlier forum notes (no URL recorded; not re-checked).

**Does a cheap satisfactory alternative already exist?** Yes. For the core job a complete switch-and-lamp kit costs US$31–38 (fixed 20 psi), US$56–63 (adjustable) or about US$16 (water temperature), with 9 V battery versions at US$52–80 for cars with no electrical system. For "configurable and tells me the peak afterwards" gauges cost US$123–250 per channel with the sender included. The SPA/Racetech DG200 (about £134–202 ex VAT for two channels with sensors) and AutoMeter Spek-Pro already offer an external lamp or relay output, so the candidate's whole function set is on sale with a live reading the candidate would not have. Only a display-less box is unoccupied, which is a reduction, not an advantage; absence in 46 searches is not proof of absence.

**Why prices are what they are / where a saving could come from:** Switch kits contain no electronics and are volume catalogue items, so a microcontroller product cannot be cheaper than a snap-action switch and a pilot lamp. Programmable gauges bundle a sender, display, housing, harness, warranty and two margins. A blind module saves only the display and movement (perhaps US$15–30), while senders, lamp, harness and owner labour at A$150/h dominate; there is no evident cost advantage.

**Cost inputs (about 25 units, with basis)**

| Item | Figure | Basis label | Source / part number |
|---|---|---|---|
| MCU STM32G030F6P6TR | US$1.0927 @30 (US$0.9633 @100) | Current supplier price (JLCPCB/LCSC, 2026-11-17, ex freight/GST/assembly) | C529330 |
| 5 V automotive LDO TPS7B6950QDBVRQ1 | US$0.8584 @30 | Current supplier price | C132202 |
| Load-dump TVS SM8S24A | US$0.8339 @30 | Current supplier price | C314439 |
| Reverse-polarity P-FET DMP6023LE-13 | US$0.6963 @30 | Current supplier price | C154901 |
| Lamp driver BTS5090-1EJA | US$0.7651 @30 | Current supplier price | C534811 |
| Low-side driver ZXMS6004FFTA | US$0.4391 @30 | Current supplier price | C95063 |
| Quad op-amp MCP6004T-I/SL | US$0.3342 @30 | Current supplier price | C7378 |
| Setup OLED 0.96" HS96L03W2C03 | US$1.7398 @30 (not sunlight-readable) | Current supplier price | C5248080 |
| Passives, test points | US$1.50–2.50 | Engineering estimate | — |
| Electronic parts subtotal | about US$9.5 per board at 25–30 (US$8.2 at 100) | Current supplier price plus engineering estimate | lamp LED excluded |
| Bare board, SMT assembly, extended-part fees | US$6–9 at 25 (US$3–5 at 100) | Engineering estimate; not quoted today (unresolved) | — |
| Assembled, untested control board | US$16–19 (A$23–28) at 25; US$12–14 at 100 | Current supplier price plus engineering estimate | — |
| DT 4-way connector pair with contacts and wedges | about US$6.0 | Current supplier price (sum); some lines have 0–25 in stock | DT04-4P C139530, DT06-4S-P012 C415745 |
| Lowdoller 0–150 psi pressure sender | US$40.99 (another listing US$69.99) | Published retail price (search-result summary) | [DIY Autotune](https://diyautotune.com/products/ldm-150-psi-pressure-sensor) |
| AEM 100 psig brass sender kit 30-2131-100 | US$78.44–113.33 | Published retail price (search-result summary) | [USP Motorsports](https://www.uspmotorsports.com/product/aem-100-psig-brass-sensor-kit-75771183) |
| Honeywell MIP 100 psi industrial sender | US$69.61 (qty 1) | Published distributor price (search-result summary) | [DigiKey](https://azcus.digikey.com/en/products/detail/honeywell-sensing-and-productivity-solutions/MIPAN2XX100PSAAX/10671077) |
| AEM 30-2012 temperature sender kit | US$47.77–66.99 (one Australian listing A$254.95, outlier) | Published retail price (search-result summary) | [Fidanza](https://fidanza.com/aem-universal-1-8in-ptf-water-coolant-oil-temperature-sensor-kit-30-2012) |
| Generic stainless pressure sender | US$10–20; no price obtained | Unresolved assumption / engineering estimate; listings disagree on range and quality | no price URL recorded |
| Generic NTC temperature sender | US$5–12; no price obtained | Unresolved assumption / engineering estimate | no URL recorded |
| Own-build bright lamp / enclosure / harness / packaging | US$4–15 / US$5–12 / US$12–20 / US$2–4 | Engineering estimate (enclosure unresolved) | — |
| Kit roll-up A, generic senders | US$54–102 (A$78–148) at 25; about A$65–128 at 100 | Engineering estimate | — |
| Kit roll-up B, branded senders at retail (trade price unresolved) | US$128–207 (A$186–300) at 25; about A$167–276 at 100 | Engineering estimate | — |
| Per-kit labour | 35–60 min (A$88–150); 20–30 min with outsourced harness | Engineering estimate | — |
| Support per unit sold | 10–20 min (A$25–50) | Engineering estimate | — |
| Cost before development recovery | A$191–348 (A) or A$299–500 (B) | Engineering estimate | — |
| One-time owner hours | 210–440 h (A$31,500–66,000 at A$150/h): electronics 40–80, firmware 60–120, enclosure/lamp/harness 30–80, documentation 20–40, validation 60–120 | Engineering estimate | — |
| One-time cash costs | A$3,000–14,000: references/jig A$400–1,400, prototypes and samples A$1,000–2,500, EMC pre-compliance A$1,500–8,000 | Engineering estimate; EMC figure unresolved (no quote) | — |
| Break-even | 185–390 kits at A$170 margin; 450–940 at A$70 | Engineering estimate | — |

At US$149 (about A$216) the kit loses money in almost every case; at US$249 (about A$361) scenario A leaves A$13–170 per kit. Working rate A$1 ≈ US$0.69.

**What must be demonstrated before claiming equivalent useful performance:**
- Sender accuracy at the trip point (about ±2–3 psi at 15–40 psi, ±2–3 °C at 100–130 °C), including after heat cycling and a teardown of low-cost senders.
- Vibration and leak survival of engine-mounted senders, the strongest fear in the forum evidence.
- False-alarm behaviour at legitimately low hot idle, cranking, kill-switch and brown-out; fixing it properly implies RPM gating and per-engine setup.
- Catching a 0.3–0.5 s pressure dip without tripping on noise, and recording minimum and duration.
- Daylight visibility compared side by side with a Longacre Gagelite and AutoMeter Pro-Lite.
- Electrical robustness beside magneto/CDI ignitions, load dump, reverse polarity and shorted outputs; battery operation if speedway is claimed.
- Latched recall surviving immediate power loss; setup without a laptop; fitment across thread types; claim wording as a "warning indicator" only.

**Register relationship:** RD-032 (EngineGuard / general engine-protection monitor) is dropped on an owner scope decision, and the specific reason was not recovered; the reopening condition (a clearly differentiated revised scope selected by the owner) is not met. RD-089 (stand-alone warning module) and RD-090 (compact direct-input monitor with warning/recall, PLEX-inspired) are unadopted assistant suggestions; their condition (a concrete user-selected requirement and evidence of a worthwhile advantage) is not met. DEC-019 (Knock Meter boundary against engine-protection promises) is not addressed and the "engine-protection" framing runs against it. RD-001 RevMax must not absorb it; RD-096/RD-097 (matching instruments, waterproof panel) are occupied by Longacre SMi Elite; RD-015/DEC-044 (dash display sourcing) returns as a blocker once a live reading is wanted. No recorded rejection reason or blocker is addressed.

**Red-team: reasons to reject, cheapest validation step, kill criteria:**
- Squeezed from both sides: US$16–63 kits below, US$123–250 gauges above, with at least one already offering the external lamp/relay output.
- Sender-, plumbing- and support-limited, with liability exposure from an "engine protection" claim (DEC-019, RD-032).
- Demand not evidenced where SkidLabz sells, and A$32k–66k of design time needs roughly 185–940 kits against 20–25-unit batches.
- Cheapest step (about an hour, no hardware): ask the owner whether the RD-032 reason covers this narrower scope, then show at least 10 prospective buyers the Longacre adjustable kit (about US$60), a dual alarm gauge with senders (Innovate MTX-D about US$190–246 or DG200 about £134–202 ex VAT) and the module at a cost-covering price (about A$349 / US$240).
- Kill if: the owner confirms the RD-032 reason applies; fewer than about 8 of 20 qualified prospects (or 10 firm pre-orders) choose the module at A$349 or more; no prospect names a need the US$60 kit or US$125–250 alarm gauge fails to meet; or kit cost cannot be brought under about half the accepted price (already failed on current estimates unless senders are omitted).

**Lookups not performed / unknowns:**
- No retail or manufacturer page was opened; every web price is a search-result summary, and no forum thread was re-read.
- Not found or not captured: PLEX µSDM and GaugePilot prices; Moroso, Allstar, QuickCar 61-751 prices; Koso; Accusump switches; an AUD price for an oil-pressure kit.
- Engine Watchdog TM4 current price and whether its oil-pressure alarm is adjustable; Muirhead/RCT price; DG200 price conflict, latching and minimum recall; MTX-D lamp output; CANchecked threshold setting.
- Generic sender, enclosure and sealed button prices; trade prices; JLCPCB board/assembly/freight fees.
- Australian EMC obligations (unresolved; US position from memory of 47 CFR 15.103(a), not re-read) and consumer-law liability.
- Freight Australia to US and US tax/duty not researched. Search coverage was 46 US-biased searches; the DG200 surfaced only on the third SPA-related query, so a niche match could have been missed.

### V2 — Low-pressure tyre-gauge checker / reference station, and evidence for the existing tyre-gauge investigation (RD-003)

**Validator's verdict:** The trust problem is real but the product request is not. Racers on both forums say they cannot tell which gauge is right, yet nobody across KartPulse's five gauge threads (32 distinct posters, read directly) or GRM's eight or more (search-index summaries only) asks for a checker, master gauge or calibration service. As a SkidLabz product the checker should be rejected or not opened: adequate substitutes exist, and the value lies in calibration labour and authority, which a small unaccredited maker is poorly placed to sell. It is worth building only as an internal fixture for RD-003 validation. The forum evidence adds user-language requirements for RD-003 and supports DEC-013, but addresses none of DEC-011, DEC-012 or DEC-040. Status stays unchanged. All findings are the validator's, dated 2026-11-17.

**What the customer actually needs:** Individual owner-drivers (the people who posted) are unlikely buyers, because their gauges cost US$27–180 and "$300? Hard pass" was said on KartPulse. Plausible buyers are institutions: teams with several gauges in one tent, kart shops, tyre vendors, clubs or tracks. That is tens of units per country (Karting Australia's 2023 "About" document gives 64 affiliated clubs, per a search summary). To report a 0.1 psi offset with confidence the checker needs about ±0.05 psi (±0.35 kPa) expanded uncertainty over pit temperatures, roughly 0.17 % of 30 psi (validator's estimate, using the usual 4:1 convention). That suffices for 0.5 %-class and analogue gauges, gives about 2:1 against a "±0.1 psi" gauge, and cannot judge the Prisma or Intercomp 0.1 % claims, which racers already use as their benchmark.

**Existing gauges, references, checkers and services**

All rows were seen on 2026-11-17. Every row is a search-result summary, not a directly read page. Retail page dates are unknown and prices may be stale; several listings were out of stock. "No URL recorded" means the notes give none.

| Product or service | What it does / accuracy claim | Price as found | Date seen | Source | Evidence type |
|---|---|---|---|---|---|
| Longacre Basic Digital 0–60 psi (52-53006) | Entry digital, 0.2 psi steps; 0.8 % (2021 catalogue) | US$54.99 (one retailer), about US$59 (another), US$44.99 in 2021 catalogue | 2026-11-17 | [discoveryparts](https://discoveryparts.com/products/longacre-basic-digital-2-0-tire-gauge-0-60-psi-53006); [tirehardware](https://tirehardware.com/product-tag/tire-pressure-tool) | Search-result summary, not directly read page |
| Longacre Semi-Pro Digital 0–60 psi (52-53003) | 0.1 psi, bleed, auto-off; 0.5 % (2021 catalogue) | US$86.96–111.99; US$99.99 in 2021 catalogue | 2026-11-17 | [ogracing](https://www.ogracing.com/products/longacre-semi-pro-digital-tire-gauge-0-60-psi); [fastracer](https://fastracer.com/products/longacre-semi-pro-digital-tire-pressure-gauge) | Search-result summary, not directly read page |
| Longacre Pro Digital 0–25 psi and 0–60 psi (52-53000) | Back-lit, 0.1 psi; "higher accuracy" (no figure) | 0–25: US$126–158; 0–60: US$158.99–179.99; US$149.99 in 2021 catalogue | 2026-11-17 | [0–25](https://www.ogracing.com/products/longacre-pro-digital-tire-gauge-0-25-psi); [0–60](https://www.ogracing.com/products/longacre-pro-digital-tire-gauge-0-60-psi) | Search-result summary, not directly read page |
| Longacre analogue Deluxe 2.5" 0–15, Magnum 3.5" 0–15, Magnum 0–60 | Dial gauges; accuracy not stated (a GRM poster said "within 1/2 psi or so") | US$69.99 / 109.99 / 84.99 | 2026-11-17 | [Deluxe](https://www.ogracing.com/products/longacre-deluxe-tire-gauge-0-15-psi); [Magnum 0–15](https://www.ogracing.com/longacre-magnum-tire-gauge-0-15-psi); [Magnum 0–60](https://fastracer.com/products/longacre-magnum-3-1-2-analog-tire-pressure-gauge) | Search-result summary, not directly read page |
| Longacre 2" 0–15 psi analogue, Australia | Dial gauge | A$109 | 2026-11-17 | [Revolution Racegear](https://www.revolutionracegear.com.au/product/longacre-0-15-psi-tyre-gauge/) | Search-result summary, not directly read page |
| Longacre 2.5" 0–60 analogue, Australia | Dial gauge | A$124.99 (Racer Industries); Deluxe 2.5" 0–60 A$219 (Revolution Racegear) | 2026-11-17 | [Racer Industries](https://www.racerindustries.com.au/longacre-tyre-guage-0-60psi-2.5inch); [Revolution Racegear](https://www.revolutionracegear.com.au/product/l-acre-deluxe-2-5-0-60-tyre-gauge/) | Search-result summary, not directly read page |
| Longacre Semi-Pro digital 0–60, Australia | 0.1 psi, 0.5 % | A$365.00 (13 in stock; listing about 566 days old per the search tool), about 2.3–2.9 times the US price at A$1 = US$0.69 | 2026-11-17 | [Revolution Racegear](https://revolutionracegear.com.au/product/l-acre-semi-pro-digital-0-60-psi-tyre-gauge/) | Search-result summary, not directly read page |
| Longacre Pro Precision 4½" analogue; Basic 2" analogue | ½ % claimed (Pro Precision) | US$204.99; US$28.99 (maker's own store) | 2026-11-17 | [Pro Precision](https://longacreracing.com/products/pro-precision-4inch-tire-gauge); [Basic 2"](https://longacreracing.com/products/basic-2inch-tire-gauge) | Search-result summary, not directly read page |
| Racer Industries liquid-filled 2.5" 0–60 (Longacre brand page), Australia | Dial gauge | A$149.00 | 2026-11-17 | [Racer Industries](https://www.racerindustries.com.au/longacre-2.5-inch-liquid-filled-tyre-gauge-0-60psi) | Search-result summary, not directly read page |
| Intercomp digital air gauge 360045 (superseded by 360049) | Premium digital; 0.1 % "certified" (maker advert) versus 0.5 % (two retailers) — conflict; resolution 0.01 or 0.1 psi (sources conflict) | US$395.95–399.99; 360049 US$379.99 (Tire Rack) | 2026-11-17 | [discoveryparts](https://discoveryparts.com/products/intercomp-racing-digital-air-pressure-gauge-intercomp-360045); [Tire Rack](https://www.tirerack.com/accessories/intercomp-ic360049-air-gauge) | Search-result summary, not directly read page |
| Intercomp 4" Deluxe analogue 360060 | Dial; factory match traceable to NIST, recalibration service | US$74–79 | 2026-11-17 | [Tire Rack](https://www.tirerack.com/accessories/detail.jsp?ID=166) | Search-result summary, not directly read page |
| Intercomp digital 0–100 psi, Australia | Premium digital | A$606.90 (sold out) | 2026-11-17 | [Speedway Spares](https://www.speedwayspares.com.au/products/intercomp-digital-tire-gauge-0-100psi) | Search-result summary, not directly read page |
| Intercomp 360045 / 360049, New Zealand | Premium digital | NZ$833.90 + GST / NZ$1,043.50 | 2026-11-17 | [Fastlane Spares](https://fastlanespares.co.nz/collections/tools-shop-equipment/products/intercomp-digital-tyre-pressure-gauge-with-angle-chuck) | Search-result summary, not directly read page |
| Joes Racing analogue 0–15 psi (32305); Pro 0–15 with hold valve | Dial gauges; accuracy not stated | US$26.95; US$33.98–38.95 | 2026-11-17 | [JEGS](https://www.jegs.com/i/joes-racing-products-514-32305-tire-pressure-gauge-0-15-psi) | Search-result summary, not directly read page |
| Joes Racing digital 0–60 | Digital; accuracy not stated | US$73.95 (sale) | 2026-11-17 | [ogracing](https://www.ogracing.com/products/joes-racing-products-digital-tire-pressure-gauge-0-60-psi) | Search-result summary, not directly read page |
| QuickCar digital (Economy; a 0–60 with 0.01 psi resolution) | Digital; accuracy not stated | Economy US$66.95; 0–60 price not found | 2026-11-17 | [tirehardware](https://tirehardware.com/product-category/tools/tire-gauges/page/2) | Search-result summary, not directly read page |
| Moroso digital 0–15 psi (89540), Australia | Low-range digital; 2 % claimed for Moroso gauges generally | A$452.00 | 2026-11-17 | [Enginemaster](https://www.enginemaster.com.au/products/moroso-mo89540-digital-tyre-pressure-gauge-0-15psi-2-5-8-diameter) | Search-result summary, not directly read page |
| Prisma HiPreMa 4 (0–5 bar / 72 psi) | Kart digital with memory; "<0.1 %", IP55 | £183.51 (KKC, sold out); £220.21 / £229.43 with stopwatch (Demon Tweeks via compare.parts); US$302 (Kart Kings, sold out); US$324.95 with stopwatch; HiPreMa 4X US$253 | 2026-11-17 | [KKC](https://kkckartshop.co.uk/products/go-kart-prisma-digital-hpm4-tyre-pressure-gauge-0-5-bar72-psi-racing); [reach.dog](https://reach.dog/shop/rev-performance-materials/products/prisma-tire-gauge-stopwatch) | Search-result summary, not directly read page |
| Motion Pro digital 0–60 psi 08-0684 (replaced by 08-0751) | Motorcycle/kart digital; ±0.6 psi (forum quote of maker spec) | US$79.99–109.99, mostly out of stock; 08-0751 about US$159.99; Australian RRP A$169.95 in 2017 | 2026-11-17 | [RevZilla](https://www.revzilla.com/motorcycle/motion-pro-digital-tire-pressure-gauge); [Cycle Online](https://www.cycleonline.com.au/?p=82983) | Search-result summary, not directly read page |
| Fastmate RaceSense pocket gauge; gauge with pyrometer | NFC app gauge; ±0.1 psi (maker claim) | Pocket US$315–385; with pyrometer US$449–490; UK £225 / £275–280 | 2026-11-17 | [HMS Motorsport](https://www.hmsmotorsport.com/item/racesense--pocket-tire-gauge); [Wine Country Motorsports](https://winecountrymotorsports.com/products/racesense-tire-gauge-with-pyrometer) | Search-result summary, not directly read page |
| Camozzi digital PRO gauge with case, Australia (kart shop) | Kart digital; accuracy and range not stated | A$198.95 inc. tax | 2026-11-17 | [Karting Direct](https://kartingdirect.com.au/home/2411-tyre-pressure-gauge-kartelli-115mm-dial.html) (listing surfaced by search; product/URL pairing uncertain) | Search-result summary, weak |
| Alfano TyreControl 2 (A1900; A1910; "Air") | Kart gauge/pyrometer logger with app; accuracy not in summaries | £383.00 (A1910, KKC); £396 (Demon Tweeks); €439.00 inc. tax (A1900, French listing); US$484.00 (sold out); NZ$779 (Air), NZ$839 excl. GST (sold out) | 2026-11-17 | [KKC](https://kkckartshop.co.uk/products/go-kart-alfano-new-v2-tyre-control-pressure-with-temperature-gauge-a1910-race); [Harris Race Radios](https://harrisraceradios.com/products/alfano-tyre-control-2-digital-air-pressure-only-gauge) | Search-result summary, not directly read page |
| Unipro UniTire V2 / UniTire IR | Kart gauge; "< ±0.01 bar" typical (2020 forum quote) | V2 €338.80–358.00 (Speedwear.be), €340.00–362.67 excl. VAT (Kartshop.com), £255.00 sale (Zipnorth); IR £306.31 (out of stock) | 2026-11-17 | [Speedwear.be](https://speedwear.be/en/store/karting-speedwear/pit-and-paddock-karting/tyre-pressure-gauges/unitire-v2-black/); [Zipnorth](https://zipnorth.com/collections/digital-stopwatch-tyre-pressure-gauge) | Search-result summary, not directly read page |
| Dill 8500 Certified Gauge Check Station (tyre trade) | Bench/wall station with reference gauge and standard + large-bore ports; reference "re-calibrated normally every 12 months"; accuracy not in summary | US$349.99 (Zoro) – 409.99 – 479.99 (Newegg); 8500-D price not captured | 2026-11-17 | [Zoro](https://www.zoro.com/dill-air-controls-dill-gauge-check-station-dil8500/i/G108181684); [Tire Supply Network](https://tiresupplynetwork.com/products/dill-certified-gauge-check-station-8500); [8500-D](https://www.alltiresupply.com/products/dill-8500-d-gauge-check-station-w-digital-display) | Search-result summary, not directly read page |
| Haltec GCS-A Gauge Check Station | Analogue, 160 psi; ±1 % FS (±1.6 psi) | US$409.99 (backordered) – 436.99 | 2026-11-17 | [Zoro](https://www.zoro.com/haltec-analog-gauge-check-station-160-psi-gcs-a/i/G4635994); [Tire Supply Network](https://tiresupplynetwork.com/products/haltec-gauge-check-station) | Search-result summary, not directly read page |
| Dill 8860-C master gauge (0–160 psi, 2 psi increments) | Shop master for checking tyre gauges; accuracy not stated | US$122.99–149.99 | 2026-11-17 | [Tire Supply Network](https://tiresupplynetwork.com/products/dill-8860-c-master-gauge) | Search-result summary, not directly read page |
| PCL master pressure gauge (10–160 psi) | Fleet master gauge | About £204 (about £244 before discount) | 2026-11-17 | [JHM Butt](https://www.jhmbuttco.com/pcl-master-pressure-gauge99.html) | Search-result summary, not directly read page |
| FSR Racing Mobile Bleeder Tank (dirt/sprint) | Small tank with analogue gauge to 15 psi for setting tyre bleeders; no accuracy stated | US$163.97 | 2026-11-17 | [tirehardware](https://tirehardware.com/product-tag/fsr-racing) | Search-result summary, not directly read page |
| "Tire Bleeder Setting Tank" (Speedway Motors, Walmart listing) | Tank + gauge to 15 psi; no accuracy stated; one buyer review says the gauge was 4 psi off, another that it set bleeders consistently | US$164.99 | 2026-11-17 | [Walmart](https://www.walmart.com/ip/623198643) | Search-result summary, not directly read page |
| Kwik Change Economy Bleed Kit; 713-300 hand pump (0–30 psi) | Bleeder-setting kit with mechanical gauge; hand-pump setter | Kit US$260.99; pump price not shown | 2026-11-17 | [kit](https://www.speedwaymotors.com/Kwik-Change-Economy-Bleed-Kit,22.html); [pump](https://www.speedwaymotors.com/Kwik-Change-713-300-Hand-Pump-for-Setting-Bleed-Offs-0-30-PSI,21.html) | Search-result summary, not directly read page |
| Motorsport-branded low-pressure gauge checker with precision reference | — | None found in four differently worded searches | 2026-11-17 | No URL recorded | Absence in search results, not proof of absence |
| Intercomp factory recalibration and recertification | Gauges matched to a factory standard "traceable to NIST"; returnable "at any time" | Not published; forum anecdotes "small fee", "$25 service fee", "less than a new gauge", every couple of years (undated, fee currency not stated beyond "$") | 2026-11-17 | [Intercomp PDF](https://images.carid.com/intercomp/items/pdf/360060-product-information.pdf); [Rennlist thread](https://rennlist.com/forums/racing-and-drivers-education-forum/1233825-need-to-re-calibrate-intercomp-fill-bleed-tire-gauges.html) | Search-result summary; fee is an undated forum anecdote |
| Longacre recalibration | No recalibration page or fee found on the maker's site; a Rennlist user "sent an analog Longacre in for service" | Not found | 2026-11-17 | [Longacre parts page](https://longacreracing.com/collections/replacement-parts) | Search-result summary |
| Tyre-vendor track-side comparison (Comp Tire East/Goodyear at SCCA events; Dunlop tent at AMA motorcycle races) | Racer plugs own gauge into a vendor master gauge; 2006-era anecdotes, current status unknown | Apparently free | 2026-11-17 | [Rennlist thread](https://rennlist.com/forums/racing-and-drivers-education-forum/886084-tire-pressure-and-gauge-accuracy-4.html) (exact post not identified) | Search-result summary of forum posts, weak |
| Accredited and commercial labs: TOTAL Calibration Solutions (US); Trescal; calibrate.co.uk (UK) | Tyre/pressure-gauge calibration on enquiry | Not published | 2026-11-17 | [TOTAL](https://totalcal.com/milton-industries-501-calibration-services/); [Trescal](https://www.trescal.com/calibrate/longacre-racing-products-inc); [calibrate.co.uk](https://www.calibrate.co.uk/?p=10021) | Search-result summary |
| Australian NATA-accredited pressure labs (WIKA Australia and others) | ISO/IEC 17025 gauge calibration with NATA or 3.1 certificate | No per-gauge fee published; aggregator pages give a generic A$50–500 range (average about A$275–300), not gauge-specific; fee unresolved, needs a quote | 2026-11-17 | [WIKA](https://www.wika.com/en-au/calibration_service_for_pressure_measuring_instruments.WIKA); [NATA](https://nata.com.au/accredited-organisation/wika-australia-pty-ltd-410-403/) | Search-result summary; fee is an unresolved assumption |
| SSI MediaGauge MG1-30-A-9V-R (0–30 psi) | ±1.0 % FS (0.01 psi display resolution is not accuracy) | US$118.99–184.89 | 2026-11-17 | [Zoro](https://www.zoro.com/ssi-digital-industrial-pressure-gauge-0-to-30-psi-2-12-in-dial-14-in-npt-bottom-location-mg1-30-a-9v-r/i/G4708356/); [PartsSource](https://www.partssource.com/parts/ssi/MG130A9VR) | Search-result summary, not directly read page |
| SSI MG-30-A-9V-R (0–30 psi) | ±0.25 % (page header) versus ±0.50 % (spec table) — conflict | US$239.72 (list US$461.00) | 2026-11-17 | [Kele](https://www.kele.com/product/pressure/digital-pressure-gauges/ssi/mg-30-a-9v-r) | Search-result summary, not directly read page |
| Dwyer DPG-103 (0–30 psi) | ±0.25 % FS (about ±0.075 psi); one seller says 0.5 %; NIST-certificate variant exists | US$308.50–341.87 (MSRP US$389.60) | 2026-11-17 | [Zoro](https://www.zoro.com/dwyer-instruments-digital-process-pressure-gauge-0-to-30-psi-3-in-dial-14-in-npt-bottom-location-dpg-103/i/G1437996); [ITM](https://www.itm.com/product/dwyer-dpg-103-pressure-gauge-digital-30psi) | Search-result summary, not directly read page |
| Keller LEO2 digital manometer (e.g. −1…3 bar) | <0.1 % FS at room temperature (about ±0.06 psi on a 4 bar span) | From US$330 (plus 15 % surcharge since 2025-08-07, per a distributor); €417–441 | 2026-11-17 | [Instrumart](https://www.instrumart.com/products/30984/keller-leo2-digital-pressure-gauge) | Search-result summary, not directly read page |
| Generic "digital test pressure gauge" 0–30 psi (Zoro); Measureman economy digital 0–60 | ±0.25 %; 1 % | US$427.99; US$39.97 | 2026-11-17 | [Zoro](https://www.zoro.com/i/G0167885/); Measureman: no URL recorded (reach.dog listing) | Search-result summary |
| Ashcroft 2089 digital test gauge | 0.05 % FS total error band including temperature, 0–150 °F | US$1,048.95 (range unstated) – 1,421 (15 psi); +3.5 % surcharge from 2026-08-04 | 2026-11-17 | [Mitchell Instrument](https://www.mitchellinstrument.com/ashcroft-2089-precision-digital-test-gauge.html); [Transcat](https://transcat.com/ashcroft-2089-30-2089-sd-02l-15-208565) | Search-result summary, not directly read page |
| Fluke 700G05 (−14 to 30 psi); 700RG05 reference | 0.05 % FS | US$1,059.99 (possibly stale) – 1,733.84; 700RG05 US$1,646.95 | 2026-11-17 | [Transcat](https://transcat.com/fluke-700g05-fluke-700g05); [Test Equipment Depot](https://www.testequipmentdepot.com/fluke-700rg05-reference-pressure-test-gauge-14-to-30-psi-97-to-2-bar.html) | Search-result summary, not directly read page |
| Additel 681 (30 psi variants) | 0.05 % FS | US$1,304 (0.05 % model, range unstated); US$1,647 (compound 30 psi variant); ADT681A "from US$1,433" | 2026-11-17 | [Tequipment](https://www.tequipment.net/Additel/681-05-CP30-PSI-N2-DL/Process-Pressure-Gauges/); [Instrumentation2000](https://www.instrumentation2000.com/amp/additel-adt681-05.html) | Search-result summary, not directly read page |
| Ametek Crystal XP2i 30 psi (30PSIXP2I) with ISO 17025 certificate | 0.1 % of reading (one listing); -S2 variant 0.02 % FS (accuracy basis conflicts) | US$1,884.31–1,913.00; -S2 US$2,319.68–2,355.00; data-logging US$2,406–2,859 | 2026-11-17 | [Transcat](https://www.transcat.com/crystal-engineering-xp2i-30psixp2i-pressure-gauge); [Global Test Supply](https://www.globaltestsupply.com/product/ametek-crystal-xp2i-digital-pressure-gauge-30psixp2i) | Search-result summary, not directly read page |
| Ametek M&G PK II pneumatic deadweight tester, to 30 psi | ±0.015 % (±0.025 % option) | US$9,719–13,066 | 2026-11-17 | [Transcat](https://transcat.com/ametek-m-g-pk-pk2-30-ss) | Search-result summary, not directly read page |
| Calibration pump kits: Ralston DP0V + digital gauge; Instrumart DTG kit; Dwyer PCHP-1 (pump only); PIE 020-0237; Ralston DP0V-KIT6-VF | Bench comparison pumps and kits | US$1,037.83–1,060.51; US$1,170 (kits from US$995); US$2,019.05; US$717.00; US$1,190.96 | 2026-11-17 | [Ralston](https://www.testequipmentdepot.com/ralston-dp0v-15psig-d-125-psi-9-bar-pneumatic-cylinder-hand-pump-with-15-psi-digital-pressure-gauge-14-male-npt-process-connection-3-ft-hose.html); [Instrumart](https://instrumart.com/assets/digital_press_calib_kits.pdf); [Dwyer](https://dwyer-inst.com/seriespchp.html); [PIE](https://www.tequipment.net/Pie/process-calibration/pressure-calibration/); [KIT6-VF](https://www.globaltestsupply.com/product/ralston-dp0v-pneumatic-pump-kit-dp0v-kit6-vf) | Search-result summary, not directly read page |
| Bicycle shock pump (RockShox/Fox HP, 300–350 psi, bleed button) | Possible low-volume pressure source; fit to a manifold not checked | US$33.99–40.00 (RockShox); US$35.00 (Fox); digital-gauge versions US$70–80 | 2026-11-17 | [Fanatik Bike](https://www.fanatikbike.com/products/rockshox-high-pressure-fork-shock-pump-300-psi) | Search-result summary, not directly read page |
| Brass 1/8" NPT Schrader tank valve (Milton S-684, Tru-Flate 38-900) | Tyre-valve test port | US$2.41–5.18 each; Milton box of 100 US$144.12 (about US$1.44 each) | 2026-11-17 | [Home Depot](https://www.homedepot.com/p/Milton-1-8-in-NPT-Brass-Tank-Valve-Box-of-100-684BK/312884097); [The Paint Store](https://thepaintstore.com/products/tru-flate-1-8-in-mnpt-tank-valve-38-900) | Search-result summary, not directly read page |

Other notes: Druck DPI 104 and WIKA CPG1500 prices were not obtained, nor any cheap (sub-US$200) hand-pump calibrator kit (two searches returned only industrial suppliers; lowest branded pump US$717). No ready-made Schrader-port manifold for checking racing gauges was found (absence in search results).

**Does a cheap satisfactory alternative already exist?** Yes. Free: put two or three gauges on the same tyre in turn, which finds disagreement but not which gauge is right. Next, buy a second, better gauge as a "benchmark" (Longacre Semi-Pro about US$87–112, Longacre Pro US$126–180, Prisma about US$250–325); a KartPulse user's new Prisma agreed "down to the tenth" with a seven-year-old Longacre. Then a racer can assemble a real reference today: a Keller LEO2 (about US$380 with the surcharge) or Dwyer DPG-103 (US$309–342) plus a brass tee and tank valve, roughly US$320–400 (A$465–580) in parts (sum of search prices plus about US$10 fittings, estimated). An SSI MG1 at US$119–185 is not adequate. Dirt racers with a bleeder-setting tank (US$164–261) already own a low-pressure test volume whose weak point is its plain analogue gauge. No motorsport-branded precision checker was found, and tyre-trade stations (US$350–480) are 0–160 psi and useless at 5–30 psi. What does not exist off the shelf is a packaged low-pressure station with tyre-valve ports, pump/bleed and a dated calibration table: a convenience gap, not a capability gap, and no forum evidence shows anyone looking for it.

**Technical credibility and reference chain:**
- Datasheet accuracy of stocked board-mount sensors is not reference grade. Honeywell ABP2: ±0.25 % FSS accuracy, ±1.5 % FSS total error band, ±0.25 % FSS stability over 1,000 hours (search of datasheet copies). Honeywell HSC: ±1 % FSS total error band over 0–50 °C (search). Honeywell MPR total error band ±1.5 % FSS is from memory, unverified.
- ST LPS28DFW (absolute, 24-bit; datasheet DS13317 Rev 1, December 2021, via search): absolute accuracy mode 2 about ±0.36 % (roughly ±0.16–0.21 psi at 30 psi gauge; band and percentage basis unresolved, confirm on the PDF); relative accuracy ±1 hPa (about ±0.015 psi) at 25 °C; stability ±1 hPa/year. Values are typical, not guaranteed. The gap between absolute and relative accuracy makes "stable sensor plus per-unit calibration" plausible but makes the result depend entirely on calibration.
- Any accuracy better than about ±0.15–0.3 psi must therefore come from per-unit multi-point calibration against a better master. ±0.05 psi over 0–30 psi and about 10–35 °C is a plausible target (validator's estimate, not demonstrated). It would not credibly referee a Prisma or Intercomp 0.1 % claim.
- Master needed: a 0.05 % FS 0–30 psi digital test gauge (Fluke 700G05, Ashcroft 2089, Additel 681), US$1,050–1,750 (about A$1,520–2,540), or Crystal XP2i at US$1,884–1,913 (about A$2,730–2,775), before freight and GST (search prices × 1.45). The Keller LEO2 is too close to the product target to calibrate against (ratio about 1:1). A deadweight tester is not justified at 25–100 units.
- One piece of equipment can serve both jobs: the same master gauge, pump and Schrader manifold are the RD-003 validation rig and the checker's calibration rig. The master is an RD-003 cost the checker could share. Caveats: pressing a gauge on fills its volume (about 1.4 psi drop for 50 mL test volume and 5 mL gauge at 15 psi, a calculation with assumed volumes), so reference and gauge must read the same volume simultaneously; chuck sealing is the main mechanical risk; pumping heat settles in 10–30 s.

**Cost inputs (about 25 units, with basis)**

Basis labels: "current supplier price" = fetched 2026-11-17 from JLCPCB/LCSC, USD, excluding assembly, freight and GST; "published price" = search-result retail summary; "engineering estimate" = validator's estimate; "unresolved assumption" = nobody has checked. A$1 ≈ US$0.69. This is an input table, not a quotation.

| Item | Figure | Basis label | Source / part number |
|---|---|---|---|
| Pressure sensor, ST LPS28DFWTR (digital absolute, 260–4060 hPa) | US$5.31 at 25-unit batch (30-break); US$4.78 at 100; stock 115 | Current supplier price | LCSC C3263277; only stocked low-cost part spanning 0–30 psi gauge; stock only just covers one batch of 25–100 |
| Honeywell ABP2LANT060PG2A3XX (0–60 psi) | US$15.06 / 13.70 / 12.51 at 10 / 30 / 100; stock 2 (LCSC 1) | Current supplier price | C3263584; not available in batch quantity |
| Honeywell ABP2LANT030PGAA5XX (0–30 psi, 5 V) | US$24.42 at 10; stock 4 | Current supplier price | C5937006 |
| Other stocked sensors considered (ABP2 10 bar, MPRLS 0–25 psi absolute, TE MS5803/MS5837-class, Novosense, Infineon, NXP) | US$2.96–27.14 | Current supplier price | C3033011, C3257154, C5166455, C2887941, C5441134/C5441130, C538504, C459977/C459979; all wrong range, too coarse or MAP-class (class from memory, unverified) |
| Honeywell SSC/HSC, first-generation ABP, TE MS5525, All Sensors DLHR, Amphenol, CFSensor XGZP | Zero or not listed (SSC DIP shows US$17.28 at 1–30 with zero stock) | Current supplier price | Would need DigiKey/Mouser purchase with hand or consigned assembly |
| MCU STM32G031F8P6 | US$1.15 (US$1.02 at 100); stock 3,322 | Current supplier price | C529334 |
| Display 0.96" 128×64 OLED | US$1.74 (US$1.55 at 100); stock 4,578 | Current supplier price | C5248080 |
| Regulator; AA battery holders ×2 | US$0.29–0.56; US$0.66 | Current supplier price | C39051 or C5142805; C5290181 |
| Passives, buttons, connector, ESD | US$1.50 (US$1.20 at 100) | Engineering estimate | Generic |
| Bare PCB + SMT assembly share | US$3–5 (US$1.50–2.50 at 100) | Engineering estimate | JLCPCB fee schedule not re-quoted |
| Electronics subtotal | About US$16–22 (US$12–17 at 100) | Sum of the above | — |
| Schrader tank valves ×2 | US$4.80–10.40 (US$2.90–5.00 at 100) | Published price | Milton/Tru-Flate type |
| Manifold block | US$15–30 (US$8–18 at 100) | Engineering estimate | No quotation obtained |
| Reservoir and tube | US$3–10 (US$2–8) | Engineering estimate | — |
| Fine bleed / needle valve | US$5–15 (US$4–12) | Engineering estimate | Same sourcing family as the DEC-040 bleed-valve problem; treat as unresolved |
| Hand pump (bicycle shock-pump class) | US$34–40 (US$30–40) | Published price; trade price and suitability unresolved | RockShox/Fox HP |
| Case; O-rings, fasteners, cells; printed sheet, manual, carton | US$8–20; US$3–5; US$3–5 (at 100: US$6–15; 2.50–4; 2–4) | Engineering estimate | — |
| Total parts per unit, about 25 units | About US$92–157 (A$133–228) with pump; US$58–117 (A$84–170) without | Arithmetic sum, dominated by estimates, not quotations | — |
| Total parts per unit, about 100 units | About US$69–123 (A$100–178) with pump; US$39–83 (A$57–120) without | As above | — |
| Alternative: bought test gauge plus manifold | US$350–460 parts (Keller LEO2 about US$380 or Dwyer DPG-103 US$309–342, plus US$40–80 manifold/case) | Published price plus engineering estimate | Equals what the customer can assemble; no margin room |
| Per-unit labour | 1.5–2.2 h, about A$225–330 (assembly 30–45 min; leak test 10; calibration 20–30; temperature check 15–30; pack 15) | Engineering estimate, owner labour A$150/h | Two to three times the parts cost |
| Design labour (electronics 15–25 h; firmware 25–40; mechanical 25–45; calibration rig 20–30; validation 30–50; documentation 15–25) | 130–215 h, A$19,500–32,250 | Engineering estimate | — |
| Master reference gauge (shared with RD-003) | US$1,050–1,750, about A$1,520–2,540 plus freight and GST | Published price (search) | See table above |
| Accredited calibration of master, per year | A$200–400; fee not found in three searches | Unresolved assumption | Needs a quote |
| Pump, fittings, temperature enclosure, prototype parts | A$500–1,500 | Engineering estimate | — |
| Annual re-check service | A$75–115 labour per unit plus two-way freight; export units would in practice never be re-checked | Engineering estimate | — |
| Direct cost per unit | 25 units: A$310–560; 100 units: A$280–510; with development about A$500–870 at 100 units | Engineering estimate (illustrative) | Design labour and equipment about A$22,000–36,000 |
| Cost-recovering price | About A$670–1,160 (US$460–800) direct at 100 units with 25 % margin; about A$950–1,650 through a 30 % reseller; at 25 units development cost alone exceeds any plausible price | Engineering estimate; margins are illustrative assumptions | Against US$320–400 self-assembled |
| SkidLabz accreditation (ISO/IEC 17025) | Not costed | Unresolved assumption | Out of proportion to volume; without it a certificate is a manufacturer's test report, not a NATA certificate |

**What must be demonstrated before claiming equivalent useful performance:**
- Demand: named buyers (clubs, shops, teams, tyre vendors) who say they would pay a stated price, not racers who agree gauges disagree.
- Field problem size: measured offsets of a sample of real gauges at 5/10/15/20/30 psi. If most are within ±0.2–0.3 psi there is no story.
- Reference performance: ±0.05 psi against the master at 5, 20 and 35 °C on at least five prototypes, and again after six months, including transport and a drop test.
- Port sealing: leak-free, repeatable connection with ball, angle, straight and small-hub kart chucks and hold-valve gauges; comparison repeatability of 0.03 psi or better.
- Traceability wording that a NATA lab or adviser confirms is acceptable for an unaccredited manufacturer.
- An advantage over a Keller LEO2 plus tank valve that a buyer will pay for (currently unproven).
- Per-unit calibration in 30 minutes or less, or the labour model fails.

**What the forum evidence adds for RD-003 (status unchanged):**
- User-language requirements: karts about 5–15 psi, where 0.25–0.5 psi is a real change and ±0.6 psi "a big swing"; sprint-car rears about 4.5–8 psi, where one new gauge was 1.5 psi out (Hoseheads, search-engine summary); cars at 25–40 psi are a different audience (RD-065). Settling time (about 10–30 s), air loss on small kart tyres and chucks fitting small hubs are stated annoyances. Robustness is the trust issue: drift after drops, analogue creep, digital drift over 1–2 years and failure after a cold soak (GRM, index summaries only).
- Trusted competitor gauges and prices: Longacre digital (about US$87–180) and Prisma (about US$250–325 / £184–229) are liked and long-lived; Intercomp (US$380–400) is respected but called "stupid expensive"; US$300 draws "hard pass". Comfortable band roughly US$90–220. Australian shelf prices are far above US prices (Longacre Semi-Pro digital A$365, Intercomp digital A$606.90, Moroso A$452), but these are reseller listings with uncertain dates, not demand evidence.
- DEC-013 (no Bluetooth/app/temperature/logging in V1) is supported: reported faults in premium kart gauges are in memory and recording functions. A dated per-unit calibration table or check speaks to the stated worry more directly than extra features.
- DEC-011 (sensor cost/supply), DEC-012 (plumbing) and DEC-040 (bleed valve) are not addressed. There is no Australian demand evidence, no volume or willingness-to-pay data beyond anecdotes, and no dissatisfaction with Longacre digital at about US$90–110, the hard competitor.

**Register relationship:**
- RD-092 (gauge / pressure calibrator, unadopted suggestion): the checker is this idea narrowed to low-pressure tyre gauges; record new evidence there. Its reopening condition (a concrete user-selected requirement and evidence of a worthwhile product advantage) is not met. Facts worth keeping: trade check stations, the US$320–400 self-assembly route and Intercomp's recalibration service.
- RD-003: the forum evidence is supporting only; the internal reference fixture is validation equipment, not a separate product. Do not change status.
- RD-016 (sprintcar electronic tyre bleeders, paused): bleeders are set against gauges on setting tanks; an accurate reference is a better gauge on equipment racers already own. Retention, valve supply, control validation and unit cost are untouched.
- RD-065 (wider-range general gauge): evidence both ways; advance condition unchanged. RD-064 (budget variant): consistent with the record; Longacre Basic, Joes and QuickCar occupy the slot. RD-088 (general pressure tester): no tyre-forum evidence.
- Competitor lists: Prisma, Alfano, Unipro, Fastmate/RaceSense, Moroso, Camozzi, FSR Racing, Dill, Haltec (tyre-tool brand), Milton, SSI, Dwyer, Ashcroft, Keller and others were not found in the lists; adding them is for the coordinator to decide.

**Red-team: reasons to reject, cheapest validation step, kill criteria:**
- No one is asking, and the free workaround satisfies the people who complain; buyers would be institutions, a much smaller group than the posters.
- Adequate substitutes exist at or below any price SkidLabz could reach (US$320–400 assembled, second gauge US$87–180, maker recalibration, old free vendor comparisons, trade stations and bleeder tanks).
- The value is authority and calibration labour, which a small unaccredited maker is worst placed to sell; support is dispute-heavy; export units cannot practically be re-checked; a ±0.05 psi home-brand reference cannot overrule Prisma or Intercomp gauges. The LPS28DFW is the only suitable stocked sensor (115 pieces) and the fine-bleed valve is in the DEC-040 sourcing family.
- Verdict by form: internal fixture yes (master ≈ A$1,500–2,500, shared); service only as a by-product (a 10-minute check costs about A$25 of owner time at A$150/h); product not supported by the evidence.
- Cheapest validation step: once the RD-003 fixture exists, take it to one or two local kart or speedway meetings, offer free checks at 5/10/15/20 psi, record make, age and offset, and ask whether owners would pay for a re-check and whether a club or shop would buy a station at a stated price. Before the fixture exists, ask three or four local kart shops, tyre vendors and clubs whether anyone has ever asked to have a gauge checked.
- Kill criteria (thresholds are judgements): fewer than about one gauge in five off by more than 0.3 psi at 10 psi or 0.5 psi at 20–30 psi; owners prefer buying a new gauge or no club/shop commits at about A$700+ direct; prototype cannot hold ±0.05 psi from 5 to 35 °C, drifts more than ±0.03 psi in six months or cannot seal repeatably; per-unit calibration cannot be brought under about 30 minutes; an accredited lab or motorsport brand offers low-pressure tyre-gauge checks under about A$50–80 with quick turnaround (fee currently unresolved).

**Lookups not performed / unknowns:**
- About 50 web searches; no page outside JLCPCB, LCSC and KartPulse was read directly, so every retail price is a search-result summary with unknown page date. GRM pages were not read (access refused); its test article date (November 2009, republished 2022) is from search summaries. Hoseheads was not probed again (rate limit).
- Not obtained: Druck DPI 104 and WIKA CPG1500 prices; plain 0–30 psi Additel 681 price; sub-US$200 hand-pump calibrator kit; needle valve and manifold prices; Dill 8500-D price; Kwik Change 713-300 pump price; Australian prices for Prisma, Alfano, Unipro, Joes and Longacre Pro digital; QuickCar 0–60 digital price.
- NATA calibration fee for a pressure gauge not found (three searches); needs one quote request, not made. Intercomp and Longacre recalibration fees are unpublished (only undated Intercomp anecdotes). Whether any shop, vendor or club offers gauge checks today is not established (two roughly 2006 anecdotes). Club-level rules requiring calibrated gauges were not searched. Market count is only Karting Australia's 64 clubs (2023).
- Conflicting or unconfirmed specifications: Intercomp accuracy (0.1 % vs 0.5 %) and resolution; SSI MG-30 (0.25 % vs 0.5 %); Dwyer DPG-103 (0.25 % vs 0.5 %); Crystal XP2i (0.1 % of reading vs 0.02 % FS); LPS28DFW mode-2 basis; Honeywell MPR and Novosense classes (from memory). The Camozzi A$198.95 product/URL pairing is uncertain.
- JLCPCB assembly, CNC manifold and enclosure costs are estimates. The private SkidLabz tyre-gauge repository was not read, so sensors already assessed for RD-003 and existing reference equipment are unknown.

### V3 — Load-cell valve-spring force tester / tester reference

**Validator's verdict:** Do not advance as a product. The hypothesised product already exists at a price SkidLabz cannot approach: Proform 66836 (digital vise/arbor "mini", US$178–224) and 66842 (the same with a height micrometer, US$183–240). Whether those are satisfactory is unproven either way, since no independent accuracy test, no published accuracy and no sensing principle (strain-gauge cell or hydraulic capsule) was established. On the validator's estimates, materials alone (A$175–345 at 25 units) match or exceed the Proform retail price before A$113–195 of labour per unit and A$20,800–42,300 of one-time cost. The only distinct element is a traceable full-range verification reference, wanted by perhaps three or four forum users in six years.

**What the customer actually needs:** The requesters are low-volume or hobby engine builders who cannot justify US$1,000 for a Rimac or Intercomp and distrust cheap hydraulic minis (sticking, leaks, non-repeatable). Minimum useful spec (the validator's estimate): 1 lb resolution; ±1% of reading or ±2 lb from about 50 lb to full scale across 5–40 °C; peak hold; lb and kg; 0–700 lb covers flat-tappet, hydraulic-roller and mild solid-roller work, while race solid-roller needs 1,000 lb or more. Height, not force, is the binding bench error: at 300–700 lb/in a 0.010" error is 3–7 lb, and the best-documented "7–9% low" case ended with a depth gauge 0.050" out. Force-only is sufficient for verifying another tester (a puck in series), but the latest requester said he would not want a vise-mounted tool. Adjacent uses (clutch, wastegate, kart, torsion-bar springs) are not evidenced; the kart forum's one spring thread ended "No tool requested".

**Competing products and prices**

All web prices are search-result summaries, not directly read pages (retailer pages could not be opened); listing capture dates unknown, several shown out of stock. Forum prices are the poster's figure at the post date (directly read posts).

| Product | What it does | Price as found | Date seen | Source | Evidence type |
|---|---|---|---|---|---|
| Proform 66836 digital mini | Hex-bodied puck for vise/arbor/drill press; 0–700 lb × 2 lb, peak hold, 9 V battery; principle not established | US$177.99–223.73 at five US retailers (outliers US$346.99–385.29); Australian listing sold out, price not shown | 2026-11-17 | [Mancini](https://www.manciniracing.com/dimivaspte.html), [90racing](https://90racing.com/products/proform-66836), [OnlyInStock](https://www.onlyinstock.com/products/proform-66836), [Engine Master AU](https://enginemaster.com.au/products/proform-pr66836-valve-spring-tester-digital-mini-vise-arbor-mount-0-700-lbs-range-each) | Search-result summary |
| Proform 66836, owner view | "5 stars… way better than the analog version" | — | 2023-06-09 | [Speed-Talk t=67090](https://www.speed-talk.com/forum/viewtopic.php?t=67090) | Forum post read directly |
| Proform 66836, retailer rating | 4.75/5 from 12 ratings; review text not seen | — | 2026-11-17 | [Summit](https://www.summitracing.com/search/part-type/valve-spring-testers) | Search-result summary |
| Proform 66842 digital mini + micrometer | As 66836 plus 1.500–2.295" micrometer in 0.01" steps | US$182.99–239.71 (JEGS US$196.99, Speedway Motors US$189.99; outlier US$397.35); C$302–393; A$450.21 "flash sale" at Engine Master | 2026-11-17 | [JEGS](https://www.jegs.com/i/proform-778-66842-digital-valve-spring-tester-with-micrometer-0-01-in-increments-backlit-display), [Speedway Motors](https://www.speedwaymotors.com/Proform-66842-Digital-Valve-Spring-Tester-with-Micrometer-Combo,540472.html), [Engine Master AU](https://enginemaster.com.au/products/proform-pr66842-digital-mini-valve-spring-tester-range-0-700lbs-x-2lb-increments) | Search-result summary |
| Proform 66776 digital bench tester | Billet frame, digital height micrometer; 0–1,000 lb × 1 lb | US$620.99–650.99 (four retailers), US$758–797 (three more); MSRP US$683.99; A$1,289.70 tax-inclusive, sold out (Engine Master); NZ$1,497.10 | 2026-11-17 | [Classic Industries](https://www.classicindustries.com/product/66776-BCHW.html), [Vivid](https://www.vividracing.com/pro-form-bench-mount-1000-lbs-capacity-digital-valve-spring-tester-red-anodized-aluminum-finish-p-153796954.html), [Engine Master AU](https://enginemaster.com.au/products/proform-pr66776-h-d-digital-bench-top-valve-spring-tester-up-to-1000lbs-pressure) | Search-result summary |
| Proform 67601 digital on-head | 0–600 lb × 5 lb; RD-020 class, not a bench tester | US$310–614 | 2026-11-17 | [Proform](https://proformparts.com/product-detail/67601/digital-valve-spring-pressure-tester-adjustable-0-600lb-range-5lb-increments) | Search-result summary |
| Proform 66775 / 66774 analog bench/vise | Analog gauge frames, 700 / 300 lb | US$391.99–489.06 / US$373.99–448.58 | 2026-11-17 | [CSP Racing](https://www.cspracing.com/products/proform-66775-engine-valve-spring-tester-700-lb-rating-heavy-duty-billet-aluminum-red) | Search-result summary |
| Generic hydraulic mini | Hydraulic, analog gauge, 0–700 lb typical | "less than $100" (2024); about US$75 (earlier GRM notes) | 2024-07 | [Speed-Talk t=68722](https://www.speed-talk.com/forum/viewtopic.php?t=68722) | Forum post read directly |
| Comp Cams 5314 mini | Hydraulic mini, 0–1,000 lb | US$165.77–247.61; A$380.60 tax-inclusive, sold out; NZ$380.90 + GST | 2026-11-17 | [JB's](https://jbspowercentre.com/products/bdqq-5314), [Engine Master AU](https://enginemaster.com.au/products/comp-cams-mini-valve-spring-tester-co5314-0-1000-lb-in) | Search-result summary |
| LSM SM-600 bench-top | Bench frame, 0–600 lb gauge (poster believes hydraulic) | US$499.99; NZ$1,157.06 + GST (600), NZ$1,343.10 + GST (1,000) | 2026-11-17 | [Pit Stop USA](https://pitstopusa.com/products/lsm-racing-products-spring-machine-bench-top-valve-spring-tester-w-0-600-gauge), [Fast Lane Spares](https://fastlanespares.co.nz/products/lsm-bench-top-valve-spring-tester) | Search-result summary |
| Rimac "Big Blue" BB0500 / BB1000 (now Proform) | Mechanical bench tester, analog dial | US$949.95 / US$1,002.00; used 500 lb about US$600 (2020 forum) | 2026-11-17 | [JEGS](https://www.jegs.com/i/Proform/778/BB0500/10002/-1), [Global Test Supply](https://www.globaltestsupply.com/product/rimac-bb1000-ngine-valve-spring-tester) | Search-result summary; forum figure read directly |
| Intercomp 100058 digital bench | Strain-gauge load cell, 1,000 lb; ±0.25% of reading, 0.2 lb steps (reseller brochure) | US$895.00; A$1,958.77 tax-inclusive, sold out; A$1,626.90, sold out | 2026-11-17 | [Pit Stop USA](https://pitstopusa.com/products/intercomp-digital-valve-spring-tester), [Performance Wholesale](https://performancewholesale.com.au/products/intercomp-racing-1-000lb-valve-spring-pressure-tester), [Speedway Spares](https://speedwayspares.com.au/products/intercomp-valve-spring-tester-1000lbs) | Search-result summary |
| Intercomp 100450 on-engine | 600 lb electronic, adjustable | US$514.51 / US$578.97, out of stock; a stale JEGS listing shows US$799.00 (part number not confirmed) | 2026-11-17 | [Pit Stop USA](https://pitstopusa.com/products/intercomp-valve-seat-pressure-tester) | Search-result summary |
| Buxton Bench Pro | Load cell plus position sensor, computed results | US$1,595 + US$189 firmware; "$1800"; current price not found | 2019-06 / 2020-02 | [Speed-Talk t=60160](https://www.speed-talk.com/forum/viewtopic.php?t=60160) | Forum post read directly |
| Performance Trends tester, Complete Kit SPV11C-STK and Rimac retrofit kit | Calibrated load cell, length sensor, electronics and software without the frame; retrofit converts a Rimac | Price not found (three searches); shipping "as low as $80" | 2026-11-17 | [Valve spring tester](https://performancetrends.com/Valve_Spring_Tester.htm), [Rimac kit](https://performancetrends.com/Rimac_Spring_Tester_Kit_B.htm) | Search-result summary |
| Rimac/Proform BB1901 3-in-1 calibration spring kit | Calibrated springs with chart, about 10–640 lb | US$79.95–84.95; NZ$214.50 + GST | 2026-11-17 | [JEGS](https://jegs.com/i/Proform/778/BB1901/10002/-1), [Goodson](https://goodson.com/products/rimac-calibrated-test-spring-set) | Search-result summary |
| Comp Cams 5316 calibrated spring | Whether a certificate is supplied is unclear | US$45.95; about US$35 in 2016 | 2026-11-17 / 2016-07 | [JEGS](https://www.jegs.com/vpt/COMP-Cams/Valve+Spring+Tester), [Speed-Talk t=47010](https://www.speed-talk.com/forum/viewtopic.php?t=47010) | Search-result summary; forum post |
| ATO 500 kg spoke-type cell + display controller | Strain-gauge cell with panel indicator (not a hand tool) | US$263.00 (micro button cell version US$340.00) | 2026-11-17 | [Walmart listing](https://www.walmart.com/c/kp/compression-load-cell-with-display) | Search-result summary |
| Generic cell-and-indicator kits (eBay) | Capacity and accuracy not confirmed | About US$116–500 | 2026-11-17 | [eBay store](https://www.ebay.com/str/qlsensors) | Search-result summary |
| 5,000 N external-sensor hand-held force gauges | Peak hold, ±0.5% (listing) | Ambiguous: US$78 / 107 / 556 on NBC Lab pages (model mapping unclear); US$614.70–675.56 (Walmart) | 2026-11-17 | [NBC Lab](https://www.nbclab.com/cp/C2A0310AECB319A7.html) | Search-result summary (ambiguous) |
| Mark-10 M5-1000 | Industrial gauge, ±0.1% | US$1,700 | 2026-11-17 | [ABQ Industrial](https://abqindustrial.net/store/force-and-torque-measurement-c-101/digital-force-gages-c-101_15/mark-10-m5-1000-advanced-digital-force-gauge-series-5-1000-lbf-500-kg-5000-n-capacity-p-685-op-1175_4997.html) | Search-result summary |
| Free alternatives | Local shop checks springs ("all 16 for ten bucks", 2017); bathroom scale under a drill press (to about 300 lb) | About US$10 / owned | 2017-12 | [Speed-Talk t=51845](https://www.speed-talk.com/forum/viewtopic.php?t=51845) | Forum post read directly |

The earlier "about US$602" figure for the 66842 was a mis-attribution: no such 66842 listing was found; it matches the 66776 bench tester or upper 67601 listings. The sensing principle of every Proform digital unit is not established (manuals could not be opened).

**Does a cheap satisfactory alternative already exist?** The same product concept exists cheaply (Proform 66836/66842, US$178–240); "satisfactory" is unproven but more likely yes than no for a hobby buyer. A complete 1,000 lb digital bench tester with height gauge (Proform 66776, US$621–797) already sits in the gap the forum describes, and calibration springs (US$46–85) let owners verify from about 10 to 640 lb. Local Australian retail is much higher (66842 A$450; 66776 A$1,290; Intercomp A$1,627–1,959, all shown sold out), an import-margin gap rather than a technology gap. Unserved: a traceable reference for 640–1,000+ lb (three or four forum users) and a stiff, inexpensive frame with trustworthy height readout, which is a mechanical product.

**Why prices are what they are / where a saving could come from:** The electronics are only about 5–10% of unit cost; cost sits in the transducer, hardened ground platens, machined body and per-unit calibration labour. No saving is evident: even at 100 units the validator's variable cost sits at or above the Proform retail price, and a direct-sourced cell at US$20–45 is an unresolved assumption (no quotation). A "reference" claim adds recurring accredited-calibration cost.

**Cost inputs (about 25 units, with basis)**

| Item | Figure | Basis label | Source / part number |
|---|---|---|---|
| Bridge ADC HX711 | US$0.328 @50 (US$0.302 @100) | Current supplier price (JLCPCB/LCSC, 2026-11-17, ex fees/freight/GST) | C43656 |
| Bridge ADC CS1237 | US$0.462 @30 | Current supplier price | C77801 |
| Bridge ADC ADS1232IPWR | US$1.917 @30 | Current supplier price | C27919 |
| MCU CH32V003F4P6 / STM32G030F6P6TR | US$0.237 @50 / US$1.093 @30 | Current supplier price | C5187096 / C529330 |
| OLED 0.96" HS96L03W2C03 | US$1.740 @30 (not sunlight-readable) | Current supplier price | C5248080 |
| Segment LCD glass or 4-digit LED | Not found as stocked part; LED digits est. US$0.30–0.80 | Unresolved assumption | — |
| Passives, PCB fabrication and assembly fees | US$0.80–1.50 / US$4–8 per board | Engineering estimate (fee schedule not looked up) | — |
| Electronics subtotal | About US$11–16 (A$16–23) at 25; cost-down about US$8–13 | Current supplier price plus engineering estimate | — |
| Load cell, 1,000 kg button, class C2 (Phidgets) | US$50.00 list; US$60.50, £58.18, €75.62 at resellers | Published manufacturer/distributor price (search-result summary) | [Phidgets](https://www.phidgets.com/?prodid=231) |
| Load cell, S-type 500 kg C3 (Phidgets) | US$50.00 list; US$71.54 incl. tariffs; £51.64 | Published price (search-result summary) | [Robotshop](https://www.robotshop.com/products/phidgets-steel-s-type-load-cell-500kg-c3) |
| Spoke/pancake 500 kg, ±0.2% | US$114.95 or 259.00 (inconsistent listing) | Unresolved assumption | [VXB](https://vxb.com/products/spoke-type-load-cell-sensor-for-scales-tension-and) |
| Omega LCHD-500 / LSHD-500 pancake, ±0.1% | US$1,566 / US$1,705 | Published price (search-result summary) | [Omega](https://www.dwyeromega.com/en-us/fully-submersible-waterproof-low-profile-load-cells/LSHD/p/LSHD-500) |
| Direct-from-maker 500 kg cell, 25–100 pcs | US$25–60 (US$20–45 at 100) | Unresolved assumption (no quotation) | — |
| Machined body / hardened platens / window and fasteners / batteries and packing / freight and scrap | A$35–90 / A$30–70 / A$8–15 / A$8–18 / A$10–25 | Engineering estimate (no drawing or quotation) | — |
| Unit materials total | A$175–345 (US$121–238) at 25; A$140–265 at 100 | Composite: supplier price + published cell price + estimates; not a quotation | — |
| Per-unit labour | 0.75–1.3 h (A$113–195); calibration alone 20–35 min | Engineering estimate | — |
| Support per unit | 0.25–0.5 h (A$38–75) | Engineering estimate | — |
| Variable cost per unit | A$326–615 at 25; A$291–535 at 100 | Engineering estimate | — |
| Owner hours, one-time | 117–230 h (A$17,550–34,500 at A$150/h): electrical 15–30, firmware 25–50, mechanical 25–45, calibration fixture 12–25, validation 30–60, documentation 10–20 | Engineering estimate | — |
| Reference cell + indicator / accredited calibration (initial) / press frame and fixtures / prototypes / benchmark purchases | A$1,500–4,000 / A$400–1,000 / A$300–800 / A$600–1,500 / about A$400–520 | Unresolved assumption (first two) and engineering estimate; benchmark prices are search-result summaries | — |
| One-time total | About A$20,800–42,300 | Engineering estimate | — |
| Fully loaded cost per unit | A$1,160–2,310 at 25; A$500–960 at 100 | Engineering estimate arithmetic (not a forecast) | — |
| Recurring recalibration | A$400–1,000 fee + A$300–450 labour every 12–24 months | Unresolved assumption | — |

Exchange rate used: US$1 ≈ A$1.45; Australian GST 10%. Accredited force calibration (NMI, NATA laboratories) is quote-only with no published prices.

**What must be demonstrated before claiming equivalent useful performance:**
- That the sub-US$250 Proform units are not good enough: test a 66836/66842 against a traceable reference at 50–700 lb, cold and warm, centred and 5 mm off-centre, ten repeats (within about ±1% or ±3 lb would answer the complaint commercially).
- What is inside the Proform (strain-gauge cell or hydraulic capsule).
- A buyer count rather than a thread count (at least 25 identifiable buyers at the required price) and a route to US hobby engine builders.
- That buyers will pay about US$400–600 for traceability rather than US$46–85 for calibration springs.
- A height answer at least as good as the 66842 micrometer, or an explicit force-only scope.
- A written quotation for a reference cell, indicator and accredited calibration.
- Survival of coil-bind overload by test; any adjacent use needs its own demand evidence.

**Register relationship:** RD-020 (on-engine digital valve-spring checker) is Rejected, commercial (owner, 2026-10-20, reaffirmed 2026-10-27): many alternatives exist, expected racer sales are low, commercial case poor; its retained boundary is that a basic load-cell-and-display product was already compared with inexpensive options. The bench/reference form differs in place of use and buyer, but none of the three reasons is addressed (alternatives strengthened) and the reopening test is not met. RD-092 (gauge/pressure calibrator) is an unadopted suggestion; forum evidence does not change it. RD-017 (torsion-bar tester, paused: no economical reference rig) would gain at most the force leg of a verification route, not a resolution. RD-021, RD-018 and RD-049 are not reopened; RD-018's lesson is that calibration and mechanical parts, not electronics, defeat the economics.

**Red-team: reasons to reject, cheapest validation step, kill criteria:**
- Another brand of an existing cheap product at a cost disadvantage (materials alone at or above Proform retail).
- It does not fix height and frame error, and the latest requester does not want a vise-mounted tool.
- Wrong customers (US hobby engine builders, not speedway racers), unmeasured demand, and open-ended calibration, certificate and dispute support at A$150/h.
- Cheapest step: about one owner hour reading the Proform manuals and owner reviews on an unrestricted connection; if still open, buy one 66842 and a BB1901 kit (about A$400–520 landed, 3–5 owner hours) and test it before buying reference equipment or designing a board.
- Kill if: the Proform reads within about ±1% or ±3 lb across 50–700 lb and repeats within 2 lb; it contains a strain-gauge cell; a non-certified unit cannot come under about A$250 landed cost (or a certified unit cannot sell profitably below about US$400); fewer than about 25 identifiable buyers or no US channel; reference route over about A$5,000 up front or A$1,000 a year; or no overload-tolerant design within cost.

**Lookups not performed / unknowns:**
- No retailer or manufacturer page was read directly (42 searches, all summaries); Proform manuals unreachable.
- Sensing principle of all Proform digital units; any independent accuracy test or written owner review.
- Current prices not found: Buxton Bench Pro, Performance Trends units and kits, PAC T900, Goodson and Larson calibration springs, Rimac BB1902/BB1903, several Engine Master AUD prices, Amazon/AliExpress kits, crane scales and hydraulic tongue-weight scales.
- Bare cell prices at 25–100 units from Chinese makers; NATA calibration and reference-cell quotations; JLCPCB fee schedule; CNC quotations.
- Market size and adjacent uses (no targeted search); several forum threads relied on the earlier researcher's ledger and were not re-read; photo attachments are hidden from guests; a 2009–2019 search-index gap may hide owner reports. Typical spring-load figures come from search summaries of magazine and retailer guides.

### V4 — Plug-in ignition / start-circuit tester for spec kart engines

**Validator's verdict:** Reject the hypothesised engine-specific inline loom breakout; the narrower variants are commodity items. The pain recurs every season, but nobody asks for a tester (zero product requests in 72 threads read), and the one function that separates the concept from a voltmeter, trigger/primary pulse indication, was decisive in only about 2 identified cases. Looms vary widely (six or more lead sets, connector families unidentified), and the validator's estimate is about 115–215 owner hours (A$17k–32k) for one engine family against a price ceiling of roughly US$60–100. This is a different, narrower form of RD-029 plus RD-083, and its recorded reasons apply.

**What the customer actually needs:** The recurring job is "the starter does nothing or spins but will not turn the engine: battery, loom/switch/relay, or starter?", then "it cranks but will not fire: is there spark?". Minimum useful function: battery voltage at rest and minimum during cranking, the same at the starter terminal (to show loom/relay drop), and a spark-present indication; cranking speed has some value because self-powered kart ignitions do not spark below a threshold speed (forum staff: roughly 150–750 rpm depending on system). The first two are a voltmeter with min-hold and the third an in-line spark checker; the loom-specific breakout adds only kill-line state and trigger pulse indication, and cannot give a trustworthy stator/CDI verdict without known good/bad reference data that neither IAME nor the forum publishes. Buyers would be owner-drivers and karting parents unsure with a multimeter, secondarily kart shops, who already own meters, spares and (for Rotax) factory testers; no post states willingness to pay.

**Root-cause tally from the threads read**

Counts as given by the validator: 53 distinct fault cases in 50 additional threads (2018-11 to 2026-10), of which 33 were identified and 20 unresolved. Identified causes: battery 7, starter/brushes/bendix 5, harness/connector/fuse 4, switch 1, stator/pickup 2, coil/ECU/power pack 1, plug/cap/HT lead 1, carburation/flooding/technique 6, engine-mechanical 6. Starting-circuit faults are 17 of 33 (52%); ignition electronics 3 of 33 (9%); fuel plus mechanical 12 of 33 (36%). "Breakout would have helped" is at most 16 of 33, and in at least 9 of those a voltmeter under crank, load tester, charger boost or jumper already did or would do the same; the pulse-indication function was decisive in 2 identified cases (B6, C6), at most 9 of 53 counting unresolved no-spark cases. The tally under-represents hard-to-diagnose faults (20 of 53 unresolved), and photos were not opened. Sampled threads (a selection from the validator's 53-case tally):

| Thread | Date | Engine | Actual cause | Would a breakout have helped? |
|---|---|---|---|---|
| [A1 ka-wont-start-spark-issue](https://forums.kartpulse.com/t/ka-wont-start-spark-issue/12680) | 2024-08 | KA100 | Flooded crankcase | No |
| [A3/A4/A5 ka100-starter-issues](https://forums.kartpulse.com/t/ka100-starter-issues/7896) | 2021-08 | KA100 | Broken brush lead; two battery cases (one "everything except the battery" replaced) | Starter partial; battery yes (a meter would do) |
| [A6 new-ka100-not-starting](https://forums.kartpulse.com/t/new-ka100-not-starting/10538) | 2023-04 | KA100 | Choke/priming technique | Partial (spark indicator) |
| [A7 no-spark-from-head](https://forums.kartpulse.com/t/no-spark-from-head-on-ignition-ka100/9874) | 2022-11 | KA100 | Unresolved; cap/coil connection suspected | Partial |
| [A9 wiring-harness-start-button](https://forums.kartpulse.com/t/ka100-wiring-harness-start-button/4277) | 2019-07 | KA100 | Battery (12.4 V at rest, bad) | Yes (meter does it) |
| [A10 test-a-ka100-stator](https://forums.kartpulse.com/t/how-to-test-a-ka100-stator/12726) | 2024-08 | KA100 | Unresolved; no known stator test | Possibly (needs reference data) |
| [B3 replacing-carb](https://forums.kartpulse.com/t/iame-x30-not-starting-after-replacing-carb/3009) | 2018-11 | X30 | Damaged piston ring | No |
| [B4 iame-starter](https://forums.kartpulse.com/t/iame-starter/5233) | 2020-02 | X30 | Under-charged battery (11.38 V at starter) | Yes (meter does it) |
| [B6 x30-help-needed](https://forums.kartpulse.com/t/x30-help-needed-please/4360) | 2019-08 | X30 | Stator failed (sparks only with kill switch held) | Possibly yes |
| [B7 stator-mechanical-failure](https://forums.kartpulse.com/t/x30-stator-mechanical-failure/9289) | 2022-06 | X30 | Rotor nut loose | No |
| [B8 swift-x-ka-harness](https://forums.kartpulse.com/t/iame-swift-x-ka-harness-new-style/15285) | 2026-03 | X30/KA | Ignition adapter cable missing from kit | No (parts knowledge) |
| [C1 leopard-starting-issues](https://forums.kartpulse.com/t/leopard-starting-issues/6201) | 2020-07 to 2020-12 | Leopard | Unresolved; power-box fuse, bendix | Partial |
| [C5 leopard-ignition-issues](https://forums.kartpulse.com/t/iame-leopard-ignition-issues-comet-kart/7929) | 2021-08 | Leopard | New stator died twice; cause not established | No (on-track failure) |
| [C6 iame-ignition-help](https://forums.kartpulse.com/t/iame-ignition-help/8273) | 2021-11 | Leopard | Open crimp splice on coil drive wire | Yes (no drive pulse) |
| [C8 leopard-power-pack-issue](https://forums.kartpulse.com/t/leopard-power-pack-issue/9123) | 2022-05 | Leopard | Stuck switch inside potted power pack | No (internal fault) |
| [D1 rotax-evo-no-spark](https://forums.kartpulse.com/t/rotax-evo-starting-issues-no-spark/10507) | 2023-04 | Rotax EVO | Slipped ring and bad crank sensor | Partial at best |
| [D3 rotax-starter-not-engaging](https://forums.kartpulse.com/t/rotax-starter-not-engaging/9499) | 2022-08 | Rotax | Battery sag under load (staff: "70% of the time") | Yes (meter does it) |
| [D5 misfire-rotax-max-senior](https://forums.kartpulse.com/t/misfire-rotax-max-senior/7717) | 2021-07 | Rotax | Loose screws inside engine; not electrical | No (misdiagnosis warning) |
| [D8 rotax-starter-issue](https://forums.kartpulse.com/t/rotax-starter-issue/5084) | 2020-01 | Rotax | Battery: 12 V at rest, 3.5 V on start | Yes (meter does it) |
| [E1 vortex-rok-wont-start](https://forums.kartpulse.com/t/vortex-rok-engine-update-still-wont-start/15267) | 2026-03 | Vortex ROK | Crank seals and main bearings | No |
| [E2 vortex-rok-update](https://forums.kartpulse.com/t/vortex-rok-update-suffering/15354) | 2026-03 | Vortex ROK | Probable loom/relay/button voltage drop | Yes (meter does it) |
| [E10 starter-motor-super-rok](https://forums.kartpulse.com/t/starter-motor-in-vortex-super-rok/5923) | 2020-05 | Super ROK | Battery plus bad relay connection | Yes (meter does it) |
| [E11 rok-vlr-wont-fire-up](https://forums.kartpulse.com/t/rok-vlr-wont-fire-up/14419) | 2025-07 | ROK VLR | Unresolved after replacing stator, coil, plug, boot | Possibly |

**Competing products and prices**

Every web row is a search-result summary, not a directly read page, seen 2026-11-17 with page date unknown; treat prices as unverified. Forum prices are as stated on the post date.

| Product | What it does | Price as found | Date seen | Source | Evidence type |
|---|---|---|---|---|---|
| Oppama PET-4000 pulse ignition checker (Kitaco 752-0600005) | Adjustable-gap spark output / coil check without removing stator or flywheel; sold by kart shops | £65.11 (ZipNorth); US$71.24 eBay (from Japan, about A$101.50 as listed); ¥5,280 sale; kartshop.com price not shown | 2026-11-17 | [ZipNorth](https://zipnorth.com/products/go-kart-oppama-pulse-pet-4000-ignition-checker-karting-race-racing), [eBay](https://www.ebay.com/itm/175337275508), [bikeman.jp](https://bikeman.jp/en/products/kt-752-0600005), [kartshop.com](https://kartshop.com/shop/pulse-ignition-checker-35513p.html) | Search-result summary |
| Rotax Harness Tester (Max EVO) | Dealer tool checking the EVO harness | US$440.99 | 2026-11-17 | [Point Karting](https://pointkarting.com/products/cable-harness-tester) | Search-result summary |
| Rotax EVO ECU tester | Checks ECU function and legality | €561.95 (Radne); €727.30 (Itaka); Point Karting price not shown | 2026-11-17 | [Radne](https://www.radne.com/products/rotax-evo-ecu-test), [Itaka](https://www.itakashop.com/gb/157-professionals-engines-tools?page=2), [Point Karting](https://pointkarting.com/products/ecu-tester) | Search-result summary |
| Pittsburgh in-line spark checker 63590 (Harbor Freight) | Neon in-line spark indicator; the one recommended in forum thread 14419 | US$4.99 | 2026-11-17 | [Harbor Freight](https://go.harborfreight.com/sku/63590) | Search-result summary |
| Other in-line spark testers (US) | Same function | Performance Tool W86554 US$6.29 (Zoro), US$8.19 (Lordco, currency as listed); Lisle 20580 US$26.73; Oregon 42-031 US$28.59 | 2026-11-17 | [Zoro](https://zoro.com/performance-tool-inline-ignition-spark-tester-w86554-w86554/i/G2038160), [Eppy's](https://www.eppys.com/product/noid-light-test-kits/in-line-spark-tester-with-coil-on-plkug-wire) | Search-result summary |
| In-line spark testers (Australia) | Same function | SP Tools SP61030 A$14.95 inc. GST (A$15.00 maker); AP Tools DA1280 A$15.95; Kincrome adjustable A$22.72; Toledo A$24.27 / 26.99 / 28.49; Lisle 20610 A$51.50 | 2026-11-17 | [SP Tools](https://www.sptools.com/inline-ignition-spark-tester.html), [GSS](https://www.gssautoparts.com.au/DA1280), [Kincrome](https://www.australianonlinecarparts.com.au/adjust-ignition-spark-teste), [Super Cheap Auto](https://www.supercheapauto.com.au/p/toledo-toledo-spark-plug-lead-tester/SPO81646.html), [Discount Trader](https://www.discounttrader.com.au/product/lisle-inline-spark-tester-20610) | Search-result summary |
| Schumacher BT-100 battery load tester | Battery volts under load (retailers disagree whether load is 100 A or 50 A) | US$43.20–44.49; US$54.99–64.99 elsewhere; US$78.99 MSRP | 2026-11-17 | [Zoro](https://www.zoro.com/schumacher-electric-battery-load-tester-analog-100-a-bt-100/i/G722885791/) | Search-result summary |
| RMSTATOR RM10001 DVA adapter | Peak-voltage reading for stator/pickup/CDI while cranking | US$65.32; A$125.99 (currency presumed AUD); NZ$159.99 | 2026-11-17 | [Motomentum](https://motomentum.com/products/rmstator-voltage-peak-reading-adapter-dva-adapter-mpn-rm10001), [Star Cycle Gear](https://starcyclegear.com.au/products/rms10001) | Search-result summary |
| Electronic Specialties 640 DVA adaptor | Same | US$123.33 (list US$137) | 2026-11-17 | [Toolsource](https://www.toolsource.com/leads-and-probes-c-1321_408_511/electronic-specialties-640-dva-adaptor-p-97246.html) | Search-result summary |
| TecMate IgnitionMate TS-91 / Duo | Powersports peak-voltage ignition tester | US$371.25–481.73; A$1,092.91 / 1,367.95 (presumed AUD); EU MSRP €429.37 | 2026-11-17 | [Toolsource](https://www.toolsource.com/motorcycle-ignition-tools-c-468_872/tecmate-ts91-ignitionmate-peakvoltage-ignition-tester-p-102757.html), [Star Cycle Gear](https://starcyclegear.com.au/products/tecmate-ignitionmate-diagnostic-tool-includes-tm-99) | Search-result summary |
| Basic digital multimeter | Volts under crank, continuity | US$15–25 | 2021-09 | Forum thread 7929 (no URL recorded) | Forum post read directly |
| Parts people swap instead | IAME X30 2021 harness kit US$168.26 / purple-pigtail kit US$190.00; KA100 coil US$106.99–117.70; KA100 stator US$120–199.12; KA100 brush kit US$35.79; TaG battery 12 V 9 Ah US$54.00; Rotax EVO harness US$527.77 (a £95.33 ZipNorth listing conflicts, possibly a sub-loom; forum 2020 "$150ish"); Rotax pre-EVO harness US$178–229.49; Rotax EVO ECU US$179–376.74 | As listed | 2026-11-17 | [Comet harness](https://cometkartsales.com/products/ife-05004-new-2021-x30-wiring-harness-kit), [Point Karting KA100 coil](https://pointkarting.com/products/ka100-ignition-coil), [Point Karting brushes](https://pointkarting.com/products/ka-100-starter-brush-kit), [Comet battery](https://cometkartsales.com/collections/electrical), [Point Karting Rotax harness](https://pointkarting.com/products/rotax-evo-wiring-harness-assembly) | Search-result summary |

No IAME-, Selettra- or PVL-branded tester and no loom tester for KA100/X30/ROK was found; Australian kart-shop prices were not found in four searches. Forum-stated swap costs: plug cap US$4 vs coil US$100 (2022-11); brush kit US$15–20 (2021-11); Leopard ignition box US$200 (2021-11); full gen-2 Rotax conversion about US$500 (2020-08).

**Does a cheap satisfactory alternative already exist?** Yes, for the faults that actually occur. A US$5–30 in-line spark checker (A$15–29 locally) plus a US$15–25 multimeter read while someone presses start covers battery sag, loom/relay/switch drop, "is 12 V reaching the starter" and "is there spark", which is every electrical case in the tally where a pit tester could have helped, except possibly B6/C6 and unresolved no-spark cases. A US$43–55 load tester removes the need to interpret a voltmeter; for stator/CDI, a DVA adapter (US$65) or the PET-4000 (about US$71) is the existing tool. What alternatives lack is packaging and a plain-language verdict, which is also where a wrong verdict becomes SkidLabz's support problem; the people who skipped the meter show a behaviour gap, not a tool gap.

**Why prices are what they are / where a saving could come from:** Spark checkers and meters are commodity items, and the PET-4000 and a load tester set a price ceiling of about US$60–100; swapping a spare battery, brush kit or harness (US$54 / US$36 / US$168–190) is the other benchmark. The electronics are trivial in cost; connectors, hand-built cable labour and enclosure dominate, and none of the connector figures is a quotation for a part known to fit. A clip-lead design avoids the loom problem but is then functionally a voltmeter plus a spark checker.

**Cost inputs (about 25 units, with basis)**

| Item | Figure | Basis label | Source / part number |
|---|---|---|---|
| MCU CH32V003F4P6 / STM32G030F6P6TR | US$0.305 (1+) / US$1.268 (10+); at 100: US$0.237 / US$0.963 | Current supplier price (JLCPCB/LCSC, 2026-11-17, ex fees/freight/GST) | C5187096 / C529330 |
| Optocoupler ×2, comparator, TVS ×2, 5 V LDO | US$0.046 each, US$0.061, US$0.054 each, US$0.130 | Current supplier price | C2912100, C7955, C78413, C16106 |
| Indicator LEDs ×8 | US$0.008 each; daylight-visible LEDs add an estimated US$0.50–1.00 per unit | Current supplier price; engineering estimate | C2286 |
| Small display | Estimated US$1.5–3; not priced (only a zero-stock placeholder) | Unresolved assumption | — |
| Passives, PCB (50 × 80 mm), assembly and set-up fees | US$0.60; US$0.80–1.50; US$1.50–2.50 | Engineering estimate (PCB fee structure not re-read) | — |
| Electronics subtotal | About US$4–8 at 25 (US$3–6 at 100) | Sum of the above | — |
| Illustrative Superseal 2-way housings; Deutsch DT04-2P | US$0.29 / US$0.35 (30+); US$0.64 (30+) | Current supplier price; relevance to any kart loom unresolved | C187804, C86482; C138527 |
| Pass-through tap per 2-way joint | US$0.9–1.2 (Superseal) or US$1.6–2.0 (DT) | Engineering estimate; unresolved if the real plug is proprietary | — |
| IAME adapter leads as fallback source of mating halves | US$15.52 (IAE-06100) / US$33.92 (IFE-05401D) | Published retailer price (search-result summary) | [Comet](https://cometkartsales.com/IAME-KA100-Ignition-and-Electrical-Parts/) |
| Cable and clips / enclosure / label and packaging / freight share | US$3–6 / US$2–5 / US$1.5–3 / US$2–3 | Engineering estimate | — |
| Parts total, clip-lead LED version | About US$14–24 (A$20–35) at 25; US$10–18 at 100 | Engineering estimate (mostly) | — |
| Parts total, inline version, one family's connectors | About US$22–40 (A$32–58) at 25; US$17–32 at 100 | Engineering estimate; connector cost unresolved | — |
| Per-unit labour | Clip-lead 20–30 min (A$50–75); inline 45–75 min (A$110–190); electronics programming/test 5–10 min | Engineering estimate; cable-house quotation not obtained | — |
| Support per unit sold | 0.25–0.5 h in year one (A$38–75), inline version | Engineering estimate | — |
| One-time owner hours, one family | 115–215 h (A$17,250–32,250 at A$150/h): loom reverse-engineering 15–30, PCB 20–35, firmware 25–50, cable design 10–20, enclosure 10–20, documentation 15–30, validation 20–30 | Engineering estimate | — |
| Each additional family or loom generation | 45–90 h (A$6,750–13,500) | Engineering estimate | — |
| Sample hardware to buy | 2021-style X30 set US$708.51 (about A$1,027); KA100 set plus Rotax EVO set add about US$400–600 and US$980–1,230; budget A$1,500–3,000 per two families | Published retailer price sum (search-result summary); budget is an engineering estimate | — |
| Illustrative revenue | At US$79 ex tax: 25 units A$2,860; 100 units A$11,450; 300 units A$34,350 against about A$85–250 unit cost including labour | Engineering estimate (not a forecast) | — |

Working rate A$1 ≈ US$0.69.

**What must be demonstrated before claiming equivalent useful performance:**
- Measured, not assumed: real no-start cases at a kart track resolved faster than with a voltmeter and a US$5 spark checker in a non-technical parent's hands.
- That one or two lead sets cover most engines in the paddock (count harness generations at two or three Australian club days).
- The connector families and a small-quantity source for mating halves.
- Known-good versus known-bad signal data for at least one stator/coil generation separating them at cranking speed (resistance cannot).
- That a pit-only tester is acceptable to scrutineers and never stays on the kart.
- That buyers pay above the PET-4000 / load-tester band, and through which channel.
- That a cable-assembly supplier can build lead sets at a margin.

**Register relationship:** This is a narrower, materially different version of RD-029 (Pro-Mag / race-ignition diagnostic tools, deprioritised) joined to RD-083 (basic battery tester, unadopted suggestion). RD-029's recorded rationale (from a recovered assistant recap, owner wording not recovered) is limited Australian equipment access and a tiny local sprint-car magneto market; equipment access applies in full (SkidLabz has no kart engines, looms or faulty reference parts), and the market reason applies in weaker form (X30, KA3/KA4 and Rotax are mainstream classes, but only entry counts were found and no purchase intent). RD-083's weak-differentiation reason applies in full to the cranking-voltage function. RD-041 is a similar pattern; RD-030 and RD-095 are not applicable; no DEC- record specific to these ideas was found. The reopening condition for RD-029 (a credible market and practical access to representative ignition systems) is not met, and no register status is changed.

**Red-team: reasons to reject, cheapest validation step, kill criteria:**
- The measured problem is mostly not the one the product solves: of 33 identified causes, 12 were fuel or mechanical and 17 starting-circuit faults a voltmeter, load tester or jumper already isolates; the distinctive function mattered in about 2.
- Engine-specific looms multiply variants and support under a low price ceiling (six or more lead sets, hand-built cables A$110–190 labour each, Rotax's own harness tester at US$441 as a volume signal).
- No access and no trustworthy verdict: no engines or faulty reference parts, no published good/bad values, hot or on-track faults a pit tester cannot see, and class rules that forbid leaving anything in the loom (search summaries).
- Cheapest step: one or two Australian club race days with a multimeter, an A$15 spark checker and a notebook, by arrangement with a kart shop or engine builder, logging each no-start (engine, loom generation, cause, minutes, tool); about 8–16 owner hours (A$1,200–2,400) and under A$50 of tools. Near-zero alternative: ask two Australian kart shops about PET-4000 demand.
- Kill if: the trackside log repeats the forum tally; fewer than about a quarter of cases need pulse or kill-line indication; more than two lead sets are needed for about 70% of karts or mating connectors are not purchasable in small quantities; shops already hold the tools and nobody volunteers above about A$100; or no shop will lend engines and known-bad parts. The first three are already met or likely.
- A universal clip-lead start-circuit checker would avoid the loom problem but competes with A$15–65 commodity items (RD-083's finding) and needs a reason to buy that was not found.

**Lookups not performed / unknowns:**
- Australian kart-shop prices for harness, coil, stator, relay and battery (four searches, US/EU only); PET-4000 stock at Australian shops.
- Connector families and part numbers for IAME (Selettra) and Rotax EVO plugs (two searches); IAME KA100 complete harness price.
- Briggs & Stratton 19368, Lisle 50850, Oregon 42-078, Stens 750-082 prices (nothing usable); small-battery testers and Australian load-tester prices (not searched).
- Current Karting Australia class-rule wording and full 2026 Rotax regulations (snippets only); class participation limited to entry lists, no market size claimed.
- Vortex ROK loom details and prices; PVL, TKART and manufacturer manuals (located, not readable).
- No cable-assembly, enclosure or PCB quotation; images, videos and attachments not opened; KartPulse skews to US club racing; topic 12322 fetched but not read; 20 of 53 cases unresolved. A search session limit interrupted work once; 32 searches completed.

### A — Torsion-bar consistency checker kit: coordinator's price checks and estimate inputs

This candidate was **not** given an independent validation. The forum evidence is in the HoseHeads ledger (HH-02 to HH-09, HH-21, HH-31). The items below are the coordinator's own checks and estimate inputs.

**Competing products and prices**

| Product | What it does | Price as found | Date | Source | Evidence type |
|---|---|---|---|---|---|
| Intercomp 100451 torsion bar tester, digital, 48" | Purpose-built bench tester | US$3,540.99; shown "Not Available" | 2026-11-17 | [Summit Racing](https://www.summitracing.com/parts/ICP-100451) | Search-result summary, not directly read page |
| Intercomp purpose-built tester | Same class | "three grand" | 2009 post | HH-21 | Search-engine summary of a forum post |
| AccuForce torsion bar dyno | Touch screen, stores 199 bars, rate every quarter inch | "mid $5000.00 range" | 2011-01-23 post | HH-02 | Forum post read directly; promotional |
| Roehrig, Maxwell testers | Dyno-class | "thousands of dollars" | 2009 post | HH-21 | Search-engine summary of a forum post |
| DIY load cell and degree wheel | Comparative check | About US$100 in parts (poster's estimate) | 2009 post | HH-21 | Search-engine summary of a forum post |
| Maxim X-Check | Checker or rater; nature and price unknown | Not found in two searches | 2026-11-17 | — | No result |
| Intercomp 100059 coil spring tester | Different product, shown for scale | About US$1,295 | 2026-11-17 | [Speedway Motors](https://www.speedwaymotors.com/Intercomp-100059-Digital-Coil-Spring-Tester,238.html) | Search-result summary |
| New 30" sprint-car torsion bars | Reference bars for check standards | US$178.99–185.99 each; NZ$358.30 before GST | 2026-11-17 | [90 Racing](https://90racing.com/products/mpd-racing-301025), [Pit Stop USA](https://pitstopusa.com/c-1213536.html), [Fast Lane Spares](https://fastlanespares.co.nz/products/strange-sprint-car-torsion-bar) | Search-result summary |

**Cost inputs (about 25 units, with basis)**

| Item | Figure | Basis label | Source / part number |
|---|---|---|---|
| Bridge ADC CS1237; MCU STM32G030; 0.96" OLED | US$0.46 at 30; US$1.09 at 30; US$1.74 at 30 | Current supplier price (JLCPCB, 2026-11-17) | Carried from validation V3 |
| Assembled display-unit board | A$16–25 | Engineering estimate built on the prices above | Same basis as V3's electronics subtotal |
| Angle sensor, consumer IMU LSM6DSOTR | US$3.99 / 3.45 / 2.89 / 2.56 at 1 / 10 / 30 / 100; stock 23,415 | Current supplier price (JLCPCB, 2026-11-17) | [C2655100](https://jlcpcb.com/partdetail/C2655100) |
| Angle sensor, inclinometer IIS2ICLXTR | US$20.61 at 1; US$18.64 at 30; stock 280 | Current supplier price (JLCPCB, 2026-11-17) | [C1857737](https://jlcpcb.com/partdetail/C1857737) |
| Angle sensor, inclinometer SCL3300-D01-10 | US$27.90 at 1; US$26.57 at 30; stock 575 | Current supplier price (JLCPCB, 2026-11-17) | [C3825395](https://jlcpcb.com/partdetail/C3825395) |
| Angle pod electronics, assembled | A$10–45 | Engineering estimate | Depends on sensor choice above |
| Load cell, S-type 500 kg | US$50.00 list | Published price (search-result summary) | Carried from V3 ([Robotshop listing](https://www.robotshop.com/products/phidgets-steel-s-type-load-cell-500kg-c3)) |
| Load cell direct from a maker | US$25–60 | Unresolved assumption | No quotation |
| Enclosures and pod housing; saddle adapters; cables and connectors; case, batteries, labels, manual | A$25–60; A$20–50; A$15–35; A$15–35 | Engineering estimate | No drawing or quotation |
| Inbound freight; yield; packaging; selling fees; warranty | 8–15 %; 3–8 %; A$5–10; 3–6 %; 2–5 % | Engineering estimate | — |
| Selling price | A$580–1,015 (US$400–700) | Unresolved assumption | No buyer evidence at any price |
| Per-unit owner time | Build, check and pack 55–100 min; support 20–45 min | Engineering estimate | — |
| One-time owner hours | 190–400 h: electronics 30–50, firmware 50–100, fixture and procedure 40–90, validation 50–120, documentation 20–40 | Engineering estimate | — |
| One-time cash | A$2,320–6,200: prototypes A$800–2,000; test weights and angle reference A$300–800; reference bars and their commercial rating A$720–1,900; development fixture A$500–1,500 | Engineering estimate; rating fee unresolved | — |

**What must be demonstrated before any claim is made**

- The same bar reads within about 1–2 % across repeated removal and refitting, in the car and on a simple stand.
- Friction in the bushings is cancelled by an up-and-down sweep, and arm flex and off-axis loading on the load cell are controlled or corrected.
- Readings agree with at least two bars rated on a commercial tester, or the product is described strictly as a comparator.
- Racers accept a comparative result, and know what to do when a reading disagrees with the stamped rate.
- No fatigue or remaining-life claim is made from rate alone (existing RD-017 boundary).

**Lookups not performed / unknowns**

- Whether the Maxim X-Check, the small-run "DNK" tester, AccuForce or Maxwell units are sold today, and at what price.
- Whether the Intercomp 100451 is discontinued or only out of stock at one retailer.
- Whether an Australian shop will rate bars on a commercial tester, and the fee.
- Bar sizes and spline standards across sprint, midget, micro and wingless classes.
- Any current discussion outside HoseHeads; nothing after 2023 was found there.

### Other price checks made by the coordinator

| Subject | Finding | Date | Source | Evidence type |
|---|---|---|---|---|
| Four-channel thermocouple SD loggers (alternative to a purpose-built brake-temperature logger) | Triplett TMDL400 US$271.09–325.99; Extech SDL200 US$399.00; an Omega four-channel unit is at end of life with a 1 s minimum interval | 2026-11-17 | [Global Test Supply](https://www.globaltestsupply.com/product/triplett-tmdl400-wall-mount-thermocouple-data-logger-sd), [Zoro](https://www.zoro.com/triplett-4-channel-type-k-temperature-datalogger-tmdl400/i/G710934562), [TestEquity](https://www.testequity.com/category/Data-Acquisition-and-Meters/Environmental-And-Temperature-Testers/Digital-Thermometers/19392-2-SDL200) | Search-result summary |
| Replacement readouts for Longacre or Intercomp scale pads | No brand-specific replacement found; generic single-channel industrial indicators US$99–385 and a summing junction box US$75 | 2026-11-17 | [eBay store](https://ebay.com/str/theloadcelldepot/category-1/_i.html), [Uline](https://www.uline.com/Product/Detail/H-4593-DIB/Platform-Scales/Display-Indicator-for-Industrial-Platform-Scale) | Search-result summary; absence is not proof |
| Kart fuel tester supply (Digatron DT-47FT, former DT-15) | Manuals found; nothing on current sales status, stock or a successor | 2026-11-17 | [DT-47FT manual](https://manuals.online/digatron/test-equipment/dt-47ft/user-manual/1bxu4) | Search-result summary |
| Valve-spring tester prices, first pass | Intercomp adjustable on-engine tester US$799.00; Proform 66842 US$196.99; Proform 66776 from US$635.99 | 2026-11-17 | [JEGS](https://www.jegs.com/i/proform-778-66842-digital-valve-spring-tester-with-micrometer-0-01-in-increments-backlit-display), [J&J Motorsports](https://jj-motorsports.com/circle-track/tools/engine-related/valve-spring-testers) | Search-result summary; superseded by V3 |

## 5. Links to matching R&D ideas and decisions

Recorded statuses are quoted as they stand in the register on 17 November 2026. None is changed by this research.

### Findings with an existing record

| Finding | Record | Class | Recorded status | Does the evidence address the recorded reason or blocker? |
|---|---|---|---|---|
| Low-pressure gauge trust | [RD-003](../../ideas/tyre-gauge.md); DEC-011, DEC-012, DEC-013, DEC-040 | 2 | Investigation / samples | No for DEC-011, DEC-012 and DEC-040. Supports DEC-013: the gauges with memory and app features are the ones with reported data-loss faults. |
| Tyre-gauge checker | [RD-092](../../ideas/gauge-calibrator.md) | 3 | Unadopted suggestion | No. Its condition is a user-selected requirement and a worthwhile advantage; nobody asked for a checker. |
| Torsion-bar consistency checker | [RD-017](../../ideas/torsion-bar-tester.md) | 2 and 3 | Paused — validation | Partly, in principle only: users frame the need as comparison, and force and angle can each be checked from first principles. Not demonstrated. |
| Electronic tyre bleeders | [RD-016](../../ideas/electronic-bleeders.md); DEC-036 to DEC-039 | 2 | Paused — feasibility | No. Maintenance complaints about mechanical bleeders are consistent with DEC-037. Adds a patent point to check in the source project. |
| Engine-protection warning module | [RD-089](../../ideas/warning-module.md), [RD-090](../../ideas/compact-engine-monitor.md); [RD-032](../../ideas/engine-guard.md); DEC-019 | 2 | Unadopted suggestions; RD-032 dropped | No. RD-032's reason is not recorded in detail; the "engine protection" framing runs against DEC-019. |
| Load-cell valve-spring force tester | [RD-020](../../ideas/valve-spring-checker.md) | 4 (3 as a bench reference) | Rejected — commercial | No. "Many alternatives exist" is strengthened; expected sales remain unevidenced. The record already notes a basic load-cell-and-display comparison. |
| Kart ignition and start-circuit tester | [RD-029](../../ideas/race-ignition-diagnostics.md), [RD-083](../../ideas/battery-tester.md) | 3 | Deprioritised; unadopted suggestion | The recorded reasons apply: no access to representative equipment, weak differentiation. "Tiny market" applies less, but no purchase intent was found. |
| Phone-free kart dash | [RD-095](../../ideas/kart-instrument.md), [RD-094](../../ideas/gps-lap-timer.md); [RD-015](../../ideas/digital-race-dash.md), DEC-044 | 2 | Unadopted suggestions; RD-015 paused — sourcing | No. It meets the same display-sourcing blocker. |
| Readout for existing scale pads | [RD-049](../../ideas/scale-reader.md) | 2 | Earlier scope rejected; later scope unapproved | Partly: shows a US installed base with failing electronics. Does not establish compatible pads, a calibration method or volume. |
| Complete corner scales | [RD-018](../../ideas/race-scales.md) | 4 | Rejected — commercial | No. Cheap new sets, a used market and occasional use reinforce it. |
| Brake-pad temperature logger | [RD-086](../../ideas/temperature-recorder.md), [RD-025](../../ideas/egt-monitor.md), [RD-071](../../ideas/surface-temperature.md) | 3 | Unadopted suggestions; research only | No blocker recorded. Demand is not shown: one maker. |
| Tyre temperature, kart TPMS | [RD-046](../../ideas/tyre-temperature.md) | 2 | Earlier scope rejected; later scope unapproved | The need is voiced by kart and circuit users; the "specific capture advantage" is not shown. |
| One-way receivers in karting | [RD-002](../../ideas/receiver.md) | 2 | Active development | Market note only. |
| Memory tach as the gearing tool; Tel-Tac pricing | [RD-001](../../ideas/revmax.md) | 2 | Active development | Consistent with the product premise; no feature request. |
| Knock monitoring on loud engines | [RD-012](../../ideas/knock-meter.md); DEC-019 | 2 | Parked — priority | Adds a technical caution about block sensors with solid-roller valvetrains. |
| Budget PDMs | [RD-011](../../ideas/pdm.md) | 2 | Parked — priority / go-no-go | Competition has grown; nothing else changes. |
| Cam-profile measuring | [RD-026](../../ideas/cam-angle-tool.md); distinct from [RD-036](../../ideas/cam-legality.md) | 2 / 3 | Research only | Buyers are builders, not officials; no volume evidence. |
| Distributor machines, advance logging | [RD-041](../../ideas/distributor-tester.md) | 2 / 3 | Research only | Shows the niche exists; does not answer the doubt about reachable demand. |
| Mechanical-injection checks | [RD-028](../../ideas/mfi-service-tester.md) | 2 tending to 5 | Deprioritised | Weakly: US questions, not purchases. Nothing on equipment access. |
| Magneto timing box | [RD-030](../../ideas/magneto-timer.md) | 5 | Deprioritised | No. |
| Toe, alignment, squaring | [RD-043](../../ideas/toe-tool.md), [RD-042](../../ideas/chassis-alignment.md), [RD-061](../../ideas/angle-meter.md) | 4 / 5 | Parked | No repeatability or usability advantage over the simple method was shown. |
| Brake-pressure gauges | [RD-047](../../ideas/brake-pressure-tester.md) | 4 | Earlier scope rejected; later scope unapproved | Leans against. |
| Fuel-used display; fuel dipstick | [RD-048](../../ideas/fuel-used-display.md) | Negative; 5 | Research only | No request found; an electronic dipstick product was praised. |
| Crew timing, transponders, club timing | [RD-051](../../ideas/crew-timing-display.md), [RD-115](../../ideas/timing-network.md) | 4 | Rejected; advised against | Reinforced: a phone app already gives crews lap times. |
| Loggers and channel expansion | [RD-004](../../ideas/racelogger.md), [RD-019](../../ideas/wideband-logger.md), [RD-087](../../ideas/general-data-recorder.md), [RD-072](../../ideas/sensor-hub.md) | 2 to 5 | Internal tool; paused — scope; unadopted | No "one function only" request found; existing modules cover channel expansion. |
| Lap timers | [RD-094](../../ideas/gps-lap-timer.md), [RD-113](../../ideas/video-sync.md) | 5 | Unadopted suggestions | Well served. |
| Fuel-legality tester | [RD-035](../../ideas/fuel-legality.md) | 4 | Rejected — commercial | Not addressed. A possible shortage of the incumbent meter is unconfirmed. |
| Jet measuring; leak-down; weather meter; battery tester | [RD-039](../../ideas/jet-comparator.md), [RD-099](../../ideas/leakdown-tester.md), [RD-085](../../ideas/weather-meter.md), [RD-083](../../ideas/battery-tester.md) | 4 / 5 | Rejected; unadopted | No. |
| Blow-by; whistler and capacity; rod-bolt stretch; sonic; valve run-out; flow-bench electronics | [RD-037](../../ideas/blow-by-meter.md), [RD-033](../../ideas/whistler-compression.md), [RD-034](../../ideas/capacity-checker.md), [RD-021](../../ideas/rod-bolt-stretch.md), [RD-024](../../ideas/sonic-thickness.md), [RD-040](../../ideas/valve-runout.md), [RD-023](../../ideas/flow-bench-processor.md) | 4 / 5 | Rejected or research only | No. |
| EGT; wideband and AFR | RD-025, [RD-082](../../ideas/portable-afr.md), [RD-084](../../ideas/basic-afr-gauge.md) | 5 | Research only; unadopted | No; one expert objection to EGT on constant-flow injection. |
| Shock and bar dyno testing | [RD-027](../../ideas/shock-dyno.md) | 5 | Parked | Bought as a service. |

### Findings with no register record

Recorded here so they are not rediscovered. None is proposed as a new record.

| Finding | Class | Note |
|---|---|---|
| Orphaned dyno electronics and software | 1; 5 for whole-system retrofit | Most repeated Speed-Talk complaint; poor fit for small-batch, low-support production. |
| Timing lights on CDI and multi-spark ignitions | 1 | Commodity category; no product request. |
| Kill switch that stops the engine without harming the alternator | 1, largely 5 | A wiring-knowledge problem; solid-state isolators exist. |
| Small-engine dyno electronics kit | 1 against the register; 5 in the market | A forum member already sells one in small batches. |
| Cool-suit controllers; budget race radios | 1 / 5 | DIY or existing vendors; not electronics-led. |
| Micro-sprint electric fuel pump running after a crash | 1, weak | One 2009 post, search-summary grade; generic cut-offs exist; safety-critical. |

## 6. Searches and sections that produced little useful evidence

Detail is in the "Low-yield searches and sections" list under each forum in section 3. Across the four forums:

- **Complaint phrases found little.** Searches for "too expensive", "overpriced", "nobody makes", "wish someone made" and "made my own" mostly returned off-topic posts on every forum. Searching by the job or the instrument, and screening titles, was far more productive.
- **HoseHeads site search is title-only.** "bleeder" matches 3 threads in about 60,760, "tester" 2 and "gauge" 4. Planned title searches for tach, scales, injection, magneto, fuel pressure, stagger, data, radio and others were not run because the reader was blocked.
- **HoseHeads current activity** is news, schedules and fan debate. Nothing technical from 2024–2026 was found.
- **Speed-Talk guest search** omits about mid-2009 to late 2019 and rejects short terms such as "DIY" and "EGT". Nothing was found on lifter bleed-down testers, pushrod-deflection tools, ring-tension gauges, oil-pump test stands, injector flow benches or carburettor float-level tools.
- **GRM** produced no request for a fuel-used display, a cool-suit controller or a brake-bias gauge, and only one clear case of a team reverting from a complicated solution to a simpler one (fuel injection back to a carburettor, September 2025).
- **KartPulse** produced no dedicated tester for kart electrics, no request for a gauge checker in five further searches, and nothing bearing on scale readouts.
- **Not found anywhere:** evidence of demand for torsion-bar or shock-dyno electronics outside HoseHeads; any stated purchase intent with a price attached, apart from one "I will buy one" about a hobbyist's kart logger.

## 7. Unknowns that materially affect the conclusions

1. **HoseHeads was barely read.** The torsion-bar and bleeder findings rest on two threads read in full plus index rows and search-engine summaries. Quotes, prices and who said what in the other threads need re-reading in a browser.
2. **GRM was not read at source.** Dates, reply counts and attribution are uncertain; some start dates are estimates.
3. **Whether a cheap torsion-bar tester is on sale today.** The Maxim X-Check, the small-run "DNK" unit, AccuForce and Maxwell were not found in two searches. The Intercomp tester is listed but shown unavailable at one retailer.
4. **Volume.** No forum gives an installed base or sales figure for anything. Recurrence of a question is not a count of buyers.
5. **Competitor prices are search summaries.** No manufacturer or retailer page was opened. Several listings may be stale or sale prices; conflicts are flagged where seen.
6. **Whether the existing digital spring testers are accurate.** Their sensing principle and accuracy were not established.
7. **Tax, duty and freight.** GST registration is assumed, not verified. US duty or tariff on Australian goods, and freight in either direction, were not researched.
8. **Australian compliance for 12 V accessories.** The applicable EMC standard and whether testing is needed are unresolved; the same question would apply to existing products.
9. **Accredited calibration fees** for a master pressure gauge or a reference load cell were not found.
10. **Australian relevance.** Posters are overwhelmingly from the US. Australian class rules on bleeders, data acquisition and one-way receivers were not examined.
11. **Where current discussion happens.** Private groups and social media were outside scope; current sprint-car technical talk has probably moved there (an inference, not checked).
12. **The reason RD-032 was dropped** is not recorded in detail, so it cannot be tested against new evidence.
13. **Patent position on electronic bleeders.** Reported from a web-search summary only; not verified and not legal advice.
14. **Kart fuel-tester supply.** One wanted post suggests scarcity; one search found no statement either way.

## 8. Names not yet in the competitor lists

Names met in this research that a search of the two competitor lists did not find. They are listed for later upkeep; no competitor record was added, and inclusion here classifies no business.

- **From HoseHeads:** AccuForce, Maxwell Industries, Maxim X-Check, the "DNK" tester, Quick Racing Products, OC Shocks, Competition Suspension Inc., Tru-Square, Safety First USA / Xtreme Fuel Stick, Westhold, King Racing Products, Total Seal, Good Vibrations Motorsports, TI22, Hot Shot, Big Toob.
- **From Speed-Talk:** Audie, Buxton, Rimac, LSM, SuperFlow, YourDyno, DEPAC, Land & Sea, J&S, Turner, Andrews, MJP, Paramount, Mityvac, Goodson.
- **From the validations:** FSR Racing, Dill, Haltec, Keller, SPA Design / Racetech, Scintex, Engine Watchdog, Oppama. Further names are in the tables in section 4.
- **From GRM and KartPulse:** see the "Products and prices named" list under each forum in section 3.

## 9. Economics model output

Inputs are ranges. "Best" pairs low costs with the high price; "worst" the reverse; "mid" uses midpoints. Owner labour is A$150/hour. All figures are A$ excluding GST. Inputs for V1–V4 are the validators' estimates from section 4; inputs for item A are the coordinator's estimates from section 4. These are estimates, not quotations, and the units-per-year columns are scenarios, not forecasts.

### A. Torsion-bar rate comparator kit (narrower RD-017) — coordinator's engineering estimate

| Per unit (A$, ex-GST) | Best case | Mid | Worst case |
|---|---:|---:|---:|
| Selling price | 1,015 | 798 | 580 |
| Materials (parts, PCBA, mechanical, cable) | 137 | 237 | 337 |
| Inbound freight / purchasing overhead | 11 | 27 | 51 |
| Yield / rework allowance | 4 | 15 | 31 |
| Packaging | 5 | 8 | 10 |
| Selling / payment fees | 30 | 36 | 35 |
| Warranty allowance | 20 | 28 | 29 |
| **Cash cost per unit** | 208 | 350 | 492 |
| **Cash contribution per unit** | 807 | 447 | 88 |
| Owner labour per unit (build + support) @ A$150/h | 188 | 275 | 363 |
| **Contribution after owner labour** | 619 | 172 | -275 |
| Owner time per unit (hours: build + support) | 1.25 | 1.83 | 2.42 |

| One-time (A$) | Best case | Mid | Worst case |
|---|---:|---:|---:|
| Owner development hours | 190 | 295 | 400 |
| Owner time @ A$150/h | 28,500 | 44,250 | 60,000 |
| Cash: prototypes, fixtures, reference equipment, compliance | 2,320 | 4,260 | 6,200 |
| **Total one-time incl. owner time** | 30,820 | 48,510 | 66,200 |

| Break-even units | Best case | Mid | Worst case |
|---|---:|---:|---:|
| Cash outlay only ÷ cash contribution | 3 | 10 | 71 |
| All one-time incl. owner time ÷ contribution after owner labour | 50 | 281 | never |

| Annual result at mid-case (A$) | 10 units/yr | 25 units/yr | 50 units/yr |
|---|---:|---:|---:|
| Cash contribution | 4,474 | 11,185 | 22,371 |
| Contribution after owner labour | 1,724 | 4,310 | 8,621 |
| Owner hours consumed (build + support) | 18 | 46 | 92 |
| Years to recover all one-time incl. owner time (mid) | 28.1 | 11.3 | 5.6 |
| Years to recover all one-time incl. owner time (worst) | never | never | never |

### V1. Engine-protection warning kit, generic senders (validator's estimates)

| Per unit (A$, ex-GST) | Best case | Mid | Worst case |
|---|---:|---:|---:|
| Selling price | 361 | 288 | 216 |
| Materials (parts, PCBA, mechanical, cable) | 78 | 113 | 148 |
| Inbound freight / purchasing overhead | 6 | 13 | 22 |
| Yield / rework allowance | 3 | 7 | 14 |
| Packaging | 0 | 0 | 0 |
| Selling / payment fees | 11 | 13 | 13 |
| Warranty allowance | 7 | 10 | 11 |
| **Cash cost per unit** | 105 | 156 | 208 |
| **Cash contribution per unit** | 256 | 132 | 8 |
| Owner labour per unit (build + support) @ A$150/h | 112 | 156 | 200 |
| **Contribution after owner labour** | 144 | -24 | -192 |
| Owner time per unit (hours: build + support) | 0.75 | 1.04 | 1.33 |

| One-time (A$) | Best case | Mid | Worst case |
|---|---:|---:|---:|
| Owner development hours | 210 | 325 | 440 |
| Owner time @ A$150/h | 31,500 | 48,750 | 66,000 |
| Cash: prototypes, fixtures, reference equipment, compliance | 3,000 | 8,500 | 14,000 |
| **Total one-time incl. owner time** | 34,500 | 57,250 | 80,000 |

| Break-even units | Best case | Mid | Worst case |
|---|---:|---:|---:|
| Cash outlay only ÷ cash contribution | 12 | 64 | 1,662 |
| All one-time incl. owner time ÷ contribution after owner labour | 240 | never | never |

| Annual result at mid-case (A$) | 10 units/yr | 25 units/yr | 50 units/yr |
|---|---:|---:|---:|
| Cash contribution | 1,325 | 3,312 | 6,625 |
| Contribution after owner labour | -238 | -594 | -1,188 |
| Owner hours consumed (build + support) | 10 | 26 | 52 |
| Years to recover all one-time incl. owner time (mid) | never | never | never |
| Years to recover all one-time incl. owner time (worst) | never | never | never |

### V2. Tyre-gauge checker / reference station (validator's estimates)

| Per unit (A$, ex-GST) | Best case | Mid | Worst case |
|---|---:|---:|---:|
| Selling price | 650 | 550 | 450 |
| Materials (parts, PCBA, mechanical, cable) | 84 | 156 | 228 |
| Inbound freight / purchasing overhead | 7 | 18 | 34 |
| Yield / rework allowance | 3 | 10 | 21 |
| Packaging | 5 | 8 | 10 |
| Selling / payment fees | 20 | 25 | 27 |
| Warranty allowance | 13 | 19 | 22 |
| **Cash cost per unit** | 131 | 235 | 343 |
| **Cash contribution per unit** | 519 | 315 | 107 |
| Owner labour per unit (build + support) @ A$150/h | 275 | 359 | 442 |
| **Contribution after owner labour** | 244 | -44 | -335 |
| Owner time per unit (hours: build + support) | 1.83 | 2.39 | 2.95 |

| One-time (A$) | Best case | Mid | Worst case |
|---|---:|---:|---:|
| Owner development hours | 130 | 172 | 215 |
| Owner time @ A$150/h | 19,500 | 25,875 | 32,250 |
| Cash: prototypes, fixtures, reference equipment, compliance | 2,220 | 3,330 | 4,440 |
| **Total one-time incl. owner time** | 21,720 | 29,205 | 36,690 |

| Break-even units | Best case | Mid | Worst case |
|---|---:|---:|---:|
| Cash outlay only ÷ cash contribution | 4 | 11 | 41 |
| All one-time incl. owner time ÷ contribution after owner labour | 89 | never | never |

| Annual result at mid-case (A$) | 10 units/yr | 25 units/yr | 50 units/yr |
|---|---:|---:|---:|
| Cash contribution | 3,150 | 7,875 | 15,750 |
| Contribution after owner labour | -438 | -1,094 | -2,188 |
| Owner hours consumed (build + support) | 24 | 60 | 120 |
| Years to recover all one-time incl. owner time (mid) | never | never | never |
| Years to recover all one-time incl. owner time (worst) | never | never | never |

### V3. Load-cell valve-spring force puck (validator's estimates)

| Per unit (A$, ex-GST) | Best case | Mid | Worst case |
|---|---:|---:|---:|
| Selling price | 433 | 360 | 288 |
| Materials (parts, PCBA, mechanical, cable) | 175 | 260 | 345 |
| Inbound freight / purchasing overhead | 0 | 0 | 0 |
| Yield / rework allowance | 0 | 0 | 0 |
| Packaging | 0 | 0 | 0 |
| Selling / payment fees | 13 | 16 | 17 |
| Warranty allowance | 9 | 13 | 14 |
| **Cash cost per unit** | 197 | 289 | 377 |
| **Cash contribution per unit** | 236 | 72 | -89 |
| Owner labour per unit (build + support) @ A$150/h | 150 | 210 | 270 |
| **Contribution after owner labour** | 86 | -138 | -359 |
| Owner time per unit (hours: build + support) | 1.00 | 1.40 | 1.80 |

| One-time (A$) | Best case | Mid | Worst case |
|---|---:|---:|---:|
| Owner development hours | 117 | 174 | 230 |
| Owner time @ A$150/h | 17,550 | 26,025 | 34,500 |
| Cash: prototypes, fixtures, reference equipment, compliance | 3,200 | 5,510 | 7,820 |
| **Total one-time incl. owner time** | 20,750 | 31,535 | 42,320 |

| Break-even units | Best case | Mid | Worst case |
|---|---:|---:|---:|
| Cash outlay only ÷ cash contribution | 14 | 77 | never |
| All one-time incl. owner time ÷ contribution after owner labour | 240 | never | never |

| Annual result at mid-case (A$) | 10 units/yr | 25 units/yr | 50 units/yr |
|---|---:|---:|---:|
| Cash contribution | 717 | 1,791 | 3,583 |
| Contribution after owner labour | -1,383 | -3,459 | -6,917 |
| Owner hours consumed (build + support) | 14 | 35 | 70 |
| Years to recover all one-time incl. owner time (mid) | never | never | never |
| Years to recover all one-time incl. owner time (worst) | never | never | never |

### V4. Kart ignition / start-circuit inline tester, one engine family (validator's estimates)

| Per unit (A$, ex-GST) | Best case | Mid | Worst case |
|---|---:|---:|---:|
| Selling price | 145 | 116 | 87 |
| Materials (parts, PCBA, mechanical, cable) | 32 | 45 | 58 |
| Inbound freight / purchasing overhead | 0 | 0 | 0 |
| Yield / rework allowance | 1 | 2 | 5 |
| Packaging | 0 | 0 | 0 |
| Selling / payment fees | 4 | 5 | 5 |
| Warranty allowance | 3 | 4 | 4 |
| **Cash cost per unit** | 40 | 57 | 72 |
| **Cash contribution per unit** | 105 | 59 | 15 |
| Owner labour per unit (build + support) @ A$150/h | 163 | 225 | 288 |
| **Contribution after owner labour** | -58 | -166 | -273 |
| Owner time per unit (hours: build + support) | 1.08 | 1.50 | 1.92 |

| One-time (A$) | Best case | Mid | Worst case |
|---|---:|---:|---:|
| Owner development hours | 115 | 165 | 215 |
| Owner time @ A$150/h | 17,250 | 24,750 | 32,250 |
| Cash: prototypes, fixtures, reference equipment, compliance | 1,500 | 2,250 | 3,000 |
| **Total one-time incl. owner time** | 18,750 | 27,000 | 35,250 |

| Break-even units | Best case | Mid | Worst case |
|---|---:|---:|---:|
| Cash outlay only ÷ cash contribution | 14 | 38 | 203 |
| All one-time incl. owner time ÷ contribution after owner labour | never | never | never |

| Annual result at mid-case (A$) | 10 units/yr | 25 units/yr | 50 units/yr |
|---|---:|---:|---:|
| Cash contribution | 592 | 1,481 | 2,962 |
| Contribution after owner labour | -1,658 | -4,144 | -8,288 |
| Owner hours consumed (build + support) | 15 | 38 | 75 |
| Years to recover all one-time incl. owner time (mid) | never | never | never |
| Years to recover all one-time incl. owner time (worst) | never | never | never |
