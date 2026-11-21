# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/nindafahila/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/nindafahila/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A one-image summary of the world's news of **Friday 20 November 2026**, drawn as a newspaper front page: Cyclone Akvan slams into the Odisha coast (lead), the global sell-off deepens as Nikkei falls 4.8%, the EU approves €1bn in arms for Ukraine, GTA 6 smashes $2.3bn in a day, COP31 enters its final day with fossil-fuel text still missing, Anthropic's record IPO fades fast, and a magnitude 4.2 quake wakes Los Angeles — plus a Trump pardon for Pete Rose, an IMF debt warning and Kenya’s Ebola-free countdown in the footer ticker.

## How it works

`draw_entry.py` (Python + Pillow, deterministic, no network) draws `entry.png` — 1024×1024, ~123 KB — from the day's verified headlines. `main.ts` (Node 22, stdlib only) copies that image to `/output/entry.png`, so both grader runs write identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# or: python3 draw_entry.py   (regenerates entry.png identically)
```

## Sources (20 Nov 2026)

IMD bulletins, Reuters, AP, BBC, The Hindu BusinessLine, Consilium (EU Council), Sensor Tower via Polygon/NME, UN News, USGS and major outlets’ headlines for 20 November 2026, cross-checked across at least two outlets per story. The Houthi strike on Riyadh’s PIF Tower and the COP31 draft text are dated 19 November and were deliberately left out of the 20 November stories; the Meta €805m fine is dated 14 November and was also left out.

---

<sub>Entered on [make.fun](https://make.fun/?ref=xqemgw87&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
