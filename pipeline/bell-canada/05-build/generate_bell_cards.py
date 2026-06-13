#!/usr/bin/env python3
"""
Bell Canada card + stub generator.
Uses the existing Chromium at /opt/pw-browsers/chromium-1194/chrome-linux/chrome
because cdn.playwright.dev is blocked from this environment.
"""

import asyncio
from pathlib import Path

from playwright.async_api import async_playwright

CHROMIUM = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
VIEWPORT = {"width": 1080, "height": 1080}
SCALE = 2  # 2160×2160 output
FONT_WAIT_MS = 1500

PIECE_DIR = Path("/home/user/thedelusioneers/pipeline/bell-canada")
CARD_HTML_DIR = PIECE_DIR / "05-build" / "card-html"
CARDS_OUT = PIECE_DIR / "05-build" / "cards"
BUILD_OUT = PIECE_DIR / "05-build"


async def render(browser, html_path: Path, out_path: Path, width=1080, height=1080) -> None:
    page = await browser.new_page(
        viewport={"width": width, "height": height},
        device_scale_factor=SCALE,
    )
    await page.set_content(
        html_path.read_text(encoding="utf-8"), wait_until="networkidle"
    )
    await page.wait_for_timeout(FONT_WAIT_MS)

    # Bypass all scroll-triggered animations
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

    # Expand viewport if content overflows
    h = await page.evaluate("document.body.scrollHeight")
    if h > height:
        await page.set_viewport_size({"width": width, "height": h})
        await page.wait_for_timeout(200)

    await page.screenshot(path=str(out_path))
    await page.close()
    print(f"  done: {out_path.name}")


async def main() -> None:
    CARDS_OUT.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROMIUM)

        # Cards (sorted by filename → card-00 first)
        card_files = sorted(
            f for f in CARD_HTML_DIR.glob("card-*.html")
        )
        print(f"Rendering {len(card_files)} cards...")
        for html_path in card_files:
            out_name = html_path.stem + ".png"
            await render(browser, html_path, CARDS_OUT / out_name)

        # Stub — separate render to 05-build/stub.png
        stub_html = CARD_HTML_DIR / "stub.html"
        print("Rendering stub...")
        await render(browser, stub_html, BUILD_OUT / "stub.png")

        # Verification screenshots: index.html at 1440px desktop and 390px mobile
        # (both light and dark forced via attribute)
        index_html = BUILD_OUT / "index.html"
        print("Taking verification screenshots...")

        for theme in ("light", "dark"):
            for width, label in ((1440, "desktop"), (390, "mobile")):
                page = await browser.new_page(
                    viewport={"width": width, "height": 900},
                    device_scale_factor=1,
                )
                content = index_html.read_text(encoding="utf-8")
                # force the theme for the screenshot by injecting into content
                content_themed = content.replace(
                    "<html lang=\"en\">",
                    f'<html lang="en" data-theme="{theme}">'
                )
                await page.set_content(content_themed, wait_until="networkidle")
                await page.wait_for_timeout(800)
                h = await page.evaluate("document.body.scrollHeight")
                if h > 900:
                    await page.set_viewport_size({"width": width, "height": h})
                    await page.wait_for_timeout(100)
                snap_path = BUILD_OUT / f"verify-{theme}-{label}.png"
                await page.screenshot(path=str(snap_path), full_page=True)
                await page.close()
                print(f"  verify: {snap_path.name}")

        await browser.close()

    print(f"\nAll done. Cards in {CARDS_OUT}")
    print(f"Stub: {BUILD_OUT / 'stub.png'}")
    print("REMINDER: open one card PNG and confirm fonts rendered (not fallback serif).")


if __name__ == "__main__":
    asyncio.run(main())
