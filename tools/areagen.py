"""Builds the area-guide pages (/areas/<slug>/ and /areas/)."""
import json, re
import facts
import areas as AR

AREA_CSS = """<style>
.pricebox{background:#fff;border:1px solid var(--line);border-left:4px solid var(--accent);padding:18px 20px;margin:24px 0}
.pricebox .big{font-family:var(--serif);font-size:34px;font-weight:800;line-height:1.1}
.pricebox .sub{font-size:15px;color:var(--muted)}
.tagrow{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 0}.tagrow i{font-style:normal;font-size:13px;border:1px solid var(--line);padding:3px 10px;border-radius:20px;background:#fff}
.agrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:18px;margin:16px 0 40px}
.acard{display:block;background:#fff;border:1px solid var(--line);padding:18px;text-decoration:none;color:var(--ink)}
.acard:hover{border-color:var(--accent)}
.acard b{font-family:var(--serif);font-size:22px;display:block}.acard span{font-size:13px;color:var(--muted);letter-spacing:.05em;text-transform:uppercase}
.acard em{display:block;font-style:normal;color:var(--accent);font-weight:600;margin:8px 0 6px}.acard p{font-size:15px;line-height:1.5;margin:0}
</style>"""


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
    return (f'<a class="acard" href="/areas/{a["slug"]}/"><span>{e(a["prov"])}</span><b>{e(a["name"])}</b>'
            f'<em>Flats from about {eur(a["flat"])}/m²</em><p>{e(a["hook"])}</p></a>')


def page(a, others, B):
    e, BASE = B["e"], B["BASE"]
    url = f'{BASE}/areas/{a["slug"]}/'
    p = pct(a)
    faq = [(q, ans if ans else price_answer(a)) for q, ans in a["faq"]]
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
            f'<h2>Getting around</h2><p>{a["around"]}</p>'
            f'<h2>Everyday life</h2><p>{a["life"]}</p>'
            f'<h2>Who {e(a["name"])} suits</h2><p>{a["suits"]}</p>')
    faq_html = "".join(f"<details><summary>{e(q)}</summary><p>{x}</p></details>" for q, x in faq)
    srcs = [(f'RealAdvisor – house prices in {a["name"]}', a["url"]), ("RealAdvisor – house prices in Spain", AR.SPAIN_URL)]
    src_html = "".join(f'<li><a href="{u}" rel="nofollow noopener" target="_blank">{e(t)}</a></li>' for t, u in srcs)
    cards = "".join(card(o, e) for o in others)
    return (B["head"](title, desc, url, AREA_CSS + '<meta property="og:type" content="article">' + ldh) +
            f'<div class="wrap crumbs"><a href="/">Home</a> › <a href="/areas/">Area guides</a> › {e(a["name"])}</div>'
            f'<header class="head"><div class="kicker">{e(a["prov"])} · {e(a["region"])}</div><h1>Living in {e(a["name"])}</h1><p class="lead">{e(a["hook"])}</p>'
            f'<div class="tagrow">{"".join("<i>" + e(t) + "</i>" for t in a["tags"])}</div>'
            f'<p class="meta">By La Comercial Inmobiliaria · Prices checked {B["UPDATED_TXT"]}</p></header>'
            f'<article class="body">{body}{B["cta"]()}<h2>Frequently asked questions</h2>{faq_html}<h2>Sources</h2><ul class="src">{src_html}</ul>'
            '<p class="src">Prices are modelled averages that change every month. We re-check them regularly; ask us for real, current homes.</p></article>'
            f'<section class="related"><div class="wrap"><h2>More hidden places nearby</h2><div class="agrid">{cards}</div><p><a href="/areas/">All area guides →</a></p></div></section>'
            + B["footer"]())


def index(B):
    e, BASE = B["e"], B["BASE"]
    url = BASE + "/areas/"
    vb_card = ('<a class="acard" href="/areas/villablino/"><span>León</span><b>Villablino &amp; Laciana Valley</b>'
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
