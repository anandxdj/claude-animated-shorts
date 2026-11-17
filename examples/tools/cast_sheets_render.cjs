const { chromium } = require("playwright"); const fs = require("fs");
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage();
  pg.on("console", m => console.log(m.text())); pg.on("pageerror", e => console.log("ERR", e.message));
  await pg.setContent("<html><body style='margin:0'></body></html>");
  await pg.addScriptTag({ path: __dirname + "/casts.js" });
  for (const k of ["millennium", "pisa", "whale"]) {
    const url = await pg.evaluate(k => window.drawSheet(k), k);
    fs.writeFileSync(`${__dirname}/cast_${k}.png`, Buffer.from(url.split(",")[1], "base64")); console.log("wrote", k);
  }
  await b.close();
})();
