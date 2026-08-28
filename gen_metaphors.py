#!/usr/bin/env python3
"""Generate section 35 — metaphor example sentences, deduped across sources."""
from pathlib import Path


def norm(s):
    return " ".join(s.lower().rstrip(".").split())


# (category, sentence) — categories for sorting within section
RAW = [
    # Image 1 — 50 Examples (25 shown)
    ("nature", "The candle flame danced like a ballerina in the wind."),
    ("emotions", "Her forgiveness was a balm that healed my wounds."),
    ("setting", "The city streets were veins, pulsing with life and energy."),
    ("emotions", "His dreams were butterflies, fragile and beautiful."),
    ("nature", "The thunder was a giant's roar, shaking the earth."),
    ("life", "Love is a puzzle, fitting the pieces of two hearts together."),
    ("nature", "The rain was a symphony, playing a soothing melody."),
    ("emotions", "His ambition was a burning fire that fueled his actions."),
    ("nature", "The stars were sparkling jewels strewn across the night sky."),
    ("life", "Life is a journey, with twists and turns along the way."),
    ("voice", "Her voice was a lullaby, calming and comforting."),
    ("nature", "The snowflakes were delicate kisses from the winter sky."),
    ("nature", "The road was a ribbon, leading us to new adventures."),
    ("emotions", "His heart was a prison, locked away from love."),
    ("abstract", "Time is a thief that steals youth and beauty."),
    ("nature", "The forest was a green carpet stretching as far as the eye could see."),
    ("emotions", "Her laughter was contagious, spreading joy like wildfire."),
    ("nature", "The wind whispered secrets through the trees, sharing its ancient wisdom."),
    ("emotions", "His smile was a rainbow on a stormy day."),
    ("life", "Love is a battlefield, where hearts are won and lost."),
    ("setting", "The city was a concrete jungle, bustling with activity."),
    ("voice", "Her words were honey, sweetening the bitter truth."),
    ("nature", "The moon was a lantern illuminating the night."),
    ("nature", "The waves were dancers, gracefully moving to the rhythm of the ocean."),
    ("life", "Life is a book, with each chapter bringing new experiences."),
    # Image 2 — 100 Metaphor Sentences (18 shown)
    ("nature", "The autumn leaves were a kaleidoscope of colors, painting the landscape with their vibrant hues."),
    ("nature", "The winter wind howled like a wounded wolf, echoing through the barren landscape."),
    ("nature", "The starry sky was a tapestry of dreams, inspiring wonder and contemplation."),
    ("nature", "The city's skyline at sunset was a painting, brushed with strokes of gold and orange."),
    ("nature", "The rain was a chorus of whispers, serenading the earth with its gentle patter."),
    ("nature", "The sunflower turned its face towards the sun, a worshipper seeking warmth and light."),
    ("emotions", "His tears were a river, flowing freely down his cheeks, carrying away his sorrow."),
    ("emotions", "Her laughter was a bubbling brook, filling the air with infectious joy."),
    ("emotions", "Her determination was a hammer, shattering barriers and forging her own path."),
    ("voice", "His voice was a velvet knife, cutting through the silence with its smooth precision."),
    ("body", "Her touch was a feather, delicately brushing against my skin and sending shivers down my spine."),
    ("emotions", "His smile was a lighthouse, guiding me through the stormy seas of life."),
    ("abstract", "The world of politics was a chessboard, where every move carried consequences."),
    ("abstract", "His ideas were seeds, planted in fertile minds and growing into mighty oaks of innovation."),
    ("emotions", "His dreams were wild stallions, galloping freely through the expanse of his imagination."),
    ("abstract", "Time was a thief in the night, silently stealing away the moments we wished to hold onto."),
    ("emotions", "Her creativity was a bubbling cauldron, concocting ideas that sparked like magic potions."),
    ("life", "The relationship was a tightrope, balancing between love and uncertainty with each step."),
    # Image 3 — metaphor + simile combined (15)
    ("combo", "Her laughter was a melody, as sweet as a lullaby, and it danced through the room like sunlight through the trees."),
    ("combo", "The old house was a time machine, creaking like a forgotten memory and smelling like dust-covered secrets."),
    ("combo", "His determination was a roaring fire, fierce as a storm, burning through obstacles like a relentless wave."),
    ("combo", "The city was a jungle, as chaotic as a beehive, with skyscrapers standing like sentinels over the bustling streets."),
    ("combo", "Her mind was a labyrinth, as complex as a spider's web, filled with thoughts that twisted like vines in the dark."),
    ("combo", "The teacher's voice was a gentle breeze, soothing as a summer's day, guiding the students like a lighthouse through fog."),
    ("combo", "The book was a portal, opening worlds as expansive as the universe, and each page turned like a key unlocking new realms."),
    ("combo", "The storm was a wild beast, roaring like an angry lion, and the lightning struck like a dancer's sharp movements."),
    ("combo", "His kindness was a warm blanket, comforting as a childhood memory, wrapping around others like a protective shield."),
    ("combo", "The deadline loomed like a storm cloud, dark and foreboding, pushing us forward like a relentless current."),
    ("combo", "Her gaze was a sharp knife, cutting through the silence like a whisper in a crowded room, revealing truths as clear as crystal."),
    ("combo", "The wedding was a fairy tale, as enchanting as a moonlit night, with every detail falling into place like pieces of a dream."),
    ("combo", "The old library was a treasure chest, filled with books as valuable as gold, each one a key to a different adventure like stars in the sky."),
    ("combo", "His temper was a volcano, erupting like a sudden tempest, and his calm demeanor was as deceptive as a still lake."),
    ("combo", "The argument was a chess game, strategic and tense like a high-stakes match, each word a move in a complex battle of wits."),
    # Image 4 — 100 Metaphor Sentences (17 shown)
    ("emotions", "Her forgiveness was a soothing balm, healing the wounds of past mistakes."),
    ("nature", "The sun dipped below the horizon, bidding farewell with a golden kiss."),
    ("abstract", "His mind was a maze, each thought leading to a complex web of possibilities."),
    ("body", "Her eyes were sapphire pools, reflecting the depths of her emotions."),
    ("setting", "The city's skyline was a jagged silhouette, reaching for the heavens."),
    ("emotions", "His determination was a roaring fire, fueling his relentless pursuit of success."),
    ("nature", "The waves crashed against the shore like a chorus of thunderous applause."),
    ("voice", "His jokes were daggers, cutting through the tension in the room."),
    ("nature", "The snow-covered landscape was a pristine canvas, untouched by human hands."),
    ("voice", "Her voice was a gentle breeze, caressing our ears with its melodic tones."),
    ("abstract", "The world of politics is a murky swamp, filled with hidden agendas and shifting alliances."),
    ("emotions", "Her smile was a beacon of light, illuminating the darkest corners of my day."),
    ("body", "The basketball player was a skyscraper on the court, towering over his opponents."),
    ("voice", "His words were honey, sweetening the conversation with every syllable."),
    ("nature", "The raindrops danced on the windowpane, a delicate ballet of nature."),
    ("emotions", "She wore her failures like badges of honor, each one a stepping stone towards success."),
]

# Drop shorter sentence when another is a strict prefix extension (same opening)
ORDER = ["nature", "emotions", "body", "voice", "life", "setting", "abstract", "combo"]
CAT_TITLES = {
    "nature": "Nature, weather &amp; landscape",
    "emotions": "Emotions &amp; personality",
    "body": "Body &amp; physical presence",
    "voice": "Voice, words &amp; communication",
    "life": "Love, life &amp; relationships",
    "setting": "Places &amp; setting",
    "abstract": "Mind, time &amp; abstract ideas",
    "combo": "Metaphor + simile combined",
}


def dedupe(items):
    seen = set()
    out = []
    # Sort by length descending so longer variants win when one starts with another
    for cat, sent in sorted(items, key=lambda x: -len(x[1])):
        key = norm(sent)
        if key in seen:
            continue
        # Skip if a longer version with same prefix already kept
        if any(key != sk and sk.startswith(key) for sk in seen):
            continue
        # Remove shorter kept entries that this sentence extends
        seen = {sk for sk in seen if not key.startswith(sk) or sk == key}
        seen.add(key)
        out.append((cat, sent))
    return out


def main():
    unique = dedupe(RAW)
    by_cat = {c: [] for c in ORDER}
    for cat, sent in unique:
        by_cat[cat].append(sent)
    for cat in ORDER:
        by_cat[cat].sort(key=str.lower)

    blocks = []
    n = 0
    for cat in ORDER:
        sents = by_cat[cat]
        if not sents:
            continue
        items = "".join(f"<li>{s}</li>" for s in sents)
        blocks.append(f'''        <div class="entry filterable">
          <h3>{CAT_TITLES[cat]}</h3>
          <ul class="single" style="columns:2;column-gap:1.4rem;list-style:disc;padding-left:1.1rem;margin:0.35rem 0;">{items}</ul>
        </div>''')
        n += len(sents)

    html = f'''      <section id="metaphors">
        <h2>35. Metaphor Example Sentences</h2>
        <p class="note">Example lines from your sheets, sorted by theme A&ndash;Z within each group. Duplicates and near-duplicates removed ({n} sentences).</p>
{chr(10).join(blocks)}
      </section>

'''
    out = Path(__file__).with_name("_metaphors_section.html")
    out.write_text(html, encoding="utf-8")
    print(f"unique sentences: {n}")
    print(f"written {out.name}")

if __name__ == "__main__":
    main()
