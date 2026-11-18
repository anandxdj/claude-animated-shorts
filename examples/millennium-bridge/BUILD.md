# The Bridge That Taught a Crowd to March: the built short

`video.mp4` is the finished example: 66.6 s, 1080x1920, 30 fps, with narration, an original score and synthesized SFX.
It was made by following `SKILL.md` from step 3 on, starting from `templates/bridge/`.

## What was done, step by step
3. **Voice.**
   - `voice/voice.wav` is the script read by the Piper TTS voice `en_US-ryan-high`, one line at a time, with 0.55 s gaps.
   - `voice/words.json` holds word timings from faster-whisper (`small.en`). The words are replaced with the script's own spelling, and one start time was hand-fixed ("Back").
   - That voice is trained on a **CC BY-NC-SA** dataset, so it's for non-commercial use only. Record your own voice before publishing (the skill's rule anyway).
4. **Shot plan.**
   - `src/story.ts` has 18 shots timed to `words.json`, with cuts 2 f before their word.
   - It also adds the new physics: `swayAmp` (the deck's sideways sway grows from "wiggle" on), `syncK` (the share of walkers locked in step) and `swayX` (the deck offset along the span).
5. **World.**
   - `src/world.ts` moves the deck, rails, posts and hangers sideways with the sway, and the chains by half as much.
   - It drops the collapse effects, puts a closed-bridge board (`fxClosed`, no text) on the sign, and adds the shock absorbers that bolt on one after another in shot 16.
6. **Characters.**
   - `src/cast.ts` has 74 modern walkers in both directions; shots 4 and 9 use 114.
     - Their steps blend from each person's own pace to the shared 1 Hz sway.
     - Walkers who have locked in lean with the deck.
   - The new scenes:
     - The ice-cream tourist and the wobbling commuter (shot 7).
     - The falling ice cream (shot 10).
     - The TV and its two viewers (shot 11).
     - The bouncy castle, where one kid jumps and then all four bounce together (shot 13).
     - The engineer with the hammer (shot 15).
   - The 1831 riflemen strolling out of step (shot 17) are the template's `tourists()`.
7. **Post.** Unchanged: ink, lens blur, bloom and grade come straight from the template.
8. **Sound.**
   - `audio/sound.py` builds on the template's `dsp.py` and `instruments.py`.
   - **Score:** an original tune at 120 bpm, so a half-bar matches the 1 Hz sway. It runs:
     - full band for the hook;
     - music box for the setting;
     - pizzicato oompah plus a snare roll as the sway grows;
     - vibes for the "Luckily / Unluckily" lines;
     - warm pads for the explanation;
     - timpani under "shut";
     - fife and drum for 1831;
     - the full band in step for the ending.
   - **SFX:** footsteps that lock onto the beat as `syncK` grows, steel creaks once per sway cycle, a murmur and the river, whooshes on cuts, impact thuds, the ice cream's fall and plop, the TV sting, the castle boings, the hammer clang and the damper clunks.
   - **Mix:** music ducked 6 dB under words, then the standard (music +3 dB, SFX -6 dB). Result: -15.1 LUFS integrated, -1.2 dBTP, exactly 66.600 s.
10. **Render.**
    - `COMP=MillenniumShort DPR=0.6667 CONC=3 node ../tools/clip-linux.mjs out/video.mp4 0 1997 1`, then mux with `audio/mix.wav`.
    - This box has no GPU, so the WebGL buffer was 720x1280 (`post.dpr` 0.6667) at about 5 s per frame; the browser upscales to 1080x1920.
    - On a GPU machine, drop `DPR` and render the 2K final with `--scale 1.3333`.
    - What happened along the way:
      - The first full render crashed at the first crossfade (`fx.ink.dispose is not a function`). That's now fixed in `templates/bridge/Bridge.tsx`.
      - In a later 900-frame run, the long-lived browser tabs lost the world's painted textures by shot 18 (black deck). A fresh render of that shot was correct, so the video is spliced from fresh renders. Keep long runs to a few hundred frames per process on software WebGL.
      - QA (`templates/scripts/short_qa.py`) found one walker vanishing on frame 1909. The "too close to the lens" rule is now decided per shot instead of per frame, and that range was re-rendered.
    - Final QA: 1998 frames, 66.600 s, -15.1 LUFS, no black, white or frozen frames, 0 held frames.
      - The remaining flagged "pops" are intended: the bouncy-castle jumps (f 1236-1380) and a damper snapping on (f 1588).
      - The 1 s near-silence at 37.0 s is the deadpan beat after "on the news".

Only `story.ts`, `cast.ts` and `world.ts` differ from `templates/bridge/`.
To rebuild:
1. Copy `templates/bridge/` to `src/videos/millennium/`.
2. Overwrite those three files with the ones in `src/`.
3. Register `MillenniumShort` next to `BridgeShort`.

## Shots (frames at 30 fps)
| # | Frames | Light | What |
|---|---|---|---|
| 1 | 0-161 | day | Hook: low 3/4 on the swaying crowd (flash-forward to full sway), roll on "dance" |
| 2 | 161-294 | day | White flash; aerial over the river and the town, calm deck |
| 3 | 294-370 | day | Down the deck at rail height |
| 4 | 370-455 | day | High over the entrance, through the tower arch: the packed deck ("Ninety thousand") |
| 5 | 455-577 | day | Low by the deck edge: feet and rails as the wiggle starts |
| 6 | 577-601 | day | Cut + kick on "Sideways" |
| 7 | 601-747 | day | The ice-cream tourist sways along; the commuter wobbles behind |
| 8 | 747-859 | day | Wide 3/4, the whole deck swinging, rolls in time |
| 9 | 859-1007 | day | Crane up over 2,000 strangers in step |
| 10 | 1007-1056 | day | Under the bridge: an ice cream drops into the calm river ("nobody fell in") |
| 11 | 1056-1146 | day | A TV on the riverside plays the wobble; two viewers ("the whole world watched") |
| 12 | 1146-1209 | golden | The empty bridge swaying at its own rhythm |
| 13 | 1209-1401 | golden | Bouncy castle: one kid jumps, then everyone bounces together |
| 14 | 1401-1501 | golden | Side view: the deck nudges the crowd, the crowd nudges back (kicks) |
| 15 | 1501-1553 | day | The engineer hammers up the closed-bridge sign on "shut" |
| 16 | 1553-1687 | day | Under the deck: shock absorbers bolt on one after another |
| 17 | 1687-1829 | golden | 1831: the riflemen stroll across out of step |
| 18 | 1829-1998 | day | 2000: tourists march in step by themselves; crane out |

## Known gaps (it's an example, not a final)
- The world is the 1831 chain bridge and town from the template, not the real steel Millennium Bridge, St Paul's or the Tate.
- Shots 2 and 3 show the deck calm on purpose (before "wiggle"), but they're still story-time flash-backs of the same crowd.
- No Opus verifier rounds (`SKILL.md` step 9) were run against the reference frames.
- The narration is TTS, so its delivery is flatter than a human read.
