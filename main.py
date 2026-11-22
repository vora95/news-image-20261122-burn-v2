#!/usr/bin/env python3
"""THE SUNDAY WIRE - news-image-20261122 (burn v2).

A one-page wire-service front page summing up the world news of Sunday
22 November 2026: three verified leads in full-width rows (COP31 deal,
Russia's 400-drone barrage on Ukraine, Iran's strikes on US bases in
Bahrain), ten medium stories, a dotted world map, 25 more stories, and a
DATE CHECK box listing what was left out on purpose.

Python 3.13, standard library only. Copies entry.png to the output dir.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
print("copied entry to", OUT)
