// usage: COMP=BridgeShort node scripts/clip.mjs out.mp4 <from> <to> [scale] [every]
import { bundle } from "@remotion/bundler";
import { renderMedia, selectComposition } from "@remotion/renderer";
import path from "node:path";
const [out, from, to, scale = "0.5", every = "1"] = process.argv.slice(2);
const id = process.env.COMP || "BridgeShort";
const chromiumOptions = { gl: "swangle" };
const inputProps = process.env.DPR ? { post: { dpr: Number(process.env.DPR) } } : {};
const serveUrl = await bundle({ entryPoint: path.resolve("src/index.ts"), publicDir: path.resolve("public") });
const composition = await selectComposition({ serveUrl, id, chromiumOptions, inputProps });
const t0 = Date.now(); let last = 0;
await renderMedia({ composition, serveUrl, codec: "h264", outputLocation: out, inputProps, frameRange: [Number(from), Number(to)], everyNthFrame: Number(every), scale: Number(scale), chromiumOptions, concurrency: Number(process.env.CONC || 2), timeoutInMilliseconds: 600000, muted: true,
  onProgress: ({ renderedFrames }) => { if (renderedFrames - last >= 10) { last = renderedFrames; console.log(renderedFrames, ((Date.now() - t0) / 1000).toFixed(0) + "s"); } } });
console.log("done", ((Date.now() - t0) / 1000).toFixed(0) + "s");
