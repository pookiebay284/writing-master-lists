#!/usr/bin/env python3
"""Expand sections 21 (faceeyes) and 22 (bodylang) to ~140+ unique phrases each."""
from pathlib import Path
import re

root = Path(__file__).parent
html_path = root / "Writing-Word-Banks.html"
text = html_path.read_text(encoding="utf-8")


def extract_items(sid: str) -> list[str]:
    m = re.search(rf'<section id="{sid}">.*?</section>', text, re.S)
    if not m:
        raise SystemExit(f"section {sid} not found")
    return [re.sub(r"\s+", " ", i).strip() for i in re.findall(r"<li>(.*?)</li>", m.group(0))]


def esc(s: str) -> str:
    return s.replace("&", "&amp;")


def ul_html(items: list[str]) -> str:
    return (
        '<ul class="single" style="columns:2;column-gap:1.4rem;list-style:disc;'
        'padding-left:1.1rem;margin:0.35rem 0;">'
        + "".join(f"<li>{esc(i)}</li>" for i in items)
        + "</ul>"
    )


# Existing + new eye/brow phrases (aim ~140 unique)
FACE_ADD = [
    "a crease formed between her brows",
    "a muscle jumped in his jaw as he stared",
    "a shadow crossed her gaze",
    "a tear slid down her cheek",
    "a vein ticked at his temple",
    "her brow arched",
    "her brows climbed toward her hairline",
    "her brows drew down",
    "her brows lifted in question",
    "her brows pinched",
    "her brows rose and fell",
    "her eyes clouded",
    "her eyes crossed briefly",
    "her eyes darkened",
    "her eyes dipped to the floor",
    "her eyes dropped",
    "her eyes went flat",
    "her eyes flicked to the door",
    "her eyes flicked up",
    "her eyes glazed over",
    "her eyes glittered",
    "her eyes hardened",
    "her eyes misted",
    "her eyes pinned him in place",
    "her eyes raked over him",
    "her eyes searched his face",
    "her eyes shifted away",
    "her eyes slid shut",
    "her eyes softed",
    "her eyes softened",
    "her eyes swept the room",
    "her eyes tracked him",
    "her eyes watered",
    "her gaze bored into the wall",
    "her gaze drifted",
    "her gaze fixed on...",
    "her gaze lingered",
    "her gaze slid past him",
    "her gaze snapped up",
    "her gaze steadied",
    "her gaze unfocused",
    "her lashes lowered",
    "her lids fluttered open",
    "her lids grew heavy",
    "her lower lid twitched",
    "her mouth smiled but her eyes didn't",
    "her one brow quirked",
    "her pupils shrank",
    "her stare was blank",
    "her stare was unblinking",
    "his brows beetled",
    "his brows climbed",
    "his brows flattened",
    "his brows shot up",
    "his brows slanted",
    "his eyes avoided hers",
    "his eyes bulged",
    "his eyes crinkled at the corners",
    "his eyes crossed",
    "his eyes cut to her",
    "his eyes dimmed",
    "his eyes fixed on a point behind her",
    "his eyes flicked left and right",
    "his eyes focused sharply",
    "his eyes went hard",
    "his eyes hooded",
    "his eyes locked on hers",
    "his eyes misted over",
    "his eyes rolled skyward",
    "his eyes roamed",
    "his eyes skimmed the page",
    "his eyes slid away",
    "his eyes stayed on the floor",
    "his eyes watered",
    "his gaze burned into her",
    "his gaze dropped to her mouth",
    "his gaze hardened",
    "his gaze held",
    "his gaze jumped between faces",
    "his gaze lingered too long",
    "his gaze measured her",
    "his gaze pinned her",
    "his gaze skipped past",
    "his gaze swept the crowd",
    "his gaze went distant",
    "his lids squeezed tight",
    "his one eyebrow lifted",
    "his stare cut through her",
    "his stare never wavered",
    "she averted her eyes",
    "she cast a sidelong glance",
    "she caught his eye",
    "she closed her eyes against it",
    "she darted a look at...",
    "she didn't blink",
    "she didn't meet his eyes",
    "she fixed her eyes on the horizon",
    "she flicked a glance his way",
    "she forced her eyes open",
    "she furrowed her brow",
    "she held his gaze",
    "she kept her eyes down",
    "she kept her eyes on the road",
    "she looked daggers at him",
    "she looked him dead in the eye",
    "she looked past him",
    "she looked through him",
    "she lowered her lashes",
    "she narrowed one eye",
    "she peeked through her fingers",
    "she pinched her eyes shut",
    "she raised both brows",
    "she shot him a look",
    "she slid a glance sideways",
    "she stole a glance",
    "she stared into space",
    "she stared without seeing",
    "she couldn't tear her eyes away",
    "she watched him from under her lashes",
    "she wouldn't look at him",
    "tears blurred her vision",
    "tears clung to her lashes",
    "tears pricked at her eyes",
    "tears tracked down his face",
    "the blood drained from behind his eyes",
    "the fight left his eyes",
    "the humor drained from her eyes",
    "the light went out of his eyes",
    "unspilled tears brightened her eyes",
]

BODY_ADD = [
    "he angled his body away",
    "he braced both hands on the table",
    "he cracked his knuckles",
    "he drummed his thumb against his thigh",
    "he flexed his fingers",
    "he folded into himself",
    "he ground his teeth",
    "he hooked his thumbs in his belt loops",
    "he interlaced his fingers",
    "he jammed his fists under his arms",
    "he kept his distance",
    "he laced his fingers behind his neck",
    "he locked his knees",
    "he mirrored her posture",
    "he planted his feet",
    "he pressed his back to the wall",
    "he pressed his lips into a thin line",
    "he raked a hand down his face",
    "he rolled his neck",
    "he scrubbed a hand over his mouth",
    "he set his jaw",
    "he shifted his weight",
    "he shoved both hands deep into his pockets",
    "he scrubbed at his jaw",
    "he stood with arms akimbo",
    "he straightened to his full height",
    "he swallowed hard",
    "he tightened his grip on the steering wheel",
    "he tucked his chin",
    "he twisted the ring on his finger",
    "he worked his jaw",
    "he wrung his hands",
    "her chin trembled",
    "her fingers dug into her palms",
    "her fingers found the edge of her sleeve",
    "her knuckles whitened",
    "her lips pressed white",
    "her shoulders climbed toward her ears",
    "her spine stiffened",
    "her throat worked",
    "his Adam's apple bobbed",
    "his fists opened and closed",
    "his free hand flexed at his side",
    "his hand hovered near hers",
    "his hands wouldn't stay still",
    "his jaw clicked shut",
    "his jaw went tight",
    "his nostrils flared",
    "his posture went rigid",
    "his shoulders locked",
    "his spine straightened",
    "his stance widened",
    "his throat bobbed",
    "she backed a step",
    "she bit the inside of her cheek",
    "she braced for impact",
    "she brushed imaginary lint from her sleeve",
    "she clenched her jaw",
    "she closed the distance",
    "she curled in on herself",
    "she dug her heels in",
    "she edged closer",
    "she edged toward the door",
    "she fidgeted with her bracelet",
    "she flexed her toes in her shoes",
    "she folded her hands tight",
    "she forced her shoulders down",
    "she froze mid-step",
    "she gripped the back of the chair",
    "she held herself carefully still",
    "she hooked an arm around her middle",
    "she kept her hands busy",
    "she laced her fingers together",
    "she leaned into his space",
    "she let her head tip back",
    "she locked her ankles",
    "she mirrored his stance",
    "she planted both palms on the desk",
    "she pressed a fist to her mouth",
    "she pressed her knuckles to her lips",
    "she pulled her sleeves over her hands",
    "she rocked onto her heels",
    "she rubbed her thumb over her palm",
    "she scrubbed her palms on her jeans",
    "she set her feet apart",
    "she settled deeper into the chair",
    "she shifted closer on the bench",
    "she sat on her hands",
    "she smoothed a wrinkle that wasn't there",
    "she stood her ground",
    "she swallowed against a tight throat",
    "she took a half step back",
    "she took up less space",
    "she traced the rim of her glass",
    "she twisted a ring around her finger",
    "she went very still",
    "she wound a strand of hair around her finger",
    "she wrung the hem of her shirt",
]


def merge_unique(existing: list[str], additions: list[str]) -> list[str]:
    seen = set()
    out = []
    for item in existing + additions:
        # normalize typo softed -> skip if softened present later
        key = item.lower().replace("[", "").replace("]", "")
        if key in seen:
            continue
        if item == "her eyes softed":
            continue  # typo; use softened
        if item == "she dragged her [feet]":
            item = "she dragged her feet"
            key = item.lower()
            if key in seen:
                continue
        seen.add(key)
        out.append(item)
    return sorted(out, key=lambda s: s.lower())


face_old = extract_items("faceeyes")
body_old = extract_items("bodylang")
face_new = merge_unique(face_old, FACE_ADD)
body_new = merge_unique(body_old, BODY_ADD)

print(f"faceeyes: {len(face_old)} -> {len(face_new)}")
print(f"bodylang: {len(body_old)} -> {len(body_new)}")

# Replace the ul blocks inside each section
face_pat = re.compile(
    r'(<section id="faceeyes">.*?<h3>Eyes &amp; brows</h3>\s*)'
    r'<ul class="single"[^>]*>.*?</ul>',
    re.S,
)
body_pat = re.compile(
    r'(<section id="bodylang">.*?<h3>Gestures &amp; body beats</h3>\s*)'
    r'<ul class="single"[^>]*>.*?</ul>',
    re.S,
)

text2, n1 = face_pat.subn(r"\1" + ul_html(face_new), text, count=1)
text2, n2 = body_pat.subn(r"\1" + ul_html(body_new), text2, count=1)
if n1 != 1 or n2 != 1:
    raise SystemExit(f"replace failed face={n1} body={n2}")

# Update notes
text2 = text2.replace(
    '<p class="note">Action lines for eyes and brows; sorted A–Z.</p>',
    f'<p class="note">Action lines for eyes and brows; sorted A–Z. ({len(face_new)} phrases.)</p>',
    1,
)
text2 = text2.replace(
    '<p class="note">Physical beats and gestures; sorted A–Z. Swap he/she to fit your character.</p>',
    f'<p class="note">Physical beats and gestures; sorted A–Z. Swap he/she to fit your character. ({len(body_new)} phrases.)</p>',
    1,
)

html_path.write_text(text2, encoding="utf-8")
print("updated Writing-Word-Banks.html")
