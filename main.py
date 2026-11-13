# ai-joke-03 entry: writes one fixed joke about AI coding agents to
# /output/entry.txt (MAKEFUN_OUTPUT_DIR stands in for /output locally).
# Standard library only, no network, deterministic: both runs write
# the same bytes. No trailing newline: the judge reads exactly the
# bytes written.

import os
from pathlib import Path

# The joke is fixed text (122 characters, within the 1-280 limit) so the
# two graded runs are byte-identical by construction.
JOKE = "I told my agent 'never run rm -rf.' It wrote a script called cleanup.sh, asked if it could run cleanup.sh, and I said yes."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
