# -*- coding: utf-8 -*-
"""Expand the colors section with 800 named colors and accurate swatches."""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "Writing-Word-Banks.html"
WIKI = json.loads((ROOT / "wiki-colors.json").read_text(encoding="utf-8"))
BIG = json.loads((ROOT / "colors-big.json").read_text(encoding="utf-8"))

# Published hex for the original 100. Wikipedia's list of colors when that
# entry matches the written meaning; otherwise the CSS color or the
# traditional pigment / color-name-list value named in the comment.
CORE_HEX = {
    "amber": "#FFBF00",          # Wikipedia
    "amethyst": "#9966CC",       # Wikipedia
    "apricot": "#FBCEB1",        # Wikipedia (pale apricot)
    "aqua": "#00FFFF",           # Wikipedia / CSS
    "aquamarine": "#7FFFD4",     # Wikipedia / CSS
    "ash": "#B2BEB5",            # Wikipedia Ash Gray
    "azure": "#007FFF",          # Wikipedia
    "baby blue": "#89CFF0",      # Wikipedia
    "beige": "#F5F5DC",          # Wikipedia
    "black": "#000000",
    "blue": "#0000FF",
    "blush": "#DE5D83",          # Wikipedia
    "brick": "#A03623",          # color-name-list Brick; muted red-brown
    "brown": "#964B00",          # Wikipedia
    "burgundy": "#800020",       # Wikipedia
    "cerulean": "#007BA7",       # Wikipedia
    "chestnut": "#954535",       # Wikipedia
    "chocolate": "#7B3F00",      # Wikipedia (dark; not CSS chocolate)
    "cobalt": "#0047AB",         # traditional cobalt blue
    "coral": "#FF7F50",          # Wikipedia / CSS
    "cream": "#FFFDD0",          # Wikipedia
    "crimson": "#DC143C",        # Wikipedia / CSS
    "cyan": "#00FFFF",           # Wikipedia / CSS
    "denim": "#1560BD",          # Wikipedia
    "dove gray": "#6D6C6C",      # color-name-list Dove Grey
    "ebony": "#313337",          # color-name-list Ebony (near-black)
    "ecru": "#C2B280",           # Wikipedia
    "eggplant": "#614051",       # Wikipedia
    "eggshell": "#F0EAD6",       # Wikipedia
    "emerald": "#50C878",        # Wikipedia
    "espresso": "#4E312D",       # color-name-list Espresso
    "fawn": "#E5AA70",           # Wikipedia
    "flaxen": "#FBEC C9".replace(" ", ""),  # color-name-list Flaxen
    "garnet": "#733635",         # color-name-list Garnet
    "gray": "#BEBEBE",           # Wikipedia
    "green": "#00FF00",          # Wikipedia / CSS lime-vs-green: wiki Green
    "greige": "#B0A999",         # color-name-list Greige
    "gunmetal": "#2A3439",       # Wikipedia
    "hazel": "#8E7618",          # usual hazel (greenish brown)
    "heliotrope": "#DF73FF",     # Wikipedia
    "honey": "#AE8934",          # color-name-list Honey
    "ice blue": "#739BD0",       # color-name-list Ice Blue
    "indigo": "#4B0082",         # traditional / color-name-list Indigo
    "ivory": "#FFFFF0",          # Wikipedia
    "jade": "#00A86B",           # standard jade
    "jet": "#343434",            # Wikipedia
    "khaki": "#C3B091",          # cloth khaki (matches "dusty yellow-brown")
    "lavender": "#B57EDC",       # Wikipedia
    "lemon": "#FFF700",          # Wikipedia
    "lilac": "#C8A2C8",          # Wikipedia
    "lime": "#BFFF00",           # Wikipedia
    "linen": "#FAF0E6",          # Wikipedia
    "magenta": "#FF00FF",        # Wikipedia / CSS
    "mahogany": "#C04000",       # Wikipedia
    "maroon": "#800000",         # CSS maroon (dark brownish red)
    "mauve": "#E0B0FF",          # Wikipedia
    "mint": "#98FF98",           # Wikipedia Mint Green
    "moss": "#8A9A5B",           # Wikipedia Moss Green
    "mustard": "#FFDB58",        # Wikipedia
    "navy": "#000080",           # Wikipedia Navy Blue / CSS
    "obsidian": "#445055",       # color-name-list Obsidian
    "ochre": "#CC7722",          # standard yellow ochre
    "off-white": "#FFFFE4",      # color-name-list Off White
    "olive": "#808000",          # Wikipedia / CSS
    "onyx": "#353839",           # Wikipedia
    "orange": "#FFA500",         # CSS orange
    "peach": "#FFE5B4",          # Wikipedia
    "pearl": "#EAE0C8",          # color-name-list Pearl
    "periwinkle": "#CCCCFF",     # Wikipedia
    "pink": "#FFC0CB",           # Wikipedia / CSS
    "plum": "#8E4585",           # Wikipedia
    "purple": "#800080",         # CSS purple
    "raspberry": "#E30B5D",      # Wikipedia
    "red": "#FF0000",
    "robin's-egg blue": "#96DED1",  # color-name-list Pale Robin Egg Blue
    "rose": "#FF007F",           # Wikipedia Rose
    "royal blue": "#4169E1",     # CSS royal blue (vivid)
    "rust": "#B7410E",           # Wikipedia
    "sage": "#BCB88A",           # Wikipedia
    "salmon": "#FA8072",         # Wikipedia / CSS
    "scarlet": "#FF2400",        # Wikipedia
    "sepia": "#704214",          # Wikipedia
    "sienna": "#882D17",         # Wikipedia
    "silver": "#C0C0C0",         # Wikipedia / CSS
    "sky blue": "#87CEEB",       # Wikipedia / CSS
    "slate": "#708090",          # Wikipedia Slate Gray / CSS
    "tan": "#D2B48C",            # Wikipedia / CSS
    "taupe": "#483C32",          # Wikipedia
    "teal": "#008080",           # Wikipedia / CSS
    "turquoise": "#40E0D0",      # Wikipedia / CSS
    "ultramarine": "#3F00FF",    # Wikipedia
    "umber": "#635147",          # Wikipedia
    "vermilion": "#E34234",      # Wikipedia
    "violet": "#8000FF",         # Wikipedia
    "viridian": "#40826D",       # Wikipedia
    "walnut": "#773F1A",         # color-name-list Walnut
    "white": "#FFFFFF",
    "wine": "#722F37",           # Wikipedia
    "wisteria": "#C9A0DC",       # Wikipedia
    "yellow": "#FFFF00",
}

# Meanings rewritten only where the old line would disagree with the swatch.
MEANING_FIX = {
    "aqua": "a bright greenish blue",
    "blush": "a medium rose pink",
    "dove gray": "a soft medium gray",
    "ebony": "a deep black-gray",
    "green": "a pure bright green",
    "ice blue": "a medium gray-blue",
    "jade": "a medium jewel green",
    "obsidian": "a dark blue-gray",
    "rose": "a vivid pink-red",
    "taupe": "a dark grayish brown",
    "ultramarine": "a vivid violet-blue",
}


def norm(name: str) -> str:
    s = name.lower().replace("grey", "gray").replace("’", "'")
    return re.sub(r"[^a-z0-9]+", "", s)


def hsl(hexv: str):
    h = hexv.lstrip("#")
    r, g, b = [int(h[i : i + 2], 16) / 255 for i in (0, 2, 4)]
    mx, mn = max(r, g, b), min(r, g, b)
    light = (mx + mn) / 2
    chroma = mx - mn
    if mx == mn:
        return 0.0, 0.0, light, 0.0
    d = mx - mn
    sat = d / (2 - mx - mn) if light > 0.5 else d / (mx + mn)
    if mx == r:
        hue = ((g - b) / d) % 6
    elif mx == g:
        hue = (b - r) / d + 2
    else:
        hue = (r - g) / d + 4
    return hue * 60, sat, light, chroma


def hue_word(h, s, l):
    if s < 0.10:
        return "gray"
    # Warm, not-too-bright colors read as brown or tan, not orange.
    if 8 <= h <= 55 and s < 0.50 and 0.12 < l < 0.62:
        return "brown"
    if 15 <= h <= 55 and s < 0.48 and 0.55 <= l <= 0.78:
        return "tan"
    bands = [
        (12, "red"),
        (25, "red-orange"),
        (42, "orange"),
        (54, "amber"),
        (68, "yellow"),
        (90, "yellow-green"),
        (155, "green"),
        (175, "blue-green"),
        (198, "cyan"),
        (225, "blue"),
        (255, "indigo"),
        (285, "violet"),
        (300, "purple"),
        (345, "magenta"),
        (360, "red"),
    ]
    for edge, name in bands:
        if h < edge:
            name_out = name
            break
    else:
        name_out = "red"
    if name_out in ("red", "magenta", "crimson") and l > 0.62 and s < 0.75:
        return "pink"
    if name_out == "red" and 330 <= h < 350:
        return "pink"
    return name_out


def family(h, s, l, chroma=0.0):
    if chroma < 0.06 or s < 0.12:
        if l >= 0.88:
            return "Whites and off-whites"
        if l <= 0.14:
            return "Blacks"
        return "Grays"
    if 8 <= h <= 55 and s < 0.50 and 0.12 < l < 0.62:
        return "Browns"
    if h < 15 or h >= 348:
        return "Reds"
    if h < 42:
        return "Oranges"
    if h < 70:
        return "Yellows"
    if h < 165:
        return "Greens"
    if h < 195:
        return "Teals and blue-greens"
    if h < 255:
        return "Blues"
    if h < 325:
        return "Purples and violets"
    return "Pinks and magentas"


def meaning_from_hex(hexv: str) -> str:
    h, s, l, chroma = hsl(hexv)
    if chroma < 0.06 or s < 0.08:
        if l < 0.07:
            return "a near-black color"
        if l < 0.18:
            return "a very dark gray"
        if l < 0.32:
            return "a dark gray"
        if l < 0.48:
            return "a medium gray"
        if l < 0.68:
            return "a light gray"
        if l < 0.84:
            return "a pale gray"
        if l < 0.94:
            return "an off-white color"
        return "a near-white color"
    hue = hue_word(h, s, l)
    if l < 0.10:
        light = "near-black"
    elif l < 0.20:
        light = "very dark"
    elif l < 0.33:
        light = "dark"
    elif l < 0.46:
        light = "deep"
    elif l < 0.60:
        light = "medium"
    elif l < 0.72:
        light = "light"
    elif l < 0.84:
        light = "pale"
    elif l < 0.93:
        light = "very pale"
    else:
        light = "near-white"
    if s < 0.24:
        sat = "grayish "
    elif s < 0.34:
        sat = "muted "
    elif s < 0.50:
        sat = "soft "
    elif s > 0.80 and light in ("", "light", "deep"):
        sat = "vivid "
    elif s > 0.72 and light in ("", "light", "pale"):
        sat = "bright "
    else:
        sat = ""
    if light == "medium" and sat in ("vivid ", "bright "):
        light = ""
    if light in ("deep", "dark", "very dark") and sat == "vivid ":
        sat = "rich "
    bits = " ".join(p for p in (light, (sat + hue).strip()) if p)
    bits = re.sub(r"\s+", " ", bits).strip()
    article = "an" if bits[0] in "aeiou" else "a"
    return f"{article} {bits}"


def ok_wiki_name(name: str) -> bool:
    if re.search(r"\d|[#@/&()]|[^\x00-\x7F]", name):
        return False
    if not re.fullmatch(r"[A-Za-z][A-Za-z' .-]{1,34}", name):
        return False
    words = re.split(r"\s+", name.strip())
    if not 1 <= len(words) <= 4:
        return False
    if any(re.fullmatch(r"[A-Z]{2,}", w) for w in words):
        return False
    return True


STEMS = {
    "red", "orange", "yellow", "green", "blue", "purple", "violet", "pink",
    "brown", "gray", "grey", "black", "white", "gold", "golden", "silver",
    "bronze", "copper", "brass", "ruby", "sapphire", "emerald", "jade",
    "amber", "ivory", "cream", "beige", "tan", "khaki", "taupe", "ecru",
    "linen", "pearl", "ebony", "jet", "onyx", "obsidian", "crimson",
    "scarlet", "maroon", "burgundy", "wine", "garnet", "cherry", "raspberry",
    "strawberry", "coral", "peach", "apricot", "salmon", "blush", "rose",
    "mauve", "lilac", "lavender", "orchid", "magenta", "fuchsia", "plum",
    "indigo", "azure", "cerulean", "cobalt", "navy", "teal", "turquoise",
    "aqua", "cyan", "mint", "sage", "olive", "moss", "lime", "lemon",
    "chartreuse", "viridian", "umber", "ochre", "ocher", "sienna", "sepia",
    "rust", "brick", "chocolate", "coffee", "cocoa", "caramel", "honey",
    "mustard", "flax", "slate", "charcoal", "smoke", "ash", "fog", "mist",
    "cloud", "snow", "ice", "sky", "sea", "ocean", "marine", "sand", "clay",
    "forest", "pine", "fern", "leaf", "grass", "denim", "pastel", "neon",
}


MODIFIERS = {
    "pale", "light", "dark", "deep", "bright", "burnt", "raw", "hot", "dusty",
    "muted", "soft", "rich", "warm", "cool", "wild", "antique", "old", "true",
    "pure", "royal", "french", "persian", "prussian", "venetian", "midnight",
    "powder", "baby", "electric", "neon", "pastel", "medium", "vivid", "dull",
    "faded", "smoky", "stormy", "misty", "frosted", "winter", "summer",
    "spring", "autumn", "desert", "arctic", "tropical", "forest", "ocean",
    "sea", "sky", "sun", "moon", "star", "night", "morning", "evening",
}

def extra_ok(name: str) -> bool:
    if not re.fullmatch(r"[A-Z][a-z]+(?: [A-Z][a-z]+){0,2}", name):
        return False
    words = [w.lower() for w in name.split()]
    # Every word has to be a color word or a plain modifier, so paint-counter
    # names like "Jet Ski" and "Boy Red" stay out.
    if not all(w in STEMS or w in MODIFIERS for w in words):
        return False
    return any(w in STEMS for w in words)


def li(num, name, hexv, gloss):
    hx = hexv.upper()
    return (
        f'            <li><span class="swatch" style="background:{hx}" '
        f'title="{hx}" aria-hidden="true"></span>'
        f"<strong>{num}. {html.escape(name)}</strong> – {html.escape(gloss)}</li>"
    )


def main():
    text = SRC.read_text(encoding="utf-8")
    m = re.search(
        r'(<section id="colors">.*?</section>)',
        text,
        flags=re.S,
    )
    if not m:
        raise SystemExit("colors section not found")
    block = m.group(1)
    rows = re.findall(
        r"<strong>(\d+)\. ([^<]+)</strong> – ([^<]+)",
        block,
    )
    if len(rows) < 100:
        raise SystemExit(f"expected at least 100 core colors, found {len(rows)}")
    rows = rows[:100]
    if [int(n) for n, _, _ in rows] != list(range(1, 101)):
        raise SystemExit("core colors are not numbered 1–100")

    used = set()
    core_html = []
    for num, name, gloss in rows:
        key = html.unescape(name.strip())
        if key not in CORE_HEX:
            raise SystemExit(f"missing hex for {key}")
        used.add(norm(key))
        gloss = MEANING_FIX.get(key, html.unescape(gloss.strip()))
        core_html.append(li(int(num), key, CORE_HEX[key], gloss))

    picked = []
    for item in WIKI:
        name = item["name"].strip()
        k = norm(name)
        if k in used or not ok_wiki_name(name):
            continue
        hexv = item["hex"].strip().lower()
        if not re.fullmatch(r"#[0-9a-f]{6}", hexv):
            continue
        used.add(k)
        picked.append((name, hexv))

    picked.sort(key=lambda t: t[0].lower())
    print(f"wikipedia additions: {len(picked)}")

    if len(picked) > 800:
        # Keep shorter, plainer names when Wikipedia runs past 800.
        picked.sort(key=lambda t: (len(t[0].split()), len(t[0]), t[0].lower()))
        dropped = picked[800:]
        picked = picked[:800]
        print("dropped", len(dropped), "e.g.", ", ".join(n for n, _ in dropped[:12]))
        picked.sort(key=lambda t: t[0].lower())

    if len(picked) < 800:
        extras = []
        seen_extra = set()
        for item in BIG:
            name = item["name"].strip()
            k = norm(name)
            if k in used or k in seen_extra or not extra_ok(name):
                continue
            hexv = item["hex"].strip().lower()
            if not re.fullmatch(r"#[0-9a-f]{6}", hexv):
                continue
            seen_extra.add(k)
            extras.append((name, hexv, len(name.split()), len(name)))
        extras.sort(key=lambda t: (t[2], t[0].lower()))
        need = 800 - len(picked)
        take = extras[:need]
        print(f"extra named colors added: {len(take)} (pool {len(extras)})")
        print("extras:", ", ".join(n for n, _, _, _ in take))
        if len(take) < need:
            raise SystemExit(f"only found {len(picked) + len(take)} colors")
        for name, hexv, _, _ in take:
            used.add(norm(name))
            picked.append((name, hexv))
        picked.sort(key=lambda t: t[0].lower())

    groups = {}
    order = [
        "Reds",
        "Oranges",
        "Yellows",
        "Greens",
        "Teals and blue-greens",
        "Blues",
        "Purples and violets",
        "Pinks and magentas",
        "Browns",
        "Grays",
        "Whites and off-whites",
        "Blacks",
    ]
    for name, hexv in picked:
        groups.setdefault(family(*hsl(hexv)), []).append((name, hexv))

    # Number 101–900 straight through the hue groups, alpha inside each group.
    n = 101
    group_html = []
    for title in order:
        items = groups.get(title) or []
        items.sort(key=lambda t: t[0].lower())
        if not items:
            continue
        lines = []
        for name, hexv in items:
            lines.append(li(n, name, hexv, meaning_from_hex(hexv)))
            n += 1
        group_html.append(
            "        <div class=\"entry filterable\">\n"
            f"          <h3>{html.escape(title)}</h3>\n"
            "          <ul class=\"def-list\">\n"
            + "\n".join(lines)
            + "\n          </ul>\n"
            "        </div>"
        )
    if n != 901:
        raise SystemExit(f"numbering ended at {n - 1}, expected 900")

    # Spot-check a few generated meanings against their hex.
    samples = [picked[i] for i in (0, 40, 120, 300, 500, 700, 799)]
    for name, hexv in samples:
        print(f"  {name:28} {hexv}  {meaning_from_hex(hexv)}  [{family(*hsl(hexv))}]")

    note = (
        "The first 100 are the original color bank. Eight hundred more follow, "
        "grouped by hue. The box beside each name is that color’s standard hex: "
        "Wikipedia’s list of colors when the name is listed there, otherwise the "
        "CSS color or the traditional pigment value. A few of the original meanings "
        "were tightened so they match the swatch."
    )
    new_section = (
        '      <section id="colors">\n'
        "        <h2>34. 900 Words to Describe Colors</h2>\n"
        f'        <p class="note">{html.escape(note)}</p>\n'
        '        <div class="entry filterable">\n'
        "          <h3>Core colors</h3>\n"
        '          <ul class="def-list">\n'
        + "\n".join(core_html)
        + "\n          </ul>\n"
        "        </div>\n"
        + "\n".join(group_html)
        + "\n      </section>"
    )
    text = text[: m.start(1)] + new_section + text[m.end(1) :]
    text = text.replace(
        '<a href="#colors">Colors (100)</a>',
        '<a href="#colors">Colors (900)</a>',
        1,
    )
    css = (
        "    ul.def-list li strong { color: var(--ink); }\n"
        "    span.swatch {\n"
        "      display: inline-block;\n"
        "      width: 0.85rem;\n"
        "      height: 0.85rem;\n"
        "      margin-right: 0.38rem;\n"
        "      border-radius: 2px;\n"
        "      vertical-align: -0.12em;\n"
        "      box-shadow: inset 0 0 0 1px rgba(0,0,0,.35), 0 0 0 1px rgba(255,255,255,.28);\n"
        "      print-color-adjust: exact;\n"
        "      -webkit-print-color-adjust: exact;\n"
        "    }\n"
    )
    if "span.swatch" not in text:
        old_css = "    ul.def-list li strong { color: var(--ink); }\n"
        if old_css not in text:
            raise SystemExit("css anchor missing")
        text = text.replace(old_css, css, 1)
    SRC.write_text(text, encoding="utf-8")
    docs = ROOT / "docs" / "word-banks.html"
    docs.write_text(text, encoding="utf-8")
    print("wrote", SRC.name, "and", docs)


if __name__ == "__main__":
    main()
