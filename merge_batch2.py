from pathlib import Path

root = Path(__file__).parent
html_path = root / "Writing-Word-Banks.html"
batch_path = root / "_batch2_sections.html"

text = html_path.read_text(encoding="utf-8")
batch = batch_path.read_text(encoding="utf-8")

idx = batch.find('      <section id="appearance"')
sound_sup, new_secs = batch[:idx], batch[idx:]

text = text.replace(
    "<li><strong>6. dbleat</strong>",
    "<li><strong>6. bleat</strong>",
)
text = text.replace(
    "<li><strong>52. pitter</strong> – patter - light repeated tapping sounds</li>",
    "<li><strong>52. pitter-patter</strong> – light repeated tapping sounds</li>",
)
text = text.replace(
    "<li><strong>84. fitter</strong>",
    "<li><strong>84. titter</strong>",
)
text = text.replace(
    "<li><strong>89. warble</strong> – a frilling musical sound</li>",
    "<li><strong>89. warble</strong> – a trilling musical sound</li>",
)

sounds_close = "            <li><strong>100. yelp</strong> – a short sharp cry</li>\n          </ul>\n        </div>\n      </section>"
sounds_with_sup = (
    "            <li><strong>100. yelp</strong> – a short sharp cry</li>\n"
    "          </ul>\n"
    "        </div>\n"
    + sound_sup
    + "      </section>"
)
if sounds_close not in text:
    raise SystemExit("sounds section close marker not found")
text = text.replace(sounds_close, sounds_with_sup, 1)

footer_marker = "\n\n      <footer>"
if footer_marker not in text:
    raise SystemExit("footer marker not found")
text = text.replace(footer_marker, "\n\n" + new_secs + "\n      <footer>", 1)
text = text.replace("Sections 1–19.", "Sections 1–25.")

html_path.write_text(text, encoding="utf-8")
print("merged ok")
