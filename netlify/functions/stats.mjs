import { getStore } from "@netlify/blobs";

// Target markets. Add countries here as new audiences are opened (e.g. "Netherlands").
const TARGET = ["United Kingdom", "United States", "Canada", "Australia", "New Zealand", "Ireland", "Netherlands", "Germany", "Belgium", "Sweden", "Norway", "Denmark", "Switzerland"];
const FLAGS = { "United Kingdom": "🇬🇧", "United States": "🇺🇸", "Canada": "🇨🇦", "Australia": "🇦🇺", "New Zealand": "🇳🇿", "Ireland": "🇮🇪", "Netherlands": "🇳🇱", "Germany": "🇩🇪", "Belgium": "🇧🇪", "Sweden": "🇸🇪", "Norway": "🇳🇴", "Denmark": "🇩🇰", "Switzerland": "🇨🇭", "Spain": "🇪🇸" };

// Data-centre towns (Google, AWS, Microsoft, Meta): visits from here are robots, not buyers.
const DC = /^(Council Bluffs|Ashburn|The Dalles|Boardman|Prineville|Quincy|Moncks Corner|Lenoir|Mayes County|Pryor|Altoona|Papillion|Des Moines|Santa Clara|San Jose|Clifton|Forest City|Douglas County)$/i;
const channel = (ref) => {
  const r = ref.toLowerCase();
  if (r.startsWith("utm:")) { const u = r.slice(4); return /tiktok|tt/.test(u) ? "TikTok" : /google/.test(u) ? "Google" : /insta|ig/.test(u) ? "Instagram" : /face|fb/.test(u) ? "Facebook" : /whats|wa/.test(u) ? "WhatsApp" : /mail|newsletter/.test(u) ? "Email" : u; }
  if (r === "direct") return "Direct / app (no referrer)";
  if (/tiktok/.test(r)) return "TikTok";
  if (/(^|\.)google\./.test(r)) return "Google";
  if (/bing|duckduckgo|yahoo|ecosia|brave/.test(r)) return "Other search engines";
  if (/chatgpt|openai|perplexity|claude|gemini|copilot/.test(r)) return "AI assistants";
  if (/facebook|fb\.|instagram/.test(r)) return "Facebook / Instagram";
  if (/youtube/.test(r)) return "YouTube";
  if (/reddit/.test(r)) return "Reddit";
  if (/whatsapp|wa\.me/.test(r)) return "WhatsApp";
  return "Other websites";
};

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

export default async (req) => {
  const url = new URL(req.url);
  const key = url.searchParams.get("key");
  if (!process.env.STATS_KEY || key !== process.env.STATS_KEY) {
    return new Response(`<!doctype html><meta name=viewport content="width=device-width"><form style="font:18px sans-serif;margin:40px"><p>Stats key</p><input name=key type=password style="font-size:18px"> <button>Open</button></form>`,
      { status: 401, headers: { "content-type": "text/html; charset=utf-8" } });
  }
  const days = Math.min(parseInt(url.searchParams.get("days") || "30", 10) || 30, 365);
  const only = url.searchParams.get("view") || "target";
  const since = new Date(Date.now() - (days - 1) * 864e5).toISOString().slice(0, 10);
  const { blobs } = await getStore("visits").list();
  const parsed = blobs.map((b) => b.key.split("|")).filter((p) => p.length >= 6 && p[0] >= since)
    .map((p) => ({ p, bot: p[8] === "bot" || (p.length >= 8 && DC.test(decodeURIComponent(p[6]))) || (p.length >= 8 && !p[5] && decodeURIComponent(p[6]) === "Unknown") }));
  const bots = parsed.filter((x) => x.bot).map((x) => x.p);
  const all = parsed.filter((x) => !x.bot).map((x) => x.p)
    .map((p) => ({ day: p[0], country: decodeURIComponent(p[1]), device: p[2], ref: decodeURIComponent(p[3]), page: decodeURIComponent(p[4]), lang: p.length >= 7 ? decodeURIComponent(p[5]) : "", city: p.length >= 8 ? decodeURIComponent(p[6]) + " (" + decodeURIComponent(p[1]) + ")" : "" }))
        .map((r) => ({ ...r, channel: channel(r.ref) }))
    .map((r) => ({ ...r, expat: r.country === "Spain" && r.lang && !/^(es|ca|gl|eu)/.test(r.lang) }));
  const tgt = all.filter((r) => TARGET.includes(r.country) || r.expat);
  const expats = all.filter((r) => r.expat).length;
  const es = all.filter((r) => r.country === "Spain" && !r.expat);
  const rest = all.length - tgt.length - es.length;
  const rows = only === "all" ? all : tgt;

  const count = (list, f) => Object.entries(list.reduce((a, r) => ((a[r[f]] = (a[r[f]] || 0) + 1), a), {})).sort((a, b) => b[1] - a[1]);
  const table = (title, list, f, byKey) => {
    const e = count(list, f); if (byKey) e.sort((a, b) => b[0].localeCompare(a[0]));
    const max = Math.max(1, ...e.map((x) => x[1]));
    const label = (k) => (f === "country" ? (FLAGS[k] ? FLAGS[k] + " " : "") + k : (k || "unknown"));
    return `<h2>${title}</h2><table>${e.map(([k, v]) => `<tr${f === "country" && TARGET.includes(k) ? " class=t" : ""}><td>${esc(label(k))}</td><td class=n>${v}</td><td class=bar><i style="width:${(v / max) * 100}%"></i></td></tr>`).join("") || "<tr><td>No visits yet</td></tr>"}</table>`;
  };
  const q = (d, v) => `?key=${encodeURIComponent(key)}&days=${d}&view=${v}`;
  const links = [7, 30, 90, 365].map((d) => `<a href="${q(d, only)}"${d === days ? " class=on" : ""}>${d} days</a>`).join(" ");
  const views = `<a href="${q(days, "target")}"${only === "target" ? " class=on" : ""}>Target audience</a> <a href="${q(days, "all")}"${only === "all" ? " class=on" : ""}>Everyone</a>`;
  const pct = all.length ? Math.round((tgt.length / all.length) * 100) : 0;

  const html = `<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><meta name=robots content=noindex><title>Visits · Hidden Spain Bargains</title>
<style>body{font:16px/1.4 system-ui,sans-serif;margin:0 auto;max-width:720px;padding:20px;color:#1a1a1a}h1{font-size:22px}h2{font-size:17px;margin:28px 0 8px;color:#8B0000}
.kpis{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:16px 0}.kpi{background:#f6f1ea;padding:14px;border-radius:8px}.kpi b{display:block;font-size:34px;color:#8B0000;line-height:1.1}.kpi span{font-size:13px;color:#555}
.kpi.main{background:#8B0000;color:#fff}.kpi.main b,.kpi.main span{color:#fff}
table{width:100%;border-collapse:collapse}td{padding:6px 4px;border-bottom:1px solid #eee;word-break:break-word}.n{text-align:right;width:50px;font-weight:600}
.bar{width:35%}.bar i{display:block;height:10px;background:#8B0000;border-radius:5px}tr.t td:first-child{font-weight:700}
a{color:#8B0000;margin-right:10px}a.on{font-weight:700;text-decoration:none;border-bottom:2px solid #8B0000}.note{font-size:13px;color:#666;margin-top:24px}</style></head><body>
<h1>Hidden Spain Bargains · Visits</h1><p>${links}</p><p>${views}</p>
<div class=kpis><div class="kpi main"><b>${tgt.length}</b><span>target audience (${pct}%)</span></div><div class=kpi><b>${expats}</b><span>foreigners in Spain</span></div><div class=kpi><b>${es.length}</b><span>Spanish-speaking, in Spain</span></div><div class=kpi><b>${rest}</b><span>other countries</span></div></div>
<p style="font-size:14px;color:#555">Robots filtered out: <b>${bots.length}</b> (data centres, automated browsers). They are not counted anywhere below.</p>
${table(only === "target" ? "Target countries" : "By country", only === "target" ? tgt : all, "country")}
${table("Cities", rows, "city")}
${table("Browser language", rows, "lang")}
${table("Pages they read", rows, "page")}
${table("Where they come from (channel)", rows, "channel")}
${table("Referring website (detail)", rows, "ref")}
${table("By day", rows, "day", true)}
${table("Device", rows, "device")}
<p class=note>Your own visits from this device are not counted (a private cookie was set when you opened this page). Target audience = visits from ${TARGET.map(esc).join(", ")}, plus visits from Spain whose browser is not in Spanish, Catalan, Galician or Basque (foreigners living in Spain). Visits recorded before 14 Nov 2026 have no language data. Tip: TikTok and Instagram apps often hide where a visitor came from, so put links with ?utm_source=tiktok (or instagram, whatsapp) in your bio and messages.</p>
<script>document.cookie="hsb_me=1; max-age=315360000; path=/; SameSite=Lax"</script>
</body></html>`;
  return new Response(html, { headers: { "content-type": "text/html; charset=utf-8", "cache-control": "no-store" } });
};
