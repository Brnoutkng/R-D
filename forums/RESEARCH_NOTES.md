# What the technical discussions suggest

[Community directory](README.md) · [Existing ideas](../REGISTER.md) · [Decision history](../DECISIONS.md)

**Reviewed 17 November 2026 — Australia/Melbourne**

These are research questions drawn from sampled public discussions. They are not new approved products, a measure of demand or a reason to change an existing project status. The directory is intended to make the next investigation more efficient: start from a concrete job, recover independent examples, and check what we have already decided.

## Most useful problem themes

### 1. Simple engine-health logging without a full modern ECU package

An owner of a carburetted car asks for basic RPM and temperature logging in [this projectcar discussion](https://www.reddit.com/r/projectcar/comments/1qisg4j/data_logger_for_carby_car/). A track-day driver asks for temperature and pressure channels to diagnose an intermittent fault in [this CarTrackDays discussion](https://www.reddit.com/r/CarTrackDays/comments/1pt5hh2/any_good_reasonably_priced_data_logger/). These are different jobs from video coaching or comparing lap times.

**Question to investigate:** What is the minimum useful set of channels, and how much installation, sensor selection and log review will the user tolerate? Check what existing instruments already solve before proposing another logger.

**Existing R&D boundary:** [RaceLogger](../ideas/racelogger.md) is an active internal tool; commercial release is a separate decision. [Wideband logger](../ideas/wideband-logger.md) has unresolved commercial scope. These examples do not convert either into an approved new product.

### 2. Knowing that a recording actually exists

In [r/HPtuners](https://www.reddit.com/r/HPtuners/comments/1mt05yp/mpvi3_standalone_data_logging_issue/), users describe triggering standalone logging without receiving a saved file and reverting to a laptop. A later reply reports recovery after updates and reconfiguration, while other replies still describe difficulty. An [automotive ESP32 logger discussion](https://www.reddit.com/r/esp32/comments/1o2vzti/esp32_cyd_data_logging_in_a_car_handling_sudden/) raises power loss and SD corruption.

**Question to investigate:** Can the user distinguish ready, recording, saved and failed states, then recover the useful data after an interrupted session? This is a reliability and feedback problem; the threads do not establish a general vendor defect or failure rate.

**Existing R&D boundary:** Relevant to physical capture validation in [RaceLogger](../ideas/racelogger.md) and useful operation of [LogWorks](../ideas/logworks.md). A software demonstration is not evidence of reliable complete-system capture.

### 3. Tyre measurements that fit the time available

[Grassroots Motorsports](https://grassrootsmotorsports.com/forum/grm/how-do-you-record-your-track-day-data/262354/page1/) describes paper sheets, phone/laptop files and logging packages. [r/Autocross](https://www.reddit.com/r/Autocross/comments/1lpkd9h/) contains both interest in faster pressure capture and objections to another manual-entry app. [Bob’s 4 Cycle](https://4cycle.com/karting/threads/finding-your-setup-numbers.139420/) shows that interpreting measurements against changing conditions can be as difficult as collecting them.

**Question to investigate:** Which step is actually awkward—taking a reading, attaching it to the correct wheel/run, recording conditions, or deciding what to change? Preserve the negative evidence: paper and familiar tools may already be sufficient.

**Existing R&D boundary:** [Tyre gauge](../ideas/tyre-gauge.md) remains an investigation. [Tyre temperature](../ideas/tyre-temperature.md) has mixed scope, including a rejection of the initial dirt-market pyrometry case. Circuit/kart examples do not reverse that decision. [Generic setup app](../ideas/generic-setup-app.md), [digital stagger](../ideas/digital-stagger.md) and [race scales](../ideas/race-scales.md) retain their recorded rejections.

### 4. Integration and useful interpretation, not just more channels

[Track Mustangs Online](https://trackmustangsonline.com/threads/canbus-data.19972/) includes questions about what temperature channels actually represent. [Rennlist](https://rennlist.com/forums/data-acquisition-and-analysis-for-racing-and-de/1514859-methods-to-capture-canbus-some-options-i-ve-used-recently.html) describes a CAN-to-RaceChrono bridge. [MoTeC’s setup-sheet discussion](https://motec.zendesk.com/hc/en-gb/community/posts/16900949606159-Setup-sheet-without-excel) shows a desire to keep setup context near the analysis. [PCMHacking](https://pcmhacking.net/forums/) supplies a much more specific older-ECU integration context.

**Question to investigate:** Is the difficulty the physical interface, channel identity, configuration persistence, time alignment or knowing what the data means? Separate transferable usability issues from one vehicle’s CAN mapping. A better guide or adapter may solve the job without a whole new platform.

**Existing R&D boundary:** [RaceOS](../ideas/raceos.md), [RaceCal](../ideas/racecal.md) and [LogWorks](../ideas/logworks.md) are internal tools. Keep those purposes distinct from the rejected generic setup-app proposal and from any future commercial software decision.

### 5. Instrument installation, support and everyday use

[Bob’s MyChron setup question](https://4cycle.com/karting/threads/how-to-work-a-mychron5.124308/) is explicitly from a micro-sprint owner. [CKRC’s instrument thread](https://ckrc.com/forums/viewtopic.php?t=5323) describes a display problem while data still recorded. [r/Karting](https://www.reddit.com/r/Karting/comments/1tvvwtc/what_data_logging_devices_do_you_use/) discusses software usability and the value of using equipment other racers know. Comments disagree about then-current mobile support; no present feature limitation is established here.

**Question to investigate:** Would clearer pickup instructions, suitable mounting/accessories, simple configuration or better support remove the friction? The relevant problem may be around an existing instrument rather than a need to replace it.

**Existing R&D boundary:** [RevMax](../ideas/revmax.md) has its own active preproduction scope. [Kart instrument](../ideas/kart-instrument.md) and [GPS lap timer](../ideas/gps-lap-timer.md) remain historical unadopted suggestions. These discussions do not add features to RevMax or approve those suggestions.

### 6. Trustworthy workshop measurements and fixtures

The remembered HoseHeads discussions are [torsion bar tester, 11 April 2009](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/torsion-bar-tester-731127) and [Torsion bar tester, 21 January 2011](https://www.hoseheadforums.com/discussion/forum/hoseheads-sprint-car-general-forum-2/torsion-bar-tester-841457). They discuss test fixtures, measurement consistency and equipment identification. [HybridZ’s flow-bench discussion](https://forums.hybridz.org/topic/141283-nissan-l-series-cylinder-head-flow-bench-testing-and-development/) stresses method and calibration. [RX7Club’s compression-tester question](https://www.rx7club.com/general-rotary-tech-support-11/looking-trust-worthy-rotary-compression-tester-1165850/) shows uncertainty about trustworthy readings and suitable equipment.

**Question to investigate:** What reference, procedure and fixture make the reading credible? An inexpensive display does not resolve an uncertain test method. Historical sourcing complaints do not establish current unavailability.

**Existing R&D boundary:** [Torsion-bar tester](../ideas/torsion-bar-tester.md) remains paused on validation, including access to an economical trusted reference. [Flow-bench processor](../ideas/flow-bench-processor.md) remains research-only. [Rod-bolt stretch tool](../ideas/rod-bolt-stretch.md) already has a record; a homemade-gauge forum example should attach there, not create a duplicate idea.

### 7. Small physical controls and installation details

A [DragRaceResults discussion](https://drr.infopop.cc/eve/forums/a/tpc/f/80760912/m/9087097307) asks about moving a transbrake button to reduce reach, while avoiding a cable catching in the steering column. [NICOclub](https://forums.nicoclub.com/post6869376.html) contains an unidentified differential/parts question. These are concrete examples of ergonomics, compatibility and missing documentation.

**Question to investigate:** Is there a recurring fitment or identification job that existing brackets, routing, labels or instructions fail to handle? This could be an accessory or support opportunity, but one question does not establish a product gap. Forum modifications are not validated engineering instructions.

**Existing R&D boundary:** Search the current register and [manufacturer/reseller references](../competitors/README.md) before creating an idea. This research pass did not approve a new control, mounting or brake-related project.

### 8. Timing and run records have local constraints

A [r/DirtRacing maker post](https://www.reddit.com/r/DirtRacing/comments/1xaaohe/my_track_only_runs_transponders_for_the_late/) describes limited timing coverage for some classes and a DIY logging approach; comments raise class permissions and track infrastructure. The maker’s performance claims were not independently tested. [r/dragracing](https://www.reddit.com/r/dragracing/comments/1n05fwk/log_booksspreadsheetsapps_how_do_you_store_your/) compares paper, spreadsheets and apps, including the difference between available remote weather data and actual trackside measurements.

**Question to investigate:** What does the track already provide, what does the class permit, and which missing information changes a real decision? Keep local infrastructure and rules separate from general enthusiasm for telemetry.

**Existing R&D boundary:** [Crew timing display](../ideas/crew-timing-display.md) retains its commercial rejection. [Timing network](../ideas/timing-network.md), [timing import](../ideas/timing-import.md) and [race logbook](../ideas/race-logbook.md) remain historical unadopted suggestions. Another timing post is not a reopening condition by itself.

## Later investigations

[Forum deep dive 01](../research/forum-deep-dive-01/REPORT.md) (17 November 2026) took four of these sources further: HoseHeads, KartPulse, Grassroots Motorsports and Speed-Talk. It tested the strongest findings against current products and small-batch costs, and records which leads were set aside and why. Read its report and [evidence file](../research/forum-deep-dive-01/EVIDENCE.md) before repeating work on those forums. It also found that HoseHeads has moved platform: the legacy thread links formerly given in theme 6 opened unrelated threads and have been replaced with current addresses.

## How to use the sources for the next idea

1. **Start from the job.** Search for the action or failure: measuring, fitting, setting up, diagnosing, saving or interpreting. A broad search for “product ideas” mostly finds other makers’ proposals.
2. **Recover the actual discussion.** Read the original question, replies and any reported resolution. Preserve the URL, evidence date and whether the author is a racer, workshop user, student, seller or maker.
3. **Look for independent repeats and objections.** Three independent users describing the same job are more informative than three reposts of one build. Record adequate existing solutions, unwillingness to add complexity and reasons people prefer paper.
4. **Check the existing idea and decision.** Search aliases and related tools in the register. Attach the new evidence to the existing record. Reopening requires a change that addresses the recorded rejection or blocker.
5. **Frame the smallest unresolved question.** Identify the missing fact: current alternatives, installation time, local frequency, buying behaviour, measurement validation or practical support cost. Do not turn a forum anecdote directly into a specification.

Use the [finding template](../templates/FORUM_FINDING_TEMPLATE.md) to retain the evidence without creating another unstructured idea list. No scheduled monitoring, subscriptions, forum accounts or posting were set up by this research pass.

## Search patterns worth reusing

These are suggested searches, not claims that every phrase already returned results. Replace the domain or discipline to suit the investigation.

| Purpose | Search pattern |
|---|---|
| Installation trouble | `site:forums.kartpulse.com (sensor OR MyChron OR Alfano) (install OR mount OR battery)` |
| Sprint equipment jobs | `site:hoseheadforums.com (tester OR bleeder OR tach OR scales) (problem OR setup OR calibration)` |
| Track logging failures | `site:reddit.com/r/CarTrackDays (logger OR logging) (missing OR unreliable OR pressure)` |
| Drag-racing workflow | `site:drr.infopop.cc (button OR logger OR weather OR delay) (mount OR trigger OR problem)` |
| ECU diagnostics | `site:pcmhacking.net/forums (logging OR ALDL OR sensor) (noise OR error OR setup)` |
| Tyre recording objections | `site:reddit.com/r/Autocross (pressure OR temperature) (paper OR app OR log)` |
| Measurement trust | `site:speed-talk.com/forum (tester OR gauge OR measurement) (calibration OR repeatability)` |
| Practical alternatives | `"<task or product>" ("workaround" OR "made my own" OR "too expensive" OR "don't need")` |

Search engines may interpret brackets, quotes and OR differently. If results are poor, split a compound search into a few simple topic-and-problem queries.

## Limits of this pass

The directory is broad, but it is not an exhaustive review of every post or every racing community. It is stronger on publicly indexed English-language material, with one German technical karting source and several Australian sources. Recent Australian sprint/dirt-oval technical evidence remains a useful gap to fill. Private groups, Discord discussions and deleted posts were not inspected.

An activity label reports what was visible in the sampled evidence. It does not establish posting frequency, audience size, market size, current prices, current product specifications or current class legality. The source cards preserve old dates, access failures, spam and index-only limitations so the next review can build on this one accurately.
