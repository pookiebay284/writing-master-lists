#!/usr/bin/env python3
"""Merge batch 8 into Writing-Word-Banks.html."""
from pathlib import Path

root = Path(__file__).parent
html_path = root / "Writing-Word-Banks.html"
batch_path = root / "_batch8_sections.html"

text = html_path.read_text(encoding="utf-8")
batch = batch_path.read_text(encoding="utf-8")

footer_marker = "\n\n      <footer>"
if footer_marker not in text:
    raise SystemExit("footer marker not found")
text = text.replace(footer_marker, "\n\n" + batch + footer_marker, 1)
text = text.replace("Sections 1–58.", "Sections 1–61.")

batch8_links = """      <a href="#advanced">Advanced vocab (100)</a>
      <a href="#gorgeous">Gorgeous (100)</a>
      <a href="#rarewords">Heard but hard (100)</a>
    </nav>"""

nav_instructions = """      <a href="#instructions">Giving instructions (100)</a>
    </nav>"""
nav_instructions_new = """      <a href="#instructions">Giving instructions (100)</a>
""" + batch8_links

nav_drama = """      <a href="#drama">Drama (100)</a>
    </nav>"""
nav_drama_new = """      <a href="#drama">Drama (100)</a>
      <div class="group">Dialogue &amp; craft</div>
      <a href="#condolences">Condolences (100)</a>
      <a href="#conflict">Conflict resolution (100)</a>
      <a href="#silences">Awkward silences (100)</a>
      <a href="#endconvo">Ending conversations (100)</a>
      <a href="#fragments">Sentence fragments (100)</a>
      <a href="#instructions">Giving instructions (100)</a>
""" + batch8_links

if nav_instructions in text:
    text = text.replace(nav_instructions, nav_instructions_new, 1)
elif nav_drama in text:
    text = text.replace(nav_drama, nav_drama_new, 1)
else:
    raise SystemExit("nav marker not found")

html_path.write_text(text, encoding="utf-8")
print("merged ok")
