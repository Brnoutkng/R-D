# Competitors and market references

Two places to check the businesses and product brands we have already discussed:

- **[Resellers, distributors and race shops](RESELLERS.md)** — Rocket Industries, VPW, Smiley’s, IBRP, QSS and the other retail/sourcing references.
- **[Manufacturers and product brands](MANUFACTURERS.md)** — Longacre, Intercomp, AFCO, JOES, QuickCar, Tel-Tac, RACEceiver and the other product-maker references.

Each record says why the name came up, preserves useful aliases/product names, links the historical evidence and records the role/classification source where available. Businesses with both roles have one underlying record and appear in both views.

## Coverage

The review recovered **208 business, brand and historical reference records**: **44 primarily filed with sellers** and **164 filed with product makers/developers and their related historical references**. This is not a count of verified competing companies: the second group includes software, OEM sourcing leads, legacy brands and unresolved names, each visibly separated.

The evidence comprises recovered chat summaries, saved research and relevant source documents from the existing review of 13 accessible development repositories. It is not a complete transcript export of every chat. Newly found names should be added with their historical context rather than assumed to have been discussed before.

## How to use the lists

Search the brand, business or product alias before starting another catalogue review. A historical mention does not mean we selected that supplier, confirmed a commercial opportunity or reactivated a product. Current project decisions remain in the [ideas register](../REGISTER.md).

The most useful distinctions are kept explicit:

- Tel-Tac includes Oval Track Pro/OTP; Rugged Radios includes Nitro Bee Xtreme.
- RIFE is linked to Motion Raceworks; Proflow to VPW; Aeroflow to Rocket Industries.
- RaceBase is Computech software; Circle Track App is Wehrs Machine software.
- The recorded raceparts.com.au source is Barnier Race Parts. QSS is Performance Wholesale’s speedway division.
- Smiley’s historical shorthand, Speedway Motors Queensland, Clarksons and other ambiguous labels retain qualifications.

See [sources and name corrections](SOURCES.md) for the evidence and exclusions.

## Maintenance

Edit [competitors.json](../data/competitors.json) and [competitor_sources.json](../data/competitor_sources.json), then regenerate these pages:

```sh
python scripts/render_competitors.py
```

Preserve aliases and historical reasons. Separate the evidence that a name was mentioned from the evidence that classifies the business. Add no new competitor merely because it appears in current search results.

**Review date:** 17 November 2026, Australia/Melbourne. Raw conversations, private transaction details and engineering source content are not reproduced here.
