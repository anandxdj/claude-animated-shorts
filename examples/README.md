# Examples

What the skill produces, run in a Linux cloud box (no GPU, headless Chromium with software WebGL).

## 1. The proven short: `bridge-preview/`
`templates/bridge/` dropped unchanged into a fresh Remotion 4 project and rendered:
- `hook.mp4`: shot 1, the hook (frames 0-129, 540x960, silent). The final 1440x2560 render uses `--scale 1.3333`.
- `keyframes.jpg`: one frame from each of 14 shots, from the town aerial to the tourists' crane-out.

The Kenney CC0 kit (`public/bridge/kenney/*.glb`) was not installed, so stalls, banners, carts and bushes are missing.
Everything else (world, ink, lens blur, grade, characters) is the template as shipped.

## 2. A new short, built and rendered: `millennium-bridge/video.mp4`
**The Bridge That Taught a Crowd to March** (66.6 s, 1080x1920) has narration (Piper TTS), an original score and synthesized SFX.
`millennium-bridge/BUILD.md` covers every step, the 18 shots, and what's still rough. Only `story.ts`, `cast.ts` and `world.ts` differ from the template.

## 2-4. Three new shorts, planned with the skill
Each folder covers pipeline steps 1-4 of `SKILL.md`, plus the cast:

| Folder | Short | Story |
|---|---|---|
| `millennium-bridge/` | **The Bridge That Taught a Crowd to March** (~71 s) | London, 2000: the crowd makes a new footbridge sway sideways. A sequel and callback to the bridge short. |
| `leaning-tower/` | **The Tower That Was Saved by a War** (~68 s) | Pisa, 1173-2001: a war pause let the soil firm up, the tower is curved like a banana, and the 1990s rescue. |
| `exploding-whale/` | **The Day It Rained Whale** (~69 s) | Florence, Oregon, 1970: the highway department dynamites a beached whale. |

Files in each folder:
- `SCRIPT.md`: facts with sources, the everyday analogy, the script and the beat map (hook, setting, action, snap, "Luckily / Unluckily", explanation, consequence, callback).
- `words.est.json`: **estimated** word timings at the bridge short's pace (~2.9 words/s with pauses). Replace it with real speech-to-text timings once the voice is recorded.
- `SHOTPLAN.md`: shots with frames, light preset, crowd mode, lens-blur strength and camera direction, following the skill's camera rules.
- `shots.ts.txt`: the `SHOTS` table, ready to paste into `story.ts`. It is `.txt` so it can't break `tsc`.
- `cast.png`: the cast, drawn by the unchanged `templates/bridge/toon.ts`. Only new `Outfit` colours and hats were needed.

To turn one into a video, continue at step 5 of `SKILL.md`:
1. Record the voice and get the real `words.json`.
2. Re-time with `tools/make_example.py`.
3. Copy `templates/bridge/`, then rewrite `CAMS`, `KICKS`, `DOF` and the set dressing in `build.ts`/`world.ts`.

## `tools/`
- `stills-linux.mjs`, `clip-linux.mjs`: Linux versions of `bridge-stills.mjs`. They use bundled Chromium with `gl: "swangle"` instead of the hard-coded Windows Chrome path.
  - Usage: `COMP=BridgeShort node stills-linux.mjs out/x_ 60,700 0.5` and `node clip-linux.mjs out.mp4 0 129 0.5`.
  - Software WebGL runs ~45 s for a single still and ~5.5 s per frame for a clip (4 cores). A full 67 s short takes about 3 hours at 0.5 scale, so use a GPU machine for finals.
- `make_example.py`: makes all four planning files above from one beat table per short. Run `python make_example.py <outdir>`.
- `cast_sheets.ts.txt` + `cast_sheets_render.cjs`: the cast-sheet renderer.
  - Rename the `.txt` file to `.ts` inside a project that has `src/videos/bridge/toon.ts`.
  - Bundle it with `esbuild --bundle --format=iife --outfile=casts.js`, then run the `.cjs` file with Playwright.

All three stories are real events. Check the facts against the sources listed before recording.
