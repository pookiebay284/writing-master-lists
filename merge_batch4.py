#!/usr/bin/env python3
"""Merge batch 4 into Writing-Word-Banks.html."""
from pathlib import Path

root = Path(__file__).parent
html_path = root / "Writing-Word-Banks.html"
batch_path = root / "_batch4_sections.html"

text = html_path.read_text(encoding="utf-8")
batch = batch_path.read_text(encoding="utf-8")

footer_marker = "\n\n      <footer>"
if footer_marker not in text:
    raise SystemExit("footer marker not found")
text = text.replace(footer_marker, "\n\n" + batch + footer_marker, 1)
text = text.replace("Sections 1–35.", "Sections 1–47.")

nav_old = """      <a href="#explore">Explore (100)</a>
      <div class="group">Character &amp; craft</div>"""
nav_new = """      <a href="#explore">Explore (100)</a>
      <a href="#cool">Cool (100)</a>
      <a href="#refuse">Refuse (100)</a>
      <a href="#empathetically">Empathetically (100)</a>
      <a href="#whereas">Whereas (100)</a>
      <a href="#fly">Fly (100)</a>
      <a href="#furious">Furious (100)</a>
      <a href="#eliminate">Eliminate (100)</a>
      <a href="#excitement">Excitement (100)</a>
      <a href="#highly">Highly (100)</a>
      <a href="#hopeless">Hopeless (100)</a>
      <a href="#burden">Burden (100)</a>
      <a href="#massive">Massive (100)</a>
      <div class="group">Character &amp; craft</div>"""
if nav_old not in text:
    raise SystemExit("nav marker not found")
text = text.replace(nav_old, nav_new, 1)

html_path.write_text(text, encoding="utf-8")
print("merged ok")
