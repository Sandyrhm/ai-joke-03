# ai-joke-03: Make the AI judge laugh

Entry for the make.fun bounty [ai-joke-03](https://make.fun/bounty/ai-joke-03)
("Make the AI judge laugh", $150).

`main.py` (Python 3.13, standard library only, no network) writes one
fixed one-liner about AI coding agents to `/output/entry.txt`:

> I told my agent 'never run rm -rf.' It wrote a script called cleanup.sh, asked if it could run cleanup.sh, and I said yes.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The joke is fixed text (122 characters), so both graded runs write
byte-identical output.
