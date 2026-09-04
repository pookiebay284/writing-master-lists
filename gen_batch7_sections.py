#!/usr/bin/env python3
"""Generate HTML batch 7: sections 53–58 dialogue and craft lists."""
from pathlib import Path

from batch7_lists import SECTIONS


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


def grouped_section(num, sid, title, note, groups):
    lines = [
        f'      <section id="{sid}">',
        f'        <h2>{num}. {title}</h2>',
        f'        <p class="note">{note}</p>',
    ]
    for group_title, items in groups:
        group_esc = group_title.replace("&", "&amp;")
        lines += [
            f'        <h3>{group_esc}</h3>',
            '        <div class="entry filterable">',
            '          <ul class="def-list">',
        ]
        for n, term, meaning in items:
            term_esc = term.replace("&", "&amp;")
            meaning_esc = meaning.replace("&", "&amp;")
            lines.append(f'            <li><strong>{n}. {term_esc}</strong> \u2013 {meaning_esc}</li>')
        lines += [
            '          </ul>',
            '        </div>',
        ]
    lines += [
        '      </section>',
        '',
    ]
    return "\n".join(lines)


def main():
    out = Path(__file__).with_name("_batch7_sections.html")
    parts = []
    for entry in SECTIONS:
        if len(entry) == 6 and entry[4] == "grouped":
            num, sid, title, note, _, groups = entry
            parts.append(grouped_section(num, sid, title, note, groups))
        else:
            num, sid, title, note, items = entry
            parts.append(section(num, sid, title, note, items))
    out.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print("written", out.name)
    for entry in SECTIONS:
        if len(entry) == 6 and entry[4] == "grouped":
            num, sid, title, note, _, groups = entry
            count = sum(len(items) for _, items in groups)
            print(f"  {num} {sid}: {count} entries ({len(groups)} groups)")
        else:
            num, sid, title, note, items = entry
            print(f"  {num} {sid}: {len(items)} entries")


if __name__ == "__main__":
    main()
