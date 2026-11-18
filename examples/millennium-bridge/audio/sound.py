# Sound for "The Bridge That Taught a Crowd to March": original score + synthesized SFX + mix, built on the
# template's dsp.py / instruments.py. Everything is timed to the picture (story.ts) and the voice (words.json).
# Mix rule (SKILL.md): voice unchanged, music ducked under speech, SFX -6 dB; -15 LUFS integrated, <= -1 dBTP.
import sys, json, os
sys.path.insert(0, "/home/user/claude-animated-shorts/templates/audio")
import numpy as np
from scipy import signal
from dsp import SR, ns, tt, rng, lp, hp, bp, place, pan, st, widen, fades, dbg, read_wav, write_wav, integrated, true_peak, make_ir, convolve_st, norm_to, colored, smooth_noise
import instruments as I

HERE = os.path.dirname(os.path.abspath(__file__))
FPS, TOTAL = 30, 1998
DUR = TOTAL / FPS
N = ns(DUR)
W = json.load(open(os.path.join(HERE, "../voice/words.json")))
R = rng(2000)
F = I.m2f
Q = 0.5  # quarter note at 120 bpm: the 1 Hz sway is one half-bar

# ---------------- picture timeline (mirrors story.ts) ----------------
CUTS = [161, 294, 370, 455, 577, 601, 747, 859, 1007, 1056, 1146, 1209, 1401, 1501, 1553, 1687, 1829, 1915]
FLASH = 161 / FPS
KICKS = [(19.24, 1.0), (34.7, 0.3), (47.1, 0.5), (48.54, 0.5), (51.38, 0.6)]
WIGGLE = 16.6
DECK = [(0, 1007), (1401, 1501), (1829, TOTAL)]  # frames with the crowd on the deck
PLOP = 34.72
HAMMER = 51.38
DAMPERS = [52.3 + 0.17 * k for k in range(9)]
CASTLE_SOLO, CASTLE_ALL = (40.38, 42.9), 42.9

def sway_amp(tau):
    return float(np.interp(tau, [WIGGLE, 19.3, 24.2, 27.6, 33], [0, 0.1, 0.18, 0.3, 0.38], left=0, right=0.38))

def shot_tau(t):
    """story time of the shot on screen (story.ts tau)"""
    f = t * FPS
    if f < 161: return 27 + t
    if f < 455: return t - 10
    if f < 1007: return t
    if 1401 <= f < 1501: return t
    return None

# ---------------- music ----------------
mus = np.zeros((2, N))
C = {"C": [48, 52, 55], "F": [53, 57, 60], "G": [55, 59, 62], "Am": [57, 60, 64], "G7": [55, 59, 65], "Dm": [50, 53, 57], "E7": [52, 56, 62]}
PROG = ["C", "F", "G", "C", "Am", "F", "G7", "C"]
MEL = [  # (beat offset in bar, midi, beats) a bouncy original tune, one bar per chord
    [(0, 72, 1), (1, 76, 1), (2, 79, 1.5), (3.5, 77, 0.5)], [(0, 77, 1), (1, 76, 0.5), (1.5, 74, 0.5), (2, 72, 2)],
    [(0, 74, 1), (1, 79, 1), (2, 77, 1), (3, 74, 1)], [(0, 76, 1.5), (1.5, 74, 0.5), (2, 72, 2)],
    [(0, 76, 1), (1, 81, 1), (2, 79, 1), (3, 76, 1)], [(0, 77, 1), (1, 81, 1), (2, 84, 2)],
    [(0, 83, 1), (1, 81, 0.5), (1.5, 79, 0.5), (2, 77, 1), (3, 74, 1)], [(0, 72, 3), (3, 67, 1)],
]
def bar_t(t0, b): return t0 + b * 4 * Q

def oompah(t0, t1, vel, bounce=1.0):
    b = 0
    while bar_t(t0, b) < t1 - 0.01:
        ch = C[PROG[b % 8]]
        for k in range(4):
            t = bar_t(t0, b) + k * Q
            if t >= t1: break
            if k % 2 == 0:
                place(mus, pan(I.pluck(F(ch[0] - 12 + (7 if k == 2 else 0)), vel, R, 0.6), -0.1), t)
            else:
                for i, m in enumerate(ch):
                    place(mus, pan(I.pluck(F(m + 12), vel * 0.45 * bounce, R, 0.35, bright=0.7), -0.4 + 0.4 * i), t)
        b += 1

def tune(t0, t1, fn, vel, transpose=0, p=0.25):
    b = 0
    while bar_t(t0, b) < t1 - 0.01:
        for off, m, beats in MEL[b % 8]:
            t = bar_t(t0, b) + off * Q
            if t >= t1: break
            x = fn(F(m + transpose), vel, R) if fn is not I.fife else I.fife(F(m + transpose), beats * Q * 0.9, vel, R)
            place(mus, pan(x, p), t)
        b += 1

def drums(t0, t1, vel, roll_from=None):
    t = t0
    k = 0
    while t < t1 - 0.01:
        place(mus, pan(I.brush(vel * (1.0 if k % 2 else 0.6), R), 0.15), t)
        t += Q; k += 1
    if roll_from:
        for tr, v in I.snare_roll(roll_from, t1, 0.15, 0.7, R):
            place(mus, pan(I.snare(v * vel, R, buzz=True), 0.1), tr)

def pad_at(t, chord, dur, vel=0.35):
    place(mus, I.pad([F(m) for m in C[chord]], dur, vel, R, att=0.5, rel=1.0), t)

# hook (0 - 5.37): the whole band, swaying
oompah(0.0, FLASH, 0.55); tune(0.0, FLASH, I.glock, 0.45); drums(0.0, FLASH, 0.5)
place(mus, pan(I.cymbal(0.5, R), 0.3), FLASH)
# setting (5.37 - 15.2): calm, the band waits; light glock + pad
for b, ch in enumerate(["C", "F", "C", "G", "C"]): pad_at(FLASH + b * 2.0, ch, 2.0, 0.3)
tune(FLASH, 15.1, I.musicbox, 0.32, 0, 0.3)
# action (15.2 - 33.6): pizzicato oompah that grows with the sway; snare roll into the "perfect step" line
oompah(15.2, 24.9, 0.45, 0.7); oompah(24.9, 33.4, 0.62, 1.0)
tune(20.1, 33.4, I.glock, 0.42)
drums(15.2, 33.4, 0.45, roll_from=30.0)
place(mus, pan(I.cymbal(0.7, R), 0.25), 32.6)
# double line (33.6 - 38.2): almost nothing, a vibes shrug on each half
place(mus, pan(I.vibes(F(67), 0.5, R), -0.2), 33.62); place(mus, pan(I.vibes(F(60), 0.45, R), 0.2), 35.26)
# explanation, golden (38.2 - 50): warm pad + vibes; a boing for the castle in the SFX
for b, ch in enumerate(["Am", "F", "C", "G", "Am", "F"]): pad_at(38.2 + b * 2.0, ch, 2.0, 0.38)
tune(40.4, 50.0, I.vibes, 0.35, -12, -0.2)
# consequence (50 - 56.3): timpani under the shut, snare taps
place(mus, I.timpani(F(43), 0.7, R), HAMMER); place(mus, I.timpani(F(36), 0.6, R), 54.0)
for t in np.arange(52.0, 56.2, 2 * Q): place(mus, pan(I.snare(0.25, R), 0.1), t)
# 1831 callback (56.3 - 61): fife and drum, out of step on purpose (a little swung)
tune(56.3, 61.0, I.fife, 0.42, 0, 0.0)
for k, t in enumerate(np.arange(56.3, 61.0, Q)): place(mus, pan(I.snare(0.4 if k % 2 == 0 else 0.25, R), 0.1), t + (0.04 if k % 2 else 0))
# ending (61 - 66.6): the whole band in step; final chord + cymbal
oompah(61.0, 65.0, 0.6); tune(61.0, 65.0, I.glock, 0.45); drums(61.0, 65.0, 0.55)
for m in C["C"] + [72]: place(mus, pan(I.brass(F(m), 1.2, 0.5, R, kind="soft"), 0.0), 65.0)
place(mus, pan(I.cymbal(0.6, R), 0.2), 65.0)
mus = convolve_st(mus, make_ir(1.1, 7)) * 0.25 + mus

# ---------------- SFX ----------------
sfx = np.zeros((2, N))
def footsteps(t0, t1, density, sync, gain):
    """a crowd on a wooden deck: own-pace steps that lock onto the sway beat as sync grows"""
    for i in range(int(density)):
        own = 1.6 + 0.5 * R.random(); ph0 = R.random()
        t = t0 + ph0 / own
        while t < t1:
            s = sync(t)
            nxt = t + (1 - s) / own + s * 0.5
            tq = t if s < 0.5 else round(t * 2) / 2 + R.normal(0, 0.02 * (1 - s))
            if t0 <= tq < t1:
                x = I.brush(0.35 * R.uniform(0.6, 1.0), R, 0.12) + 0.4 * lp(R.standard_normal(ns(0.12)), 600) * np.exp(-np.arange(ns(0.12)) / ns(0.012))
                place(sfx, pan(x, R.uniform(-0.8, 0.8)), tq, gain)
            t = nxt
def syncf(t):
    tau = shot_tau(t)
    if t * FPS >= 1829: return 1.0
    return 0.0 if tau is None else float(np.clip((tau - 20) / 12, 0, 1)) ** 2 * (3 - 2 * float(np.clip((tau - 20) / 12, 0, 1)))
for a, b in DECK:
    footsteps(a / FPS, b / FPS, 26, syncf, 0.5)
# crowd murmur on the deck, river under the quiet shots
for a, b in DECK:
    n = ns((b - a) / FPS); nz = bp(colored(n, R, -1.0), 250, 2500) * (0.6 + 0.4 * smooth_noise(n, R, 0.7))
    place(sfx, widen(nz, R) * 0.05, a / FPS)
river = lp(colored(N, R, -1.0), 1200) * 0.03
sfx += widen(river, R)
# creaks of the steel as the sway grows (one per sway cycle, louder with the amplitude)
t = WIGGLE
while t < 33.5:
    if shot_tau(t) is not None and t * FPS < 1007:
        a = sway_amp(shot_tau(t))
        if a > 0.04:
            n = ns(0.5); tq = np.arange(n) / SR
            cr = bp(R.standard_normal(n), 300, 1400) * (np.sin(np.pi * tq / 0.5) ** 2) * (1 + 0.6 * np.sin(2 * np.pi * 37 * tq))
            place(sfx, pan(cr * a * 1.6, R.uniform(-0.5, 0.5)), t + 0.25)
    t += 1.0
# shot 1 also sways at full amplitude
for t in np.arange(0.25, FLASH, 1.0):
    n = ns(0.5); tq = np.arange(n) / SR
    place(sfx, pan(bp(R.standard_normal(n), 300, 1400) * np.sin(np.pi * tq / 0.5) ** 2 * 0.5, 0.3), t)
# whooshes on the glides/cuts into a new place, a flash hit after the hook
def whoosh(t, g=0.35, d=0.45):
    n = ns(d); tq = np.arange(n) / SR
    x = bp(R.standard_normal(n), 400, 5000) * np.sin(np.pi * tq / d) ** 2
    place(sfx, widen(x * g, R), t - d / 2)
for f in CUTS: whoosh(f / FPS, 0.18)
whoosh(FLASH, 0.5, 0.6)
# kicks: low thuds
for t, g in KICKS:
    place(sfx, pan(lp(R.standard_normal(ns(0.25)), 180, 2) * np.exp(-np.arange(ns(0.25)) / ns(0.05)) * 1.2 * g, 0.0), t)
# the dropped ice cream: whistle down, plop
n = ns(0.6); tq = np.arange(n) / SR
place(sfx, pan(np.sin(2 * np.pi * np.cumsum(np.linspace(1800, 600, n)) / SR) * 0.12 * np.sin(np.pi * tq / 0.6), 0.1), PLOP - 0.6)
place(sfx, pan(I.pluck(F(84), 0.8, R, 0.3) + bp(R.standard_normal(ns(0.3)), 500, 4000) * np.exp(-np.arange(ns(0.3)) / ns(0.06)) * 0.6, 0.1), PLOP)
# TV: a little news sting
for k, m in enumerate([79, 84, 88]): place(sfx, pan(I.glock(F(m), 0.4, R, 0.8), -0.3), 35.3 + 0.12 * k)
# bouncy castle boings: one kid, then everyone together on the 1.25 Hz bounce
def boing(t, g):
    n = ns(0.35); tq = np.arange(n) / SR
    f = 160 + 260 * np.exp(-tq / 0.08)
    place(sfx, pan(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tq / 0.12) * g, R.uniform(-0.3, 0.3)), t)
t = CASTLE_SOLO[0]
while t < 46.75:
    if t < CASTLE_ALL:
        boing(t, 0.25)
    else:
        for k in range(4): boing(t + R.normal(0, 0.008), 0.18)
    t += 0.8
# hammer clang on "shut", damper clunks
clang = I.glock(F(70), 0.7, R, 0.6); clang[: ns(0.1)] += lp(R.standard_normal(ns(0.1)), 900) * np.exp(-np.arange(ns(0.1)) / ns(0.01))
place(sfx, pan(clang, 0.3), HAMMER)
for k, t in enumerate(DAMPERS):
    x = lp(R.standard_normal(ns(0.18)), 700, 2) * np.exp(-np.arange(ns(0.18)) / ns(0.03)) + 0.3 * I.glock(F(55 + 2 * k), 0.3, R, 0.3)[: ns(0.18)]
    place(sfx, pan(x * 0.8, -0.6 if k % 2 else 0.6), t)

# ---------------- mix ----------------
vx, vsr = read_wav(os.path.join(HERE, "../voice/voice.wav"))
from math import gcd
g_ = gcd(48000, vsr); v = signal.resample_poly(vx[0], 48000 // g_, vsr // g_)  # voice rate -> 48 kHz
voice = np.zeros(N); voice[: min(N, len(v))] = v[:N]
voice = st(voice)
# key: duck the music 6 dB while a word is spoken (smoothed)
key = np.zeros(N)
for w in W: key[ns(w["start"] - 0.05): ns(w["end"] + 0.12)] = 1
k = ns(0.12); key = np.convolve(key, np.ones(k) / k, mode="same")
mus_d = mus * dbg(-6.0 * key)[None, :]
V = integrated(voice)
mus_d = mus_d * dbg((V - 10.0) - integrated(mus_d) + 3.0)   # music bed ~ -10 LU under the voice, +3 dB standard
sfx = sfx * dbg((V - 8.0) - integrated(sfx) - 6.0)         # SFX bed, -6 dB standard
mix = voice + mus_d + sfx
g = dbg(-15.0 - integrated(mix)); mix *= g
# simple look-ahead peak limiter at -1.2 dBTP
ceil = dbg(-1.4)
env = np.max(np.abs(mix), axis=0)
gr = np.minimum(1.0, ceil / np.maximum(env, 1e-9))
la = ns(0.005); gr = -np.convolve(-gr, np.ones(la), mode="same")  # rough look-ahead min
gr = np.minimum.accumulate(gr[::-1])[::-1] if False else gr
from scipy.ndimage import minimum_filter1d, uniform_filter1d
gr = uniform_filter1d(minimum_filter1d(np.minimum(1.0, ceil / np.maximum(env, 1e-9)), ns(0.01)), ns(0.004))
mix *= gr[None, :]
mix = fades(mix, 0.002, 0.5) if mix.ndim == 1 else np.stack([fades(c, 0.002, 0.5) for c in mix])
write_wav(os.path.join(HERE, "mix.wav"), mix)
write_wav(os.path.join(HERE, "stem_music.wav"), mus_d * g)
write_wav(os.path.join(HERE, "stem_sfx.wav"), sfx * g)
print(f"mix {integrated(mix):.1f} LUFS, TP {true_peak(mix):.1f} dBTP, {mix.shape[1] / SR:.3f} s")
