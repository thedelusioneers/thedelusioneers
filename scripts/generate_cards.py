#!/usr/bin/env python3
"""
The Delusioneers — base card generator.
Encodes all production Playwright learnings. Art-desk adapts the CARDS list
per piece; the mechanics below do not change.

Usage: python scripts/generate_cards.py <piece-dir>
Reads card HTML files from <piece-dir>/05-build/card-html/
Writes PNGs to <piece-dir>/05-build/cards/
"""

import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright

VIEWPORT = {"width": 1080, "height": 1080}
SCALE = 2  # device_scale_factor → 2160×2160 output
FONT_WAIT_MS = 1500  # minimum wait after networkidle for Google Fonts


async def render_card(browser, html_path: Path, out_path: Path) -> None:
    # Fresh page per card — reliability over speed.
    page = await browser.new_page(
        viewport=VIEWPORT, device_scale_factor=SCALE
    )
    await page.set_content(  # set_content > goto for local HTML
        html_path.read_text(encoding="utf-8"), wait_until="networkidle"
    )
    await page.wait_for_timeout(FONT_WAIT_MS)

    # Bypass scroll-triggered animations before screenshotting.
    await page.evaluate(
        """() => {
            document.querySelectorAll('*').forEach(el => {
                el.style.animation = 'none';
                el.style.transition = 'none';
                el.style.opacity = '1';
                el.style.transform = 'none';
            });
        }"""
    )

    # Content-fitted height: expand viewport if content exceeds 1080px.
    height = await page.evaluate("document.body.scrollHeight")
    if height > VIEWPORT["height"]:
        await page.set_viewport_size(
            {"width": VIEWPORT["width"], "height": height}
        )
        await page.wait_for_timeout(200)

    await page.screenshot(path=str(out_path))
    await page.close()
    print(f"  ✓ {out_path.name}")


async def main(piece_dir: str) -> None:
    src = Path(piece_dir) / "05-build" / "card-html"
    out = Path(piece_dir) / "05-build" / "cards"
    out.mkdir(parents=True, exist_ok=True)

    cards = sorted(src.glob("card-*.html"))
    if not cards:
        sys.exit(f"No card-*.html files in {src}")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for html_path in cards:
            await render_card(
                browser, html_path, out / f"{html_path.stem}.png"
            )
        await browser.close()

    print(f"\n{len(cards)} cards → {out}")
    print("REMINDER: open one PNG and confirm fonts rendered (no fallback serif).")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python scripts/generate_cards.py <piece-dir>")
    asyncio.run(main(sys.argv[1]))
