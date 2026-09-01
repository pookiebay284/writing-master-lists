#!/usr/bin/env python3
"""Generate HTML batch 6: section 52 quick reactions."""
from pathlib import Path

from batch6_lists import SECTIONS


def section(num, sid, title, note, items):
    lines = [
        f'      <section id="{sid}">',
        f'        <h2>{num}. {title}</h2>',
        f'        <p class="note">{note}</p>',
        '        <div class="entry filterable">',
        '          <ul class="def-list">',
    ]
    for n, (term, meaning) in enumerate(items, 1):
        term_esc = term.replace("&", "&amp;")
        meaning_esc = meaning.replace("&", "&amp;")
        lines.append(f'            <li><strong>{n}. {term_esc}</strong> \u2013 {meaning_esc}</li>')
    lines += [
        '          </ul>',
        '        </div>',
        '      </section>',
        '',
    ]
    return "\n".join(lines)


def main():
    out = Path(__file__).with_name("_batch6_sections.html")
    parts = [section(num, sid, title, note, items) for num, sid, title, note, items in SECTIONS]
    out.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print("written", out.name)
    for num, sid, title, note, items in SECTIONS:
        print(f"  {num} {sid}: {len(items)} entries")


if __name__ == "__main__":
    main()
