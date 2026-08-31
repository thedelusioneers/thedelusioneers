# BUILD NOTES — bell-canada

Date: 2026-06-13
Builder: art-desk

## Deviations from standard SOP

### Playwright Chromium download blocked
`cdn.playwright.dev` is in the network egress blocklist. Standard
`playwright install chromium` fails (403). Resolved by using the
existing Chromium at `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`
(Chromium 141.0.7390.37) via the `executable_path` parameter in
`browser.launch()`. All card spec mechanics unchanged.

**SOP CHANGELOG NOTE:** Add to SOP: if `playwright install` fails with
403 on cdn.playwright.dev, check for existing Playwright-compatible
Chromium under `/opt/pw-browsers/` before escalating. Pass via
`executable_path` to `p.chromium.launch()`.

### Google Fonts load
Cards use `@import url('https://fonts.googleapis.com/...')` inside
`set_content()`. Fonts loaded successfully — verified visually. Special
Elite and JetBrains Mono both rendered; no fallback serif observed.

### Card set size
7 cards (card-00 through card-06), consistent with standard set size
per card-spec.md ("Standard set size: 7 cards unless the brief says
otherwise").

### Stub — Document variant
Parchment ground (#f5f0e8), ruled paper texture, black brand strip,
red accent line at top. No near-black inversion (that is the Redact
pattern). Body copy taken verbatim from stub.md (primary/main block,
not the Instagram variant). Instagram variant is in the copy file for
distribution-desk use.

### Source status note
The copy file includes a SOURCE STATUS NOTE block (PARTIAL
classification — all primary URLs 403'd from production environment).
This block is rendered verbatim in the document above the line items,
styled as a left-bordered aside in ink-light color. It is factual
metadata, not editorial copy.

### [CLAIM-NN] references
All [CLAIM-NN] and [GAP-NN] references stripped from body copy per
output contract. GAP callouts are rendered as styled UI components
(gap-callout divs with Gap-01/Gap-02 labels), not inline citations.

## Verification

Screenshots taken and visually inspected:
- verify-light-desktop.png (1440px) — PASS
- verify-light-mobile.png (390px) — PASS
- verify-dark-desktop.png (1440px) — PASS
- verify-dark-mobile.png (390px) — PASS

Card font check:
- card-00-cover.png — Special Elite title + JetBrains Mono body — PASS
- card-02-math.png — PASS
- card-06-summary.png — PASS

Both-theme verification: CONFIRMED YES

## Files produced

05-build/
  index.html
  sources.html
  stub.png
  generate_bell_cards.py
  verify-light-desktop.png
  verify-light-mobile.png
  verify-dark-desktop.png
  verify-dark-mobile.png
  card-html/
    card-00-cover.html
    card-01-charge.html
    card-02-math.html
    card-03-rule.html
    card-04-retention.html
    card-05-remedy.html
    card-06-summary.html
    stub.html
  cards/
    card-00-cover.png
    card-01-charge.png
    card-02-math.png
    card-03-rule.png
    card-04-retention.png
    card-05-remedy.png
    card-06-summary.png
