# -*- coding: utf-8 -*-
import os, json
_here = os.path.dirname(os.path.abspath(__file__))
_dd = os.path.join(_here, "data")

DATE_ISO = "2026-08-02"
DATE_HUMAN = "Sunday, August 2, 2026"
PREV_ISO = "2026-08-01"
MIN_ISO = "2026-03-19"

def _load(name):
    p = os.path.join(_dd, name)
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def _norm(items):
    out = []
    for it in items:
        out.append({
            "hero": bool(it.get("hero", False)),
            "sub": it.get("sub", ""),
            "h3": it["h3"],
            "summary": it["summary"],
            "body": it["body"],
            "sources": [(s[0], s[1]) for s in it["sources"]],
        })
    return out

_a = _load("data_a.json")
_b = _load("data_b.json")
_c = _load("data_c.json")
_d = _load("data_d.json")

MOOD = _a["mood"]

DATA = {
    "global": _norm(_a["global"]),
    "netherlands": _norm(_a["netherlands"]),
    "ai-hpc": _norm(_b["ai-hpc"]),
    "crypto-macro": _norm(_c["crypto-macro"]),
    "mental-health": _norm(_c["mental-health"]),
    "sports": _norm(_d["sports"]),
    "consumer-tech": _norm(_d["consumer-tech"]),
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
