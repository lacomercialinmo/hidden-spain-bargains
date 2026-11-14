import { getStore } from "@netlify/blobs";

const BOTS = /bot|crawl|spider|slurp|preview|headless|lighthouse|facebookexternalhit|curl|wget|python/i;
const clean = (s, n = 80) => encodeURIComponent(String(s || "").slice(0, n));

export default async (req, context) => {
  if (req.method !== "POST") return new Response("ok");
  const ua = req.headers.get("user-agent") || "";
  if (BOTS.test(ua)) return new Response(null, { status: 204 });
  let d = {};
  try { d = await req.json(); } catch {}
  let ref = "direct";
  try { if (d.r) { const h = new URL(d.r).hostname.replace(/^www\./, ""); if (!h.includes("hiddenspainbargains")) ref = h; } } catch {}
  const device = /mobi|android|iphone/i.test(ua) ? "mobile" : (/ipad|tablet/i.test(ua) ? "tablet" : "desktop");
  const country = context.geo?.country?.name || "Unknown";
  const day = new Date().toISOString().slice(0, 10);
  const lang = String(d.l || req.headers.get("accept-language") || "").slice(0, 5).toLowerCase();
  const key = [day, clean(country), device, clean(ref), clean(d.p || "/"), clean(lang, 5), crypto.randomUUID().slice(0, 8)].join("|");
  await getStore("visits").set(key, "");
  return new Response(null, { status: 204 });
};

export const config = { path: "/api/ping" };
