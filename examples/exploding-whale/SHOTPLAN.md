# The Day It Rained Whale: shot plan (step 4)

16 shots, 2077 frames at 30 fps (69.2 s). Frames come from `words.est.json` (estimated timings);
re-time them from the real `words.json` once the voice is recorded. Lighting: Grey-bright day for the beach (use the day preset with a cooler LOOK sky), golden for the epilogue.

Camera grammar from SKILL.md: cuts on big jumps, smootherstep glides of 18-40 f, every hold creeps 0.15-0.35 %/f (0.6 %/f on punch words),
4-4.6° rolls, flip-kicks decaying over 7 f on impacts. Every visual reaction lands 0-3 f before its word. No captions.

| # | Frames | Sec | Light | Crowd | DOF cInf | Beat | Shot |
|---|---|---|---|---|---|---|---|
| 1 | 0-185 | 0.0-6.2 | day | crowd | 14 | Hook | Low wide on the beach, crowd in the dunes, the whale a dark hill; on 'blowing it up' a 4 f white flash, cut to black-blue sky full of falling chunks |
| 2 | 185-279 | 6.2-9.3 | day | none | 0 | Setting | Aerial along the coast, the whale tiny on the sand; zoom push |
| 3 | 279-396 | 9.3-13.2 | day | crowd | 10 | Setting | MS of the reporter pinching his nose, wavy stink lines (fx card) |
| 4 | 396-480 | 13.2-16.0 | day | none | 12 | Setting | Insert: a highway shield sign planted in the sand (road icon only, no words); push in |
| 5 | 480-561 | 16.0-18.7 | day | crowd | 10 | Setting | Highway engineer arrives in the hard hat, smiling |
| 6 | 561-787 | 18.7-26.2 | day | none | 12 | Action | Crates stacked against the whale; then a happy daydream card of gulls nibbling crumbs |
| 7 | 787-951 | 26.2-31.7 | day | crowd | 0 | Action | Wide from behind the crowd; they shuffle back up the dunes in unison |
| 8 | 951-976 | 31.7-32.5 | day | none | 0 | Snap | Hard cut: the blast, white flash 4 f, sand column, flip kick 1.6 |
| 9 | 976-1027 | 32.5-34.2 | day | crowd | 12 | Double | Engineer's proud grin, holds, then the shadow of a falling chunk grows over him |
| 10 | 1027-1081 | 34.2-36.0 | day | crowd | 0 | Double | Crowd from the front: chunks thud all around, everyone runs |
| 11 | 1081-1192 | 36.0-39.7 | day | none | 0 | Action | Parked car; a blubber block drops in from top of frame, kick 1.0 |
| 12 | 1192-1303 | 39.7-43.4 | day | none | 12 | Action | Car owner (dazed) beside it; push in on 'whale of a deal' |
| 13 | 1303-1454 | 43.4-48.5 | golden | none | 0 | Explain | Cutaway diagram card: whale on sand, arrows bouncing off the sand, up into the air |
| 14 | 1454-1619 | 48.5-54.0 | golden | park | 7 | Explain | Kid with a soup can and a fuse on a sidewalk; can pops up, sidewalk fine |
| 15 | 1619-1845 | 54.0-61.5 | day | none | 10 | Consequence | Empty sky, then one gull peeks from behind a dune and leaves |
| 16 | 1845-2077 | 61.5-69.2 | golden | crowd | 0 | Callback | Golden: ribbon-cutting at a little park, a whale-shaped bench; crowd cheers, crane out |

## What changes from `templates/bridge/`
- `story.ts`: replace `SHOTS` with `shots.ts.txt` (saved as .txt so it never breaks tsc), rewrite `CAMS`, `KICKS`, `DOF` and `FOREGROUND` per the table.
- `build.ts` / `world.ts`: new set dressing (see the shot list); keep the sky, fog, ink, lens and grade values.
- `cast.ts` / `toon.ts`: the cast in `cast.png` is drawn with the unchanged `toon.ts`; only new `Outfit`s are needed.
- `audio/timeline.py`: mirror the new `SHOTS`, then rebuild SFX + score + mix (music +3 dB, SFX -6 dB, voice unchanged).
