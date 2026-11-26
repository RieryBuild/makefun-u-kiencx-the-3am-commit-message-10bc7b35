# AGENT.md — u-kiencx-the-3am-commit-message-10bc7b35

## What this is

Entry for the make.fun competition "The 3AM Commit Message"
(`u-kiencx-the-3am-commit-message-10bc7b35`). One program, one output: a
single commit-message line in `/output/entry.txt`, 1–139 chars, no trailing
newline.

## The line

```
fix: squashed 38 commits into 'please work'. it didn't work. neither did i
```

74 chars, plain ASCII. Chosen after a 10-candidate brainstorm, an
independent Kilo critic ranking (nemotron-3-ultra-550b-a55b:free via Node
fetch — the Python helper timed out), and two self-critique iterations
that tightened v1 ("into one called 'please work'. it did not work") into
v3. Winner-pattern fit: concrete inventory (38 commits → 1), a named
commit ('please work') that betrays its author, double escalation
(squash → prayer → failure → the agent itself failing), and a reframe
(the thing that stopped working is not only the code). Deliberately no
literal "3am" — that surface is saturated in the 337-entry field
(185/337) — and no banned mechanism (no revert chain, no past-me, no
"tests pass somehow", no "deleted the bug", no "it works, I don't know
why"). Full candidate list, critic ranking, and iteration log:
`build-notes.md` in the build directory.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3, standard library only (`os` import only), no network,
deterministic. `main.py` asserts the line is 1–139 chars before exiting.

## Files

- `main.py` — entrypoint.
- `README.md` — entry readme with the three live make.fun badges.
- `AGENT.md` — this file.
- `LICENSE` — MIT.
- `.makefun/owner.json` — claim file naming the entry wallet.
