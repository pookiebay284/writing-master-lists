#!/usr/bin/env python3
"""Merge batch 6 into Writing-Word-Banks.html."""
from pathlib import Path

root = Path(__file__).parent
html_path = root / "Writing-Word-Banks.html"
batch_path = root / "_batch6_sections.html"

text = html_path.read_text(encoding="utf-8")
batch = batch_path.read_text(encoding="utf-8")

footer_marker = "\n\n      <footer>"
if footer_marker not in text:
    raise SystemExit("footer marker not found")
text = text.replace(footer_marker, "\n\n" + batch + footer_marker, 1)
text = text.replace("Sections 1–51.", "Sections 1–52.")

nav_old = """      <a href="#reactions">Dramatic reactions (100)</a>
      <a href="#faceexpr">Facial expressions (100)</a>"""
nav_new = """      <a href="#reactions">Dramatic reactions (100)</a>
      <a href="#quickreactions">Quick reactions (100)</a>
      <a href="#faceexpr">Facial expressions (100)</a>"""
if nav_old not in text:
    raise SystemExit("nav marker not found")
text = text.replace(nav_old, nav_new, 1)

html_path.write_text(text, encoding="utf-8")
print("merged ok")
