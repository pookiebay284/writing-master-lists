#!/usr/bin/env python3
"""Append 100 new facial-expression and said-alternative entries, skipping duplicates."""
import re
from pathlib import Path

root = Path(__file__).parent
html_path = root / "Writing-Word-Banks.html"
text = html_path.read_text(encoding="utf-8")

FACE = [
    ("abashed look", "embarrassed, self-conscious face"),
    ("admiring glance", "look of warm approval"),
    ("amiable expression", "friendly, approachable face"),
    ("angry scowl", "fierce, displeased frown"),
    ("apologetic look", "sorry, regretful expression"),
    ("arched brow", "one brow lifted in doubt"),
    ("awestruck face", "face full of wonder"),
    ("baleful glare", "menacing, hostile stare"),
    ("bashful look", "shy, modest expression"),
    ("beaming smile", "wide, glowing happy smile"),
    ("bemused look", "puzzled and slightly amused"),
    ("biting your lip", "catching the lip in nerves or thought"),
    ("blazing eyes", "eyes bright with anger or excitement"),
    ("blissful expression", "deeply happy, content face"),
    ("bloodless face", "drained, very pale face"),
    ("bright-eyed look", "lively, eager expression"),
    ("calculating look", "cold, assessing expression"),
    ("cheerful grin", "openly happy grin"),
    ("close-lipped smile", "smile that hides the teeth"),
    ("cocky grin", "arrogant, confident grin"),
    ("compassionate look", "kind, caring expression"),
    ("contemptuous sneer", "lip curled in scorn"),
    ("coy smile", "playfully shy smile"),
    ("crinkled eyes", "eyes creased by a genuine smile"),
    ("crumpled face", "face twisted as if about to cry"),
    ("curious look", "openly interested expression"),
    ("dark look", "ominous, angry expression"),
    ("dazed expression", "stunned, unfocused face"),
    ("defiant glare", "bold, challenging stare"),
    ("delighted grin", "grin of pure pleasure"),
    ("despairing look", "hopeless, crushed expression"),
    ("determined mouth", "lips held firm with resolve"),
    ("devilish grin", "wicked, playful grin"),
    ("disappointed frown", "frown of letdown"),
    ("disgusted grimace", "face twisted in revulsion"),
    ("distant look", "faraway, unfocused expression"),
    ("dreamy expression", "soft, lost-in-thought face"),
    ("drooping eyelids", "lids heavy with sleep or sadness"),
    ("eager expression", "keen, ready face"),
    ("earnest look", "sincere, serious expression"),
    ("ecstatic face", "face overwhelmed with joy"),
    ("empty smile", "smile with no warmth behind it"),
    ("envious look", "resentful, wanting expression"),
    ("exhausted face", "face sagging with fatigue"),
    ("faraway look", "gaze fixed on nothing present"),
    ("fearful expression", "face tight with fear"),
    ("fierce scowl", "intense, threatening frown"),
    ("flinty stare", "hard, unyielding look"),
    ("fond smile", "affectionate, tender smile"),
    ("frowning deeply", "brows pulled low in displeasure"),
    ("giddy grin", "lightheaded, excited grin"),
    ("glassy eyes", "eyes shiny and unfocused"),
    ("gleaming smile", "polished, confident smile"),
    ("gloomy expression", "dark, low-spirited face"),
    ("glowing face", "face lit with happiness"),
    ("grave expression", "solemn, serious face"),
    ("greedy look", "hungry, grasping expression"),
    ("grieving face", "face marked by loss"),
    ("guarded expression", "careful, closed-off face"),
    ("guilty look", "uneasy, caught expression"),
    ("half-smile", "smile using only part of the mouth"),
    ("happy tears", "smiling while the eyes fill"),
    ("harsh frown", "severe, unfriendly frown"),
    ("hopeful expression", "face lifted with expectation"),
    ("horror-struck face", "face frozen in horror"),
    ("hostile glare", "openly unfriendly stare"),
    ("humbled look", "modest, brought-low expression"),
    ("hungry look", "intense, wanting gaze"),
    ("hurt expression", "face showing emotional injury"),
    ("incredulous stare", "look of open disbelief"),
    ("indignant look", "offended, righteous expression"),
    ("innocent expression", "guileless, open face"),
    ("ironic smirk", "one-sided mocking smile"),
    ("jealous glare", "sharp, resentful look"),
    ("jovial expression", "hearty, good-humored face"),
    ("jubilant face", "face shining with triumph"),
    ("kind eyes", "soft, generous gaze"),
    ("lazy smile", "slow, unhurried smile"),
    ("leering grin", "unpleasant, suggestive grin"),
    ("lifeless expression", "dull, drained face"),
    ("lingering look", "gaze that stays too long"),
    ("lonely expression", "isolated, wistful face"),
    ("loving gaze", "tender, devoted look"),
    ("manic grin", "too-wide, unstable grin"),
    ("masklike face", "features held unnaturally still"),
    ("melancholy expression", "quietly sad face"),
    ("mild smile", "small, gentle smile"),
    ("mocking sneer", "scornful, taunting expression"),
    ("nervous twitch", "small involuntary jerk of the face"),
    ("open face", "honest, readable expression"),
    ("outraged expression", "face blazing with offense"),
    ("pensive look", "thoughtful, inward expression"),
    ("pitying look", "face showing sorrow for someone else"),
    ("pleading eyes", "eyes asking for mercy or help"),
    ("proud smile", "smile of earned satisfaction"),
    ("rueful smile", "regretful, self-aware smile"),
    ("secretive look", "face hiding something"),
    ("serene expression", "calm, untroubled face"),
    ("shamefaced look", "face lowered in embarrassment"),
    ("skeptical squint", "narrowed eyes full of doubt"),
    ("sleepy eyes", "lids heavy and slow to focus"),
    ("soft smile", "gentle smile without showing teeth"),
    ("startled look", "face jerked by sudden surprise"),
    ("stern expression", "severe, no-nonsense face"),
    ("stony face", "hard face that gives nothing away"),
    ("sulky pout", "pushed-out lip of resentment"),
    ("sunken eyes", "eyes hollowed by exhaustion or illness"),
    ("surprised gasp", "mouth open on a sudden breath"),
    ("tender look", "gentle, caring expression"),
    ("thoughtful frown", "brow creased in concentration"),
    ("tired eyes", "eyes dulled by lack of rest"),
    ("triumphant grin", "grin of a win just claimed"),
    ("uneasy smile", "smile that does not reach the eyes"),
    ("unreadable expression", "face that gives no clear feeling"),
    ("wary look", "cautious, watchful expression"),
    ("watery eyes", "eyes shining and about to spill"),
    ("weary expression", "face worn down by effort"),
    ("wintry smile", "cold smile with little warmth"),
    ("worried frown", "brow knit with concern"),
    ("wounded look", "face showing a fresh emotional hurt"),
    ("yearning look", "face full of longing"),
]

SAID = [
    ("accused", "Charged someone with a fault."),
    ("admonished", "Warned or scolded firmly."),
    ("agonized", "Spoke as if in pain or conflict."),
    ("apologized", "Expressed regret for a wrong."),
    ("appealed", "Made an earnest request."),
    ("applauded", "Praised warmly out loud."),
    ("babbled", "Talked quickly and unclearly."),
    ("bantered", "Traded light, teasing remarks."),
    ("barked", "Spoke in a sharp, commanding tone."),
    ("bawled", "Cried out loudly."),
    ("beckoned", "Called someone nearer."),
    ("bellowed", "Shouted in a deep, powerful voice."),
    ("beseeched", "Begged with great urgency."),
    ("burst out", "Spoke suddenly after holding words back."),
    ("cajoled", "Persuaded with flattery."),
    ("challenged", "Questioned a claim or someone's nerve."),
    ("chanted", "Spoke in a rhythmic, repeated way."),
    ("choked", "Spoke with difficulty, as if near tears."),
    ("chorused", "Spoke the same words together with others."),
    ("chuckled", "Laughed softly while speaking."),
    ("coaxed", "Persuaded gently and persistently."),
    ("commiserated", "Expressed sympathy for someone's trouble."),
    ("concluded", "Brought the remarks to an end."),
    ("confided", "Shared something private."),
    ("congratulated", "Expressed pleasure at someone's success."),
    ("contradicted", "Stated the opposite of what was said."),
    ("cooed", "Spoke in a soft, affectionate tone."),
    ("corrected", "Pointed out and fixed an error."),
    ("croaked", "Spoke in a hoarse, strained voice."),
    ("crowed", "Spoke with triumphant glee."),
    ("cursed", "Swore in anger."),
    ("deadpanned", "Spoke with a deliberately blank tone."),
    ("decided", "Announced a choice."),
    ("deflected", "Turned a question or remark aside."),
    ("demurred", "Raised a polite objection."),
    ("denounced", "Condemned publicly and strongly."),
    ("digressed", "Wandered off the subject."),
    ("dissented", "Expressed a different opinion."),
    ("doubted", "Questioned whether something was true."),
    ("entreated", "Asked earnestly and formally."),
    ("enunciated", "Spoke each word clearly."),
    ("equivocated", "Avoided a direct answer."),
    ("exaggerated", "Overstated for effect."),
    ("exulted", "Spoke with triumphant joy."),
    ("fibbed", "Told a small, unserious lie."),
    ("fired back", "Answered quickly and sharply."),
    ("flattered", "Praised in order to please."),
    ("fretted", "Spoke with anxious worry."),
    ("giggled", "Laughed lightly while speaking."),
    ("gloated", "Spoke with smug satisfaction."),
    ("groaned", "Spoke with pain or dismay."),
    ("growled", "Spoke in a low, threatening voice."),
    ("gushed", "Spoke with excessive enthusiasm."),
    ("hedged", "Avoided a clear commitment."),
    ("hissed", "Spoke in a sharp whisper."),
    ("howled", "Cried out in a long, loud wail."),
    ("huffed", "Spoke in short, irritated breaths."),
    ("hypothesized", "Offered a possible explanation."),
    ("imitated", "Copied a voice or way of speaking."),
    ("implored", "Begged desperately."),
    ("instructed", "Gave directions on what to do."),
    ("insulted", "Spoke in order to offend."),
    ("interrupted", "Cut in while someone else was speaking."),
    ("intoned", "Spoke in a slow, solemn voice."),
    ("invited", "Asked someone to join or to answer."),
    ("jeered", "Mocked with scornful shouts."),
    ("justified", "Gave reasons to defend an action."),
    ("kidded", "Joked without being serious."),
    ("lectured", "Spoke at length to teach or scold."),
    ("lied", "Stated something known to be false."),
    ("lisped", "Spoke with a softened, unclear s."),
    ("maintained", "Kept asserting the same claim."),
    ("marveled", "Spoke with wonder."),
    ("mimicked", "Copied someone's speech in order to mock."),
    ("moaned", "Spoke with a low sound of pain."),
    ("mocked", "Ridiculed through words."),
    ("mouthed", "Formed words without using the voice."),
    ("needled", "Provoked with small, repeated remarks."),
    ("opined", "Stated an opinion."),
    ("panted", "Spoke while short of breath."),
    ("parroted", "Repeated words without real thought."),
    ("persisted", "Kept speaking despite resistance."),
    ("persuaded", "Talked someone toward a decision."),
    ("piped up", "Spoke up suddenly, often in a small voice."),
    ("praised", "Spoke well of someone or something."),
    ("prayed", "Addressed a plea or thanks aloud."),
    ("preached", "Spoke with moral intensity."),
    ("predicted", "Stated what would happen next."),
    ("probed", "Asked searching questions."),
    ("proclaimed", "Announced proudly or officially."),
    ("professed", "Claimed a belief or feeling openly."),
    ("prompted", "Cued someone to speak or continue."),
    ("pronounced", "Stated formally and clearly."),
    ("purred", "Spoke in a low, pleased voice."),
    ("quavered", "Spoke with a shaking voice."),
    ("quizzed", "Asked a string of questions."),
    ("rambled", "Talked on without a clear point."),
    ("rasped", "Spoke in a rough, scraping voice."),
    ("raved", "Spoke wildly with excitement or anger."),
    ("rationalized", "Explained a fault away."),
    ("reassured", "Spoke to ease someone's fear."),
    ("rebuked", "Criticized sharply."),
    ("recited", "Spoke from memory."),
    ("reiterated", "Said the same point again for emphasis."),
    ("relented", "Gave in while speaking."),
    ("reminisced", "Spoke fondly about the past."),
    ("repeated", "Said the same words again."),
    ("reprimanded", "Scolded in a formal way."),
    ("reproached", "Expressed blame or disappointment."),
    ("roared", "Shouted with great force."),
    ("scoffed", "Spoke with mocking disbelief."),
    ("scolded", "Criticized in an angry, corrective tone."),
    ("screamed", "Shouted in a high, piercing voice."),
    ("snarled", "Spoke with open hostility."),
    ("sobbed", "Spoke while crying hard."),
    ("spluttered", "Spoke in a broken, indignant rush."),
    ("stammered", "Spoke with involuntary pauses and repeats."),
    ("taunted", "Provoked with mocking words."),
    ("threatened", "Warned of harm if not obeyed."),
    ("thundered", "Spoke in a loud, booming voice."),
    ("ventured", "Offered a remark hesitantly."),
    ("wailed", "Spoke in a long, grieving cry."),
    ("warned", "Told someone of a danger."),
    ("wheedled", "Persuaded with persistent flattery."),
    ("whimpered", "Spoke in a small, fearful voice."),
    ("whispered", "Spoke very softly."),
    ("wondered", "Spoke a question or doubt aloud."),
    ("yelped", "Spoke in a short, startled cry."),
]


def section_html(sid):
    m = re.search(rf'(<section id="{sid}">.*?</section>)', text, re.S)
    if not m:
        raise SystemExit(f"missing {sid}")
    return m.group(1)


def existing_terms(block):
    return {t.lower() for t in re.findall(r"<strong>\d+\. (.*?)</strong>", block)}


def append_items(sid, items):
    global text
    block = section_html(sid)
    have = existing_terms(block)
    fresh = []
    for term, meaning in items:
        if term.lower() in have:
            print("skip duplicate", sid, term)
            continue
        fresh.append((term, meaning))
    if len(fresh) < 100:
        raise SystemExit(f"{sid}: only {len(fresh)} new items")
    fresh = fresh[:100]
    start = len(have) + 1
    lines = []
    for i, (term, meaning) in enumerate(fresh, start):
        term_esc = term.replace("&", "&amp;")
        meaning_esc = meaning.replace("&", "&amp;")
        lines.append(f"            <li><strong>{i}. {term_esc}</strong> \u2013 {meaning_esc}</li>")
    new_block = block.replace("          </ul>", "\n".join(lines) + "\n          </ul>", 1)
    text = text.replace(block, new_block, 1)
    print(f"{sid}: {len(have)} -> {len(have) + len(fresh)}")


append_items("faceexpr", FACE)
append_items("saidalts", SAID)

text = text.replace(
    "<h2>7. 100 Words to Describe Facial Expressions</h2>",
    "<h2>7. 200 Words to Describe Facial Expressions</h2>",
    1,
)
text = text.replace(
    "Face cues and micro-expressions with meanings, numbered 1–100 as on your sheet.",
    "Face cues and micro-expressions with meanings, numbered 1–200.",
    1,
)
text = text.replace(
    "<h2>65. 100 Words to Use Instead of &ldquo;Said&rdquo;</h2>",
    "<h2>65. 200 Words to Use Instead of &ldquo;Said&rdquo;</h2>",
    1,
)
text = text.replace(
    "Dialogue-tag alternatives with meanings, numbered 1–100. Complements section 1.",
    "Dialogue-tag alternatives with meanings, numbered 1–200. Complements section 1.",
    1,
)
text = text.replace(
    '<a href="#faceexpr">Facial expressions (100)</a>',
    '<a href="#faceexpr">Facial expressions (200)</a>',
    1,
)
text = text.replace(
    '<a href="#saidalts">Said alternatives (100)</a>',
    '<a href="#saidalts">Said alternatives (200)</a>',
    1,
)

html_path.write_text(text, encoding="utf-8")
print("updated", html_path.name)
