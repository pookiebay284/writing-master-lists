#!/usr/bin/env python3
"""Merge batch 12 into Writing-Word-Banks.html."""
from pathlib import Path

root = Path(__file__).parent
html_path = root / "Writing-Word-Banks.html"
batch_path = root / "_batch12_sections.html"

text = html_path.read_text(encoding="utf-8")
batch = batch_path.read_text(encoding="utf-8")

footer_marker = "\n\n      <footer>"
if footer_marker not in text:
    raise SystemExit("footer marker not found")
text = text.replace(footer_marker, "\n\n" + batch + footer_marker, 1)
text = text.replace("Sections 1–81.", "Sections 1–93.")

batch12_links = """      <a href="#perception">Perception (100)</a>
      <a href="#heartbreaking">Heartbreaking (100)</a>
      <a href="#please">Please (100)</a>
      <a href="#embarrassing">Embarrassing (100)</a>
      <a href="#butalts">But (100)</a>
      <a href="#otherhand">On the other hand (100)</a>
      <a href="#feelings">Feelings (100)</a>
      <a href="#reflective">Reflective writing (100)</a>
      <a href="#openings">Paragraph openings (100)</a>
      <a href="#scarier">Scarier (100)</a>
      <a href="#relief">Relief (100)</a>
      <a href="#ibelieve">I believe (100)</a>
    </nav>"""

nav_vital = """      <a href="#vital">Vital (100)</a>
    </nav>"""
nav_vital_new = """      <a href="#vital">Vital (100)</a>
""" + batch12_links

if nav_vital in text:
    text = text.replace(nav_vital, nav_vital_new, 1)
else:
    raise SystemExit("nav marker not found")

html_path.write_text(text, encoding="utf-8")
print("merged ok")
