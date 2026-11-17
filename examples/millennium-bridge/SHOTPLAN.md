# The Bridge That Taught a Crowd to March: shot plan (step 4)

17 shots, 2125 frames at 30 fps (70.8 s). Frames come from `words.est.json` (estimated timings);
re-time them from the real `words.json` once the voice is recorded. Lighting: Day for the opening, golden for the explanation, day again for the callback.

Camera grammar from SKILL.md: cuts on big jumps, smootherstep glides of 18-40 f, every hold creeps 0.15-0.35 %/f (0.6 %/f on punch words),
4-4.6° rolls, flip-kicks decaying over 7 f on impacts. Every visual reaction lands 0-3 f before its word. No captions.

| # | Frames | Sec | Light | Crowd | DOF cInf | Beat | Shot |
|---|---|---|---|---|---|---|---|
| 1 | 0-178 | 0.0-5.9 | day | crowd | 14 | Hook | Low 3/4 on the packed deck, crowd swaying left-right in unison; push in 0.25 %/f, roll 4° on 'dance' |
| 2 | 178-276 | 5.9-9.2 | day | none | 0 | Setting | Aerial: St Paul's dome one end, the brick power station the other, river glittering; zoom push |
| 3 | 276-383 | 9.2-12.8 | day | none | 0 | Setting | Side view down the deck at rail height, the blade shape reading as one clean line |
| 4 | 383-473 | 12.8-15.8 | day | crowd | 0 | Setting | High wide over the entrance ramp, crowd pours on; punch push on 'ninety thousand' |
| 5 | 473-634 | 15.8-21.1 | day | crowd | 12 | Action | MS of the walkers' feet + deck edge; deck slides 4 cm sideways; cut on 'Sideways' to a frontal MS, kick |
| 6 | 634-807 | 21.1-26.9 | day | crowd | 12 | Action | Front MS of the ice-cream tourist: stance widens, body sways; the nervous commuter grabs the rail |
| 7 | 807-942 | 26.9-31.4 | day | crowd | 0 | Action | Wide 3/4: the whole deck now visibly swinging; roll 4.5° each way in time |
| 8 | 942-1076 | 31.4-35.9 | day | crowd | 0 | Snap | Top-down crane: 2,000 heads moving like one marching column; ghost rifleman flashes in for 6 f |
| 9 | 1076-1148 | 35.9-38.3 | day | crowd | 10 | Double | Calm water under the bridge, one dropped ice cream plops in |
| 10 | 1148-1222 | 38.3-40.7 | day | none | 12 | Double | TV-set card on a riverside bench showing the wobbling deck; push in on 'whole world' |
| 11 | 1222-1361 | 40.7-45.4 | golden | none | 5 | Explain | Golden wide: empty deck swaying alone at its own slow rhythm |
| 12 | 1361-1513 | 45.4-50.4 | golden | park | 7 | Explain | Park bouncy castle with kids: one jumps, then all jump together |
| 13 | 1513-1632 | 50.4-54.4 | golden | crowd | 10 | Explain | Side view: deck slides right, crowd leans left, repeat; kicks on each 'nudged' |
| 14 | 1632-1734 | 54.4-57.8 | day | none | 12 | Consequence | Engineer (stern) at a barrier with a CLOSED gate; hammer kicks |
| 15 | 1734-1838 | 57.8-61.3 | day | none | 12 | Consequence | Insert under the deck: big dampers bolted on one after another |
| 16 | 1838-1974 | 61.3-65.8 | golden | march | 0 | Callback | Crossfade to the 1831 riflemen breaking step (bridge short's world), sepia-warm golden |
| 17 | 1974-2125 | 65.8-70.8 | day | crowd | 0 | Callback | Back to 2000: tourists stroll, fall into step, the rifleman ghost grins at camera; crane out |

## What changes from `templates/bridge/`
- `story.ts`: replace `SHOTS` with `shots.ts.txt` (saved as .txt so it never breaks tsc), rewrite `CAMS`, `KICKS`, `DOF` and `FOREGROUND` per the table.
- `build.ts` / `world.ts`: new set dressing (see the shot list); keep the sky, fog, ink, lens and grade values.
- `cast.ts` / `toon.ts`: the cast in `cast.png` is drawn with the unchanged `toon.ts`; only new `Outfit`s are needed.
- `audio/timeline.py`: mirror the new `SHOTS`, then rebuild SFX + score + mix (music +3 dB, SFX -6 dB, voice unchanged).
