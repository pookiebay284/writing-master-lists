#!/usr/bin/env python3
"""Merge batch 7 into Writing-Word-Banks.html."""
from pathlib import Path

root = Path(__file__).parent
html_path = root / "Writing-Word-Banks.html"
batch_path = root / "_batch7_sections.html"

text = html_path.read_text(encoding="utf-8")
batch = batch_path.read_text(encoding="utf-8")

footer_marker = "\n\n      <footer>"
if footer_marker not in text:
    raise SystemExit("footer marker not found")
text = text.replace(footer_marker, "\n\n" + batch + footer_marker, 1)
text = text.replace("Sections 1–52.", "Sections 1–58.")

nav_old = """      <a href="#drama">Drama (100)</a>
    </nav>"""
nav_new = """      <a href="#drama">Drama (100)</a>
      <div class="group">Dialogue &amp; craft</div>
      <a href="#condolences">Condolences (100)</a>
      <a href="#conflict">Conflict resolution (100)</a>
      <a href="#silences">Awkward silences (100)</a>
      <a href="#endconvo">Ending conversations (100)</a>
      <a href="#fragments">Sentence fragments (100)</a>
      <a href="#instructions">Giving instructions (100)</a>
    </nav>"""
if nav_old not in text:
    raise SystemExit("nav marker not found")
text = text.replace(nav_old, nav_new, 1)

html_path.write_text(text, encoding="utf-8")
print("merged ok")
