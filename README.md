# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/nindafahila/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/nindafahila/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One picture that sums up **Friday 20 November 2026**, laid out like a newspaper front page. The lead is Cyclone Akvan hitting the Odisha coast; below it, six more stories — the deepening global sell-off (Nikkei −4.8%), the EU's €1bn arms approval for Ukraine, GTA 6's $2.3bn first day, COP31's final day with fossil-fuel wording still missing, Anthropic's record IPO fading fast, and the magnitude 4.2 quake that woke Los Angeles. A footer ticker adds the Trump pardon for Pete Rose, the IMF's debt warning and Kenya's Ebola-free countdown.

## How it works

`draw_entry.py` draws `entry.png` with Python + Pillow: fully deterministic, no network, 1024×1024 and about 123 KB. `main.ts` (Node 22, standard library only) copies that image to `/output/entry.png`, so the grader gets identical bytes on both runs.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# or: python3 draw_entry.py   (draws entry.png again, byte-identical)
```

## Sources (20 Nov 2026)

IMD bulletins, Reuters, AP, BBC, The Hindu BusinessLine, the EU Council (Consilium), Sensor Tower via Polygon and NME, UN News, USGS and other major outlets — every story checked against at least two outlets for 20 November 2026. Two stories were deliberately kept out because they belong to 19 November: the Houthi strike on Riyadh's PIF Tower and the COP31 draft text; the Meta €805m fine (14 November) was left out for the same reason.

---

<sub>Entered on [make.fun](https://make.fun/?ref=xqemgw87&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
