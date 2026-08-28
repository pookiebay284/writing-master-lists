#!/usr/bin/env python3
"""Generate HTML sections 20-25 + sounds supplement for Writing-Word-Banks.html."""
from pathlib import Path


def tag_block(title, words):
    words = sorted(set(w.strip() for w in words if w.strip()), key=str.lower)
    items = "".join(f"<li>{w}</li>" for w in words)
    return f'''        <div class="entry filterable">
          <h3>{title}</h3>
          <ul class="tag-list">{items}</ul>
        </div>'''


def phrase_block(title, phrases):
    phrases = sorted(set(p.strip() for p in phrases if p.strip()), key=str.lower)
    items = "".join(f"<li>{p}</li>" for p in phrases)
    return f'''        <div class="entry filterable">
          <h3>{title}</h3>
          <ul class="single" style="columns:2;column-gap:1.4rem;list-style:disc;padding-left:1.1rem;margin:0.35rem 0;">{items}</ul>
        </div>'''


def section(num, sid, title, note, inner):
    return f'''      <section id="{sid}">
        <h2>{num}. {title}</h2>
        <p class="note">{note}</p>
{inner}
      </section>
'''


existing_sounds = {
    "baa", "bang", "bark", "beat", "beep", "bleat", "bonk", "boom", "burp", "buzz", "cackle", "caw",
    "chirp", "chuckle", "clang", "clatter", "click", "coo", "cough", "crackle", "crash", "croak", "drip",
    "drone", "echo", "fizz", "gasp", "giggle", "groan", "growl", "grunt", "guffaw", "gulp", "gurgle",
    "hiss", "hoot", "howl", "hum", "jingle", "knock", "mew", "miaow", "moan", "moo", "murmur", "neigh",
    "oink", "pant", "patter", "peep", "ping", "pitter-patter", "plop", "pop", "purr", "rap", "rattle",
    "ring", "roar", "rumble", "rustle", "screech", "shriek", "shuffle", "sigh", "slurp", "snap", "snarl",
    "sneeze", "snicker", "sniffle", "snort", "sob", "splash", "splutter", "sputter", "squeal", "swish",
    "tap", "throb", "thud", "ting", "tinkle", "titter", "trill", "twang", "vroom", "wail", "warble",
    "whack", "wheeze", "whine", "whir", "whirr", "whisper", "whoosh", "yammer", "yap", "yell", "yelp",
}
sound_image = """bang bark beep bellow blare blast bleat bong boom bray buzz cackle cheep chime clack
clank clap clatter clink cluck clunk crack crackle crash creak dingdong drop drumming fizz glug gnashing
gobble grating growl grumble gurgle hiss hoot howl hum jingle jangle kachink knock mew moan mod murmur
neigh patter peal peep pop power pounding pulsing purr put-put rap rat-a-tat rattle ring rippling roar rumble
rushing rustle scream scrunch shriek sizzle slam snap snarl snort splash sputter squawk squeal squish stamp
swish swoosh tap tattoo tearing throb thud thump thunder tick tick-tock tinkle toot trill twang twitter wail
wheeze whine whir whisper yap yelp zap""".split()
sound_extra = sorted({w for w in sound_image if w.lower() not in existing_sounds}, key=str.lower)

skin = [
    "Pale", "Rosy", "Olive", "Dark", "Tanned", "Blotchy", "Smooth", "Moles", "Acne", "Dry",
    "Greasy", "Freckled", "Scars", "Birthmarks",
]

eyes_app = [
    "Small", "Large", "Average", "Grey", "Brown", "Blue", "Violet", "Pink", "Green", "Gold",
    "Hazel", "Crimson", "Amber", "Doe-eyed", "Almond", "Close-set", "Wide-set", "Deep-set",
    "Squinty", "Monolid", "Heavy eyelids", "Upturned", "Downturned",
]

hair = [
    "Thin", "Thick", "Fine", "Normal", "Greasy", "Dry", "Soft", "Shiny", "Curly", "Frizzy",
    "Wild", "Unruly", "Straight", "Smooth", "Wavy", "Floppy", "Cropped", "Pixie-cut", "Afro",
    "Shoulder length", "Back length", "Waist length", "Past hip-length", "Buzz cut", "Bald",
    "Weave", "Hair extensions", "Jaw length", "Layered", "Mohawk", "Dreadlocks", "Box braids",
    "Faux locks", "White", "Salt and pepper", "Platinum blonde", "Golden blonde", "Dirty blonde",
    "Blonde", "Strawberry Blonde", "Ombre", "Ash brown", "Mouse brown", "Chestnut brown",
    "Golden brown", "Chocolate brown", "Dark brown", "Jet black", "Ginger", "Red", "Auburn",
    "Dyed", "Thin eyebrows", "Average eyebrows", "Thick eyebrows", "Plucked eyebrows",
]

eyes_brows = [
    "his eyes widened", "her eyes went round", "her eyelids drooped", "his eyes narrowed",
    "his eyes lit up", "his eyes darted", "he squinted", "she blinked", "her eyes twinkled",
    "his eyes gleamed", "her eyes sparkled", "his eyes flashed", "his eyes glinted",
    "his eyes burned with...", "her eyes blazed with...", "her eyes sparked with...",
    "her eyes flickered with...", "glowed in his eyes", "the corners of his eyes crinkled",
    "she rolled her eyes", "he looked heavenward", "she glanced up to the ceiling", "she winked",
    "tears filled her eyes", "his eyes welled up", "her eyes swam with tears",
    "his eyes flooded with tears", "her eyes were wet", "his eyes glistened",
    "tears shimmered in her eyes", "tears shone in his eyes", "her eyes were glossy",
    "he was fighting back tears", "tears ran down her cheeks", "his eyes closed",
    "she squeezed her eyes shut", "he shut his eyes", "his lashes fluttered", "she batted her lashes",
    "his brows knitted", "her forehead creased", "his forehead furrowed", "her forehead puckered",
    "a line appeared between her brows", "his brows drew together", "her brows snapped together",
    "his eyebrows rose", "she raised a brow", "he lifted an eyebrow", "his eyebrows waggled",
    "she gave him a once-over", "he sized her up", "her eyes bored into him",
    "she took in the sight of...", "he glared", "she peered", "he gazed", "she glanced",
    "he stared", "she scrutinized", "he studied", "she gaped", "he observed", "she surveyed",
    "he gawked", "he leered", "his pupils (were) dilated", "her pupils were huge",
    "his pupils flared",
]

body = [
    "she nodded", "he bobbed his head", "she tilted her head", "he cocked his head",
    "she inclined her head", "he jerked his head toward...", "she threw her head back",
    "he lowered his head", "she hung her head", "he ducked", "she bowed her head",
    "he put his head in his hands", "he covered his eyes with a hand", "she hid behind her book",
    "she pressed her hands to her cheeks", "she raised her chin", "he lifted his chin",
    "her hands squeezed into fists", "his hands tightened into fists", "she clenched her fists",
    "she balled her fists", "he unclenched his fists", "her arms remained at her sides",
    "his arms dangled at his sides", "he shrugged", "she gave a half shrug",
    "he lifted his shoulder in a half shrug", "she gave a dismissive wave of her hand",
    "she raised a hand in greeting", "he waved", "she held up her hands", "he lifted his hands",
    "she held up her palms", "he threw his hands in the air", "she brushed her palms together",
    "he rubbed his hands together", "she made a steeple of her fingers", "he spread his hands",
    "she gesticulated", "she fanned herself", "he flapped his hands", "he waved his hands",
    "she clapped her hands", "he snapped his fingers", "she held up a finger", "she wagged a finger",
    "he pointed", "she gestured with a thumb", "he jerked his thumb toward...",
    "she extended her middle finger toward him", "he gave her the finger", "she flipped him the bird",
    "she gave him the thumbs up", "he gave him the okay sign", "she flashed a peace sign",
    "she drew a finger across her throat", "he twirled a finger next to his temple",
    "she gave a mock salute", "he pretended to shoot himself in the head", "she waggled her hips",
    "he thrust his pelvis", "he put his hands on his hips", "she rested a hand on her hip",
    "she jutted out her hip", "she shoved her hands into her pockets",
    "he jammed his hands in his pockets", "she folded her arms", "he crossed his arms over his chest",
    "she hugged herself", "he wrapped his arms around himself", "she rubbed her forearms",
    "she spread her arms wide", "she held out her hand", "he extended a hand", "he shook his head",
    "she turned her face away", "he looked away", "his breaths quickened", "she panted",
    "she was breathing hard", "his chest rose and fell with rapid breaths", "she took in a deep breath",
    "he drew in a long breath", "she took in a sharp breath", "he gasped", "she held her breath",
    "he let out a harsh breath", "she exhaled", "he blew out his cheeks", "she huffed", "he sighed",
    "she snorted", "she laughed", "he giggled", "she guffawed", "he chuckled",
    "she gave a bitter laugh", "he gave a mirthless laugh", "she tittered", "he cackled",
    "she rubbed her shoulder", "he kneaded his shoulder", "he rolled his shoulders",
    "she tensed her shoulders", "he massaged the back of his neck", "she rubbed her temples",
    "she rubbed her hands on her thighs", "she ran her hand through her hair",
    "he threaded a hand through his hair", "he raked his fingers through his hair",
    "he shoved his hair away from his face", "she toyed with a lock of hair",
    "she played with her hair", "she twirled her hair", "she wrapped a curl around her finger",
    "she tucked a lock of hair behind her ear", "he undid his ponytail", "she shook out her hair",
    "he tossed her hair", "he buried his hands in his hair", "she tugged at her hair",
    "he stroked his beard", "he scratched his beard", "she tugged at her earlobe", "he bit a nail",
    "she chewed on a cuticle", "she picked at her nails", "she inspected her fingernails",
    "he plucked at the cuff of his shirt", "she picked lint from her sleeve",
    "he adjusted the lapels of his jacket", "she fiddled with her earring",
    "he tugged at his shirt collar", "he adjusted his tie", "she smoothed down her skirt",
    "she scratched her nose", "he scratched his head", "she rubbed her forehead",
    "he blotted his forehead with a handkerchief", "she slapped her forehead",
    "he smacked his forehead", "he facepalmed", "she rubbed her eyes",
    "she pinched the bridge of her nose", "he held his nose", "he slapped a hand over her mouth",
    "she covered her mouth with her hand", "he slapped his knee", "she pressed her fingers to her lips",
    "he tapped his fingers against his lips", "she held her finger up to her lips",
    "he rubbed his chin", "she pressed a hand to her throat", "she touched her hand to her heart",
    "he pounded his chest", "he clutched his chest", "he leaned against the wall",
    "she bounced on her toes", "he danced in place", "she jumped up and down", "he tapped his foot",
    "he stomped his foot", "her toes curled", "she folded her hands in her lap",
    "she drummed her fingers on the table", "he tapped his fingers on the table",
    "he slammed his hand on the table", "she pounded her fist on the table",
    "she set her palms down flat on the table", "he rested his hands on the table",
    "she set her hands on the table, palms up", "he leaned back in his chair",
    "she hooked her feet around the chair legs", "he gripped the arm of the chair",
    "she put her hands behind her head", "he put his feet up on the desk", "he fidgeted",
    "she jiggled her foot", "he swung his leg", "she crossed her legs", "he uncrossed his legs",
    "she crossed her ankles in front of her", "she stretched out her legs in front of her",
    "he sprawled out", "he shuddered", "she flinched", "he recoiled", "he shivered", "she trembled",
    "his body shook", "she cowered", "he shrank back", "she huddled in the corner", "he pulled away",
    "she jerked away", "he turned away", "she stilled", "he froze", "she jolted upright",
    "he stiffened", "she straightened", "he tensed", "he jumped", "she jumped to her feet",
    "he stood up", "she rose from her seat", "she relaxed", "he hunched", "she slouched",
    "her shoulders sagged", "his shoulders slumped", "her shoulders rounded", "his chest caved",
    "he drooped", "she wilted", "he went limp", "he rolled his shoulders", "she squared her shoulders",
    "she clasped her hands behind her back", "he puffed out his chest", "she thrust out her chest",
    "he propped his chin on his hand", "she rested her chin on her palm", "he yawned", "she stretched",
    "he turned around", "she whirled around", "he pivoted", "she reeled", "he staggered",
    "her knees buckled", "she stepped away", "she drew nearer", "he leaned closer", "she inched forward",
    "he loomed closer", "he paced", "she shifted from one foot to the other", "he rocked back and forth",
    "he shuffled his feet", "he swayed on his feet", "she dragged her [feet]", "she cringed",
    "he pumped a fist", "he thrust his fists in the air", "she punched the air",
]

sunrise = [
    "The sun rays glint brightly in the clear waters.",
    "The sunset was glorious, all rosy and salmon-pink.",
    "The sun-lit sky and sea blend perfectly into each other.",
    "The awe-inspiring sun danced in from the horizon.",
    "Dews on the blades of grass sparkled in the sunlight.",
    "The high sunlit clouds drifted across a clear blue sky.",
    "A torch of fire started to light up the darkness around us.",
    "Basking in the golden rays, I hope to have a flattering tan.",
    "The unending bright sky was glorious luminous blue and pink.",
    "The sky was overwhelmed by crimson and amber-tinted clouds.",
    "The sun filtered through the clouds, signaling the end of the rain.",
    "It was a blindingly hot day and the humidity in the air was stifling.",
    "The whole landscape was bathed in the warm glow of the rising sun.",
    "Palm trees swayed to the gentle breeze in the warm tropical sunshine.",
    "The sun and the moon were visible in the clear blue early morning sky.",
    "The sun shone brilliantly and the water in the pond glittered invitingly.",
    "Windows threw wide in the hope of tempting in a non-existent breeze.",
    "A golden glow spread across the sky as the sun chased the dark clouds away.",
    "As the sun set, the few thin strips of clouds on the horizon turned shimmering gold.",
    "It was a lovely walk, with the sun setting behind the mountain in a sea of liquid gold.",
    "From freezing night, it turned to scorching day as the sun climbed towards its zenith.",
]

fighting = {
    "Attack with a weapon": [
        "Slice", "Pelt", "Drive", "Club", "Bombard", "Carve", "Chop", "Spear", "Brand", "Shell",
        "Hammer", "Clout", "Flog", "Bomb", "Blast", "Torpedo", "Blow up", "Stab", "Plunge", "Buffet",
        "Thwack", "Whip", "Burn", "Shoot", "Shock", "Pierce", "Cuff", "Lash", "Belt", "Birch", "Drub",
        "Cane", "Switch", "Strap", "Detonate", "Ding", "Jab", "Bat", "Penetrate", "Cut", "Bleed", "Bump",
        "Poke", "Boot", "Puncture", "Prick", "Zap", "Stick", "Smart", "Sting",
    ],
    "Attack without a weapon": [
        "Clout", "Trounce", "Whale", "Pummel", "Batter", "Maul", "Pound", "Clobber", "Crush", "Bash",
        "Wallop", "Break", "Smash", "Beat", "Whop", "Whack", "Punch", "Jump", "Clock", "Stun", "Bust",
        "Slug", "Box", "Kick", "Bite", "Shove", "Jolt", "Cuff", "Cram", "Slam", "Slog", "Biff", "Pounce",
        "Bruise", "Pinch", "Mug", "Trip", "Shake", "Trap", "Slip", "Scratch", "Bop", "Mount", "Spank",
        "Push", "Flick", "Smack", "Swat", "Pull", "Strike", "Spar",
    ],
    "Defense": [
        "Flee", "Disable", "Abandon", "Dodge", "Reel", "Deceive", "Escape", "Confuse", "Block", "Defend",
        "Run", "Retreat", "Disengage", "Regress", "Elude", "Evade", "Balk", "Bypass", "Fend off", "Duck",
        "Hide", "Sidestep", "Pull back", "Backtrack", "Recede", "Avoid", "Back", "Shuffle", "Shirk",
        "Shrink", "Hesitate",
    ],
    "General": [
        "Charge", "Combat", "Overwhelm", "Raid", "Shatter", "Mutilate", "Storm", "Punish", "Attack",
        "Hurt", "Defeat", "Wound", "Injure", "Impact", "Advance", "Agitate", "Swing", "Besiege",
        "Aggress",
    ],
}

intense = [
    "forceful", "severe", "passionate", "acute", "agonizing", "ardent", "anxious", "biting", "bitter",
    "burning", "close", "consuming", "cutting", "deep", "eager", "earnest", "excessive", "exquisite",
    "extreme", "fervent", "fervid", "fierce", "forcible", "great", "harsh", "impassioned", "keen",
    "marked", "piercing", "powerful", "profound", "sharp", "strong", "vehement", "violent", "vivid",
    "vigorous",
]

liquid = [
    "damp", "cream", "creamy", "dripping", "ichorous", "juicy", "moist", "luscious", "melted", "pulpy",
    "sappy", "soaking", "solvent", "sopping", "succulent", "viscous", "wet", "aqueous", "broth",
    "elixir", "extract", "flux", "juice", "liquor", "nectar", "sap", "sauce", "secretion", "solution",
    "vitae", "awash", "moisture", "boggy", "dewy", "drenched", "drip", "drop", "droplet", "drowning",
    "flood", "flooded", "flowing", "fountain", "jewel", "leaky", "milky", "overflowing", "saturated",
    "slick", "slippery", "soaked", "sodden", "soggy", "stream", "swamp", "tear", "teardrop", "torrent",
    "waterlogged", "watery", "weeping",
]

lithe = [
    "agile", "lean", "pliant", "slight", "spare", "sinewy", "slender", "supple", "deft", "fit",
    "flexible", "lanky", "leggy", "limber", "lissom", "lissome", "nimble", "sinuous", "skinny", "sleek",
    "slim", "svelte", "trim", "thin", "willowy", "wiry",
]

moan = [
    "beef", "cry", "gripe", "grouse", "grumble", "lament", "lamentation", "plaint", "sob", "wail",
    "whine", "bemoan", "bewail", "carp", "deplore", "grieve", "keen", "sigh", "mewl",
]


def dedupe_sort(words):
    seen = set()
    out = []
    for w in sorted(words, key=str.lower):
        k = w.lower()
        if k not in seen:
            seen.add(k)
            out.append(w)
    return out


def main():
    parts = []

    parts.append(f'''        <div class="entry filterable">
          <h3>More sound words (A–Z)</h3>
          <p class="note" style="margin:0 0 0.35rem;font-size:0.86rem;">From your sound list — words not already in the numbered 1–100 above.</p>
          <ul class="tag-list">{"".join(f"<li>{w}</li>" for w in sound_extra)}</ul>
        </div>''')

    parts.append(section(20, "appearance", "Appearance — Skin, Eyes &amp; Hair",
        "Physical descriptors sorted A–Z within each group.",
        "\n".join([
            tag_block("Skin", skin),
            tag_block("Eyes", eyes_app),
            tag_block("Hair", hair),
        ])))

    parts.append(section(21, "faceeyes", "Face — Eyes &amp; Brows (phrases)",
        "Action lines for eyes and brows; sorted A–Z.",
        phrase_block("Eyes &amp; brows", eyes_brows)))

    parts.append(section(22, "bodylang", "Body Language &amp; Gestures",
        "Physical beats and gestures; sorted A–Z. Swap he/she to fit your character.",
        phrase_block("Gestures &amp; body beats", body)))

    parts.append(section(23, "sunrise", "Descriptive Phrases — Sunrise / Sunset",
        "Scenery lines as on your sheet.",
        phrase_block("Sunrise / sunset", sunrise)))

    fw_inner = "\n".join(tag_block(k, dedupe_sort(v)) for k, v in fighting.items())
    parts.append(section(24, "fighting", "Fighting Words",
        "Combat verbs by type; sorted A–Z within each group (duplicates removed within a group).",
        fw_inner))

    wb_inner = "\n".join([
        tag_block("Intense", dedupe_sort(intense)),
        tag_block("Liquid", dedupe_sort(liquid)),
        tag_block("Lithe", dedupe_sort(lithe)),
        tag_block("Moan", dedupe_sort(moan)),
    ])
    parts.append(section(25, "wordbanks", "Intense · Liquid · Lithe · Moan",
        "Descriptor word banks; sorted A–Z, duplicates removed within each list.",
        wb_inner))

    Path(__file__).with_name("_batch2_sections.html").write_text("\n".join(parts) + "\n", encoding="utf-8")
    print("sound_extra", len(sound_extra))
    print("body", len(set(body)))
    print("written _batch2_sections.html")


if __name__ == "__main__":
    main()
