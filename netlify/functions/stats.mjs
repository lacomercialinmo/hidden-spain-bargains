import { getStore } from "@netlify/blobs";

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

export default async (req) => {
  const url = new URL(req.url);
  const key = url.searchParams.get("key");
  if (!process.env.STATS_KEY || key !== process.env.STATS_KEY) {
    return new Response(`<!doctype html><meta name=viewport content="width=device-width"><form style="font:18px sans-serif;margin:40px"><p>Stats key</p><input name=key type=password style="font-size:18px"> <button>Open</button></form>`,
      { status: 401, headers: { "content-type": "text/html; charset=utf-8" } });
  }
  const days = Math.min(parseInt(url.searchParams.get("days") || "30", 10) || 30, 365);
  const since = new Date(Date.now() - (days - 1) * 864e5).toISOString().slice(0, 10);
  const { blobs } = await getStore("visits").list();
  const rows = blobs.map((b) => b.key.split("|")).filter((p) => p.length >= 6 && p[0] >= since)
    .map(([day, country, device, ref, page]) => ({ day, country: decodeURIComponent(country), device, ref: decodeURIComponent(ref), page: decodeURIComponent(page) }));
  const count = (f) => Object.entries(rows.reduce((a, r) => ((a[r[f]] = (a[r[f]] || 0) + 1), a), {})).sort((a, b) => b[1] - a[1]);
  const table = (title, f, byKey) => {
    const e = count(f); if (byKey) e.sort((a, b) => b[0].localeCompare(a[0]));
    const max = Math.max(1, ...e.map((x) => x[1]));
    return `<h2>${title}</h2><table>${e.map(([k, v]) => `<tr><td>${esc(k)}</td><td class=n>${v}</td><td class=bar><i style="width:${(v / max) * 100}%"></i></td></tr>`).join("") || "<tr><td>No visits yet</td></tr>"}</table>`;
  };
  const links = [7, 30, 90, 365].map((d) => `<a href="?key=${encodeURIComponent(key)}&days=${d}"${d === days ? " class=on" : ""}>${d} days</a>`).join(" ");
  const html = `<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><meta name=robots content=noindex><title>Visits · Hidden Spain Bargains</title>
<style>body{font:16px/1.4 system-ui,sans-serif;margin:0 auto;max-width:720px;padding:20px;color:#1a1a1a}h1{font-size:22px}h2{font-size:17px;margin:28px 0 8px;color:#8B0000}
.big{font-size:44px;font-weight:700;color:#8B0000}table{width:100%;border-collapse:collapse}td{padding:6px 4px;border-bottom:1px solid #eee;word-break:break-word}.n{text-align:right;width:50px;font-weight:600}
.bar{width:35%}.bar i{display:block;height:10px;background:#8B0000;border-radius:5px}a{color:#8B0000;margin-right:10px}a.on{font-weight:700}</style></head><body>
<h1>Hidden Spain Bargains · Visits</h1><p>${links}</p><div class=big>${rows.length}</div><p>page views in the last ${days} days</p>
${table("By country", "country")}${table("By day", "day", true)}${table("Where they come from", "ref")}${table("Pages", "page")}${table("Device", "device")}
</body></html>`;
  return new Response(html, { headers: { "content-type": "text/html; charset=utf-8", "cache-control": "no-store" } });
};
