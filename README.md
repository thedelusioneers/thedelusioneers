# THE DELUSIONEERS — NEWSROOM
Claude Code multi-agent production pipeline. Internal. Not for publication.

## What this is

A repeatable agent sequence mapping the Delusioneers SOP to Claude Code
subagents. The main session is the Desk Editor (judgment); five subagents are
the desks (procedure). Cheap models do procedure; intelligence is spent only
where judgment lives.

| Desk | Agent file | Model | Job |
|---|---|---|---|
| Desk Editor | main session (CLAUDE.md) | your choice at launch | assignment, gates, dispatch |
| Documents | documents-desk.md | sonnet | primary sourcing |
| Verification | verification-desk.md | haiku | claim checking |
| Copy | copy-desk.md | sonnet | all prose |
| Art | art-desk.md | sonnet | HTML + cards + Stub image |
| Distribution | distribution-desk.md | haiku | platform packaging |

## Setup

1. Install Claude Code: `npm install -g @anthropic-ai/claude-code`
2. Clone/copy this repo, `cd` into it, run `claude`
3. Agents in `.claude/agents/` load at session start. If you edit one on disk
   mid-session, restart the session (or use `/agents` to edit live).
4. First run only: `pip install playwright --break-system-packages && playwright install chromium`

## Running a piece

```
mkdir pipeline/<slug>
cp pipeline/_templates/assignment-brief.md pipeline/<slug>/01-assignment.md
```

Then, in the Claude Code session:
1. Draft the brief together. **Gate A: you approve it.**
2. "Use the documents-desk subagent on pipeline/<slug>/01-assignment.md"
3. "Use the verification-desk subagent on pipeline/<slug>/02-source-package.md"
   — if BOUNCE REQUIRED: YES, send the report back to documents-desk; repeat.
4. **Gate B: you review the verification report.**
5. "Use the copy-desk subagent on pipeline/<slug>"
6. "Use the art-desk subagent on pipeline/<slug>"
7. "Use the distribution-desk subagent on pipeline/<slug>"
8. **Gate C: standards check. You deploy. You post. Nothing automated past here.**

## Design principles (why it's built this way)

- **Hard boundaries beat instructed boundaries.** Each desk receives only its
  contract files. Verification can't rewrite copy because it never sees copy.
- **One loop only.** Verification ↔ Documents. Everything else is linear.
- **Judgment is centralized.** Stub variant, scope, spillway test, named
  distinctions — all decided at Gate A, executed downstream, revisited nowhere.
- **Closed-world writing.** Copy-desk's universe is the verified package. A fact
  outside it does not exist, which is what makes weak models safe to use.
- **Contracts stay minimal.** Claims and source IDs travel between desks; the
  doctrine does not — it's compiled into each agent definition.

## Cost note

Multi-agent runs use roughly 4–7× the tokens of a single session. The desks are
for production runs, not exploration. Think in this Project on claude.ai;
produce here.

## Maintenance

New technical patterns → `reference/sop-changelog.md` after Gate C. When a
pattern stabilizes, fold it into the relevant reference file or agent
definition. The agent files are the SOP now; keep them current.
