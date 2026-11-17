# Idea record template

Use this when adding an idea or updating where an existing one is at. Search the register first: a new name may be an alias, companion, variant or older version of an existing entry.

## Questions the record must answer

| Field | What to record |
|---|---|
| Name and aliases | The product/tool name and names previously used for the same idea. |
| Category and kind | Whether it is a commercial product, internal tool, companion, variant, accessory, resale opportunity, research suggestion or infrastructure. Reuse the existing JSON vocabulary. |
| Status | What is happening now: active, investigating, paused for a named reason, rejected, superseded or unadopted. |
| Stage | What actually exists: idea only, repo started, feasibility, software, schematic, board, prototype received, or verified tests. |
| Reason | Why it has that status. A cost rejection needs evidence; otherwise say the economics are unresolved. |
| Repo and repo state | Link if one exists; identify a relevant non-main branch or stale main. Use `null` when no repo is known. |
| Evidence date and basis | Date of the underlying decision or observation, and whether it came from the owner, repository or research. Unknown dates stay `null`. |
| Next step | The useful resume point, without automatically scheduling or beginning it. |
| Reopen trigger | What would need to change before repeating a rejected or parked investigation. |
| Boundaries | Settled scope and distinctions that prevent repeated mistakes. |
| History | Dated decisions, corrections and superseded routes. Preserve previous reasons. |
| Sources | Existing source IDs or new evidence added to `data/sources.json`. |
| Reviewed on | When this catalogue record was reviewed, separate from the evidence date. |

## JSON shape

Add the entry to the `ideas` array in `data/ideas.json`. Replace placeholders, use the next unused ID, and choose existing category/kind/status values appropriate to the evidence.

```json
{
  "slug": "short-stable-name",
  "name": "Idea name",
  "aliases": [],
  "category": "Core products",
  "kind": "product",
  "status": "investigation",
  "stage": "What has actually been completed",
  "summary": "The practical problem and intended user.",
  "reason": "Why the idea is at this status; state any missing evidence.",
  "repo": null,
  "repo_state": "No development repository established by the available evidence.",
  "evidence_date": null,
  "basis": "Owner discussion / repository / unadopted research, as applicable",
  "confidence": "medium",
  "next_step": "The useful next action if the idea is resumed.",
  "reopen_trigger": "The evidence, economics or owner decision needed to revisit it.",
  "boundaries": [
    "A settled scope decision or an important distinction."
  ],
  "history": [
    {
      "date": null,
      "decision": "What was decided; date not recovered."
    }
  ],
  "source_ids": [],
  "id": "RD-NEXT",
  "reviewed_on": "YYYY-MM-DD"
}
```

Do not leave placeholder IDs or dates in a committed record. If a fact is unknown, record that uncertainty rather than using the review date as a substitute.

## Recording an approach we rejected or deferred

Keep the product's overall status accurate. Rejecting one display, supplier or circuit does not necessarily reject the product.

Use a detailed record in the `decisions` array of `data/decisions.json` where the reason needs to be retained:

```json
{
  "product_slug": "short-stable-name",
  "approach": "The particular route or feature considered",
  "status": "rejected",
  "reason": "The evidenced reason it was rejected, superseded or deferred.",
  "evidence_date": null,
  "reopen_trigger": "What would have to change to justify another look.",
  "source_url": null,
  "source_note": "Where the evidence came from and any limits.",
  "id": "DEC-NEXT"
}
```

Use a source URL only when available; otherwise preserve the recoverable thread title/date or other source detail in `source_note`. Do not invent a link or an owner decision.

## Finish the update

Add or update source references, keep existing IDs stable, run `python scripts/render_register.py`, and review the individual entry plus its register/decision links. Update `CURRENT_STATE.md` when the change materially affects the overall picture.
