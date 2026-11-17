# Builds examples/<name>/{SCRIPT.md, SHOTPLAN.md, words.est.json, shots.ts} from one beat table per short.
# Timing model (SKILL.md): ~3.7 words/s, +0.35 s after commas, +0.6 s after sentence ends, +0.9 s at beat ends.
import json, os, re, sys
OUT = sys.argv[1]
FPS, WPS = 30, 3.7

EX = {}
EX["millennium-bridge"] = dict(
 title="The Bridge That Taught a Crowd to March",
 facts="""- Millennium Bridge, London: steel suspension footbridge from St Paul's (north bank) to Tate Modern (south bank).
- Opened 10 June 2000. About 90,000 people crossed on the first day, up to about 2,000 on the deck at once.
- The deck swayed **sideways**. Walkers widened their stance and swayed in time with it, which pushed it further
  ("synchronous lateral excitation"). Nicknamed "the Wobbly Bridge".
- Closed 12 June 2000, two days after opening. Retrofitted with dampers for about £5 million; reopened 22 February 2002.
- No one was hurt.
- Callback: after the 1831 Broughton collapse the British Army ordered troops to break step on bridges (bridge short).
Source: Wikipedia, "Millennium Bridge, London"; Dallard et al., "The London Millennium Footbridge", The Structural Engineer 79 (2001).""",
 analogy="Everyone on a bouncy castle ends up bouncing together without planning it.",
 light_note="Day for the opening, golden for the explanation, day again for the callback.",
 beats=[
  ("Hook", "London built a brand new bridge, and on its very first day, the crowd taught it to dance.", [
    ("day", "crowd", "Low 3/4 on the packed deck, crowd swaying left-right in unison; push in 0.25 %/f, roll 4° on 'dance'", 14)]),
  ("Setting", "It's June 2000. The first new bridge in central London in over a century, a thin steel blade across the river.", [
    ("day", "none", "Aerial: St Paul's dome one end, the brick power station the other, river glittering; zoom push", 0),
    ("day", "none", "Side view down the deck at rail height, the blade shape reading as one clean line", 0)]),
  ("Setting", "Ninety thousand people turn up to walk across it.", [
    ("day", "crowd", "High wide over the entrance ramp, crowd pours on; punch push on 'ninety thousand'", 0)]),
  ("Action", "A few minutes in, the deck starts to wiggle. Not up and down. Sideways.", [
    ("day", "crowd", "MS of the walkers' feet + deck edge; deck slides 4 cm sideways; cut on 'Sideways' to a frontal MS, kick", 12)]),
  ("Action", "So everybody does what you'd do on a wobbly boat. Feet wider, and sway along with it.", [
    ("day", "crowd", "Front MS of the ice-cream tourist: stance widens, body sways; the nervous commuter grabs the rail", 12)]),
  ("Action", "Which pushes the bridge a little further. So they sway a little harder.", [
    ("day", "crowd", "Wide 3/4: the whole deck now visibly swinging; roll 4.5° each way in time", 0)]),
  ("Snap", "Two thousand strangers, who have never met, are now swaying in perfect step.", [
    ("day", "crowd", "Top-down crane: 2,000 heads moving like one marching column; ghost rifleman flashes in for 6 f", 0)]),
  ("Double", "Luckily, nobody fell in. Unluckily, the whole world watched it on the news.", [
    ("day", "crowd", "Calm water under the bridge, one dropped ice cream plops in", 10),
    ("day", "none", "TV-set card on a riverside bench showing the wobbling deck; push in on 'whole world'", 12)]),
  ("Explain", "Every bridge has a rhythm it likes to sway at. Ever been on a bouncy castle when everyone starts jumping? Nobody planned it, but you all end up bouncing together.", [
    ("golden", "none", "Golden wide: empty deck swaying alone at its own slow rhythm", 5),
    ("golden", "park", "Park bouncy castle with kids: one jumps, then all jump together", 7)]),
  ("Explain", "The bridge nudged the crowd, and the crowd nudged it right back.", [
    ("golden", "crowd", "Side view: deck slides right, crowd leans left, repeat; kicks on each 'nudged'", 10)]),
  ("Consequence", "Two days later, they shut it. It took two years and five million pounds of shock absorbers to calm it down.", [
    ("day", "none", "Engineer (stern) at a barrier with a CLOSED gate; hammer kicks", 12),
    ("day", "none", "Insert under the deck: big dampers bolted on one after another", 12)]),
  ("Callback", "Back in 1831, the army banned marching in step on bridges. In 2000, a bridge made a crowd of tourists march in step, all by itself.", [
    ("golden", "march", "Crossfade to the 1831 riflemen breaking step (bridge short's world), sepia-warm golden", 0),
    ("day", "crowd", "Back to 2000: tourists stroll, fall into step, the rifleman ghost grins at camera; crane out", 0)]),
 ])

EX["leaning-tower"] = dict(
 title="The Tower That Was Saved by a War",
 facts="""- Tower of Pisa (campanile of Pisa Cathedral). Construction began in August 1173.
- It began to sink and lean in 1178, after the third floor was built: shallow foundations on soft clay, sand and silt.
- War (Pisa against Genoa, Lucca and Florence) halted building for almost a century. The pause let the soil
  consolidate; historians and engineers agree that without it the tower would very likely have fallen.
- When work resumed (1272, Giovanni di Simone) the upper floors were built taller on one side to compensate,
  so the tower is curved. Completed with the bell chamber in 1372.
- Closed to the public January 1990 (lean about 5.5°). Stabilised 1993-2001, mainly by soil extraction from under
  the north (high) side; straightened by about 45 cm. Reopened December 2001.
Source: Wikipedia, "Leaning Tower of Pisa"; Burland, Jamiolkowski & Viggiani, "Leaning Tower of Pisa: Behaviour after Stabilization Operations" (2009).""",
 analogy="An old mattress firms up where it's been slept on; soft soil squeezed for a century firms up too.",
 light_note="Golden for the Middle Ages, day for the 1990s rescue and today.",
 beats=[
  ("Hook", "The most famous mistake in Italy was saved by a war.", [
    ("day", "crowd", "Low wide: today's tower, tourists in front doing the 'holding it up' pose; push in, roll 4° with the lean", 12)]),
  ("Setting", "It's 1173, and Pisa is rich, proud, and building the most beautiful bell tower in the world.", [
    ("golden", "builders", "Golden aerial over the cathedral square, scaffold on a white stump of a tower", 0),
    ("golden", "builders", "MS master builder (stern) unrolling plans; mason behind with a block", 10)]),
  ("Action", "Five years in, they finish the third floor. And the tower starts to lean.", [
    ("golden", "builders", "Side view of the three-storey stump; it tips 1° with a creak; mason's shock face, kick", 12)]),
  ("Action", "The ground underneath is soft clay and sand. It's like building on a wet sponge.", [
    ("golden", "none", "Cutaway: tower on a cartoon cross-section of soil; the sponge squishes under one side", 0)]),
  ("Action", "Then Pisa goes to war, and the builders down tools. For almost a hundred years.", [
    ("golden", "builders", "Builders drop tools and march off with spears; push on the empty scaffold", 0),
    ("golden", "none", "Time-lapse locked-off on the stump: seasons flicker, grass grows over the tools (a slow creep, never a frozen hold)", 0)]),
  ("Double", "Luckily, that was the best thing that could have happened. Unluckily, nobody knew it at the time.", [
    ("golden", "none", "Soil cross-section: water droplets squeeze out, the layers settle and firm up", 7),
    ("golden", "builders", "Ruined camp, the apprentice (now old) shrugs", 12)]),
  ("Explain", "While the tower sat waiting, the soil slowly squeezed out its water and got firmer. Like a mattress that's been slept on for a century.", [
    ("golden", "none", "Mattress insert: a giant dent that holds its shape; cut back to the tower, steadier", 12)]),
  ("Snap", "Without that break, the tower would have toppled before it was ever finished.", [
    ("golden", "none", "What-if: the tower built in one go topples, white flash + puff; kick", 0)]),
  ("Action", "When the builders came back, they tried to fix the lean by making the new floors taller on the short side. So the tower isn't just leaning. It's bent, like a banana.", [
    ("golden", "builders", "New floors stack up, each tilted back; side-on push in", 0),
    ("golden", "none", "Silhouette insert: a banana slides behind the tower and matches the curve", 12)]),
  ("Consequence", "By 1990 it was leaning so far that they shut it. Engineers spent eleven years pulling soil out from under the high side, until it sank back about forty-five centimetres.", [
    ("day", "none", "Gate slams, 1990 engineer looks up nervously; kick", 12),
    ("day", "none", "Cutaway: drills slurp soil from the north side, tower eases back; push in", 0)]),
  ("Callback", "Not straight, of course. Nobody comes to Pisa to see a straight tower.", [
    ("day", "crowd", "Today: tourists do the pose again; the tower 'leans' a hair more toward them; crane out", 0)]),
 ])

EX["exploding-whale"] = dict(
 title="The Day It Rained Whale",
 facts="""- 12 November 1970, Florence, Oregon: a dead sperm whale about 45 ft long, roughly 8 tons, washed up on the beach.
- Oregon's beaches were legally state highways, so the Oregon State Highway Division had to deal with it.
- It decided to blow it up with half a ton (20 cases) of dynamite, expecting small pieces that scavenging gulls would eat.
- The blast threw large chunks of blubber over spectators hundreds of feet away; one crushed a parked car.
  Its owner had bought it in a dealership promotion called "Get a Whale of a Deal". No one was injured.
- Reporter Paul Linnman's KATU footage became famous. The gulls were scared off by the noise.
- Oregon now buries or tows beached whales. In 2020, Florence named a new park "Exploding Whale Memorial Park" by public vote.
Source: Wikipedia, "Exploding whale" (and its citations to KATU and The Oregonian).""",
 analogy="A firecracker under a soup can: the can flies, the pavement stays put. A blast goes where it's easiest.",
 light_note="Grey-bright day for the beach (use the day preset with a cooler LOOK sky), golden for the epilogue.",
 beats=[
  ("Hook", "In 1970, Oregon got rid of a dead whale by blowing it up. It did not go away.", [
    ("day", "crowd", "Low wide on the beach, crowd in the dunes, the whale a dark hill; on 'blowing it up' a 4 f white flash, cut to black-blue sky full of falling chunks", 14)]),
  ("Setting", "A forty-five foot sperm whale has washed up on the beach in Florence, Oregon. It weighs eight tons, and it smells.", [
    ("day", "none", "Aerial along the coast, the whale tiny on the sand; zoom push", 0),
    ("day", "crowd", "MS of the reporter pinching his nose, wavy stink lines (fx card)", 10)]),
  ("Setting", "In Oregon, the beach counts as a highway. So it's a job for the highway department.", [
    ("day", "none", "Insert: a highway shield sign planted in the sand (road icon only, no words); push in", 12),
    ("day", "crowd", "Highway engineer arrives in the hard hat, smiling", 10)]),
  ("Action", "Their plan: half a ton of dynamite. The whale will break into tiny pieces, and the seagulls will clean up the rest.", [
    ("day", "none", "Crates stacked against the whale; then a happy daydream card of gulls nibbling crumbs", 12)]),
  ("Action", "A crowd gathers. A TV crew starts rolling. Everybody steps back to a safe distance.", [
    ("day", "crowd", "Wide from behind the crowd; they shuffle back up the dunes in unison", 0)]),
  ("Snap", "Boom.", [
    ("day", "none", "Hard cut: the blast, white flash 4 f, sand column, flip kick 1.6", 0)]),
  ("Double", "Luckily, the explosion worked. Unluckily, the explosion worked.", [
    ("day", "crowd", "Engineer's proud grin, holds, then the shadow of a falling chunk grows over him", 12),
    ("day", "crowd", "Crowd from the front: chunks thud all around, everyone runs", 0)]),
  ("Action", "One piece flattens a brand new car. Its owner had just bought it, at a sale called Get a Whale of a Deal.", [
    ("day", "none", "Parked car; a blubber block drops in from top of frame, kick 1.0", 0),
    ("day", "none", "Car owner (dazed) beside it; push in on 'whale of a deal'", 12)]),
  ("Explain", "A blast always goes where it's easiest. The sand underneath pushes back. The air above doesn't. Put a firecracker under a soup can: the can flies, the pavement stays put.", [
    ("golden", "none", "Cutaway diagram card: whale on sand, arrows bouncing off the sand, up into the air", 0),
    ("golden", "park", "Kid with a soup can and a fuse on a sidewalk; can pops up, sidewalk fine", 7)]),
  ("Consequence", "So most of the whale went up, and came straight back down. And the seagulls? They were scared off by the bang.", [
    ("day", "none", "Empty sky, then one gull peeks from behind a dune and leaves", 10)]),
  ("Callback", "Today Oregon buries its whales. And in 2020, the town voted to name a park: Exploding Whale Memorial Park.", [
    ("golden", "crowd", "Golden: ribbon-cutting at a little park, a whale-shaped bench; crowd cheers, crane out", 0)]),
 ])

def timing(beats):
    words, t = [], 0.25
    for _, line, _ in beats:
        toks = line.split()
        for i, w in enumerate(toks):
            d = (len(re.sub(r"\W", "", w)) + 2.0) / ((sum(len(re.sub(r"\W", "", x)) for x in toks) + 2.0 * len(toks)) / len(toks)) / WPS
            words.append({"word": w, "start": round(t, 3), "end": round(t + d, 3)})
            t += d
            if w.endswith((".", "?", "!", ":")): t += 0.42
            elif w.endswith((",", ";")): t += 0.18
        t += 0.15
    return words, t + 0.9

for key, E in EX.items():
    d = os.path.join(OUT, key); os.makedirs(d, exist_ok=True)
    words, dur = timing(E["beats"])
    # normalise speech rate to 3.7 w/s overall (excluding pauses): scale to target length for the word count
    n = len(words)
    total = int(round(dur * FPS))
    json.dump({"note": "ESTIMATED word timings (no voice recorded yet). Replace with real STT timings, then re-time story.ts.", "words": words}, open(os.path.join(d, "words.est.json"), "w"), indent=0)
    # shots
    shots, wi = [], 0
    for bi, (beat, line, sl) in enumerate(E["beats"]):
        nw = len(line.split()); w0, w1 = words[wi], words[wi + nw - 1]
        a = int(round((w0["start"] - (0.25 if bi else w0["start"])) * FPS)); b = int(round((w1["end"] + 0.45) * FPS)) if bi < len(E["beats"]) - 1 else total
        # split the beat's span among its shots by word count of clauses (equal split, cut lands 2 f before a word)
        span = b - a
        for si, (light, crowd, desc, dof) in enumerate(sl):
            sa = a + span * si // len(sl); sb = a + span * (si + 1) // len(sl)
            if si: # snap the cut 2 f before the nearest word start
                ws = [int(round(w["start"] * FPS)) - 2 for w in words[wi:wi + nw]]
                sa = min(ws, key=lambda x: abs(x - sa))
                shots[-1]["b"] = sa
            shots.append(dict(id=len(shots) + 1, a=sa, b=sb, light=light, crowd=crowd, beat=beat, desc=desc, dof=dof))
        wi += nw
    for i in range(1, len(shots)): shots[i]["a"] = shots[i - 1]["b"]
    shots[-1]["b"] = total
    # SCRIPT.md
    script = "\n".join(l for _, l, _ in E["beats"])
    S = [f"# \"{E['title']}\" — script v1 (example made with the cartoon-3d-short skill)",
         f"Format: ~{dur:.0f} s vertical short, {n} words (~{n / dur:.1f} words/s including pauses), one steady narrator, our own characters.",
         "", "## Facts (verify before recording)", E["facts"], "", f"**Everyday analogy:** {E['analogy']}", "", "## Script", script, "",
         "## Beat map (SKILL.md formula)", "| Beat | Line |", "|---|---|"] + [f"| {b} | {l} |" for b, l, _ in E["beats"]]
    open(os.path.join(d, "SCRIPT.md"), "w").write("\n".join(S) + "\n")
    # SHOTPLAN.md
    P = [f"# {E['title']}: shot plan (step 4)", "",
         f"{len(shots)} shots, {total} frames at {FPS} fps ({total / FPS:.1f} s). Frames come from `words.est.json` (estimated timings);",
         "re-time them from the real `words.json` once the voice is recorded. Lighting: " + E["light_note"], "",
         "Camera grammar from SKILL.md: cuts on big jumps, smootherstep glides of 18-40 f, every hold creeps 0.15-0.35 %/f (0.6 %/f on punch words),",
         "4-4.6° rolls, flip-kicks decaying over 7 f on impacts. Every visual reaction lands 0-3 f before its word. No captions.", "",
         "| # | Frames | Sec | Light | Crowd | DOF cInf | Beat | Shot |", "|---|---|---|---|---|---|---|---|"]
    for s in shots:
        P.append(f"| {s['id']} | {s['a']}-{s['b']} | {s['a']/FPS:.1f}-{s['b']/FPS:.1f} | {s['light']} | {s['crowd']} | {s['dof'] or 0} | {s['beat']} | {s['desc']} |")
    P += ["", "## What changes from `templates/bridge/`",
          "- `story.ts`: replace `SHOTS` with `shots.ts.txt` (saved as .txt so it never breaks tsc), rewrite `CAMS`, `KICKS`, `DOF` and `FOREGROUND` per the table.",
          "- `build.ts` / `world.ts`: new set dressing (see the shot list); keep the sky, fog, ink, lens and grade values.",
          "- `cast.ts` / `toon.ts`: the cast in `cast.png` is drawn with the unchanged `toon.ts`; only new `Outfit`s are needed.",
          "- `audio/timeline.py`: mirror the new `SHOTS`, then rebuild SFX + score + mix (music +3 dB, SFX -6 dB, voice unchanged)."]
    open(os.path.join(d, "SHOTPLAN.md"), "w").write("\n".join(P) + "\n")
    # shots.ts
    T = [f"// {E['title']}: SHOTS for story.ts (generated from the estimated word timings; re-time after recording)",
         f"export const TOTAL = {total};",
         "export const SHOTS: ShotDef[] = ["]
    for s in shots: T.append(f"  {{ id: {s['id']}, a: {s['a']}, b: {s['b']}, light: \"{s['light']}\", crowd: \"{s['crowd']}\", tau: (t) => t }}, // {s['beat']}")
    T.append("];")
    open(os.path.join(d, "shots.ts.txt"), "w").write("\n".join(T) + "\n")
    print(key, f"{n} words, {dur:.1f}s, {len(shots)} shots")
