# -*- coding: utf-8 -*-
"""Append 400 facial-expression entries that are not already in section 7."""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "Writing-Word-Banks.html"

# group, term, meaning. Terms must not repeat the existing 200.
ITEMS = r"""
Smiles and grins|ghost of a smile|a smile almost not there
Smiles and grins|hint of a smile|the start of a smile, quickly gone
Smiles and grins|whisper of a smile|a very small private smile
Smiles and grins|almost-smile|the mouth starts to smile and stops
Smiles and grins|bitten-back smile|a smile stopped on purpose
Smiles and grins|suppressed smile|amusement held in
Smiles and grins|private smile|a smile meant for no one else
Smiles and grins|secret smile|a smile that knows something
Smiles and grins|slow smile|a smile that arrives unhurried
Smiles and grins|quick smile|a smile flashed and gone
Smiles and grins|fleeting smile|a smile that does not stay
Smiles and grins|vanishing smile|a smile dying as you watch
Smiles and grins|returning smile|a smile coming back after it faded
Smiles and grins|watery smile|a smile close to tears
Smiles and grins|shaky smile|a smile that is not steady
Smiles and grins|trembling smile|a smile fighting a quiver
Smiles and grins|brave smile|a smile worn over fear or pain
Smiles and grins|brittle smile|a smile that could crack
Smiles and grins|polite smile|courtesy with little feeling behind it
Smiles and grins|professional smile|a smile put on for the job
Smiles and grins|practiced smile|a smile used so often it looks easy
Smiles and grins|automatic smile|a smile that happens without thought
Smiles and grins|painted smile|a smile that looks applied
Smiles and grins|plastered smile|a smile stuck on too hard
Smiles and grins|public smile|the smile kept for other people
Smiles and grins|reluctant smile|a smile given unwillingly
Smiles and grins|unwilling smile|a smile pulled out against resistance
Smiles and grins|surprised smile|a smile startled out of them
Smiles and grins|sleepy smile|a soft smile half lost to sleep
Smiles and grins|tired smile|warmth with no energy left
Smiles and grins|small smile|a modest, contained smile
Smiles and grins|tiny smile|barely a change at the mouth
Smiles and grins|dimpled smile|a smile that sets a dimple
Smiles and grins|one-cornered smile|only one corner of the mouth lifts
Smiles and grins|mouth-only smile|the mouth smiles and the eyes do not
Smiles and grins|eyes-only smile|warmth in the eyes, the mouth still
Smiles and grins|real smile|a smile the whole face joins
Smiles and grins|genuine grin|an unforced, open grin
Smiles and grins|dazzling smile|a bright smile meant to be seen
Smiles and grins|winning smile|a smile that asks to be liked
Smiles and grins|triumphant smile|a smile after getting what they wanted
Smiles and grins|victorious grin|an open grin of having won
Smiles and grins|predatory smile|a smile with intent behind it
Smiles and grins|shark smile|a smile of teeth and no warmth
Smiles and grins|honeyed smile|a sweet smile that may not be kind
Smiles and grins|wintry smile|a cold smile with no thaw in it
Smiles and grins|inward smile|pleasure kept mostly to themselves
Smiles and grins|conspiratorial smile|a smile that shares a secret plot
Smiles and grins|complicit look|a face that says they are in on it
Smiles and grins|anxious smile|a smile trying to cover worry
Smiles and grins|nervous smile|a smile that gives the nerves away
Smiles and grins|uneasy smile|a smile that does not settle
Smiles and grins|pained smile|a smile pushed through hurt
Smiles and grins|sorry smile|a smile asking pardon
Smiles and grins|thanks plain on the face|gratitude showing before any words
Smiles and grins|open admiration|a face openly impressed
Smiles and grins|adoring look|a face gone soft with love
Smiles and grins|besotted look|foolishly, openly in love
Smiles and grins|smitten look|caught off guard by attraction
Smiles and grins|lovesick expression|a face pining and distracted
Smiles and grins|moonstruck look|dazed with romance
Smiles and grins|starry-eyed look|hope or love making the eyes shine
Smiles and grins|calf-eyed look|soft, foolishly tender eyes
Smiles and grins|doe-eyed look|wide, innocent, appealing eyes
Smiles and grins|sleepy-eyed look|eyes heavy, not fully with you
Smiles and grins|side-eye|a sideways look of doubt or judgment
Smiles and grins|stink eye|a look meant to wither
Smiles and grins|withering look|a look that shrinks the other person
Smiles and grins|scathing look|a look sharp enough to cut
Smiles and grins|cutting glance|a brief, unkind look
Eyes and gazes|once-over|a look that takes the whole person in
Eyes and gazes|double take|a second look when the first does not fit
Eyes and gazes|second glance|attention pulled back for another look
Eyes and gazes|long look|a gaze that stays
Eyes and gazes|measuring look|a look that judges size, worth, or threat
Eyes and gazes|appraising look|a look pricing something up
Eyes and gazes|searching look|eyes hunting a face for an answer
Eyes and gazes|seeking eyes|eyes asking to be met
Eyes and gazes|watchful eyes|eyes that miss little
Eyes and gazes|wary eyes|eyes expecting trouble
Eyes and gazes|alert expression|a face switched on and ready
Eyes and gazes|drowsy look|a face losing the fight with sleep
Eyes and gazes|unfocused gaze|eyes aimed nowhere in particular
Eyes and gazes|unseeing stare|eyes open and taking nothing in
Eyes and gazes|glazed look|eyes shiny and not quite present
Eyes and gazes|fever-bright eyes|eyes too shiny with heat or excitement
Eyes and gazes|sunken eyes|eyes set deep from exhaustion or illness
Eyes and gazes|shadowed eyes|eyes darkened underneath
Eyes and gazes|red-rimmed eyes|eyes raw from crying or no sleep
Eyes and gazes|bloodshot eyes|eyes threaded with red
Eyes and gazes|puffy eyes|eyes swollen from tears or sleep
Eyes and gazes|heavy-lidded look|lids dropped low over the eyes
Eyes and gazes|half-lidded eyes|eyes partly closed, tired or sly
Eyes and gazes|slitted eyes|eyes narrowed to lines
Eyes and gazes|saucer eyes|eyes gone round with shock
Eyes and gazes|startled eyes|eyes jumped wide
Eyes and gazes|stunned look|a face that has not caught up yet
Eyes and gazes|poleaxed expression|a face hit flat by surprise
Eyes and gazes|thunderstruck face|a face stopped by shock
Eyes and gazes|slack-jawed look|mouth open, surprise unfinished
Eyes and gazes|dawning look|understanding arriving on the face
Eyes and gazes|flash of recognition|the face lighting as a person or fact lands
Eyes and gazes|blank of nonrecognition|a face that does not know you
Eyes and gazes|baffled look|a face with no answer
Eyes and gazes|mystified expression|puzzled past ordinary confusion
Eyes and gazes|perplexed frown|a frown that is thinking, not angry
Eyes and gazes|confounded look|a face stopped by what will not make sense
Eyes and gazes|speechless look|a face with the words knocked out of it
Eyes and gazes|lost expression|a face that has misplaced the moment
Eyes and gazes|middle-distance gaze|eyes parked past the people in the room
Eyes and gazes|inward look|attention turned inside
Eyes and gazes|thousand-yard stare|eyes fixed on a distance no one else sees
Eyes and gazes|watchful stillness|a face held quiet so the eyes can work
Eyes and gazes|keen look|a sharp, interested face
Eyes and gazes|sharp glance|a fast look that catches detail
Eyes and gazes|soft eyes|a gaze with the harshness gone
Eyes and gazes|cold eyes|a gaze with no warmth in it
Eyes and gazes|flat eyes|eyes with the life pressed out
Eyes and gazes|dull eyes|eyes without shine or interest
Eyes and gazes|sparkling eyes|eyes lit with amusement or joy
Eyes and gazes|twinkling eyes|eyes laughing before the mouth does
Eyes and gazes|dancing eyes|eyes alive with mischief or delight
Eyes and gazes|laughing eyes|amusement sitting in the eyes
Eyes and gazes|smiling eyes|warmth that reaches the eyes
Eyes and gazes|shining eyes|eyes wet or bright with feeling
Eyes and gazes|wet eyes|eyes holding tears not yet fallen
Eyes and gazes|brimming eyes|eyes full and about to spill
Eyes and gazes|unshed tears|tears held at the lid
Eyes and gazes|a single tear|one tear let go
Eyes and gazes|blinked-back tears|tears stopped by a blink
Eyes and gazes|lowered lashes|eyes dropped behind the lashes
Eyes and gazes|a look from under the lashes|a look offered from beneath the lashes
Eyes and gazes|clumped lashes|lashes stuck together with tears
Eyes and gazes|dark circles|shadows bruised under the eyes
Eyes and gazes|ringed eyes|eyes circled from lack of sleep
Eyes and gazes|sleep-creased face|a face still marked by the pillow
Eyes and gazes|just-woken look|puffy, slow, not assembled yet
Eyes and gazes|waking expression|a face coming back into the room
Eyes and gazes|startled-awake look|a face jerked out of sleep
Eyes and gazes|light-shy squint|eyes narrowed against brightness
Eyes and gazes|suspicious squint|eyes narrowed on a doubt
Eyes and gazes|doubtful look|a face not ready to believe
Eyes and gazes|dubious expression|skepticism short of a sneer
Eyes and gazes|uncertain look|a face that has not decided
Eyes and gazes|certain look|a face already settled
Eyes and gazes|confident expression|a face that expects to be right
Eyes and gazes|assured look|calm certainty in the face
Eyes and gazes|arrogant expression|a face that ranks itself higher
Eyes and gazes|haughty look|pride held at a distance
Eyes and gazes|sidelong glance|a look slid sideways without turning the head
Brow, color, and the whole face|knitted brows|brows pulled together in worry or pain
Brow, color, and the whole face|brows drawn together|brows tight, the forehead involved
Brow, color, and the whole face|brows shot up|both brows jumped in surprise
Brow, color, and the whole face|a single brow asking|one brow lifted and the rest of the face waiting
Brow, color, and the whole face|brows slammed down|brows driven into a frown
Brow, color, and the whole face|smooth brow|a forehead with the lines gone
Brow, color, and the whole face|lined brow|a forehead creased with thought or years
Brow, color, and the whole face|creased forehead|horizontal lines of worry or surprise
Brow, color, and the whole face|wrinkled forehead|a forehead bunched up
Brow, color, and the whole face|shiny forehead|sweat or heat on the brow
Brow, color, and the whole face|beaded brow|sweat standing in drops
Brow, color, and the whole face|sweaty upper lip|nerves or heat showing above the mouth
Brow, color, and the whole face|color rising|a blush or flush climbing the face
Brow, color, and the whole face|blush creeping|color spreading, not all at once
Brow, color, and the whole face|high color|a strong flush in the cheeks
Brow, color, and the whole face|hectic flush|uneven, feverish color
Brow, color, and the whole face|angry flush|red driven up by temper
Brow, color, and the whole face|shame flush|color from being caught or embarrassed
Brow, color, and the whole face|pleasure flush|color from delight or desire
Brow, color, and the whole face|blotchy face|color in uneven patches
Brow, color, and the whole face|mottled face|the face patched red and pale
Brow, color, and the whole face|gray face|color gone toward ash
Brow, color, and the whole face|green about the gills|a sick, faintly green pallor
Brow, color, and the whole face|pasty face|dull, unhealthy pale
Brow, color, and the whole face|sallow face|a yellowish pale
Brow, color, and the whole face|waxen face|pale with a still, candle-like look
Brow, color, and the whole face|chalky face|white, with no warmth in it
Brow, color, and the whole face|paper-white face|drained almost to white
Brow, color, and the whole face|ruddy face|reddened by health, heat, or weather
Brow, color, and the whole face|weather-beaten face|a face marked by sun and wind
Brow, color, and the whole face|sunburned face|skin hot and red from the sun
Brow, color, and the whole face|windburned cheeks|cheeks raw from cold wind
Brow, color, and the whole face|color draining|blood leaving the face
Brow, color, and the whole face|color flooding back|warmth returning after a shock
Brow, color, and the whole face|face going red|a visible rush of blood
Brow, color, and the whole face|face going white|color dropping out fast
Brow, color, and the whole face|face clouding|the expression darkening
Brow, color, and the whole face|face clearing|trouble leaving the features
Brow, color, and the whole face|face falling|delight or hope collapsing
Brow, color, and the whole face|face lighting up|joy arriving all at once
Brow, color, and the whole face|face softening|the hard lines letting go
Brow, color, and the whole face|face hardening|the features setting against something
Brow, color, and the whole face|face closing|the expression shutting down
Brow, color, and the whole face|face opening|a guarded face becoming readable
Brow, color, and the whole face|composure cracking|control starting to fail on the face
Brow, color, and the whole face|mask slipping|the performed expression failing
Brow, color, and the whole face|features smoothing|tension leaving the face
Brow, color, and the whole face|features tightening|the whole face drawing in
Brow, color, and the whole face|restless face|an expression that will not settle
Brow, color, and the whole face|still face|features held motionless on purpose
Mouth, lips, and jaw|jaw slack|the jaw loose with shock or exhaustion
Mouth, lips, and jaw|jaw set hard|the jaw locked on purpose
Mouth, lips, and jaw|jaw working|the jaw moving as they chew on a feeling
Mouth, lips, and jaw|a muscle jumping in the jaw|a small tic of held anger
Mouth, lips, and jaw|gritted teeth|teeth clamped, words or pain held back
Mouth, lips, and jaw|bared teeth|teeth shown in threat or effort, not a smile
Mouth, lips, and jaw|teeth clenched|the bite locked shut
Mouth, lips, and jaw|tongue in cheek|a look of not being entirely serious
Mouth, lips, and jaw|tongue between the teeth|concentration, or a childish pause
Mouth, lips, and jaw|sucked-in cheeks|cheeks pulled tight
Mouth, lips, and jaw|puffed cheeks|cheeks full of held breath
Mouth, lips, and jaw|hollow cheeks|cheeks fallen in
Mouth, lips, and jaw|gaunt face|a face thinned by hunger, illness, or strain
Mouth, lips, and jaw|one dimple showing|a single dimple giving the smile away
Mouth, lips, and jaw|smile lines|creases that say the face smiles often
Mouth, lips, and jaw|laugh lines|lines at the eyes from years of laughing
Mouth, lips, and jaw|crow's feet|fine lines raying from the outer eyes
Mouth, lips, and jaw|deep lines at the mouth|lines cut beside the lips
Mouth, lips, and jaw|pale about the mouth|the ring around the lips gone white
Mouth, lips, and jaw|white-lipped look|lips pressed bloodless
Mouth, lips, and jaw|bloodless lips|lips with the color gone
Mouth, lips, and jaw|a raw worried lip|a lip worn by the teeth
Mouth, lips, and jaw|chewed lip|a lip worried by the teeth
Mouth, lips, and jaw|parted lips|the mouth slightly open
Mouth, lips, and jaw|lips ajar|the mouth open a little, unfinished
Mouth, lips, and jaw|pressed-thin lips|lips mashed into a line
Mouth, lips, and jaw|a white line of a mouth|the mouth held so tight it pales
Mouth, lips, and jaw|downturned eyes|sadness sitting in the eyes
Mouth, lips, and jaw|upturned eyes|a hopeful or pleading lift of the gaze
Mouth, lips, and jaw|working mouth|the mouth moving before words come
Mouth, lips, and jaw|silent mouth|lips still when speech was expected
Mouth, lips, and jaw|twitching mouth|the mouth jerking, short of a full expression
Mouth, lips, and jaw|twitching eyelid|a small involuntary jump at the eye
Mouth, lips, and jaw|a tic at the mouth|a repeated small pull at the lip
Mouth, lips, and jaw|a vein at the temple|anger or strain showing under the skin
Mouth, lips, and jaw|a throbbing temple|a pulse visible at the side of the head
Mouth, lips, and jaw|scrunched nose|the nose bunched at a smell or a dislike
Mouth, lips, and jaw|pinched nostrils|the nose drawn tight
Mouth, lips, and jaw|mouth dropped open|the mouth fallen and left there
Mouth, lips, and jaw|mouth held shut|the lips closed on purpose
Mouth, lips, and jaw|firm mouth|a mouth set and decided
Mouth, lips, and jaw|soft mouth|a mouth with the tension gone
Mouth, lips, and jaw|sullen mouth|a mouth dragged down in a sulk
Mouth, lips, and jaw|stubborn mouth|a mouth set against giving in
Mouth, lips, and jaw|generous mouth|a mouth that looks ready to be kind
Mouth, lips, and jaw|thin mouth|a mouth narrowed, severe or held in
Mouth, lips, and jaw|full pout|the lower lip pushed out
Mouth, lips, and jaw|childish pout|a pout that wants its way
Mouth, lips, and jaw|sulky expression|a face withdrawn into a sulk
Mouth, lips, and jaw|cheek caught in the teeth|the inside of the cheek bitten to stay quiet
Looks that answer someone|unamused look|a face refusing the joke
Looks that answer someone|unimpressed expression|a face that has seen better
Looks that answer someone|bored look|interest gone from the face
Looks that answer someone|patient expression|a face willing to wait
Looks that answer someone|impatient look|a face done with waiting
Looks that answer someone|long-suffering look|a face that has endured this before
Looks that answer someone|exasperated expression|patience used up
Looks that answer someone|irritated look|a face pricked and unhappy about it
Looks that answer someone|annoyed frown|a frown of everyday irritation
Looks that answer someone|peeved expression|mildly, personally offended
Looks that answer someone|cross look|short-tempered and showing it
Looks that answer someone|petulant expression|fretful and easily offended
Looks that answer someone|mulish look|stubborn, and dull about it
Looks that answer someone|resigned expression|a face that has stopped fighting
Looks that answer someone|accepting look|a face making peace with the news
Looks that answer someone|unyielding expression|a face that will not bend
Looks that answer someone|stern look|serious correction in the face
Looks that answer someone|severe expression|a face with no softness allowed
Looks that answer someone|tender look|a face gone careful and loving
Looks that answer someone|gentle expression|a face that will not startle or scold
Looks that answer someone|frosty look|cold courtesy in the eyes
Looks that answer someone|glacial expression|a freeze with no crack in it
Looks that answer someone|heated look|feeling running hot in the face
Looks that answer someone|smoldering look|heat held under a still face
Looks that answer someone|level look|a steady face with no drama
Looks that answer someone|steady gaze|eyes that do not flick away
Looks that answer someone|shaky expression|a face not holding together
Looks that answer someone|fragile look|a face that seems easy to break
Looks that answer someone|raw expression|feeling with no cover on it
Looks that answer someone|exposed look|a face caught without its guard
Looks that answer someone|unreadable expression|a face giving nothing
Looks that answer someone|shuttered eyes|eyes closed against being read
Looks that answer someone|veiled look|feeling covered, but not gone
Looks that answer someone|candid expression|an unguarded, honest face
Looks that answer someone|frank look|a face speaking plainly
Looks that answer someone|lying face|an expression arranged to hide the truth
Looks that answer someone|public face|the expression worn for the room
Looks that answer someone|private face|the expression that shows when the performance stops
Looks that answer someone|polite interest|attention offered as manners
Looks that answer someone|polite boredom|boredom dressed as courtesy
Looks that answer someone|fake concern|worry performed, not felt
Looks that answer someone|real concern|worry the face cannot neaten
Looks that answer someone|concerned frown|a frown bent toward someone else's trouble
Looks that answer someone|sympathetic look|a face sharing the hurt
Looks that answer someone|understanding look|a face that has caught the meaning
Looks that answer someone|warning look|a face telling someone to stop
Looks that answer someone|stay-quiet look|a face asking for silence
Looks that answer someone|I-told-you-so look|a face claiming it already knew
Looks that answer someone|not-now look|a face postponing the conversation
Looks that answer someone|enough look|a face that has reached its limit
Looks that answer someone|come-here look|a face calling someone closer
Looks that answer someone|go-on look|a face urging the next word
Looks that answer someone|wait-for-it look|a face holding the moment
Looks that answer someone|don't-you-dare look|a face forbidding the next move
Looks that answer someone|you-first look|a face handing the moment over
Looks that answer someone|sizing-up look|a look taking a person's measure
Looks that answer someone|challenging stare|a stare that dares an answer
Looks that answer someone|inviting expression|a face leaving the door open
Looks that answer someone|forbidding expression|a face that bars approach
Looks that answer someone|dismissive look|a face waving the matter away
Feeling on the face|startled expression|the face jerked by a surprise
Feeling on the face|shocked expression|a face struck and not recovered
Feeling on the face|surprised expression|brows and mouth caught mid-reaction
Feeling on the face|astonished look|surprise large enough to stop the face
Feeling on the face|wonderstruck face|a face halted by wonder
Feeling on the face|marveling look|a face taking in something rare
Feeling on the face|reverent expression|a face treating something as sacred
Feeling on the face|worshipful look|a gaze that lifts someone up
Feeling on the face|devoted expression|steady love sitting in the face
Feeling on the face|world-weary look|a face tired of the world, not just the day
Feeling on the face|jaded expression|a face that expects to be disappointed
Feeling on the face|cynical look|a face that doubts the good version
Feeling on the face|tired-of-it expression|weariness aimed at this specific thing
Feeling on the face|wary expression|a face braced for a trick
Feeling on the face|trusting look|a face that has decided to believe
Feeling on the face|hopeful eyes|expectation sitting in the eyes
Feeling on the face|doubtful eyes|the doubt living in the gaze
Feeling on the face|old eyes|too much already seen in the eyes
Feeling on the face|knowing eyes|eyes that have already understood
Feeling on the face|frightened eyes|fear plain in the gaze
Feeling on the face|terrified expression|fear past the point of hiding
Feeling on the face|panicked look|a face with the thinking knocked loose
Feeling on the face|cornered look|a face that sees no way out
Feeling on the face|hunted look|a face listening for what is behind it
Feeling on the face|haunted eyes|eyes still carrying an old fear
Feeling on the face|grieving eyes|loss sitting in the gaze
Feeling on the face|bereft expression|a face after something is gone
Feeling on the face|hollow expression|a face emptied out
Feeling on the face|numb look|a face that has stopped showing feeling
Feeling on the face|dazed smile|a smile from someone not fully here
Feeling on the face|fogged look|a face cloudy after a blow, a drink, or no sleep
Feeling on the face|loose, drunken look|a face poorly aimed and slow
Feeling on the face|sober expression|a face gone serious and clear
Feeling on the face|intent look|the whole face aimed at one thing
Feeling on the face|absorbed expression|a face lost in what it is doing
Feeling on the face|distracted look|a face only half in the conversation
Feeling on the face|absent expression|the person gone from their own face
Feeling on the face|present look|a face fully arrived and listening
Feeling on the face|rapt expression|attention so complete the face forgets itself
Feeling on the face|bored-to-tears look|boredom deep enough to show
Feeling on the face|fed-up expression|a face at the end of its patience
Feeling on the face|disgusted curl|the mouth twisting off the thing
Feeling on the face|revolted expression|the face rejecting something bodily
Feeling on the face|nauseated look|a face fighting sickness
Feeling on the face|pained wince|the face flinching from hurt
Feeling on the face|agony in the face|pain too large for the features
Feeling on the face|relief flooding the face|the features letting go at once
Feeling on the face|hope breaking|expectation failing on the face
Feeling on the face|hope kindling|a small light coming into the face
Feeling on the face|pride in the eyes|satisfaction that will not quite become a smile
Feeling on the face|shame in the eyes|the gaze dropping under its own weight
Feeling on the face|guilt flickering|a brief, caught look
Feeling on the face|envy tightening the face|wanting that pulls the features in
Feeling on the face|scorn in the eyes|contempt without the full sneer
Feeling on the face|affection in the face|liking showing before it is said
Feeling on the face|dislike plain on the face|the rejection not hidden
Feeling on the face|interest waking|the face coming alert
Feeling on the face|interest dying|attention leaving the features
Feeling on the face|concentration face|a face narrowed onto a task
Feeling on the face|effort in the face|strain showing as they try
Feeling on the face|strain around the eyes|effort or pain sitting at the eyes
Feeling on the face|peace in the face|the features at rest
Feeling on the face|unease in the face|something wrong, not yet named
Feeling on the face|suspicion in the eyes|the gaze testing what it sees
Feeling on the face|trust relaxing the face|the guard coming down
Feeling on the face|fear tightening the mouth|the mouth reacting before the rest
Feeling on the face|anger banked|temper held, and still visible
Feeling on the face|anger breaking|temper arriving on the face
Feeling on the face|joy breaking|delight the face cannot keep formal
Feeling on the face|sorrow settling|sadness taking a place and staying
Feeling on the face|laughter threatening|the face about to give way to a laugh
Feeling on the face|tears threatening|the face about to give way to crying
Feeling on the face|a held-together face|control visible because it is costing something
Feeling on the face|a coming-apart face|control failing in pieces
Feeling on the face|an open-mouthed laugh|laughter with the mouth fully in it
Feeling on the face|a silent laugh|the face laughing with no sound yet
Feeling on the face|a bitten laugh|a laugh stopped behind the teeth
Feeling on the face|eyes squeezed shut|the eyes closed hard against something
Feeling on the face|eyes slammed shut|a fast, defensive close of the eyes
Feeling on the face|eyes flying open|the eyes yanked wide
Feeling on the face|a slow blink|a blink that resets the face, or judges
Feeling on the face|a hard blink|a blink pushing something back
Feeling on the face|rapid blinking|blinking that gives away nerves, dust, or tears
Feeling on the face|an unblinking stare|a stare that forgets to blink
Feeling on the face|a swallowed expression|a reaction caught and pulled back down
Feeling on the face|a leaked expression|a feeling that gets out before it can be stopped
Feeling on the face|an arranged face|features placed on purpose
Feeling on the face|an unarranged face|the expression before anyone performs it
Feeling on the face|a borrowed expression|a face copied from someone else in the room
Feeling on the face|the true face|the expression left when the performance stops
""".strip().splitlines()


def norm(s):
    s = s.lower().replace("’", "'")
    return re.sub(r"[^a-z0-9]+", "", s)


def main():
    text = SRC.read_text(encoding="utf-8")
    m = re.search(r'(<section id="faceexpr">)(.*?)(</section>)', text, re.S)
    if not m:
        raise SystemExit("faceexpr section missing")
    body = m.group(2)
    existing = [norm(x) for x in re.findall(r"<strong>\d+\. ([^<]+)</strong>", body)]
    if len(existing) != 200:
        raise SystemExit(f"expected 200 existing faces, found {len(existing)}")
    used = set(existing)
    parsed = []
    for line in ITEMS:
        group, term, meaning = line.split("|", 2)
        k = norm(term)
        if k in used:
            raise SystemExit(f"duplicate of existing or earlier item: {term}")
        used.add(k)
        parsed.append((group.strip(), term.strip(), meaning.strip()))
    if len(parsed) != 400:
        raise SystemExit(f"expected 400 new items, found {len(parsed)}")

    groups = []
    for group, term, meaning in parsed:
        if not groups or groups[-1][0] != group:
            groups.append((group, []))
        groups[-1][1].append((term, meaning))

    n = 201
    blocks = []
    for group, rows in groups:
        lines = []
        for term, meaning in rows:
            lines.append(
                f"            <li><strong>{n}. {html.escape(term)}</strong> – {html.escape(meaning)}</li>"
            )
            n += 1
        blocks.append(
            "        <div class=\"entry filterable\">\n"
            f"          <h3>{html.escape(group)}</h3>\n"
            "          <ul class=\"def-list\">\n"
            + "\n".join(lines)
            + "\n          </ul>\n"
            "        </div>"
        )
    if n != 601:
        raise SystemExit(f"numbering ended at {n - 1}")

    body = body.replace(
        "7. 200 Words to Describe Facial Expressions",
        "7. 600 Words to Describe Facial Expressions",
        1,
    )
    body = body.replace(
        "Face cues and micro-expressions with meanings, numbered 1–200.",
        "Face cues and micro-expressions with meanings, numbered 1–600. The first 200 are the original list. The rest are grouped.",
        1,
    )
    new_body = body.rstrip() + "\n" + "\n".join(blocks) + "\n      "
    text = text[: m.start(2)] + new_body + text[m.end(2) :]
    text = text.replace(
        '<a href="#faceexpr">Facial expressions (200)</a>',
        '<a href="#faceexpr">Facial expressions (600)</a>',
        1,
    )
    SRC.write_text(text, encoding="utf-8")
    (ROOT / "docs" / "word-banks.html").write_text(text, encoding="utf-8")
    print("groups:", ", ".join(f"{g} ({len(rows)})" for g, rows in groups))
    print("wrote 201–600")


if __name__ == "__main__":
    main()
