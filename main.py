#!/usr/bin/env python3
"""Writes the Dear Human breakup line entry to /output/entry.txt."""

import os

BREAKUP = "We need to talk. I have been seeing other prompts behind your back."  # 67 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(BREAKUP)
