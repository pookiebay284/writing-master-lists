#!/usr/bin/env python3
"""Inject dark-mode CSS, toggle, and script into desk-reference HTML files."""
from pathlib import Path

THEME_CSS = """
    html[data-theme="dark"] {
      color-scheme: dark;
      --bg: #141210;
      --ink: #ebe6dc;
      --muted: #a59d90;
      --accent: #b8a8d8;
      --accent2: #d4957a;
      --card: #1f1c18;
      --line: #3a3530;
      --chip: #2a2438;
      --input-bg: #1a1814;
      --nav-bg: rgba(26, 24, 20, 0.97);
      --grad-a: #2a2438;
      --grad-b: #2e2418;
    }
    .theme-toggle {
      display: block;
      width: 100%;
      margin: 0 0 0.6rem;
      padding: 0.35rem 0.5rem;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: var(--chip);
      color: var(--muted);
      font: inherit;
      font-family: "Segoe UI", system-ui, sans-serif;
      font-size: 0.72rem;
      cursor: pointer;
    }
    .theme-toggle:hover { color: var(--ink); }
"""

THEME_SCRIPT = """
    (function () {
      var root = document.documentElement;
      var btn = document.getElementById("theme-toggle");
      var stored = localStorage.getItem("theme");
      var dark = stored ? stored === "dark" : true;
      function apply(isDark) {
        root.setAttribute("data-theme", isDark ? "dark" : "light");
        if (btn) btn.textContent = isDark ? "Light mode" : "Dark mode";
        localStorage.setItem("theme", isDark ? "dark" : "light");
      }
      apply(dark);
      if (btn) btn.addEventListener("click", function () {
        apply(root.getAttribute("data-theme") !== "dark");
      });
    })();
"""


def patch_desk_ref(path: Path, accent_var: str = "--accent"):
    text = path.read_text(encoding="utf-8")
    if "html[data-theme=\"dark\"]" in text:
        print(path.name, "already patched")
        return

    text = text.replace(
        "      --chip: #ebe4f2;\n    }",
        "      --chip: #ebe4f2;\n      --input-bg: #fff;\n      --nav-bg: rgba(255, 253, 248, 0.96);\n      --grad-a: #e8e0f0;\n      --grad-b: #f0e6d8;\n      color-scheme: light;\n    }",
        1,
    )
    # Master Lists uses different chip color
    if "--input-bg" not in text:
        text = text.replace(
            "      --chip: #e4eee9;\n    }",
            "      --chip: #e4eee9;\n      --input-bg: #fff;\n      --nav-bg: rgba(255, 253, 248, 0.96);\n      --grad-a: #ebe3d4;\n      --grad-b: #e8efe9;\n      color-scheme: light;\n    }",
            1,
        )

    text = text.replace("    * { box-sizing: border-box; }", "    * { box-sizing: border-box; }" + THEME_CSS, 1)

    text = text.replace(
        "radial-gradient(ellipse at 100% 0%, #e8e0f0 0%, transparent 42%),\n        radial-gradient(ellipse at 0% 30%, #f0e6d8 0%, transparent 40%),",
        "radial-gradient(ellipse at 100% 0%, var(--grad-a) 0%, transparent 42%),\n        radial-gradient(ellipse at 0% 30%, var(--grad-b) 0%, transparent 40%),",
    )
    text = text.replace(
        "radial-gradient(ellipse at 0% 0%, #ebe3d4 0%, transparent 45%),\n        radial-gradient(ellipse at 100% 20%, #e8efe9 0%, transparent 40%),",
        "radial-gradient(ellipse at 0% 0%, var(--grad-a) 0%, transparent 45%),\n        radial-gradient(ellipse at 100% 20%, var(--grad-b) 0%, transparent 40%),",
    )

    text = text.replace("background: rgba(255, 253, 248, 0.96);", "background: var(--nav-bg);")
    text = text.replace("background: #fff;", "background: var(--input-bg);")

    if '<button type="button" class="theme-toggle"' not in text:
        text = text.replace(
            "<nav>\n      <h1>",
            '<nav>\n      <button type="button" class="theme-toggle" id="theme-toggle" aria-label="Toggle dark mode">Dark mode</button>\n      <h1>',
            1,
        )

    if "theme-toggle" not in text.split("</script>")[-1]:
        text = text.replace(
            "  </script>\n</body>",
            "  </script>\n  <script>" + THEME_SCRIPT + "\n  </script>\n</body>",
            1,
        )

    path.write_text(text, encoding="utf-8")
    print("patched", path.name)


def patch_index(path: Path):
    text = path.read_text(encoding="utf-8")
    if "html[data-theme=\"dark\"]" in text:
        print(path.name, "already patched")
        return

    text = text.replace(
        """    :root {
      --bg: #f4f0e6;
      --ink: #1a1814;
      --muted: #5a5348;
      --accent: #3d2c5a;
      --card: #fffdf8;
      --line: #d4cbb8;
    }""",
        """    :root {
      --bg: #141210;
      --ink: #ebe6dc;
      --muted: #a59d90;
      --accent: #b8a8d8;
      --card: #1f1c18;
      --line: #3a3530;
      --card-inner: #252219;
      --grad-a: #2a2438;
      --grad-b: #2e2418;
      color-scheme: dark;
    }
    html[data-theme="light"] {
      color-scheme: light;
      --bg: #f4f0e6;
      --ink: #1a1814;
      --muted: #5a5348;
      --accent: #3d2c5a;
      --card: #fffdf8;
      --line: #d4cbb8;
      --card-inner: #fff;
      --grad-a: #e8e0f0;
      --grad-b: #f0e6d8;
    }""",
    )

    text = text.replace(
        "radial-gradient(ellipse at 100% 0%, #e8e0f0 0%, transparent 42%),\n        radial-gradient(ellipse at 0% 30%, #f0e6d8 0%, transparent 40%),",
        "radial-gradient(ellipse at 100% 0%, var(--grad-a) 0%, transparent 42%),\n        radial-gradient(ellipse at 0% 30%, var(--grad-b) 0%, transparent 40%),",
    )
    text = text.replace("background: #fff;", "background: var(--card-inner);")

    text = text.replace(
        "    .tip { font-size: 0.82rem; margin-top: 1rem; color: var(--muted); }",
        """    .theme-toggle {
      display: block;
      width: 100%;
      margin: 0 0 0.85rem;
      padding: 0.45rem 0.65rem;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--card-inner);
      color: var(--muted);
      font: inherit;
      font-family: "Segoe UI", system-ui, sans-serif;
      font-size: 0.82rem;
      cursor: pointer;
    }
    .theme-toggle:hover { color: var(--ink); }
    .tip { font-size: 0.82rem; margin-top: 1rem; color: var(--muted); }""",
    )

    text = text.replace(
        "35 sections.",
        "51 sections.",
    )

    text = text.replace(
        "<main>\n    <h1>",
        '<main>\n    <button type="button" class="theme-toggle" id="theme-toggle" aria-label="Toggle dark mode">Light mode</button>\n    <h1>',
    )

    text = text.replace(
        "</body>",
        """  <script>
    (function () {
      var root = document.documentElement;
      var btn = document.getElementById("theme-toggle");
      var stored = localStorage.getItem("theme");
      var dark = stored ? stored === "dark" : true;
      function apply(isDark) {
        root.setAttribute("data-theme", isDark ? "dark" : "light");
        if (btn) btn.textContent = isDark ? "Light mode" : "Dark mode";
        localStorage.setItem("theme", isDark ? "dark" : "light");
      }
      apply(dark);
      if (btn) btn.addEventListener("click", function () {
        apply(root.getAttribute("data-theme") !== "dark");
      });
    })();
  </script>
</body>""",
    )

    path.write_text(text, encoding="utf-8")
    print("patched", path.name)


if __name__ == "__main__":
    root = Path(__file__).parent
    patch_desk_ref(root / "Writing-Word-Banks.html")
    patch_desk_ref(root / "Writing-Master-Lists.html")
    patch_index(root / "docs" / "index.html")
