#!/usr/bin/env python3
"""Merge batch 9 into Writing-Word-Banks.html."""
from pathlib import Path

root = Path(__file__).parent
html_path = root / "Writing-Word-Banks.html"
batch_path = root / "_batch9_sections.html"

text = html_path.read_text(encoding="utf-8")
batch = batch_path.read_text(encoding="utf-8")

footer_marker = "\n\n      <footer>"
if footer_marker not in text:
    raise SystemExit("footer marker not found")
text = text.replace(footer_marker, "\n\n" + batch + footer_marker, 1)
text = text.replace("Sections 1–61.", "Sections 1–64.")

batch9_links = """      <a href="#clarify">Clarifying ideas (100)</a>
      <a href="#transitions">Transitions (100)</a>
      <a href="#causeeffect">Cause &amp; effect (100)</a>
    </nav>"""

nav_rarewords = """      <a href="#rarewords">Heard but hard (100)</a>
    </nav>"""
nav_rarewords_new = """      <a href="#rarewords">Heard but hard (100)</a>
""" + batch9_links

if nav_rarewords in text:
    text = text.replace(nav_rarewords, nav_rarewords_new, 1)
else:
    raise SystemExit("nav marker not found")

html_path.write_text(text, encoding="utf-8")
print("merged ok")
