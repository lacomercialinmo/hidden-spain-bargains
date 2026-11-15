"""Builds the area-guide pages (/areas/<slug>/ and /areas/)."""
import json, re
import facts
import areas as AR
try:
    from area_extra import EXTRA
except ImportError:
    EXTRA = {}

AREA_CSS = """<style>
.pricebox{background:#fff;border:1px solid var(--line);border-left:4px solid var(--accent);padding:18px 20px;margin:24px 0}
.pricebox .big{font-family:var(--serif);font-size:34px;font-weight:800;line-height:1.1}
.pricebox .sub{font-size:15px;color:var(--muted)}
.tagrow{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 0}.tagrow i{font-style:normal;font-size:13px;border:1px solid var(--line);padding:3px 10px;border-radius:20px;background:#fff}
.agrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:18px;margin:16px 0 40px}
.acard{display:block;background:#fff;border:1px solid var(--line);padding:18px;text-decoration:none;color:var(--ink)}
.acard:hover{border-color:var(--accent)}
.acard img{width:calc(100% + 36px);margin:-18px -18px 12px;aspect-ratio:16/10;object-fit:cover;max-width:none}
.acard b{font-family:var(--serif);font-size:22px;display:block}.acard span{font-size:13px;color:var(--muted);letter-spacing:.05em;text-transform:uppercase}
.xlist{list-style:none;padding:0}.xlist li{border-top:1px solid var(--line);padding:12px 0}.xlist li b{display:block;font-family:var(--serif);font-size:19px;margin-bottom:2px}
.ttable{width:100%;border-collapse:collapse;font-size:16px;margin:10px 0 20px}.ttable th,.ttable td{border-top:1px solid var(--line);padding:10px 8px;text-align:left;vertical-align:top}.ttable th{width:30%;font-weight:600}
.yt{position:relative;aspect-ratio:16/9;background:#000;margin:14px 0 6px;cursor:pointer}.yt img{width:100%;height:100%;object-fit:cover;opacity:.85}
.yt button{position:absolute;inset:0;margin:auto;width:72px;height:50px;border:0;border-radius:12px;background:#c00;color:#fff;font-size:22px;cursor:pointer}
.yt iframe{position:absolute;inset:0;width:100%;height:100%;border:0}.ytcap{font-size:14px;color:var(--muted);margin:0 0 18px}
.acard em{display:block;font-style:normal;color:var(--accent);font-weight:600;margin:8px 0 6px}.acard p{font-size:15px;line-height:1.5;margin:0}
</style>"""


import os
_IMGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "area_images.json")
IMGS = json.load(open(_IMGS_PATH, encoding="utf-8")) if os.path.exists(_IMGS_PATH) else {}


def img_of(a):
    i = IMGS.get(a["slug"])
    return i if i and i.get("ok") else None


def figure(a, e):
    i = img_of(a)
    if not i:
        return ""
    lic = f'<a href="{e(i["licurl"])}" rel="nofollow noopener" target="_blank">{e(i["license"])}</a>' if i.get("licurl") else e(i["license"])
    src = i.get("remote") or f'/img/areas/{a["slug"]}.jpg'
    return (f'<figure class="cover"><img src="{e(src)}" alt="{e(a["name"])}, {e(a["prov"])}, Spain" width="{i.get("w") or 1600}" height="{i["h"]}">'
            f'<figcaption>{e(a["name"])}. Photo: {e(i["artist"] or "Wikimedia Commons contributor")}, {lic}, via '
            f'<a href="{e(i["page"])}" rel="nofollow noopener" target="_blank">Wikimedia Commons</a>.</figcaption></figure>')


def eur(n):
    return f"€{n:,}"


def pct(a):
    return round((1 - a["flat"] / AR.SPAIN_FLAT) * 100)


def price_answer(a):
    t = (f'Flats in {a["name"]} cost about {eur(a["flat"])} per m² and houses about {eur(a["house"])} per m² ({a["month"]}, RealAdvisor). '
         f'A 75 m² flat therefore works out at around {eur(int(round(a["flat"] * 75, -3)))}.')
    if pct(a) > 0:
        t += f' That is {pct(a)}% below the Spanish average for flats, {eur(AR.SPAIN_FLAT)} per m².'
    return t


def card(a, e):
    i = img_of(a)
    tsrc = (i["remote"].replace("/1280px-", "/500px-") if i and i.get("remote") else f'/img/areas/{a["slug"]}-s.jpg')
    th = f'<img src="{e(tsrc)}" alt="{e(a["name"])}" loading="lazy">' if i else ""
    return (f'<a class="acard" href="/areas/{a["slug"]}/">{th}<span>{e(a["prov"])}</span><b>{e(a["name"])}</b>'
            f'<em>Flats from about {eur(a["flat"])}/m²</em><p>{e(a["hook"])}</p></a>')


def extra_html(a, X, e):
    n = e(a["name"])
    li = lambda items: '<ul class="xlist">' + "".join(f"<li><b>{t}</b>{x}</li>" for t, x in items) + "</ul>"
    tb = lambda items: '<table class="ttable">' + "".join(f"<tr><th>{t}</th><td>{x}</td></tr>" for t, x in items) + "</table>"
    h = (f'<h2>A short history</h2><p>{X["history"]}</p>'
         f'<h2>Things to see and do in {n}</h2>{li(X["see"])}'
         f'<h2>The main square and eating out</h2><p>{X["square"]}</p>{li(X["eat"])}'
         '<p class="src">Restaurants and prices at the time of writing; opening days change, so check before you go.</p>'
         f'<h2>The year in {n}</h2>{tb(X["calendar"])}'
         f'<h2>Food and drink</h2><p>{X["food"]}</p>'
         f'<h2>Nature and outdoors</h2><p>{X["outdoors"]}</p>'
         f'<h2>Everyday life and services</h2><p>{X["services"]}</p>'
         f'<h2>Getting around: trains, buses and roads</h2>{tb(X["transport"])}'
         '<p class="src">Journey times, frequencies and fares are indicative and change with each timetable.</p>'
         f'<h2>The property market in {n}</h2><p>{X["market"]}</p>'
         f'<h3>What your budget buys</h3>{tb(X["budgets"])}'
         f'<h2>Who {n} suits</h2><p>{a["suits"]}</p>'
         '<h3>The honest downsides</h3><ul>' + "".join(f"<li>{d}</li>" for d in X["downsides"]) + '</ul>'
         f'<h2>Day trips from {n}</h2>{li(X["nearby"])}')
    if X.get("videos"):
        h += f'<h2>{n} on video</h2>' + "".join(
            f'<div class="yt" data-id="{v}" role="button" tabindex="0" aria-label="Play video: {e(t)}"><img src="https://i.ytimg.com/vi/{v}/hqdefault.jpg" alt="{e(t)}" loading="lazy"><button aria-hidden="true">▶</button></div>'
            f'<p class="ytcap">{e(t)} · <a href="https://www.youtube.com/watch?v={v}" rel="nofollow noopener" target="_blank">Watch on YouTube</a></p>' for v, t in X["videos"])
        h += ('<script>document.querySelectorAll(".yt").forEach(function(d){function p(){d.innerHTML=\'<iframe src="https://www.youtube-nocookie.com/embed/\'+d.dataset.id+\'?autoplay=1" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen title="YouTube video"></iframe>\';}'
              'd.addEventListener("click",p);d.addEventListener("keydown",function(k){if(k.key==="Enter")p();});});</script>')
    return h


def page(a, others, B):
    e, BASE = B["e"], B["BASE"]
    url = f'{BASE}/areas/{a["slug"]}/'
    p = pct(a)
    X = EXTRA.get(a["slug"])
    faq = [(q, ans if ans else price_answer(a)) for q, ans in (X["faq"] if X else a["faq"])]
    faq.append((f'Can you find me a home in {a["name"]}?',
                f'Yes. Tell us your budget and what you need. We search {a["name"]} and the area around it, check each home, and negotiate the price for you. You pay only if you buy.'))
    title = f'Living in {a["name"]}, Spain: Prices & Life | Hidden Spain Bargains'
    if len(title) > 65:
        title = f'Living in {a["name"]}, Spain | Hidden Spain Bargains'
    desc = (f'{a["name"]} ({a["prov"]}): flats about {eur(a["flat"])}/m²' + (f', {p}% below the Spanish average' if p > 0 else '') +
            '. Services, transport and who it suits.')[:158]
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": f'Living in {a["name"]}, Spain', "description": desc, "inLanguage": "en",
           "dateModified": B["UPDATED"], "author": {"@type": "Organization", "name": "La Comercial Inmobiliaria"},
           "about": {"@type": "Place", "name": f'{a["name"]}, {a["prov"]}, Spain'}},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
              {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", x)}} for q, x in faq]},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
              {"@type": "ListItem", "position": 2, "name": "Area guides", "item": BASE + "/areas/"},
              {"@type": "ListItem", "position": 3, "name": a["name"], "item": url}]}]
    ldh = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    rent = f'<br>Median rent for a flat: {eur(a["rent"])} a month.' if a.get("rent") else ""
    cmp_ = (f'{p}% below the Spanish average for flats ({eur(AR.SPAIN_FLAT)} per m²).' if p > 0
            else f'Close to the Spanish average for flats ({eur(AR.SPAIN_FLAT)} per m²), in a town with a high quality of life.')
    flat75 = eur(int(round(a["flat"] * 75, -3)))
    body = (f'<div class="pricebox"><div class="sub">Average price of a flat, {e(a["month"])}</div><div class="big">{eur(a["flat"])} per m²</div>'
            f'<p class="sub" style="margin-top:8px">{cmp_}<br>Houses: about {eur(a["house"])} per m². A 75 m² flat: around {flat75}.{rent}</p></div>'
            f'<h2>Why {e(a["name"])} stands out</h2><ul>' + "".join(f"<li>{w}</li>" for w in a["why"]) + '</ul>'
            f'<h2>Homes and prices in {e(a["name"])}</h2><p>{price_answer(a)}</p>'
            '<p>These are averages. Homes that need work, or that have been on the market for a while, often sell well below them, and that is where our negotiation makes the difference.</p>'
            + (extra_html(a, X, e) if X else
            f'<h2>Getting around</h2><p>{a["around"]}</p>'
            f'<h2>Everyday life</h2><p>{a["life"]}</p>'
            f'<h2>Who {e(a["name"])} suits</h2><p>{a["suits"]}</p>'))
    faq_html = "".join(f"<details><summary>{e(q)}</summary><p>{x}</p></details>" for q, x in faq)
    srcs = (X.get("sources", []) if X else []) + [(f'RealAdvisor – house prices in {a["name"]}', a["url"]), ("RealAdvisor – house prices in Spain", AR.SPAIN_URL)]
    src_html = "".join(f'<li><a href="{u}" rel="nofollow noopener" target="_blank">{e(t)}</a></li>' for t, u in srcs)
    cards = "".join(card(o, e) for o in others)
    ii = img_of(a)
    og = '<meta property="og:type" content="article">' + (f'<meta property="og:image" content="{ii.get("remote") or BASE + "/img/areas/" + a["slug"] + ".jpg"}">' if ii else "")
    return (B["head"](title, desc, url, AREA_CSS + og + ldh) +
            f'<div class="wrap crumbs"><a href="/">Home</a> › <a href="/areas/">Area guides</a> › {e(a["name"])}</div>'
            f'<header class="head"><div class="kicker">{e(a["prov"])} · {e(a["region"])}</div><h1>Living in {e(a["name"])}</h1><p class="lead">{e(a["hook"])}</p>'
            f'<div class="tagrow">{"".join("<i>" + e(t) + "</i>" for t in a["tags"])}</div>'
            f'<p class="meta">By La Comercial Inmobiliaria · Prices checked {B["UPDATED_TXT"]}</p></header>{figure(a, e)}'
            f'<article class="body">{body}{B["cta"]("", a["name"])}<h2>Frequently asked questions</h2>{faq_html}<h2>Sources</h2><ul class="src">{src_html}</ul>'
            '<p class="src">Prices are modelled averages that change every month. We re-check them regularly; ask us for real, current homes.</p></article>'
            f'<section class="related"><div class="wrap"><h2>More hidden places nearby</h2><div class="agrid">{cards}</div><p><a href="/areas/">All area guides →</a></p></div></section>'
            + B["footer"]())


def index(B):
    e, BASE = B["e"], B["BASE"]
    url = BASE + "/areas/"
    vb_card = ('<a class="acard" href="/areas/villablino/"><img src="/img/villablino-town.jpg" alt="Villablino" loading="lazy"><span>León</span><b>Villablino &amp; Laciana Valley</b>'
               f'<em>Homes around {e(facts.F("price_villablino"))}</em><p>A mountain town in a UNESCO Biosphere Reserve, with fibre internet and some of the lowest home prices in Spain.</p></a>')
    blocks = []
    for code, label in AR.GROUPS:
        items = sorted([a for a in AR.AREAS if a["group"] == code], key=lambda x: x["name"])
        cards = (vb_card if code == "cyl" else "") + "".join(card(a, e) for a in items)
        blocks.append(f'<h2 id="{code}" style="font-family:var(--serif);font-size:30px;margin-top:30px">{e(label)}</h2><div class="agrid">{cards}</div>')
    items = [{"@type": "ListItem", "position": i + 1, "url": f'{BASE}/areas/{a["slug"]}/', "name": f'Living in {a["name"]}'} for i, a in enumerate(AR.AREAS)]
    ld = ('<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "name": "Area guides: hidden places to live in Spain",
                                                            "url": url, "mainEntity": {"@type": "ItemList", "itemListElement": items}}, ensure_ascii=False) + '</script>')
    jump = " · ".join(f'<a href="#{c}">{e(n)}</a>' for c, n in AR.GROUPS)
    return (B["head"]("Affordable Places to Live in Spain | Hidden Spain Bargains",
                      "Hidden towns and cities in Spain with low home prices and good services: prices per m², transport, daily life and who each place suits.", url, AREA_CSS + ld) +
            '<div class="wrap crumbs"><a href="/">Home</a> › Area guides</div>'
            '<header class="head"><div class="kicker">Area guides</div><h1>Places in Spain most buyers never hear about</h1>'
            f'<p class="lead">Beautiful towns and small cities with hospitals, schools and trains, where a flat costs a fraction of the Spanish average of {eur(AR.SPAIN_FLAT)} per m². Each guide shows current prices, how to get around and who the place suits.</p>'
            f'<p class="meta">{jump} · Prices checked {B["UPDATED_TXT"]}</p></header>'
            f'<div class="wrap" style="padding-bottom:30px">{"".join(blocks)}{B["cta"]()}</div>' + B["footer"]())


def build(B):
    for a in AR.AREAS:
        others = [o for o in AR.AREAS if o["group"] == a["group"] and o is not a][:6]
        B["write"](f'areas/{a["slug"]}/index.html', page(a, others, B))
    B["write"]("areas/index.html", index(B))
    return ["/areas/"] + [f'/areas/{a["slug"]}/' for a in AR.AREAS]


def llms(BASE):
    return [f'- [Living in {a["name"]}, Spain]({BASE}/areas/{a["slug"]}/): {a["prov"]}. Flats about €{a["flat"]:,}/m² ({a["month"]}). {a["hook"]}' for a in AR.AREAS]
