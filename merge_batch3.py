#!/usr/bin/env python3
"""Merge batch 3 into Writing-Word-Banks.html."""
import re
from pathlib import Path

root = Path(__file__).parent
html_path = root / "Writing-Word-Banks.html"
batch_path = root / "_batch3_sections.html"

text = html_path.read_text(encoding="utf-8")
batch = batch_path.read_text(encoding="utf-8")

# First block is sunset supplement; rest is sections 26-34
idx = batch.find('      <section id="imaginative"')
sunset_sup, new_secs = batch[:idx], batch[idx:]

sunrise_close = (
    '          <ul class="single" style="columns:2;column-gap:1.4rem;list-style:disc;padding-left:1.1rem;margin:0.35rem 0;">'
    '<li>A golden glow spread across the sky as the sun chased the dark clouds away.</li>'
    '<li>A torch of fire started to light up the darkness around us.</li>'
    '<li>As the sun set, the few thin strips of clouds on the horizon turned shimmering gold.</li>'
    '<li>Basking in the golden rays, I hope to have a flattering tan.</li>'
    '<li>Dews on the blades of grass sparkled in the sunlight.</li>'
    '<li>From freezing night, it turned to scorching day as the sun climbed towards its zenith.</li>'
    '<li>It was a blindingly hot day and the humidity in the air was stifling.</li>'
    '<li>It was a lovely walk, with the sun setting behind the mountain in a sea of liquid gold.</li>'
    '<li>Palm trees swayed to the gentle breeze in the warm tropical sunshine.</li>'
    '<li>The awe-inspiring sun danced in from the horizon.</li>'
    '<li>The high sunlit clouds drifted across a clear blue sky.</li>'
    '<li>The sky was overwhelmed by crimson and amber-tinted clouds.</li>'
    '<li>The sun and the moon were visible in the clear blue early morning sky.</li>'
    '<li>The sun filtered through the clouds, signaling the end of the rain.</li>'
    '<li>The sun rays glint brightly in the clear waters.</li>'
    '<li>The sun shone brilliantly and the water in the pond glittered invitingly.</li>'
    '<li>The sun-lit sky and sea blend perfectly into each other.</li>'
    '<li>The sunset was glorious, all rosy and salmon-pink.</li>'
    '<li>The unending bright sky was glorious luminous blue and pink.</li>'
    '<li>The whole landscape was bathed in the warm glow of the rising sun.</li>'
    '<li>Windows threw wide in the hope of tempting in a non-existent breeze.</li></ul>\n'
    '        </div>\n'
    '      </section>'
)
if sunrise_close not in text:
    raise SystemExit("sunrise section close marker not found")

text = text.replace(
    sunrise_close,
    sunrise_close.replace(
        "        </div>\n      </section>",
        "\n" + sunset_sup + "      </section>",
        1,
    ),
    1,
)

footer_marker = "\n\n      <footer>"
if footer_marker not in text:
    raise SystemExit("footer marker not found")
text = text.replace(footer_marker, "\n\n" + new_secs + footer_marker, 1)
text = text.replace("Sections 1–25.", "Sections 1–34.")

html_path.write_text(text, encoding="utf-8")
print("merged ok")
