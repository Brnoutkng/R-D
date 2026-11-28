# SkidLabz product ideas and decisions

A shared record of the ideas we have discussed, where each one reached, and why we continued, parked or rejected it.

**Start with [the product ideas register](REGISTER.md).** Each entry links to its own record with the current status, work already done, development repo, decision history, remaining question and conditions for revisiting it.

## Where to look

| Question | Open |
|---|---|
| What ideas have we already discussed, and where are they at? | [Product ideas register](REGISTER.md) |
| What is the current overall picture? | [Current state](CURRENT_STATE.md) |
| Why did we reject or move away from an approach? | [Decision history](DECISIONS.md) |
| Which ideas were only research suggestions? | [Unadopted research suggestions](RESEARCH_SUGGESTIONS.md) |
| Where did a status or decision come from? | [Sources and repository coverage](SOURCES.md) |
| Which older statements were corrected or superseded? | [Reconciliation notes](RECONCILIATION.md) |
| Which resellers and race shops have we already discussed? | [Resellers and distributors](competitors/RESELLERS.md) |
| Which manufacturers and product brands have we already discussed? | [Manufacturers and product brands](competitors/MANUFACTURERS.md) |
| Where can we find technical racer problems and product research? | [Forums and technical communities](forums/README.md) |
| What useful problems came out of the forum research? | [Research findings and existing idea links](forums/RESEARCH_NOTES.md) |
| Which product opportunities have been tested against forum evidence, and what happened? | [Research investigations](research/README.md) |
| How do we add an idea without losing its history? | [Idea template](templates/IDEA_TEMPLATE.md) |

## What is in this register

The catalogue now contains **128 entries**, covering **13 accessible development repositories**, relevant branches and recovered chat discussions. It also preserves **45 detailed decisions** about rejected, superseded or deferred approaches.

The [main register](REGISTER.md) contains **82 records** with their current or recorded disposition. A separate [research suggestions page](RESEARCH_SUGGESTIONS.md) preserves **46 historical suggestions that were not established as adopted projects**.

Those 128 entries include commercial product ideas, internal workshop and race tools, companion software, variants, accessories, resale opportunities, historical projects and suggestions that were never adopted. They are **not 128 active products**.

The review includes the material that could be recovered. It is not a complete export of every past chat, deleted branch or private discussion. Missing dates and uncertain decisions remain explicit.

## Competitor and market-reference lists

The [competitor register](competitors/README.md) keeps the recovered business names in two places: **[resellers/distributors](competitors/RESELLERS.md)** and **[manufacturers/product brands](competitors/MANUFACTURERS.md)**. Each record gives the discussion context, aliases, role evidence and qualifications. Businesses with both roles are cross-listed from one underlying record.

The register contains **208 business, brand and historical reference records**. These include software, adjacent markets, OEM sourcing leads and unresolved older names in clearly labelled sections; they are not 207 verified competing companies. [Competitor sources and name corrections](competitors/SOURCES.md) preserve the evidence, including Tel-Tac/OTP, Rugged Radios/Nitro Bee and parent-brand relationships.

## Technical forums and product research

The [technical community directory](forums/README.md) records **56 forum/support-board locations and 22 Reddit communities**, grouped into sprint/dirt oval, karting, circuit/club racing, drift/drag/engines, electronics/data and Reddit. Each entry records technical starting points, useful research subjects, dated evidence, example discussions and access limitations. Major inaccessible boards and historical names remain clearly labelled; these are not 78 verified active communities.

[Research notes](forums/RESEARCH_NOTES.md) connect the observed problems to existing ideas and decisions. They preserve both useful requests and objections, including adequate existing solutions and preferences for simpler tools. New forum evidence does not automatically reopen a rejected project or turn an internal tool into a commercial product.

Use the [forum finding template](templates/FORUM_FINDING_TEMPLATE.md) for new evidence. Edit [data/forums.json](data/forums.json) and run `python scripts/render_forums.py` to regenerate the directory; keep the curated research notes coherent with the existing register.

## Read status and stage together

**Status** says what we are doing with an idea now: developing it, using it internally, investigating it, pausing it for a stated reason, rejecting it, or keeping it as historical reference.

**Stage** says how far it actually got: discussion only, repo started, feasibility written, software implemented, schematic or board developed, prototype received, or testing completed.

For example:

- [Street Hit Pro](ideas/street-hit-pro.md) has hardware development work but is paused on manufacturing cost.
- [Knock Meter](ideas/knock-meter.md) has a schematic candidate and is lower priority; the product was not rejected.
- [RaceLogger](ideas/racelogger.md) is a personal development tool with boards reported received, rather than an approved commercial release.
- [RaceScales](ideas/race-scales.md) was rejected on commercial economics; an older “ready to order” statement does not describe the later decision.

A repo existing does not mean a product is ready to manufacture. A paused project does not lose the work already completed. A rejected component or supplier route does not automatically reject the whole product.

## Using it from here

Before starting another investigation, search the register and read the matching decision history. Add new evidence to the existing entry when it concerns the same idea. Preserve why a previous route failed and what would have to change to make it worth reconsidering.

The editable records are [ideas.json](data/ideas.json), [decisions.json](data/decisions.json) and [sources.json](data/sources.json). The readable register, individual entries and reference pages are generated from them with:

```sh
python scripts/render_register.py
```

[AGENTS.md](AGENTS.md) records the maintenance rules.

## Detail and source boundaries

This is a **public repository**. It records general product concepts, status, reasons and source references. Detailed engineering, calibration data, commercial records and manufacturing files remain in their existing private sources. A link to a private repository does not grant access to it.

**Initial review:** 17 November 2026, Australia/Melbourne. Each entry retains its own evidence date; the review date does not make older information newly confirmed.





