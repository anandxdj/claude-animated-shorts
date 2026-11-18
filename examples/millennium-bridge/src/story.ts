// Timeline of the Millennium Bridge short (example made from the bridge template).
// Original header: timeline of the bridge short: shots timed to the the voice words (~/bridge-short/voice/words.json),
// story physics (column position, march phase, deck bounce, collapse) and the camera grammar measured in the
// reference study: continuous slow push-ins; symmetric ease-in-out moves ~23 f (10 in / 10 out), peak ~15 px/f at 720p;
// big reframes are cuts; impacts are 7-frame kicks that flip sign every frame; no hand-held float.
export const FPS = 30;
export const TOTAL = 1998;
export const D0 = 6.0; // bank top + deck height (m)
export const HALF = 27; // towers at z = +-27, span 54 m
export const FILES = [-1.65, -0.55, 0.55, 1.65];
export const ROW_GAP = 1.3;
export const COUNT = 74;
export const PARK: V3 = [70, D0, -75]; // swing pivot base (x, ground y, z)
export type V3 = [number, number, number];

export const clamp01 = (x: number) => Math.max(0, Math.min(1, x));
export const smooth = (x: number) => { const u = clamp01(x); return u * u * (3 - 2 * u); };
export const easeOut = (u: number) => 1 - (1 - clamp01(u)) ** 4;
const lin = (pts: [number, number][], x: number) => {
  if (x <= pts[0][0]) return pts[0][1];
  for (let i = 1; i < pts.length; i++) if (x <= pts[i][0]) {
    const [x0, y0] = pts[i - 1], [x1, y1] = pts[i];
    return y0 + ((y1 - y0) * (x - x0)) / (x1 - x0);
  }
  return pts[pts.length - 1][1];
};

// ---------------- story physics (tau = story time in seconds) ----------------
export const front = (tau: number) => 26 - 1.6 * (tau - 4.4); // z of the front row, marching toward -z
export const marchPhase = (tau: number) => ((tau % 1) + 1) % 1; // 1 Hz cycle = 2 steps/s, footfalls at 0 and 0.5
export const SNAP = 34.62, DROP0 = 36.35, DROP1 = 36.95;
export const amp = (tau: number) =>
  lin([[14.85, 0], [17.8, 0.07], [21.4, 0.13], [27.4, 0.26], [33.0, 0.46], [SNAP, 0.55], [SNAP + 0.35, 0.0]], tau);
export const stomp = (tau: number) => lin([[21.4, 1.0], [27.4, 1.35], [33, 1.5]], tau); // "a little harder every step"
export const shapeZ = (z: number) => (Math.abs(z) < HALF ? Math.cos((Math.PI * z) / (2 * HALF)) : 0);
export const dropW = (z: number) => smooth((20 - z) / 26); // 1 on the near half, 0 at the far tower
export const dropU = (tau: number) => (tau < DROP0 ? 0 : Math.min(1, ((tau - DROP0) / (DROP1 - DROP0)) ** 2));
export const DROP_H = 6.6;

export type BridgeState = { bounce: number; drop: number; snap: number; collapsed: boolean; sway: number };
export const deckY = (z: number, b: BridgeState) => D0 + b.bounce * shapeZ(z) - b.drop * DROP_H * dropW(z);

// ---------------- shots (timed to the Piper voice, words.json) ----------------
export type Light = "day" | "golden";
export type Crowd = "march" | "fall" | "water" | "bank" | "tourists" | "none" | "walk" | "plop" | "tv" | "castle" | "gate" | "dampers";
export type ShotDef = { id: number; a: number; b: number; light: Light; crowd: Crowd; tau: (t: number) => number; towns?: boolean };
export const SHOTS: ShotDef[] = [
  { id: 1, a: 0, b: 161, light: "day", crowd: "walk", tau: (t) => 27 + t }, // hook: flash-forward to the full sway
  { id: 2, a: 161, b: 294, light: "day", crowd: "walk", tau: (t) => t - 10, towns: true }, // aerial, calm (tau < wiggle)
  { id: 3, a: 294, b: 370, light: "day", crowd: "walk", tau: (t) => t - 10 },
  { id: 4, a: 370, b: 455, light: "day", crowd: "walk", tau: (t) => t - 10, towns: true },
  { id: 5, a: 455, b: 577, light: "day", crowd: "walk", tau: (t) => t },
  { id: 6, a: 577, b: 601, light: "day", crowd: "walk", tau: (t) => t },
  { id: 7, a: 601, b: 747, light: "day", crowd: "walk", tau: (t) => t },
  { id: 8, a: 747, b: 859, light: "day", crowd: "walk", tau: (t) => t },
  { id: 9, a: 859, b: 1007, light: "day", crowd: "walk", tau: (t) => t },
  { id: 10, a: 1007, b: 1056, light: "day", crowd: "plop", tau: (t) => t },
  { id: 11, a: 1056, b: 1146, light: "day", crowd: "tv", tau: (t) => t },
  { id: 12, a: 1146, b: 1209, light: "golden", crowd: "none", tau: (t) => t },
  { id: 13, a: 1209, b: 1401, light: "golden", crowd: "castle", tau: (t) => t },
  { id: 14, a: 1401, b: 1501, light: "golden", crowd: "walk", tau: (t) => t },
  { id: 15, a: 1501, b: 1553, light: "day", crowd: "gate", tau: (t) => t },
  { id: 16, a: 1553, b: 1687, light: "day", crowd: "dampers", tau: (t) => t },
  { id: 17, a: 1687, b: 1829, light: "golden", crowd: "tourists", tau: (t) => t + 4.5 },
  { id: 18, a: 1829, b: TOTAL, light: "day", crowd: "walk", tau: (t) => t },
];
/** crossfades (frames) at place/time changes; a white 4-frame flash after the hook */
export const XFADE: Record<number, number> = { 12: 8, 13: 8, 14: 8, 15: 8, 17: 8, 18: 8 };
export const FLASH_AT = 161;

export const shotAt = (f: number) => SHOTS.find((s) => f >= s.a && f < s.b) ?? SHOTS[SHOTS.length - 1];
/** layers to draw at frame f: base shot, plus the next shot fading in during a crossfade */
export const layersAt = (f: number): { id: number; alpha: number }[] => {
  for (const s of SHOTS) {
    const x = XFADE[s.id];
    if (x && f >= s.a - x / 2 && f < s.a + x / 2) return [{ id: s.id - 1, alpha: 1 }, { id: s.id, alpha: (f - (s.a - x / 2) + 1) / (x + 1) }];
  }
  return [{ id: shotAt(f).id, alpha: 1 }];
};

// ---------------- the wobble: lateral sway of the deck (first lateral mode ~1 Hz, half the 2 steps/s pace) ----------------
export const WIGGLE = 16.6; // "the deck starts to wiggle"
export const swayAmp = (tau: number) => lin([[WIGGLE, 0], [19.3, 0.1], [24.2, 0.18], [27.6, 0.3], [33, 0.38]], tau);
/** how many walkers have locked their step to the sway (0 = everyone on their own pace, 1 = all in step) */
export const syncK = (tau: number) => smooth((tau - 20) / 12);
/** lateral deck offset at z */
export const swayX = (z: number, b: BridgeState) => b.sway * shapeZ(z);

export const bridgeState = (id: number, t: number): BridgeState => {
  const s = SHOTS[id - 1], tau = s.tau(t);
  const k = (a: number) => ({ bounce: 0, drop: 0, snap: 0, collapsed: false, sway: a * Math.sin(2 * Math.PI * tau) });
  if (id <= 9) return k(swayAmp(tau));
  if (id === 12) return k(0.16); // the empty bridge at its own rhythm
  if (id === 14) return k(0.3);
  return k(0);
};

// ---------------- camera ----------------
// Grammar (motion.md): every move is a symmetric smootherstep glide of 18-40 f (peak speed = 1.875 x distance / dur,
// so dur >= 0.075 x the move in 720p px keeps the peak near the reference 14-25 px/f); a reframe bigger than about
// half a frame width or 40 % zoom is a hard cut on its key frame. Glides are centred on the old key frame (the
// whoosh in the sound mix peaks there), so a glide key starts dur/2 earlier. Holds push in (dolly toward the look
// point or a fov zoom near walls/towers): 0.15-0.35 %/f, ~0.6 %/f for ~35 f on the punch words. Rolls of 4-8 deg
// over >= 18 f on emphasis beats, held tilt <= 0.07 rad.
export type Cam = { pos: V3; look: V3; fov: number; roll: number };
type Shot = Partial<Cam> & { pos: V3; look: V3 };
type Key = { f: number; dur?: number; cut?: boolean; s: (f: number) => Shot };
/** reference camera ease: symmetric smootherstep (attack = release, ~10 f each on a 23 f move) */
export const glide = (u: number) => { const x = clamp01(u); return x * x * x * (x * (6 * x - 15) + 10); };
const mix = (a: Cam, b: Cam, k: number): Cam => ({
  pos: a.pos.map((v, i) => v + (b.pos[i] - v) * k) as V3, look: a.look.map((v, i) => v + (b.look[i] - v) * k) as V3,
  fov: a.fov + (b.fov - a.fov) * k, roll: a.roll + (b.roll - a.roll) * k,
});
const full = (c: Shot): Cam => ({ fov: 40, roll: 0, ...c });
const run = (keys: Key[], f: number) => {
  let cur = full(keys[0].s(f));
  for (let i = 1; i < keys.length; i++) {
    const k = keys[i];
    if (f < k.f) break;
    cur = k.cut ? full(k.s(f)) : mix(cur, full(k.s(f)), glide((f - k.f) / (k.dur ?? 24)));
  }
  return cur;
};
const T = (f: number) => f / FPS;
const Fz = (id: number, f: number) => front(SHOTS[id - 1].tau(T(f)));
/** push-in factor since f0: the subject grows ~rate per frame; `punch` raises it (with 8 f soft edges) for the first n frames */
const pushK = (f: number, f0: number, rate: number, punch = 0, n = 35) => {
  const x = Math.max(0, f - f0);
  let s = rate * x;
  if (punch > rate) for (let i = 0; i < Math.min(x, n); i++) s += (punch - rate) * Math.max(0, Math.min(1, (i + 0.5) / 8, (n - i - 0.5) / 8));
  return Math.exp(-s);
};
/** dolly push: camera slides toward the look point by factor k */
const dolly = (pos: V3, look: V3, k: number, rest: Partial<Cam> = {}): Shot =>
  ({ pos: [look[0] + (pos[0] - look[0]) * k, look[1] + (pos[1] - look[1]) * k, look[2] + (pos[2] - look[2]) * k], look, ...rest });
/** zoom push (camera stays put, for lenses next to towers / houses): tan(fov/2) shrinks by k */
const zoom = (pos: V3, look: V3, fov: number, k: number, rest: Partial<Cam> = {}): Shot =>
  ({ pos, look, fov: (360 / Math.PI) * Math.atan(Math.tan((fov * Math.PI) / 360) * k), ...rest });
/** a roll-only move on top of an existing framing */
const rolled = (s: (f: number) => Shot, roll: number) => (f: number): Shot => ({ ...s(f), roll });

// near-left anchorage where the bolt lives, and the free end of the snapped backstay
export const ANCHOR: V3 = [-2.7, D0 + 0.62, -37];
export const snapEnd = (snap: number): V3 => {
  const u = easeOut(snap);
  return [ANCHOR[0] - 0.6 * u, ANCHOR[1] + 5.5 * u - 2.0 * u * u, ANCHOR[2] + 4.5 * u];
};

// ---- framings (f -> camera); each pushes in from the frame its key starts ----
export const HERO_Z = (t: number) => 2 - 0.7 * (t - 20); // the ice-cream tourist walks toward -z through shot 7
const W1a = (f: number) => dolly([1.6, D0 + 1.3, -14], [0, D0 + 1.45, -6], pushK(f, 0, 0.0025), { fov: 40 });
const W1b = (f: number) => dolly([1.1, D0 + 1.2, -12.5], [0, D0 + 1.45, -6], pushK(f, 120, 0.002, 0.006, 30), { fov: 38, roll: 0.04 });
const W2a = (f: number) => zoom([17, 13, -52], [0, 9, 4], 44, pushK(f, 161, 0.002));
const W2b = (f: number) => zoom([10, 10.5, -42], [0, 8, 8], 42, pushK(f, 228, 0.002));
const W3a = (f: number) => dolly([2.0, D0 + 1.15, -25], [0, D0 + 1.0, 8], pushK(f, 294, 0.003), { fov: 44, roll: -0.02 });
const W4a = (f: number) => dolly([0.6, D0 + 9, -41], [0, D0 + 0.5, -14], pushK(f, 370, 0.0018, 0.006, 35), { fov: 46 });
const W5a = (f: number) => dolly([4.0, D0 + 0.7, -6.5], [1.7, D0 + 0.35, -2], pushK(f, 455, 0.0025), { fov: 38 });
const W6a = (f: number) => dolly([0.4, D0 + 1.7, -6.2], [0, D0 + 1.5, 0], pushK(f, 577, 0.004), { fov: 38, roll: -0.04 });
const W7a = (f: number) => { const z = HERO_Z(T(f)); return dolly([0.25, D0 + 1.65, z - 4.4], [-0.15, D0 + 1.45, z], pushK(f, 601, 0.002), { fov: 38 }); };
const W8a = (f: number) => dolly([9, D0 + 3.5, -18], [0, D0 + 0.9, -2], pushK(f, 747, 0.002), { fov: 44 });
const W9a = (f: number) => dolly([4, D0 + 4.5, -21], [0, D0 + 1, -5], pushK(f, 859, 0.0015), { fov: 42 });
const W9b = (f: number) => dolly([1.5, D0 + 15, -23], [0, D0, 1], pushK(f, 900, 0.0012), { fov: 42 });
const W10a = (f: number) => dolly([1.8, 0.9, -25.2], [0.3, 3.0, -18], pushK(f, 1003, 0.0022), { fov: 44, roll: -0.03 });
export const TV_AT: V3 = [-6, D0, -34];
const W11a = (f: number) => dolly([-5.3, D0 + 1.4, -38.6], [TV_AT[0], D0 + 0.85, TV_AT[2]], pushK(f, 1056, 0.002, 0.006, 30), { fov: 40 });
const W12a = (f: number) => zoom([14, 10.5, -47], [-1, 7, -4], 40, pushK(f, 1142, 0.0016));
export const CASTLE: V3 = [PARK[0] + 5.5, D0, PARK[2] + 1];
const W13a = (f: number) => dolly([CASTLE[0] - 1.0, D0 + 1.5, CASTLE[2] - 9.5], [CASTLE[0], D0 + 1.6, CASTLE[2]], pushK(f, 1205, 0.0015), { fov: 40 });
const W13b = (f: number) => dolly([CASTLE[0] + 0.6, D0 + 1.3, CASTLE[2] - 8], [CASTLE[0], D0 + 1.5, CASTLE[2]], pushK(f, 1290, 0.002), { fov: 40, roll: 0.04 });
const W14a = (f: number) => dolly([5.75, D0 + 2.45, 3.1], [0, D0 + 1.5, 6.5], pushK(f, 1397, 0.002), { fov: 44 });
const W15a = (f: number) => zoom([1.3, D0 + 1.6, -36.6], [2.9, D0 + 1.3, -31.2], 42, pushK(f, 1497, 0.0025, 0.004, 24));
const W16a = (f: number) => dolly([4.2, D0 - 2.4, -12], [0, D0 - 0.7, -4], pushK(f, 1553, 0.0025), { fov: 42 });
const W17a = (f: number) => dolly([1.7, D0 + 1.75, -15.5], [0, D0 + 1.5, -9], pushK(f, 1683, 0.0025), { fov: 40 });
const W18a = (f: number) => dolly([-1.3, D0 + 1.6, -13], [0, D0 + 1.5, -7.5], pushK(f, 1825, 0.0015, 0.006, 32), { fov: 38 });
const CRANE: V3[] = [[0, 18, -16], [17, 15, -44], [0, 7, 2]];
const C0 = 1915;
const W18b = (f: number): Shot => {
  const a = W18a(C0), s = glide((f - C0) / (TOTAL - C0)), r = 1 - s, [C, B, L] = CRANE;
  return { pos: [0, 1, 2].map((i) => r * r * a.pos[i] + 2 * s * r * C[i] + s * s * B[i]) as V3,
    look: [0, 1, 2].map((i) => a.look[i] + (L[i] - a.look[i]) * s) as V3, fov: (a.fov ?? 40) + (44 - (a.fov ?? 40)) * s, roll: 0 };
};
const CAMS: Record<number, Key[]> = {
  1: [{ f: 0, s: W1a }, { f: 120, dur: 24, s: W1b }], // centred on "dance" (f 134), roll 4.6 deg
  2: [{ f: 161, s: W2a }, { f: 228, dur: 24, s: W2b }],
  3: [{ f: 294, s: W3a }],
  4: [{ f: 370, s: W4a }], // punch on "Ninety thousand"
  5: [{ f: 455, s: W5a }],
  6: [{ f: 577, s: W6a }], // cut on "Sideways" (+ kick)
  7: [{ f: 601, s: W7a }, { f: 680, dur: 22, s: rolled(W7a, 0.035) }],
  8: [{ f: 747, s: W8a }, { f: 762, dur: 24, s: rolled(W8a, 0.04) }, { f: 800, dur: 24, s: rolled(W8a, -0.04) }, { f: 836, dur: 22, s: rolled(W8a, 0.03) }],
  9: [{ f: 859, s: W9a }, { f: 885, dur: 40, s: W9b }], // crane up over the crowd
  10: [{ f: 1003, s: W10a }],
  11: [{ f: 1056, s: W11a }],
  12: [{ f: 1142, s: W12a }],
  13: [{ f: 1205, s: W13a }, { f: 1280, dur: 26, s: W13b }], // closer as everyone jumps together
  14: [{ f: 1397, s: W14a }],
  15: [{ f: 1497, s: W15a }],
  16: [{ f: 1553, s: W16a }],
  17: [{ f: 1683, s: W17a }],
  18: [{ f: 1825, s: W18a }, { f: C0, cut: true, s: W18b }],
};

// impact kicks (reference v14): the image offset flips sign every frame (~3 px at 720p per unit), decays to 0 in
// 7 f, roll +-0.23 deg per unit; they start on the first frame at/after the event. No hand-held float.
const KICKS: [number, number][] = [[19.24, 1.0], [34.7, 0.3], [47.1, 0.5], [48.54, 0.5], [51.38, 0.6], [51.6, 0.4]];
export const kickAt = (t: number) => {
  let a = 0;
  for (const [t0, g] of KICKS) {
    const n = Math.floor((t - t0) * FPS + 1e-6);
    if (n >= 0 && n < 7) a += g * (n % 2 ? -1 : 1) * (1 - n / 7) ** 1.5;
  }
  return a;
};
export const camAt = (id: number, f: number): Cam => {
  const c = run(CAMS[id], f), a = kickAt(T(f));
  if (!a) return c;
  const d: V3 = [c.look[0] - c.pos[0], c.look[1] - c.pos[1], c.look[2] - c.pos[2]];
  const L = Math.hypot(...d), h = Math.hypot(d[0], d[2]) || 1;
  const m = (3 / 640) * Math.tan((c.fov * Math.PI) / 360) * L * a; // metres at the look distance for 3 px x a
  return { ...c, look: [c.look[0] - (d[2] / h) * m, c.look[1] + 0.6 * m, c.look[2] + (d[0] / h) * m], roll: c.roll + a * 0.004 };
};
/** frame at which the current key's move has finished (for picking billboard views per key, not per frame) */
export const keyEnd = (id: number, f: number) => {
  let e = 0;
  for (const k of CAMS[id]) if (f >= k.f) e = k.f + (k.cut ? 0 : k.dur ?? 24);
  return Math.max(f, e);
};

// ---------------- lens: depth of field + foreground framing ----------------
/** Lens blur per shot (thin lens). cInf = blur-disc radius in px at 1080x1920 for things at infinity; 0 = all sharp.
 *  Reference: DOF on in ~1/3 of shots; when on, background sigma720 CU 4.2, MS 4.0, FS 2.7, WS 1.9,
 *  foreground objects 4-8 (disc radius at 1080p = 3 x sigma720). Establishing/wide/most full shots stay sharp.
 *  Entries switch on cuts (no dur) or ramp with the camera glide they share f/dur with. focus = world point (else the
 *  camera look point). */
export type Dof = { f: number; dur?: number; cInf: number; focus?: (f: number) => V3 };
export const DOF: Dof[] = [
  { f: 0, cInf: 14 }, // hook low 3/4 on the crowd
  { f: 161, cInf: 0 }, // aerial
  { f: 294, cInf: 0 }, // down the deck
  { f: 370, cInf: 0 }, // high wide
  { f: 455, cInf: 12 }, // feet + deck edge
  { f: 577, cInf: 12 }, // frontal MS
  { f: 601, cInf: 12, focus: (f) => [-0.15, D0 + 1.6, HERO_Z(f / FPS)] }, // the tourist's eyes
  { f: 747, cInf: 0 }, // wide sway, crane
  { f: 1007, cInf: 10 }, // the water under the bridge
  { f: 1056, cInf: 12 }, // the TV on the bench
  { f: 1146, cInf: 5 }, // golden sway wide
  { f: 1209, cInf: 7 }, // bouncy castle
  { f: 1401, cInf: 0 }, // golden side view
  { f: 1501, cInf: 12, focus: () => [3.35, D0 + 1.6, -31.55] }, // engineer at the gate
  { f: 1553, cInf: 8 }, // dampers
  { f: 1687, cInf: 0 }, // 1831 riflemen strolling, crane out
];
export const dofAt = (f: number) => {
  let i = 0; while (i + 1 < DOF.length && f >= DOF[i + 1].f) i++;
  const d = DOF[i], p = DOF[Math.max(0, i - 1)];
  const k = d.dur ? Math.min(1, (f - d.f) / d.dur) : 1;
  return { cInf: p.cInf + (d.cInf - p.cInf) * k, focus: d.focus };
};
/** what the lens focuses on (DOF): the DOF table's focus point, else the camera look point */
export const focusAt = (id: number, f: number): V3 => {
  const d = dofAt(f);
  return d.focus ? d.focus(f) : camAt(id, f).look;
};

/** near framing objects: visible while a <= f < b; kit = a GLB name accepted by build.ts prop() */
// pos = base point (prop()'s x, y, z: the model's base sits on y), s = height in metres (prop()'s h), yaw in radians.
// They sit at 0.3-0.5 x the focus distance and cover 10-25 % of one frame edge, never a face; they are meant to be
// in front of the lens, so build them outside prop()'s sight-line test.
export type Fg = { a: number; b: number; kit: string; pos: V3; s?: number; yaw?: number };
export const FOREGROUND: Fg[] = [];
