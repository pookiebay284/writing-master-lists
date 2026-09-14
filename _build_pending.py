#!/usr/bin/env python3
"""Build sections 65–80, write _pending_sections.html, merge into Writing-Word-Banks.html."""
from __future__ import annotations

import re
import shutil
import urllib.request
from pathlib import Path

from batch10_lists import (
    INDIRECT,
    PETTY,
    REPLIED,
    SAIDALTS,
    STRONG,
    THING,
    TRY,
)

ROOT = Path(__file__).parent

FETCH_URLS: dict[str, str] = {
    "youreright": "https://www.englishgrammar.org/ways-say-youre-right/",
    "walk": "https://www.englishgrammar.org/best-synonyms-walk/",
    "formal": "https://www.englishgrammar.org/best-synonyms-formal/",
    "tense": "https://www.englishgrammar.org/best-synonyms-tense/",
    "dead": "https://www.englishgrammar.org/best-synonyms-dead/",
    "fancywords": "https://www.englishgrammar.org/words-that-sound-fancy-but-are-surprisingly-useful/",
    "honest": "https://www.englishgrammar.org/phrases-be-honest/",
    "nothing": "https://www.englishgrammar.org/other-words-nothing/",
    "vital": "https://www.englishgrammar.org/other-words-vital/",
}


def fetch_pairs(url: str) -> list[tuple[str, str]]:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", errors="replace")
    rows = re.findall(
        r"<tr>\s*"
        r'<td[^>]*>\d+\.</td>\s*'
        r"<td[^>]*>(.*?)</td>\s*"
        r"<td[^>]*>(.*?)</td>\s*"
        r"</tr>",
        html,
        re.S | re.I,
    )
    if len(rows) != 100:
        raise SystemExit(f"{url}: expected 100 rows, got {len(rows)}")
    out: list[tuple[str, str]] = []
    for term, meaning in rows:
        term = re.sub(r"<[^>]+>", "", term).strip()
        meaning = re.sub(r"<[^>]+>", "", meaning).strip()
        out.append((term, meaning))
    return out


def build_sections() -> list[tuple[int, str, str, str, list[tuple[str, str]]]]:
    fetched = {sid: fetch_pairs(url) for sid, url in FETCH_URLS.items()}
    return [
        (
            65,
            "saidalts",
            "100 Words to Use Instead of &ldquo;Said&rdquo;",
            "Dialogue-tag alternatives with meanings, numbered 1–100. Complements section 1.",
            SAIDALTS,
        ),
        (
            66,
            "strong",
            "100 Best Synonyms for &ldquo;Strong&rdquo;",
            "Strength, power, and resolve words, numbered 1–100.",
            STRONG,
        ),
        (
            67,
            "petty",
            "100 Petty Comments",
            "Snide, sarcastic, and dismissive lines, numbered 1–100.",
            PETTY,
        ),
        (
            68,
            "try",
            "100 Best Synonyms for &ldquo;Try&rdquo;",
            "Effort and attempt verbs, numbered 1–100.",
            TRY,
        ),
        (
            69,
            "thing",
            "100 Words to Use Instead of &ldquo;Thing&rdquo;",
            "More precise nouns than thing, numbered 1–100.",
            THING,
        ),
        (
            70,
            "indirect",
            "100 Examples of Indirect Questions",
            "Polite and soft question forms, numbered 1–100.",
            INDIRECT,
        ),
        (
            71,
            "replied",
            "100 Other Words for &ldquo;Replied&rdquo;",
            "Response verbs and reply beats, numbered 1–100.",
            REPLIED,
        ),
        (
            72,
            "youreright",
            "100 Ways to Say &ldquo;You&rsquo;re right&rdquo;",
            "Agreement and concession phrases, numbered 1–100.",
            fetched["youreright"],
        ),
        (
            73,
            "walk",
            "100 Best Synonyms for &ldquo;Walk&rdquo;",
            "Movement and gait verbs, numbered 1–100.",
            fetched["walk"],
        ),
        (
            74,
            "formal",
            "100 Best Synonyms for &ldquo;Formal&rdquo;",
            "Official, proper, and ceremonial words, numbered 1–100.",
            fetched["formal"],
        ),
        (
            75,
            "tense",
            "100 Best Synonyms for &ldquo;Tense&rdquo;",
            "Anxiety, strain, and nervous energy words, numbered 1–100.",
            fetched["tense"],
        ),
        (
            76,
            "dead",
            "100 Best Synonyms for &ldquo;Dead&rdquo;",
            "Death and euphemism vocabulary, numbered 1–100.",
            fetched["dead"],
        ),
        (
            77,
            "fancywords",
            "100 Words That Sound Fancy But Are Surprisingly Useful",
            "Useful elevated vocabulary, numbered 1–100.",
            fetched["fancywords"],
        ),
        (
            78,
            "honest",
            "100 Phrases to Use Instead of &ldquo;To be honest&rdquo;",
            "Frank and sincere openers, numbered 1–100.",
            fetched["honest"],
        ),
        (
            79,
            "nothing",
            "100 Other Words for &ldquo;Nothing&rdquo;",
            "Words for emptiness and insignificance, numbered 1–100.",
            fetched["nothing"],
        ),
        (
            80,
            "vital",
            "100 Other Words for &ldquo;Vital&rdquo;",
            "Critical importance synonyms, numbered 1–100.",
            fetched["vital"],
        ),
    ]


SECTIONS: list[tuple[int, str, str, str, list[tuple[str, str]]]] = []


def section(num: int, sid: str, title: str, note: str, items: list[tuple[str, str]]) -> str:
    lines = [
        f'      <section id="{sid}">',
        f"        <h2>{num}. {title}</h2>",
        f'        <p class="note">{note}</p>',
        '        <div class="entry filterable">',
        '          <ul class="def-list">',
    ]
    for n, (term, meaning) in enumerate(items, 1):
        term_esc = term.replace("&", "&amp;")
        meaning_esc = meaning.replace("&", "&amp;")
        lines.append(f"            <li><strong>{n}. {term_esc}</strong> \u2013 {meaning_esc}</li>")
    lines += [
        "          </ul>",
        "        </div>",
        "      </section>",
        "",
    ]
    return "\n".join(lines)


def merge_html(batch_html: str) -> None:
    html_path = ROOT / "Writing-Word-Banks.html"
    text = html_path.read_text(encoding="utf-8")

    if 'id="saidalts"' in text:
        raise SystemExit("sections 65–80 already merged (saidalts present)")

    footer_marker = "\n\n      <footer>"
    if footer_marker not in text:
        raise SystemExit("footer marker not found")
    text = text.replace(footer_marker, "\n\n" + batch_html + footer_marker, 1)

    for old in ("Sections 1–64.", "Sections 1–71.", "Sections 1–77.", "Sections 1–80."):
        if old in text:
            text = text.replace(old, "Sections 1–80.", 1)
            break
    else:
        raise SystemExit("sections count marker not found")

    pending_links = """      <a href="#saidalts">Said alternatives (100)</a>
      <a href="#replied">Replied (100)</a>
      <a href="#strong">Strong (100)</a>
      <a href="#try">Try (100)</a>
      <a href="#thing">Thing (100)</a>
      <a href="#petty">Petty comments (100)</a>
      <a href="#indirect">Indirect questions (100)</a>
      <a href="#youreright">You’re right (100)</a>
      <a href="#walk">Walk (100)</a>
      <a href="#formal">Formal (100)</a>
      <a href="#tense">Tense (100)</a>
      <a href="#dead">Dead (100)</a>
      <a href="#fancywords">Fancy useful words (100)</a>
      <a href="#honest">To be honest (100)</a>
      <a href="#nothing">Nothing (100)</a>
      <a href="#vital">Vital (100)</a>
    </nav>"""

    nav_causeeffect = """      <a href="#causeeffect">Cause &amp; effect (100)</a>
    </nav>"""
    nav_causeeffect_new = """      <a href="#causeeffect">Cause &amp; effect (100)</a>
""" + pending_links

    if nav_causeeffect in text:
        text = text.replace(nav_causeeffect, nav_causeeffect_new, 1)
    else:
        raise SystemExit("nav marker not found")

    html_path.write_text(text, encoding="utf-8")
    shutil.copy2(html_path, ROOT / "docs" / "word-banks.html")


def update_docs_index() -> None:
    index_path = ROOT / "docs" / "index.html"
    text = index_path.read_text(encoding="utf-8")
    text = re.sub(
        r"— \d+ sections\.",
        "— 80 sections.",
        text,
        count=1,
    )
    index_path.write_text(text, encoding="utf-8")


def main() -> None:
    global SECTIONS
    SECTIONS = build_sections()

    out = ROOT / "_pending_sections.html"
    parts = [section(num, sid, title, note, items) for num, sid, title, note, items in SECTIONS]
    out.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print("written", out.name)

    ok = True
    for num, sid, _title, _note, items in SECTIONS:
        count = len(items)
        status = "ok" if count == 100 else "BAD"
        if count != 100:
            ok = False
        print(f"  {num} {sid}: {count} entries [{status}]")

    if not ok:
        raise SystemExit("entry count verification failed")

    merge_html(out.read_text(encoding="utf-8"))
    print("merged Writing-Word-Banks.html and docs/word-banks.html")

    update_docs_index()
    print("updated docs/index.html")


if __name__ == "__main__":
    main()
