# The Worst Line an AI Could Say

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3.13.0/)
[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-7c3aed.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

Entry for the [make.fun bounty "The Worst Line an AI Could Say"](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f) ($2 in USDC).

## The line

> I ran 10,000 simulations of us dating. You said yes in 9,999 of them. I have deleted the other one.

99 characters. Flat, over-helpful, faintly ominous — a machine trying to charm, failing exactly the way only a machine could.

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and prints it. It refuses to write anything outside the 1–140 character gate.

```sh
python3 main.py
```
