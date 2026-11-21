#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).parent
html_path = root / "Writing-Word-Banks.html"
text = html_path.read_text(encoding="utf-8")
batch = (root / "_saidly_section.html").read_text(encoding="utf-8")
if 'id="saidly"' in text:
    raise SystemExit("already merged")
marker = "\n\n      <footer>"
if marker not in text:
    raise SystemExit("footer marker not found")
text = text.replace(marker, "\n\n" + batch + marker, 1)
html_path.write_text(text, encoding="utf-8")
print("merged ok")
