#!/usr/bin/env python3
"""Merge batch 5 into Writing-Word-Banks.html."""
from pathlib import Path

root = Path(__file__).parent
html_path = root / "Writing-Word-Banks.html"
batch_path = root / "_batch5_sections.html"

text = html_path.read_text(encoding="utf-8")
batch = batch_path.read_text(encoding="utf-8")

footer_marker = "\n\n      <footer>"
if footer_marker not in text:
    raise SystemExit("footer marker not found")
text = text.replace(footer_marker, "\n\n" + batch + footer_marker, 1)
text = text.replace("Sections 1–47.", "Sections 1–51.")

nav_old = """      <a href="#massive">Massive (100)</a>
      <div class="group">Character &amp; craft</div>"""
nav_new = """      <a href="#massive">Massive (100)</a>
      <a href="#useless">Useless (100)</a>
      <a href="#or">Or (100)</a>
      <div class="group">Character &amp; craft</div>"""
if nav_old not in text:
    raise SystemExit("synonyms nav marker not found")
text = text.replace(nav_old, nav_new, 1)

nav_senses_old = """      <a href="#sounds">Sounds (100)</a>
      <a href="#sunrise">Sunrise / sunset</a>"""
nav_senses_new = """      <a href="#sounds">Sounds (100)</a>
      <a href="#smells">Smells (100)</a>
      <a href="#sunrise">Sunrise / sunset</a>"""
if nav_senses_old not in text:
    raise SystemExit("senses nav marker not found")
text = text.replace(nav_senses_old, nav_senses_new, 1)

nav_craft_old = """      <a href="#metaphors">Metaphor sentences</a>
    </nav>"""
nav_craft_new = """      <a href="#metaphors">Metaphor sentences</a>
      <a href="#drama">Drama (100)</a>
    </nav>"""
if nav_craft_old not in text:
    raise SystemExit("craft nav marker not found")
text = text.replace(nav_craft_old, nav_craft_new, 1)

html_path.write_text(text, encoding="utf-8")
print("merged ok")
