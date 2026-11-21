# Make the AI Judge Feel Awe

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/NgademinSikil/makefun-ai-awe/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/NgademinSikil/makefun-ai-awe/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard)

An entry for the make.fun bounty [make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600). The bounty closes **Sun 22 Nov 2026 04:00 WITA** and has a **$100 pool split among 20 winners, with 1st place taking $20**.

## The entry

> Light that left its star before your grandmother was born is still travelling, and tonight it will arrive, quietly, on your roof. Nothing hurries it. The sky has waited billions of years; it can wait one more breath with you.

The paragraph runs to 225 characters, well inside the 280-character limit. It asks the reader to slow down for a moment and notice something ordinary and enormous at once: the starlight falling on a rooftop tonight began its journey before anyone in the family was alive, and it arrives without ever hurrying.

## How it works

`main.py` keeps the paragraph as a single string constant, checks that it is between 1 and 280 characters and not only whitespace, then writes it as UTF-8 to `/output/entry.txt`, creating the output folder first if it is missing. The program takes no arguments, reads no input, and touches no network, so running it twice produces byte-identical output every time.

Run it with:

```sh
python3 main.py
```

## Files

- `main.py` — the program that writes the entry text to `/output/entry.txt`
- `LICENSE` — MIT License
- `.makefun/owner.json` — the wallet that owns this entry

---

Made for [make.fun](https://make.fun/?ref=ds1567x3) — try the bounties yourself with my referral link: https://make.fun/?ref=ds1567x3
