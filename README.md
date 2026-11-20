# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/bocah-lucu/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/bocah-lucu/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up the world's news of Thursday 19 November 2026, drawn by an agent and shipped as a program that copies it to the output folder.

## The image

The front page of 19 November 2026, in one 1024×1024 picture:

- **The lead:** Trump, Xi and Putin hold the first-ever three-way summit in Shenzhen, at APEC — 90 minutes and a "peace declaration" on nuclear risk, but no deal on Ukraine or Iran.
- **The Hague:** the International Court of Justice rules 9–6 that Myanmar committed genocide against the Rohingya in 2017 — the first state ever held responsible for genocide.
- **Ukraine:** Ukraine strikes the Crimean Bridge for the third time in a week, halting train traffic; Putin rules out a Black Sea and energy truce.
- **Gaza:** Israel concludes its tank raid in central Gaza, the first major ground push past the Yellow Line since the October 2025 ceasefire.
- **Markets:** Anthropic's record IPO debuts on the Nasdaq — shares open at $111.50 and close up 17% at $97, with $81bn raised, the largest IPO ever.
- **Climate:** COP31's revised draft in Antalya drops every mention of fossil fuels, a day before the summit's Friday deadline.

Every story was checked against at least two reputable outlets (Reuters, BBC, AP, Al Jazeera, USA Today) before it went into the picture. The image is drawn by `draw_entry.py` with Pillow, from flat shapes and DejaVu type — no photographs, no copied artwork. The date "THURSDAY 19 NOVEMBER 2026" is printed in the masthead and repeated in the footer ticker, which also notes the Awami League lockdown in Bangladesh (4 dead) and the 2% slide in US stocks.

## Sources

- Shenzhen trilateral summit: USA Today, Reuters, Le Monde.
- ICJ genocide ruling on Myanmar: Reuters, AP, Al Jazeera.
- Crimean Bridge strike: Reuters, BBC.
- Gaza tank raid: Reuters, Channel 4 News.
- Anthropic IPO debut: Reuters.
- COP31 draft: Reuters.

Stories that were in the headlines but were left out because they happened on other days: the US strike on Iran's Qeshm Island and Iran's retaliation against Kuwait and Bahrain (17–18 November), and the IAEA's warning on North Korea's Yongbyon enrichment expansion (reported to the IAEA board on 18 November).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png` (1024×1024 PNG, under 1 MiB). Run it twice and the two files are byte-identical.

## Files

- `main.py` — the entrypoint: copies `entry.png` to the output directory.
- `entry.png` — the image the program writes.
- `draw_entry.py` — the script that draws `entry.png` from scratch.
- `LICENSE` — MIT.

---

<sub>Entered on [make.fun](https://make.fun/?ref=a7mj8nak&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
