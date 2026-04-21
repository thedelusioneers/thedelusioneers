<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Number — Alberta Separatism and the Polls That Made It</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=JetBrains+Mono:wght@400;500;700&display=swap');

  :root {
    --paper: #f4efe4;
    --paper-dark: #e8e1d0;
    --ink: #1c1a16;
    --ink-mid: #4a4640;
    --ink-faded: #9a9080;
    --red: #c41e1e;
    --red-dark: #8b1515;
    --red-faint: rgba(196,30,30,0.07);
    --margin-line: #c8a8a0;
    --rule: rgba(28,26,22,0.12);
    --green: #1a6b2e;
    --green-faint: rgba(26,107,46,0.07);
    --amber: #8a5a00;
    --amber-faint: rgba(138,90,0,0.07);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  html { scroll-behavior: smooth; }

  body {
    background: #1e1c18;
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    color: var(--ink);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 40px 16px 80px;
    -webkit-font-smoothing: antialiased;
    background-image:
      radial-gradient(ellipse at 20% 20%, rgba(196,30,30,0.04) 0%, transparent 60%),
      radial-gradient(ellipse at 80% 80%, rgba(196,30,30,0.03) 0%, transparent 50%);
  }

  /* Progress bar */
  .progress-bar {
    position: fixed;
    top: 0; left: 0;
    height: 2px;
    background: var(--red);
    z-index: 200;
    transition: width 0.05s linear;
    box-shadow: 0 0 6px rgba(196,30,30,0.6);
  }

  /* Main document */
  .document {
    background: var(--paper);
    width: min(900px, 96vw);
    position: relative;
    box-shadow: 0 8px 48px rgba(0,0,0,0.5), 0 2px 8px rgba(0,0,0,0.3);
    background-image:
      repeating-linear-gradient(
        0deg,
        transparent,
        transparent 23px,
        rgba(0,0,0,0.04) 23px,
        rgba(0,0,0,0.04) 24px
      );
  }

  /* Red margin line */
  .document::before {
    content: '';
    position: absolute;
    left: 72px;
    top: 0; bottom: 0;
    width: 1.5px;
    background: var(--margin-line);
    opacity: 0.6;
    pointer-events: none;
  }

  /* Hole punches */
  .document::after {
    content: '';
    position: absolute;
    left: 24px;
    top: 0; bottom: 0;
    width: 20px;
    background-image:
      radial-gradient(circle at 50% 0, #1e1c18 6px, transparent 6px),
      radial-gradient(circle at 50% 0, var(--paper-dark) 5px, transparent 5px);
    background-size: 20px 80px;
    background-repeat: repeat-y;
    background-position: 0 40px;
    pointer-events: none;
  }

  .inner {
    padding: 48px 48px 48px 96px;
  }

  /* Header */
  .doc-header {
    border-bottom: 2px solid var(--ink);
    padding-bottom: 24px;
    margin-bottom: 32px;
  }

  .doc-header .institution {
    font-size: 9px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--ink-faded);
    margin-bottom: 8px;
  }

  .doc-header h1 {
    font-family: 'Special Elite', monospace;
    font-size: clamp(22px, 4vw, 36px);
    line-height: 1.15;
    color: var(--ink);
    margin-bottom: 10px;
  }

  .doc-header .subtitle {
    font-size: 11px;
    color: var(--ink-mid);
    letter-spacing: 1px;
    line-height: 1.6;
  }

  .doc-meta {
    display: flex;
    gap: 32px;
    margin-top: 16px;
    flex-wrap: wrap;
  }

  .doc-meta span {
    font-size: 9px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--ink-faded);
  }

  .doc-meta span strong {
    color: var(--ink-mid);
  }

  /* Section headers */
  .section-head {
    font-size: 9px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--ink-faded);
    border-bottom: 1px solid var(--rule);
    padding-bottom: 6px;
    margin-bottom: 16px;
    margin-top: 40px;
  }

  /* Lede */
  .lede {
    font-family: 'Special Elite', monospace;
    font-size: 15px;
    line-height: 1.7;
    color: var(--ink);
    margin-bottom: 24px;
    max-width: 720px;
  }

  .lede em {
    font-style: normal;
    color: var(--red-dark);
    border-bottom: 1px solid var(--red-dark);
  }

  /* Key finding box */
  .finding-box {
    border: 1.5px solid var(--ink);
    padding: 20px 24px;
    margin-bottom: 32px;
    position: relative;
    background: var(--paper-dark);
    opacity: 0;
    transform: translateY(8px);
    transition: opacity 0.5s ease, transform 0.5s ease;
  }
  .finding-box.visible {
    opacity: 1;
    transform: translateY(0);
  }

  .finding-box::before {
    content: 'FINDING';
    position: absolute;
    top: -8px;
    left: 16px;
    background: var(--paper-dark);
    padding: 0 8px;
    font-size: 8px;
    letter-spacing: 3px;
    color: var(--ink-faded);
  }

  .finding-box p {
    font-size: 11.5px;
    line-height: 1.7;
    color: var(--ink-mid);
  }

  .finding-box p strong {
    color: var(--ink);
  }

  /* THE TABLE */
  .table-wrapper {
    overflow-x: auto;
    margin: 0 -16px;
    padding: 0 16px;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 10.5px;
    min-width: 700px;
  }

  thead tr {
    border-bottom: 2px solid var(--ink);
  }

  thead th {
    font-size: 8px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--ink-faded);
    text-align: left;
    padding: 8px 12px 10px;
    font-weight: 400;
    white-space: nowrap;
  }

  thead th:first-child { padding-left: 0; }

  tbody tr {
    border-bottom: 1px dotted rgba(28,26,22,0.2);
    opacity: 0;
    transform: translateY(6px);
    transition: opacity 0.4s ease, transform 0.4s ease;
  }

  tbody tr.visible {
    opacity: 1;
    transform: translateY(0);
  }

  tbody tr:hover {
    background: rgba(28,26,22,0.03);
  }

  /* Row type classes */
  tbody tr.row-artifact {
    background: var(--red-faint);
  }
  tbody tr.row-artifact:hover {
    background: rgba(196,30,30,0.1);
  }

  tbody tr.row-clean {
    background: var(--green-faint);
  }
  tbody tr.row-clean:hover {
    background: rgba(26,107,46,0.1);
  }

  tbody tr.row-conditional {
    background: var(--amber-faint);
  }
  tbody tr.row-conditional:hover {
    background: rgba(138,90,0,0.1);
  }

  td {
    padding: 14px 12px;
    vertical-align: top;
    line-height: 1.5;
    color: var(--ink-mid);
  }

  td:first-child { padding-left: 0; }

  /* Column: firm */
  td.col-firm {
    font-family: 'Special Elite', monospace;
    font-size: 11px;
    color: var(--ink);
    white-space: nowrap;
    min-width: 120px;
  }

  td.col-firm .firm-name {
    display: block;
  }
  td.col-firm .commissioner {
    font-family: 'JetBrains Mono', monospace;
    font-size: 8px;
    letter-spacing: 1px;
    color: var(--ink-faded);
    text-transform: uppercase;
    margin-top: 3px;
  }

  /* Column: dates */
  td.col-dates {
    white-space: nowrap;
    font-size: 10px;
    min-width: 100px;
  }

  td.col-dates .field-dates {
    display: block;
    color: var(--ink);
  }
  td.col-dates .sample {
    font-size: 8.5px;
    color: var(--ink-faded);
    margin-top: 2px;
  }

  /* Column: question */
  td.col-question {
    min-width: 200px;
    max-width: 260px;
    font-size: 10px;
    color: var(--ink-mid);
  }

  td.col-question .q-text {
    font-style: italic;
    color: var(--ink);
    display: block;
    margin-bottom: 4px;
  }

  td.col-question .q-type {
    font-size: 8px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--ink-faded);
  }

  /* Column: result — the number */
  td.col-result {
    text-align: right;
    white-space: nowrap;
    min-width: 80px;
  }

  .number-clean {
    font-family: 'Special Elite', monospace;
    font-size: 20px;
    color: var(--green);
    display: block;
    line-height: 1;
  }

  .number-artifact {
    font-family: 'Special Elite', monospace;
    font-size: 20px;
    color: var(--red);
    display: block;
    line-height: 1;
  }

  .number-conditional {
    font-family: 'Special Elite', monospace;
    font-size: 20px;
    color: var(--amber);
    display: block;
    line-height: 1;
  }

  .number-sub {
    font-size: 8.5px;
    color: var(--ink-faded);
    margin-top: 3px;
    display: block;
    text-align: right;
  }

  /* Column: note */
  td.col-note {
    font-size: 9.5px;
    color: var(--ink-faded);
    max-width: 220px;
    line-height: 1.5;
  }

  td.col-note strong {
    color: var(--red-dark);
    font-weight: 500;
  }

  td.col-note .tag {
    display: inline-block;
    font-size: 7.5px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 1px 5px;
    border: 1px solid currentColor;
    margin-bottom: 4px;
    border-radius: 1px;
  }

  .tag-artifact { color: var(--red-dark); }
  .tag-clean { color: var(--green); }
  .tag-conditional { color: var(--amber); }

  /* Section divider within table */
  tr.table-divider td {
    padding: 6px 0 4px;
    border-bottom: 1.5px solid var(--ink);
  }

  tr.table-divider td span {
    font-size: 8px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--ink-faded);
  }

  /* Legend */
  .legend {
    display: flex;
    gap: 24px;
    margin: 16px 0 32px;
    flex-wrap: wrap;
  }

  .legend-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 9px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--ink-faded);
  }

  .legend-swatch {
    width: 12px;
    height: 12px;
    border: 1px solid currentColor;
  }

  .legend-item.clean { color: var(--green); }
  .legend-item.artifact { color: var(--red-dark); }
  .legend-item.conditional { color: var(--amber); }

  /* Analysis section */
  .analysis-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    margin-top: 8px;
  }

  @media (max-width: 600px) {
    .analysis-grid { grid-template-columns: 1fr; }
  }

  .analysis-cell {
    border-top: 2px solid var(--ink);
    padding-top: 16px;
    opacity: 0;
    transform: translateY(8px);
    transition: opacity 0.5s ease, transform 0.5s ease;
  }

  .analysis-cell.visible {
    opacity: 1;
    transform: translateY(0);
  }

  .analysis-cell .cell-label {
    font-size: 8px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--ink-faded);
    margin-bottom: 10px;
    display: block;
  }

  .analysis-cell p {
    font-size: 11px;
    line-height: 1.7;
    color: var(--ink-mid);
  }

  .analysis-cell p strong {
    color: var(--ink);
  }

  /* The delta callout */
  .delta-callout {
    border: 1.5px solid var(--red);
    padding: 24px 28px;
    margin: 32px 0;
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 0 28px;
    align-items: center;
    opacity: 0;
    transform: translateY(8px);
    transition: opacity 0.5s ease, transform 0.5s ease;
  }

  .delta-callout.visible {
    opacity: 1;
    transform: translateY(0);
  }

  .delta-number {
    font-family: 'Special Elite', monospace;
    font-size: clamp(52px, 10vw, 72px);
    color: var(--red);
    line-height: 1;
    text-align: center;
  }

  .delta-number .delta-unit {
    font-size: 14px;
    display: block;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--red-dark);
    margin-top: 4px;
  }

  .delta-text {
    font-size: 11px;
    line-height: 1.7;
    color: var(--ink-mid);
  }

  .delta-text strong { color: var(--ink); }

  /* Closure */
  .closure {
    margin-top: 48px;
    padding-top: 32px;
    border-top: 2px solid var(--ink);
    text-align: center;
    opacity: 0;
    transform: translateY(16px);
    transition: opacity 0.8s ease, transform 0.8s ease;
  }

  .closure.visible {
    opacity: 1;
    transform: translateY(0);
  }

  .closure-stamp {
    font-family: 'Special Elite', monospace;
    font-size: clamp(16px, 4vw, 24px);
    color: var(--red);
    letter-spacing: 3px;
    text-transform: uppercase;
    border: 3px solid var(--red);
    padding: 14px 28px;
    display: inline-block;
    transform: rotate(-1.5deg);
    position: relative;
    line-height: 1.3;
    margin-bottom: 24px;
  }

  .closure-stamp::after {
    content: '';
    position: absolute;
    inset: -6px;
    border: 1px solid var(--red);
    opacity: 0.35;
  }

  .closure-sub {
    font-size: 10px;
    color: var(--ink-faded);
    letter-spacing: 1.5px;
    line-height: 2;
    text-transform: uppercase;
  }

  .closure-sub a {
    color: var(--ink-mid);
    text-decoration: none;
    border-bottom: 1px dotted var(--ink-faded);
  }

  /* Source footnotes */
  .footnotes {
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px dashed var(--rule);
  }

  .footnotes p {
    font-size: 8.5px;
    color: var(--ink-faded);
    line-height: 1.8;
    letter-spacing: 0.5px;
  }

  .footnotes p strong {
    color: var(--ink-mid);
  }

  /* Scroll hint */
  .scroll-hint {
    position: fixed;
    bottom: 24px;
    left: 50%;
    transform: translateX(-50%);
    color: rgba(244,239,228,0.4);
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    text-transform: uppercase;
    z-index: 100;
    transition: opacity 0.6s;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    pointer-events: none;
  }

  .scroll-hint .arrow {
    animation: bobDown 1.5s ease-in-out infinite;
  }

  @keyframes bobDown {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(5px); }
  }

  .scroll-hint.hidden { opacity: 0; }

  /* Tear edges */
  .tear-top, .tear-bottom {
    width: min(900px, 96vw);
    height: 20px;
    background: var(--paper);
  }

  .tear-top {
    mask-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 900 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0,20 L0,10 Q9,0 18,10 Q27,20 36,10 Q45,0 54,10 Q63,20 72,10 Q81,0 90,10 Q99,20 108,10 Q117,0 126,10 Q135,20 144,10 Q153,0 162,10 Q171,20 180,10 Q189,0 198,10 Q207,20 216,10 Q225,0 234,10 Q243,20 252,10 Q261,0 270,10 Q279,20 288,10 Q297,0 306,10 Q315,20 324,10 Q333,0 342,10 Q351,20 360,10 Q369,0 378,10 Q387,20 396,10 Q405,0 414,10 Q423,20 432,10 Q441,0 450,10 Q459,20 468,10 Q477,0 486,10 Q495,20 504,10 Q513,0 522,10 Q531,20 540,10 Q549,0 558,10 Q567,20 576,10 Q585,0 594,10 Q603,20 612,10 Q621,0 630,10 Q639,20 648,10 Q657,0 666,10 Q675,20 684,10 Q693,0 702,10 Q711,20 720,10 Q729,0 738,10 Q747,20 756,10 Q765,0 774,10 Q783,20 792,10 Q801,0 810,10 Q819,20 828,10 Q837,0 846,10 Q855,20 864,10 Q873,0 882,10 Q891,20 900,10 L900,20 Z' fill='white'/%3E%3C/svg%3E");
    -webkit-mask-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 900 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0,20 L0,10 Q9,0 18,10 Q27,20 36,10 Q45,0 54,10 Q63,20 72,10 Q81,0 90,10 Q99,20 108,10 Q117,0 126,10 Q135,20 144,10 Q153,0 162,10 Q171,20 180,10 Q189,0 198,10 Q207,20 216,10 Q225,0 234,10 Q243,20 252,10 Q261,0 270,10 Q279,20 288,10 Q297,0 306,10 Q315,20 324,10 Q333,0 342,10 Q351,20 360,10 Q369,0 378,10 Q387,20 396,10 Q405,0 414,10 Q423,20 432,10 Q441,0 450,10 Q459,20 468,10 Q477,0 486,10 Q495,20 504,10 Q513,0 522,10 Q531,20 540,10 Q549,0 558,10 Q567,20 576,10 Q585,0 594,10 Q603,20 612,10 Q621,0 630,10 Q639,20 648,10 Q657,0 666,10 Q675,20 684,10 Q693,0 702,10 Q711,20 720,10 Q729,0 738,10 Q747,20 756,10 Q765,0 774,10 Q783,20 792,10 Q801,0 810,10 Q819,20 828,10 Q837,0 846,10 Q855,20 864,10 Q873,0 882,10 Q891,20 900,10 L900,20 Z' fill='white'/%3E%3C/svg%3E");
    mask-size: cover;
    -webkit-mask-size: cover;
    margin-top: 40px;
    box-shadow: 0 -4px 20px rgba(0,0,0,0.3);
  }

  .tear-bottom {
    mask-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 900 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0,0 L0,10 Q9,20 18,10 Q27,0 36,10 Q45,20 54,10 Q63,0 72,10 Q81,20 90,10 Q99,0 108,10 Q117,20 126,10 Q135,0 144,10 Q153,20 162,10 Q171,0 180,10 Q189,20 198,10 Q207,0 216,10 Q225,20 234,10 Q243,0 252,10 Q261,20 270,10 Q279,0 288,10 Q297,20 306,10 Q315,0 324,10 Q333,20 342,10 Q351,0 360,10 Q369,20 378,10 Q387,0 396,10 Q405,20 414,10 Q423,0 432,10 Q441,20 450,10 Q459,0 468,10 Q477,20 486,10 Q495,0 504,10 Q513,20 522,10 Q531,0 540,10 Q549,20 558,10 Q567,0 576,10 Q585,20 594,10 Q603,0 612,10 Q621,20 630,10 Q639,0 648,10 Q657,20 666,10 Q675,0 684,10 Q693,20 702,10 Q711,0 720,10 Q729,20 738,10 Q747,0 756,10 Q765,20 774,10 Q783,0 792,10 Q801,20 810,10 Q819,0 828,10 Q837,20 846,10 Q855,0 864,10 Q873,20 882,10 Q891,0 900,10 L900,0 Z' fill='white'/%3E%3C/svg%3E");
    -webkit-mask-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 900 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0,0 L0,10 Q9,20 18,10 Q27,0 36,10 Q45,20 54,10 Q63,0 72,10 Q81,20 90,10 Q99,0 108,10 Q117,20 126,10 Q135,0 144,10 Q153,20 162,10 Q171,0 180,10 Q189,20 198,10 Q207,0 216,10 Q225,20 234,10 Q243,0 252,10 Q261,20 270,10 Q279,0 288,10 Q297,20 306,10 Q315,0 324,10 Q333,20 342,10 Q351,0 360,10 Q369,20 378,10 Q387,0 396,10 Q405,20 414,10 Q423,0 432,10 Q441,20 450,10 Q459,0 468,10 Q477,20 486,10 Q495,0 504,10 Q513,20 522,10 Q531,0 540,10 Q549,20 558,10 Q567,0 576,10 Q585,20 594,10 Q603,0 612,10 Q621,20 630,10 Q639,0 648,10 Q657,20 666,10 Q675,0 684,10 Q693,20 702,10 Q711,0 720,10 Q729,20 738,10 Q747,0 756,10 Q765,20 774,10 Q783,0 792,10 Q801,20 810,10 Q819,0 828,10 Q837,20 846,10 Q855,0 864,10 Q873,20 882,10 Q891,0 900,10 L900,0 Z' fill='white'/%3E%3C/svg%3E");
    mask-size: cover;
    -webkit-mask-size: cover;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
  }

  @media (max-width: 640px) {
    .inner { padding: 32px 24px 32px 56px; }
    .doc-header h1 { font-size: 20px; }
    .delta-callout { grid-template-columns: 1fr; text-align: center; }
  }
</style>
</head>
<body>

<div class="progress-bar" id="progressBar"></div>
<div class="scroll-hint" id="scrollHint">
  <span>Scroll</span>
  <span class="arrow">↓</span>
</div>

<div class="tear-top"></div>

<div class="document">
<div class="inner">

  <!-- HEADER -->
  <div class="doc-header">
    <div class="institution">The Delusioneers — Alberta Series · Polling Architecture</div>
    <h1>The Number</h1>
    <div class="subtitle">
      Eight polling firms. Eight months. The same electorate.<br>
      Why the number you saw in the headline was probably not the one the poll produced.
    </div>
    <div class="doc-meta">
      <span>Period: <strong>Sept 2025 – Apr 2026</strong></span>
      <span>Polls reviewed: <strong>13</strong></span>
      <span>Range (dedicated AB polls): <strong>23% – 31%</strong></span>
      <span>Range (reported): <strong>23% – 47%</strong></span>
      <span>Published: <strong>April 2026</strong></span>
    </div>
  </div>

  <!-- LEDE -->
  <p class="lede">
    Every poll on Alberta separatism published between September 2025 and April 2026
    was conducted on the same population. The dedicated Alberta surveys — where a firm
    samples 700 to 3,200 Albertans specifically and asks a clean independence question —
    cluster in a band of <em>23% to 31%</em>. The numbers above 35% that dominated coverage
    are not from those surveys. They are products of the instrument: the question asked,
    the sample used, the scenario constructed. This is the record.
  </p>

  <!-- FINDING BOX -->
  <div class="finding-box reveal-item">
    <p>
      <strong>The same firm, one week apart, produced 29% and 47% from the same population.</strong>
      Léger's dedicated Alberta survey (May 9–12, 2025, n=1,000) asked Albertans directly
      about independence: 29% support. Léger's national survey (May 16–18, 2025, n=1,537 nationally,
      unweighted Alberta n=133) asked the same question in a national context: 47% of the Alberta
      subsample support. The May 16–18 figure was reported by Global News and Canadian Press as
      "almost half of Albertans." The subsample size, margin of error, and the existence of the
      earlier dedicated survey were not disclosed in that coverage.
    </p>
  </div>

  <!-- LEGEND -->
  <div class="section-head">Table legend</div>
  <div class="legend">
    <div class="legend-item clean">
      <div class="legend-swatch" style="background: var(--green-faint); border-color: var(--green);"></div>
      Dedicated Alberta survey · clean independence question
    </div>
    <div class="legend-item conditional">
      <div class="legend-swatch" style="background: var(--amber-faint); border-color: var(--amber);"></div>
      Conditional / scenario-based / stress-tested
    </div>
    <div class="legend-item artifact">
      <div class="legend-swatch" style="background: var(--red-faint); border-color: var(--red-dark);"></div>
      National subsample · multi-scenario aggregate · modeled projection
    </div>
  </div>

  <!-- THE TABLE -->
  <div class="section-head">All polls · September 2025 – April 2026</div>
  <div class="table-wrapper">
    <table>
      <thead>
        <tr>
          <th>Firm / Commissioner</th>
          <th>Field dates</th>
          <th>AB sample</th>
          <th>Question (paraphrased)</th>
          <th>Format</th>
          <th style="text-align:right">Result</th>
          <th>Notes</th>
        </tr>
      </thead>
      <tbody>

        <!-- DIVIDER: DEDICATED CLEAN -->
        <tr class="table-divider reveal-item">
          <td colspan="7"><span>· · · Dedicated Alberta surveys · clean independence question · · ·</span></td>
        </tr>

        <!-- ThinkHQ -->
        <tr class="row-clean reveal-item">
          <td class="col-firm">
            <span class="firm-name">ThinkHQ</span>
            <span class="commissioner">Self-commissioned</span>
          </td>
          <td class="col-dates">
            <span class="field-dates">Sept 2025</span>
            <span class="sample">n not published</span>
          </td>
          <td>Albertans only</td>
          <td class="col-question">
            <span class="q-text">"If a provincial referendum on separation were held tomorrow, would you vote to separate or remain?"</span>
            <span class="q-type">Mock ballot · binary</span>
          </td>
          <td>Binary yes/no</td>
          <td class="col-result">
            <span class="number-clean">23%</span>
            <span class="number-sub">separate</span>
          </td>
          <td class="col-note">
            <span class="tag tag-clean">Clean</span><br>
            Earliest data point in current cycle. Baseline for subsequent comparison.
          </td>
        </tr>

        <!-- Léger / Postmedia May 9-12 ROW 1 -->
        <tr class="row-clean reveal-item">
          <td class="col-firm">
            <span class="firm-name">Léger / Postmedia</span>
            <span class="commissioner">Postmedia</span>
          </td>
          <td class="col-dates">
            <span class="field-dates">May 9–12, 2025</span>
            <span class="sample">n=1,000 Albertans</span>
          </td>
          <td>Albertans only</td>
          <td class="col-question">
            <span class="q-text">"To what extent would you support or oppose the province of Alberta becoming a country independent of Canada?"</span>
            <span class="q-type">Support/oppose scale · Alberta independence only</span>
          </td>
          <td>4-point scale</td>
          <td class="col-result">
            <span class="number-clean">29%</span>
            <span class="number-sub">support</span>
          </td>
          <td class="col-note">
            <span class="tag tag-clean">Clean</span><br>
            Dedicated Alberta survey. Clean independence question. Reported correctly by CTV as "29%." Same firm asked national subsample one week later; produced 47%.
          </td>
        </tr>

        <!-- Léger / Postmedia May 9-12 ROW 2 — western bloc -->
        <tr class="row-conditional reveal-item">
          <td class="col-firm">
            <span class="firm-name">Léger / Postmedia</span>
            <span class="commissioner">Postmedia</span>
          </td>
          <td class="col-dates">
            <span class="field-dates">May 9–12, 2025</span>
            <span class="sample">n=1,000 Albertans</span>
          </td>
          <td>Albertans only</td>
          <td class="col-question">
            <span class="q-text">"Alberta, Saskatchewan, British Columbia, and Manitoba forming an independent country"</span>
            <span class="q-type">Multi-province scenario · same survey, different question</span>
          </td>
          <td>4-point scale</td>
          <td class="col-result">
            <span class="number-conditional">35%</span>
            <span class="number-sub">support</span>
          </td>
          <td class="col-note">
            <span class="tag tag-conditional">Scenario</span><br>
            Same survey, different question. A western bloc scenario — not Alberta independence. Reported alongside 29% figure in some coverage without distinguishing the two questions.
          </td>
        </tr>

        <!-- Research Co. -->
        <tr class="row-clean reveal-item">
          <td class="col-firm">
            <span class="firm-name">Research Co.</span>
            <span class="commissioner">Self-commissioned</span>
          </td>
          <td class="col-dates">
            <span class="field-dates">Jan 4–6, 2026</span>
            <span class="sample">n=703 Albertans</span>
          </td>
          <td>Albertans only</td>
          <td class="col-question">
            <span class="q-text">"Alberta becoming a country independent from Canada"</span>
            <span class="q-type">Support/oppose · Alberta independence only</span>
          </td>
          <td>Support/oppose</td>
          <td class="col-result">
            <span class="number-clean">31%</span>
            <span class="number-sub">support</span>
          </td>
          <td class="col-note">
            <span class="tag tag-clean">Clean</span><br>
            Up 9 points from June 2023 baseline. 42% among 18–34. Reported as "three-in-ten." Credibility interval ±3.7 pp.
          </td>
        </tr>

        <!-- Ipsos -->
        <tr class="row-clean reveal-item">
          <td class="col-firm">
            <span class="firm-name">Ipsos</span>
            <span class="commissioner">Self-commissioned</span>
          </td>
          <td class="col-dates">
            <span class="field-dates">Jan 9–14, 2026</span>
            <span class="sample">~500 Albertans</span>
          </td>
          <td>Albertans + Quebecers (national study)</td>
          <td class="col-question">
            <span class="q-text">"Vote for province to begin process of separating from Canada" — initial question before stress-testing</span>
            <span class="q-type">Yes/lean yes/lean no/no · initial then conditional</span>
          </td>
          <td>2-stage</td>
          <td class="col-result">
            <span class="number-clean">29%</span>
            <span class="number-sub">yes/lean</span>
          </td>
          <td class="col-note">
            <span class="tag tag-clean">Clean (initial)</span><br>
            Drops to <strong>16%</strong> after cost stress-test. Committed: 55% of yes voters. Conditional: 25%. Symbolic: 20%. Credibility interval ±5.4 pp for AB/QC samples.
          </td>
        </tr>

        <!-- Angus Reid -->
        <tr class="row-clean reveal-item">
          <td class="col-firm">
            <span class="firm-name">Angus Reid</span>
            <span class="commissioner">Self-commissioned</span>
          </td>
          <td class="col-dates">
            <span class="field-dates">Feb 2–6, 2026</span>
            <span class="sample">n=979 Albertans</span>
          </td>
          <td>Albertans only</td>
          <td class="col-question">
            <span class="q-text">"Definitely leave / Lean leave / Lean stay / Definitely stay / Undecided"</span>
            <span class="q-type">5-point spectrum · includes lean</span>
          </td>
          <td>5-point spectrum</td>
          <td class="col-result">
            <span class="number-clean">29%</span>
            <span class="number-sub">leave/lean</span>
          </td>
          <td class="col-note">
            <span class="tag tag-clean">Clean</span><br>
            Only 8% "definitely leave." Includes lean. Reported as "3 in 10." ±3 pp.
          </td>
        </tr>

        <!-- Abacus -->
        <tr class="row-clean reveal-item">
          <td class="col-firm">
            <span class="firm-name">Abacus Data</span>
            <span class="commissioner">Self-commissioned</span>
          </td>
          <td class="col-dates">
            <span class="field-dates">Feb 20–25, 2026</span>
            <span class="sample">n=1,000 Albertans</span>
          </td>
          <td>Albertans only</td>
          <td class="col-question">
            <span class="q-text">"The Province of Alberta shall become a sovereign country and cease to be a province of Canada"</span>
            <span class="q-type">Agree/disagree · constitutional language</span>
          </td>
          <td>Agree/disagree</td>
          <td class="col-result">
            <span class="number-clean">26%</span>
            <span class="number-sub">agree</span>
          </td>
          <td class="col-note">
            <span class="tag tag-clean">Clean</span><br>
            Constitutional framing ("cease to be a province") produces the lowest dedicated-survey number. Reported headline: "Rock solid majority opposed."
          </td>
        </tr>

        <!-- Pollara decided -->
        <tr class="row-clean reveal-item">
          <td class="col-firm">
            <span class="firm-name">Pollara</span>
            <span class="commissioner">Self-commissioned</span>
          </td>
          <td class="col-dates">
            <span class="field-dates">Mar 16–25, 2026</span>
            <span class="sample">n=3,200 Albertans</span>
          </td>
          <td>Albertans only · largest sample</td>
          <td class="col-question">
            <span class="q-text">"If a referendum held tomorrow — vote for or against separating from Canada?"</span>
            <span class="q-type">Binary referendum · decided vote only</span>
          </td>
          <td>Binary yes/no</td>
          <td class="col-result">
            <span class="number-clean">27%</span>
            <span class="number-sub">separate</span>
          </td>
          <td class="col-note">
            <span class="tag tag-clean">Clean</span><br>
            Described as "5-year high." Pollara's tracker began Jan 2021 — not an all-time record. ±1.7 pp. Largest dedicated Alberta sample in table.
          </td>
        </tr>

        <!-- Mainstreet clean -->
        <tr class="row-clean reveal-item">
          <td class="col-firm">
            <span class="firm-name">Mainstreet Research</span>
            <span class="commissioner">Self-commissioned</span>
          </td>
          <td class="col-dates">
            <span class="field-dates">Feb 10–12, 2026</span>
            <span class="sample">n=1,504 Albertans</span>
          </td>
          <td>Albertans only · <strong>telephone IVR</strong></td>
          <td class="col-question">
            <span class="q-text">"If a referendum were held today on if Alberta should become an independent country, how would you vote?"</span>
            <span class="q-type">Binary referendum · all voters including don't know</span>
          </td>
          <td>Binary yes/no/DK</td>
          <td class="col-result">
            <span class="number-clean">30%</span>
            <span class="number-sub">independent country</span>
          </td>
          <td class="col-note">
            <span class="tag tag-clean">Clean</span><br>
            Only telephone survey in table — IVR methodology. 34% undecideds removed. ±2.5 pp. Same survey also asked conditional scenarios (see below). Notably: only <strong>9% of respondents listed "Alberta Independence" as their greatest concern</strong> — behind cost of living (26%), healthcare (22%), crime, education, immigration, taxes, and threats to freedoms.
          </td>
        </tr>

        <!-- DIVIDER: CONDITIONAL -->
        <tr class="table-divider reveal-item">
          <td colspan="7"><span>· · · Conditional scenarios — same surveys, different questions · · ·</span></td>
        </tr>

        <!-- Mainstreet US scenario -->
        <tr class="row-conditional reveal-item">
          <td class="col-firm">
            <span class="firm-name">Mainstreet Research</span>
            <span class="commissioner">Self-commissioned</span>
          </td>
          <td class="col-dates">
            <span class="field-dates">Feb 10–12, 2026</span>
            <span class="sample">n=1,504 Albertans</span>
          </td>
          <td>Albertans only</td>
          <td class="col-question">
            <span class="q-text">"If the US promised an economic union with an independent Alberta, allowing a one-to-one exchange of Canadian dollars into US dollars, how would you vote?"</span>
            <span class="q-type">Conditional · US annexation scenario</span>
          </td>
          <td>Binary yes/no/DK</td>
          <td class="col-result">
            <span class="number-conditional">28%</span>
            <span class="number-sub">independent country</span>
          </td>
          <td class="col-note">
            <span class="tag tag-conditional">Scenario</span><br>
            US economic union scenario — the proposal APP leaders reportedly discussed in Washington — <strong>decreases</strong> support 2 points from the clean question. Dollar parity with the US does not move Alberta separatists. 32% undecideds removed.
          </td>
        </tr>

        <!-- Mainstreet pipeline scenario -->
        <tr class="row-conditional reveal-item">
          <td class="col-firm">
            <span class="firm-name">Mainstreet Research</span>
            <span class="commissioner">Self-commissioned</span>
          </td>
          <td class="col-dates">
            <span class="field-dates">Feb 10–12, 2026</span>
            <span class="sample">n=1,504 Albertans</span>
          </td>
          <td>Albertans only</td>
          <td class="col-question">
            <span class="q-text">"If the proposed pipeline agreement between Danielle Smith and Mark Carney were to fall apart, and a referendum were held..."</span>
            <span class="q-type">Conditional · federal resource policy failure scenario</span>
          </td>
          <td>Binary yes/no/DK</td>
          <td class="col-result">
            <span class="number-conditional">33%</span>
            <span class="number-sub">independent country</span>
          </td>
          <td class="col-note">
            <span class="tag tag-conditional">Scenario</span><br>
            Pipeline failure scenario produces the highest conditional number: +3 points from clean question. Federal resource policy — not American annexation — is the lever. 37% undecideds removed. Confirms grievance is economic, not cultural.
          </td>
        </tr>

        <!-- DIVIDER: ARTIFACTS -->
        <tr class="table-divider reveal-item">
          <td colspan="7"><span>· · · Numbers above 35% — what produced them · · ·</span></td>
        </tr>

        <!-- Léger CP national -->
        <tr class="row-artifact reveal-item">
          <td class="col-firm">
            <span class="firm-name">Léger / Canadian Press</span>
            <span class="commissioner">Self-commissioned</span>
          </td>
          <td class="col-dates">
            <span class="field-dates">May 16–18, 2025</span>
            <span class="sample">n=133 unweighted<br>n=171 weighted</span>
          </td>
          <td><strong style="color:var(--red-dark)">National survey · AB subsample only</strong></td>
          <td class="col-question">
            <span class="q-text">"Support or oppose the province of Alberta becoming a country independent of Canada"</span>
            <span class="q-type">Support/oppose · asked in national survey context</span>
          </td>
          <td>4-point scale</td>
          <td class="col-result">
            <span class="number-artifact">47%</span>
            <span class="number-sub">support</span>
          </td>
          <td class="col-note">
            <span class="tag tag-artifact">Subsample</span><br>
            National survey n=1,537. Alberta subsample: <strong>133 unweighted / 171 weighted</strong>. Implied credibility interval ±8.5 pp vs. ±3.1% for the dedicated 1,000-person Alberta survey one week earlier. Reported by Global News and CP as "almost half of Albertans" — subsample size not disclosed. Same firm, same question, seven days apart: <strong>29% vs. 47%.</strong>
          </td>
        </tr>

        <!-- Pollara protest vote -->
        <tr class="row-artifact reveal-item">
          <td class="col-firm">
            <span class="firm-name">Pollara</span>
            <span class="commissioner">Self-commissioned</span>
          </td>
          <td class="col-dates">
            <span class="field-dates">Mar 16–25, 2026</span>
            <span class="sample">n=2,576 (remain/undecided only)</span>
          </td>
          <td>Albertans who said "remain" only</td>
          <td class="col-question">
            <span class="q-text">"Even if I don't want Alberta to separate, I'd consider voting for separatism as a way to send a message to Ottawa"</span>
            <span class="q-type">Protest vote · agree/disagree · asked of non-separatists only · projected to full sample</span>
          </td>
          <td>Agree/disagree → modeled projection</td>
          <td class="col-result">
            <span class="number-artifact">42%</span>
            <span class="number-sub">projected</span>
          </td>
          <td class="col-note">
            <span class="tag tag-artifact">Projection</span><br>
            Not a ballot question result. A modeled figure: 27% decided + 15% who agreed with protest-vote statement. Assumes 100% follow-through on stated intent. Reported in Pollara's own key findings summary alongside 27% decided vote as a comparable figure.
          </td>
        </tr>

      </tbody>
    </table>
  </div>

  <!-- DELTA CALLOUT -->
  <div class="delta-callout reveal-item">
    <div class="delta-number">
      18
      <span class="delta-unit">points</span>
    </div>
    <div class="delta-text">
      The spread between the <strong>lowest dedicated Alberta survey result</strong> (Abacus, 26%, constitutional framing,
      Feb 2026) and the <strong>highest dedicated Alberta survey result</strong> (Research Co., 31%, Jan 2026) is
      5 percentage points. The spread between the lowest dedicated result and the highest reported figure
      (Léger/CP national subsample, 47%, May 2025) is <strong>21 points</strong> — driven entirely by sample
      architecture, not separatist sentiment. Every dedicated Alberta poll conducted between September 2025
      and April 2026, regardless of firm, question wording, or field date, falls within a
      <strong>23%–31% band.</strong>
    </div>
  </div>

  <!-- ANALYSIS -->
  <div class="section-head">What the table shows</div>

  <div class="analysis-grid">

    <div class="analysis-cell reveal-item">
      <span class="cell-label">The band is stable</span>
      <p>
        Six firms asked a clean independence question of a dedicated Alberta sample
        between September 2025 and April 2026. The results: 23%, 29%, 29%, 31%, 26%, 27%.
        The range is 8 points across eight months. <strong>No firm produced a dedicated
        Alberta result above 31%.</strong> The variation within the band is within normal
        credibility intervals for online surveys.
      </p>
    </div>

    <div class="analysis-cell reveal-item">
      <span class="cell-label">The question constrains the answer</span>
      <p>
        Abacus used constitutional language ("cease to be a province") and produced
        the lowest number: 26%. Pollara used referendum language ("vote for or against")
        and produced 27%. Research Co. used "independent from Canada" and produced 31%.
        <strong>The wording difference produces a 5-point spread.</strong> The subsample
        and framing differences produce a 21-point spread.
      </p>
    </div>

    <div class="analysis-cell reveal-item">
      <span class="cell-label">The 47% is a subsample artifact</span>
      <p>
        Léger's May 16–18 national survey contained 133 unweighted Albertans — a
        subsample with an implied credibility interval of ±8.5 percentage points.
        The same firm's dedicated Alberta survey one week earlier found 29%.
        <strong>The 18-point gap between those two numbers is not a change in sentiment.
        It is the margin of error in action.</strong>
      </p>
    </div>

    <div class="analysis-cell reveal-item">
      <span class="cell-label">The 42% is a modeled projection</span>
      <p>
        Pollara's protest-vote figure is not a poll result. It is a calculation:
        the 27% decided vote plus the proportion of "remain" voters who agreed with
        a protest-vote statement, assuming 100% follow-through. Stated intent and
        ballot behaviour are not equivalent. <strong>Reported alongside 27% in Pollara's
        own key findings without methodological distinction.</strong>
      </p>
    </div>

    <div class="analysis-cell reveal-item">
      <span class="cell-label">The "5-year high" claim</span>
      <p>
        Pollara describes 27% as "the highest level recorded in over 5 years of
        tracking." Their tracker began in January 2021, at a starting figure of 23% —
        itself during the Kenney government's Fair Deal Panel, a period of
        government-organized separatist consultation. <strong>The record is measured
        against a baseline set at a moment of elevated grievance.</strong> Ipsos's
        longitudinal data shows 19% in 2001 and 25% in 2020.
      </p>
    </div>

    <div class="analysis-cell reveal-item">
      <span class="cell-label">What no poll asked</span>
      <p>
        No polling firm between September 2025 and April 2026 asked Albertans:
        "What would make separation unnecessary?" Léger's Q4 (May 2025) came closest:
        58% said federal government actions could influence their view, with
        <strong>37% movable toward staying and 21% movable toward leaving.</strong>
        The 37% figure did not appear in any headline.
      </p>
    </div>

    <div class="analysis-cell reveal-item">
      <span class="cell-label">The issue-salience gap</span>
      <p>
        Mainstreet (Feb 2026) asked Albertans their greatest issue of concern.
        <strong>9% listed "Alberta Independence."</strong> Cost of living led at 26%,
        healthcare at 22%, followed by crime, education, immigration, taxes, and
        threats to freedoms — all ahead of separation. The same survey found 30%
        would vote to separate in a referendum. A movement polling at 30% as a
        referendum intention that ranks ninth as an issue of concern is not a
        separatist movement. It is a policy lever.
      </p>
    </div>

    <div class="analysis-cell reveal-item">
      <span class="cell-label">The US scenario finding</span>
      <p>
        APP leaders reportedly discussed a US$500M transition loan and dollar-parity
        exchange with Trump officials in Washington. Mainstreet tested the dollar-parity
        scenario directly: support for separation <strong>drops 2 points</strong> when
        the US economic union is offered — from 30% to 28%. The annexation framing
        suppresses, not grows, Alberta separatism. The pipeline failure scenario
        (+3 points) outperforms the US economic union scenario (-2 points) by 5 points.
        Alberta separatism responds to federal resource policy. It does not respond
        to American financial offers.
      </p>
    </div>

  </div>

  <!-- CLOSURE -->
  <div class="closure reveal-item" id="closure">

    <div class="closure-stamp">
      The number<br>is the instrument
    </div>

    <div style="height: 24px;"></div>

    <div class="closure-sub">
      All data sourced from primary polling PDFs and firm press releases.<br>
      Léger May 16–18 subsample confirmed from primary PDF (Special Report, May 20, 2025).<br>
      Pollara April 2026 field dates from methodology appendix, Alberta Spotlight.<br>
      Ipsos field dates: January 9–14, 2026. Confederation Stress Test media release.<br><br>
      thedelusioneers.substack.com · @the_delusioneers<br>
      No returns. No refunds. No records.
    </div>
  </div>

  <!-- FOOTNOTES -->
  <div class="footnotes">
    <p>
      <strong>Sources:</strong>
      ThinkHQ Alberta Separation Survey (Sept 2025) ·
      Léger/Postmedia Alberta Separatism PDF May 14, 2025 (leger360.com) ·
      Léger Special Report May 20, 2025 — Trust in Government and Views on Provincial Sovereignty (leger360.com) ·
      Research Co. Alberta Separation Survey Jan 8, 2026 (researchco.ca) ·
      Ipsos Confederation Stress Test Media Release Jan 25, 2026 (ipsos.com) ·
      Angus Reid Alberta Independence Survey Feb 9, 2026 (angusreid.org) ·
      Mainstreet Research Alberta Survey Feb 10–12, 2026 (mainstreetresearch.ca) ·
      Abacus Data Alberta Sovereignty Survey Feb 2026 (abacusdata.ca) ·
      Pollara Alberta Spotlight April 2026 (pollara.com) ·
      AFP Fact Check: "Invented graphic flips poll results on Alberta independence support" (Feb 2026)
    </p>
  </div>

</div><!-- end .inner -->
</div><!-- end .document -->

<div class="tear-bottom"></div>

<script>
  // Progress bar
  const progressBar = document.getElementById('progressBar');
  const scrollHint = document.getElementById('scrollHint');

  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    progressBar.style.width = (scrollTop / docHeight * 100) + '%';
    if (scrollTop > 150) scrollHint.classList.add('hidden');
    else scrollHint.classList.remove('hidden');
  }, { passive: true });

  // Scroll reveal
  const revealItems = document.querySelectorAll('.reveal-item');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, 60);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

  revealItems.forEach(el => observer.observe(el));
</script>

</body>
</html>
