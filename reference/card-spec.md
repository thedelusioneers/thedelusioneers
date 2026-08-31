# PNG CARD SPEC
Compiled from SOP v1.1 + production learnings.

## Technical
- 1080×1080 px, Playwright (Python, async_api), headless Chromium
- device_scale_factor: 2 → 2160×2160 output
- Fonts: Google Fonts via @import in card HTML
- page.set_content() is more reliable than page.goto() for local HTML
- Wait: page.wait_for_timeout(1500) after networkidle, minimum, for fonts
- Fresh page per card
- Bypass scroll-triggered CSS animations via page.evaluate() before screenshot
- Coordinates: getBoundingClientRect() + window.scrollY — NOT .bounding_box()
- Content-fitted height where needed: document.body.scrollHeight; dynamically
  expand viewport if content exceeds 1080px
- Output: card-NN-slug.png into 05-build/cards/

## Card anatomy (fixed)
- TOP: brand bar (black, "The Delusioneers" + series name)
- ACCENT: 4px red line
- CONTENT: card label + card title + card body (flex, fills remaining space)
- BOTTOM: attribution bar (sources left, @handle right)

## Card set structure
- card-00-cover — piece title, framing, what it covers
- card-NN-slug — one per mechanism/section
- card-NN-summary — totals, key finding, closing line
- Standard set size: 7 cards unless the brief says otherwise

## Failure check
Open at least one output PNG. If text renders in fallback serif, fonts did not
load — rebuild. Do not ship fallback-font cards.
