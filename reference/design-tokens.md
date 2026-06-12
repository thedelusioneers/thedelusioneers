# DESIGN TOKENS — THE DELUSIONEERS
Compiled from SOP v1.1. Art-desk reads this before any build. Do not improvise.

## Fonts
- Display: Special Elite (Google Fonts)
- Body/mono: JetBrains Mono (Google Fonts)

## Light mode (:root)
- --bg: #f5f0e8            (parchment / ruled paper)
- --ink: #0d0d0d            (deep ink; some legacy pieces use #1a1a1a)
- --red: #c41e1e            (accent)
- --surround: #2a2825       (dark outer background, both modes)
- Ruled paper texture: repeating-linear-gradient, line color rgba(0,0,0,0.042)

## Dark mode ([data-theme="dark"])
- --bg: #1e1c1a   (site pieces) / #1a1a18 (cool dark, some pieces — match the brief)
- --ink: #e8e3d8
- --ink-light: #b0a898
- --ink-faded: #6a6458
- --red: #e03535
- --border: rgba(232,227,216,0.15)
- --surround: #111010

## Theming rules (mandatory)
- ALL colors via CSS custom properties; :root defines light, [data-theme="dark"]
  overrides every var. Never hardcode palette values in component styles.
- Toggle sets data-theme on <html>; persists to localStorage 'delusioneers-theme';
  respects prefers-color-scheme on first visit if no saved preference.
- Components with dark backgrounds in light mode (.action-block, .deadline-banner)
  need explicit [data-theme="dark"] overrides to maintain contrast.

## Standard page furniture
- Header: reference/header-component.html — brand link → thedelusioneers.ca,
  social icons (Threads J, Threads D, Instagram, Substack, Bluesky), theme
  toggle. Lives in the surround, above .page. Never modified per-piece.
- Progress bar (scrolly pieces only): fixed top, var(--red), 3px.
- Tear edges (scrolly pieces only): top and bottom, SVG mask, wavy.
- Scroll reveals (scrolly pieces only): opacity 0→1, translateY(12px)→0.

## Format containers
- Receipt/ledger: line items with amounts, spacers, closure stamp.
- Maintenance log: table rows, equipment summary, inspector's note.
- Playbook: two-column instrument tables, structural rhyme blocks.
- Spillway: NO scrollytelling, NO progress bar, NO tear edges. Inline CSS
  visuals (proportional-width bar charts via ::before, dashed-border legend
  boxes, flex-wrap timeline strips with border-top accents, tl-now in red,
  tl-election dashed/faded). Citizen action block at bottom (background
  var(--ink), red CTA button, mailto + web link). Deadline banner: full-width
  dark bar, prominent date, sub-label.
- Source page: always a separate HTML file, linked from main doc footer,
  grouped by jurisdiction.
