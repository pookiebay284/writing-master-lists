# Writing Master Lists

Free desk reference for fiction writing — facial expressions, body language, emotions, traits, senses, settings, action verbs, and dialogue beats.

## Files

| File | Best for |
|------|----------|
| `Writing-Master-Lists.html` | Original huge desk reference (emotions, gestures, world, combat, etc.) |
| `Writing-Word-Banks.html` | **Volume 2** — said/action synonyms, personality, emotions, reactions, faces, suddenly/abnormal/awkward/literally/and, impact verbs, decision collocations, smart/fun words, materials, sounds (19 sections) |
| `Writing-Master-Lists.md` | Edit notes / pointers for the original HTML |

## How to download / save a PDF

1. Open `Writing-Master-Lists.html` or `Writing-Word-Banks.html` in Chrome, Edge, or Firefox.
2. Press **Ctrl+P** (or use the button on the page).
3. Choose **Save as PDF** / **Microsoft Print to PDF**.

## Location

`C:\Users\liamd\Documents\writing-master-lists\`

## GitHub Pages (mobile link)

The site lives in the **`docs/`** folder:

| URL path | File |
|----------|------|
| `/` | Landing page — links to both volumes + Palette Studio |
| `/word-banks.html` | Volume 2 (`Writing-Word-Banks.html`) |
| `/master-lists.html` | Volume 1 (`Writing-Master-Lists.html`) |
| `/palette.html` | Palette Studio — image extract, harmony, color wheel |

After publishing, your link will look like:

**`https://YOUR-GITHUB-USERNAME.github.io/writing-master-lists/`**

### Publish / update

1. One-time: sign in with GitHub CLI — run `gh auth login` and follow the browser prompt.
2. From this folder, run:

```powershell
.\deploy-github-pages.ps1
```

That creates the repo (if needed), pushes `main`, and turns on GitHub Pages from `/docs`.

## Audiobook Studio (personal, local)

A private Kokoro reader lives in `audiobook-studio/`. It is **not** part of the public GitHub Pages site. Run it on this PC, then copy chapter MP3s to your phone.

```powershell
cd audiobook-studio
.\start.ps1
```

See `audiobook-studio/README.md` for voices, chapter files, and GPU notes.
