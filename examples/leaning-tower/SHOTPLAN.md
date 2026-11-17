# The Tower That Was Saved by a War: shot plan (step 4)

16 shots, 2044 frames at 30 fps (68.1 s). Frames come from `words.est.json` (estimated timings);
re-time them from the real `words.json` once the voice is recorded. Lighting: Golden for the Middle Ages, day for the 1990s rescue and today.

Camera grammar from SKILL.md: cuts on big jumps, smootherstep glides of 18-40 f, every hold creeps 0.15-0.35 %/f (0.6 %/f on punch words),
4-4.6° rolls, flip-kicks decaying over 7 f on impacts. Every visual reaction lands 0-3 f before its word. No captions.

| # | Frames | Sec | Light | Crowd | DOF cInf | Beat | Shot |
|---|---|---|---|---|---|---|---|
| 1 | 0-110 | 0.0-3.7 | day | crowd | 12 | Hook | Low wide: today's tower, tourists in front doing the 'holding it up' pose; push in, roll 4° with the lean |
| 2 | 110-199 | 3.7-6.6 | golden | builders | 0 | Setting | Golden aerial over the cathedral square, scaffold on a white stump of a tower |
| 3 | 199-281 | 6.6-9.4 | golden | builders | 10 | Setting | MS master builder (stern) unrolling plans; mason behind with a block |
| 4 | 281-430 | 9.4-14.3 | golden | builders | 12 | Action | Side view of the three-storey stump; it tips 1° with a creak; mason's shock face, kick |
| 5 | 430-581 | 14.3-19.4 | golden | none | 0 | Action | Cutaway: tower on a cartoon cross-section of soil; the sponge squishes under one side |
| 6 | 581-658 | 19.4-21.9 | golden | builders | 0 | Action | Builders drop tools and march off with spears; push on the empty scaffold |
| 7 | 658-738 | 21.9-24.6 | golden | none | 0 | Action | Time-lapse locked-off on the stump: seasons flicker, grass grows over the tools (a slow creep, never a frozen hold) |
| 8 | 738-816 | 24.6-27.2 | golden | none | 7 | Double | Soil cross-section: water droplets squeeze out, the layers settle and firm up |
| 9 | 816-916 | 27.2-30.5 | golden | builders | 12 | Double | Ruined camp, the apprentice (now old) shrugs |
| 10 | 916-1154 | 30.5-38.5 | golden | none | 12 | Explain | Mattress insert: a giant dent that holds its shape; cut back to the tower, steadier |
| 11 | 1154-1282 | 38.5-42.7 | golden | none | 0 | Snap | What-if: the tower built in one go topples, white flash + puff; kick |
| 12 | 1282-1436 | 42.7-47.9 | golden | builders | 0 | Action | New floors stack up, each tilted back; side-on push in |
| 13 | 1436-1595 | 47.9-53.2 | golden | none | 12 | Action | Silhouette insert: a banana slides behind the tower and matches the curve |
| 14 | 1595-1734 | 53.2-57.8 | day | none | 12 | Consequence | Gate slams, 1990 engineer looks up nervously; kick |
| 15 | 1734-1873 | 57.8-62.4 | day | none | 0 | Consequence | Cutaway: drills slurp soil from the north side, tower eases back; push in |
| 16 | 1873-2044 | 62.4-68.1 | day | crowd | 0 | Callback | Today: tourists do the pose again; the tower 'leans' a hair more toward them; crane out |

## What changes from `templates/bridge/`
- `story.ts`: replace `SHOTS` with `shots.ts.txt` (saved as .txt so it never breaks tsc), rewrite `CAMS`, `KICKS`, `DOF` and `FOREGROUND` per the table.
- `build.ts` / `world.ts`: new set dressing (see the shot list); keep the sky, fog, ink, lens and grade values.
- `cast.ts` / `toon.ts`: the cast in `cast.png` is drawn with the unchanged `toon.ts`; only new `Outfit`s are needed.
- `audio/timeline.py`: mirror the new `SHOTS`, then rebuild SFX + score + mix (music +3 dB, SFX -6 dB, voice unchanged).
