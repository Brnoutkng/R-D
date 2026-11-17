# Maintaining the SkidLabz R&D register

This repository helps Steven avoid repeating product investigations and losing the reasons behind decisions. Keep records practical: what the idea is, where it reached, what happened to it, and what would justify another look.

## Read before investigating

1. Read [CURRENT_STATE.md](CURRENT_STATE.md), then search [REGISTER.md](REGISTER.md) for the name, aliases and related product.
2. Read that entry and its records in [DECISIONS.md](DECISIONS.md) before recommending a previously considered route.
3. Check [RECONCILIATION.md](RECONCILIATION.md) and the cited source when old statements conflict.

An entry's next step records its resume point. It is not an instruction to start that project during unrelated catalogue maintenance.

## Preserve the actual decision

- Keep **current status** separate from **achieved stage**. A developed project can be paused; a repo can exist without hardware; a received board can remain untested.
- Record a rejection reason when evidence establishes it. Do not convert inactivity, high cost estimates or an unresolved issue into a permanent owner rejection.
- Preserve rejected and superseded routes, including their reasons and reopening conditions. Do not erase them when a newer route is selected.
- Keep assistant research suggestions identified as suggestions unless the owner adopted them. Product variants, companion software, internal tools and infrastructure are not automatically separate commercial products.
- Combine aliases and historical names where they refer to the same idea. Preserve old identifiers and links.
- Use `null` for an unknown date and plain wording such as “not established” for missing facts. Do not invent a reason to make a record look complete.

## Reconcile evidence carefully

A newer specific owner statement takes precedence over an older repository summary or the global date on a control file. Compare the date and scope of the actual evidence, not just the file's last commit.

Check relevant branches when main is stale. Distinguish owner reports, source documents, design calculations and physical results. Do not turn a software test, rendered PCB, supplier intake or manufacturing package into proof of a validated product.

A catalogue review date means the record was reviewed. It does not mean its underlying claim was newly confirmed that day. Preserve source dates, confidence and uncertainty.

## Edit records, then generate pages

The source records are:

- `data/ideas.json`: idea identity, status, stage, reasons, history and source references.
- `data/decisions.json`: detailed rejected, superseded or deferred approaches.
- `data/sources.json`: evidence sources and repository snapshots.

Use [templates/IDEA_TEMPLATE.md](templates/IDEA_TEMPLATE.md) when adding a record. Preserve existing `RD-`, `DEC-` and source IDs; assign the next unused ID for new records. Reuse an existing source ID when it is the same evidence.

After changing the JSON, run:

```sh
python scripts/render_register.py
```

Review the generated entry and indexes for correct status, links and counts. Generated files include `REGISTER.md`, `RESEARCH_SUGGESTIONS.md`, `DECISIONS.md`, `SOURCES.md` and `ideas/<slug>.md`; make their substantive changes through the source records and renderer rather than editing generated text in isolation. Keep the narrative README, CURRENT_STATE and RECONCILIATION pages coherent with those records when counts or conclusions change.

Follow the owner's **main-only workflow** for this repository. Keep completed or in-progress catalogue work and `CURRENT_STATE.md` coherent on main; do not create routine development branches.

## Maintain the two competitor lists

Before repeating market/catalogue research, search [resellers](competitors/RESELLERS.md) and [manufacturers/product brands](competitors/MANUFACTURERS.md), including aliases. Their source records are `data/competitors.json` and `data/competitor_sources.json`; regenerate the four pages in `competitors/` with `python scripts/render_competitors.py`.

- Separate evidence that a name was historically mentioned from evidence that classifies its current business role. New web results alone do not establish a past discussion.
- Preserve manufacturer, own-brand supplier, reseller, software, historical benchmark and OEM-lead distinctions. Do not claim that every own-brand item is manufactured in-house.
- Group product aliases under the evidenced brand. Keep related brands searchable with their parent relationship stated; cross-listed mixed businesses have one underlying record.
- Keep uncertain spellings and identities explicit. Do not invent a website, silently substitute a similar company or infer closure from a failed URL.
- Retain pending/OEM/early-market sections as historical references; inclusion is not supplier approval, a current product recommendation or project reactivation.

## Keep the catalogue scoped and useful

This is a public summary. Keep detailed private designs, calibration data, manufacturing outputs, negotiated commercial records and contact/payment details in their source repositories or threads. Link to evidence without copying those details here.

A catalogue update changes this repository. Changes to a product's design, files or development status belong to the corresponding source project and should not be implied by editing its catalogue entry.

Do not turn the register into a fresh product recommendation list, add speculative features to active products, or reopen old investigations merely to fill gaps. Record the useful unresolved question and its evidence instead.
