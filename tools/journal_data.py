# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sec_a import GLOBAL, NETHERLANDS, MOOD
from _sec_b import AI_HPC
from _sec_c import CRYPTO_MACRO, MENTAL_HEALTH
from _sec_d import SPORTS, CONSUMER_TECH

DATE_ISO = "2026-07-12"
DATE_HUMAN = "Sunday, July 12, 2026"
PREV_ISO = "2026-07-11"
MIN_ISO = "2026-03-19"

DATA = {
    "global": GLOBAL,
    "netherlands": NETHERLANDS,
    "ai-hpc": AI_HPC,
    "crypto-macro": CRYPTO_MACRO,
    "mental-health": MENTAL_HEALTH,
    "sports": SPORTS,
    "consumer-tech": CONSUMER_TECH,
}

SECTIONS = [
    ("global", "Global News", "#1B998B"),
    ("netherlands", "Netherlands", "#E8703A"),
    ("ai-hpc", "AI & HPC", "#7B2D8E"),
    ("crypto-macro", "Crypto & Macro", "#E8B130"),
    ("mental-health", "AI & Mental Health", "#D63B47"),
    ("sports", "Sports", "#2478A0"),
    ("consumer-tech", "Consumer Tech", "#3D5A80"),
]
