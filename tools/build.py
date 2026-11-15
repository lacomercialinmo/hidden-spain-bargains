#!/usr/bin/env python3
"""Builds Hidden Spain Bargains: menu, guides, buyers guide, properties search, sitemap, robots, llms."""
import glob, html, importlib.util, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from postlib import TOPICS, closer, mid_card, home_word
from sitedata import BASE, PROVINCES, PROPERTIES, nav_html, NAV_HEAD, NAV_JS, card_html, prop_url, prov_name
import facts, proofcheck

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
UPDATED = "2026-11-14"
UPDATED_TXT = "November 2026"
CONTACT_EMAIL = os.environ.get("HSB_EMAIL", "")  # set by the site owner; the contact form works without it

COUNTRIES = {
    "uk": ("United Kingdom", "🇬🇧", "From the UK"),
    "us": ("United States", "🇺🇸", "From the US"),
    "ca": ("Canada", "🇨🇦", "From Canada"),
    "au": ("Australia", "🇦🇺", "From Australia"),
    "nz": ("New Zealand", "🇳🇿", "From New Zealand"),
}
IMG_ALT = {
    "laciana-valley": "Aerial view of Villablino and the Laciana Valley mountains",
    "town": "Villablino town centre surrounded by mountains",
    "nature": "Autumn forests and mountains in the Laciana Valley",
    "ski": "Skiing at Leitariegos ski resort near Villablino",
    "heritage": "Stone bell tower and slate roofs in a Laciana Valley village",
    "health": "Health centre in Villablino",
    "pool": "Outdoor swimming pool in Villablino",
    "pavilion": "Covered sports pavilion in Villablino",
    "food": "Supermarket in Villablino",
    "pharmacy": "Pharmacy in Villablino",
    "banks": "Bank branch with ATM in Villablino",
    "postal": "Post office service in Villablino",
}
WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.4-.7-2.9-1.1-4.7-4.1-4.9-4.3-.1-.2-1.2-1.6-1.2-3s.7-2.1 1-2.4c.3-.3.6-.4.8-.4h.6c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .6l-.4.6-.4.5c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1.1c.2-.3.4-.2.7-.1l2 1c.3.1.5.2.6.3.1.2.1.7-.1 1.3z"/></svg>'
PING = '<script>try{if(document.cookie.indexOf("hsb_me=1")<0)fetch("/api/ping",{method:"POST",keepalive:true,headers:{"content-type":"application/json"},body:JSON.stringify({p:location.pathname,r:document.referrer,l:navigator.language,w:screen.width,u:new URLSearchParams(location.search).get("utm_source"),b:navigator.webdriver?1:0})})}catch(e){}</script>'
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Jost:wght@400;500;600&display=swap" rel="stylesheet">')

def e(s):
    return html.escape(str(s), quote=True)

def head(title, desc, canon, extra=""):
    return (f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{e(title)}</title>\n<meta name="description" content="{e(desc)}">\n<link rel="canonical" href="{canon}">\n'
            f'<meta property="og:title" content="{e(title)}">\n<meta property="og:description" content="{e(desc)}">\n<meta property="og:url" content="{canon}">\n'
            f'{FONTS}\n<link rel="stylesheet" href="/css/guide.css">\n{NAV_HEAD}\n{extra}\n</head>\n<body>\n{nav_html()}\n')

def footer():
    return ('<footer class="footer"><div class="wrap"><div><b>Hidden Spain Bargains</b><br>by La Comercial Inmobiliaria · <a href="https://lacomercial.app.link">lacomercial.app.link</a></div>'
            '<div><a href="/properties/">Properties</a> · <a href="/guides/">Articles</a> · <a href="/buyers-guide/how-we-work.html">How we work</a> · <a href="/buyers-guide/buying-costs-and-taxes.html">Costs &amp; taxes</a><br><a href="/legal-notice.html">Legal notice</a> · <a href="/privacy.html">Privacy</a></div>'
            f'<div>WhatsApp / phone: <a href="https://wa.me/34641188959">+34 641 18 89 59</a><br>Information checked {UPDATED_TXT}. Not legal or tax advice.</div></div></footer>'
            f'<a class="wa" href="https://wa.me/34641188959?text=Hi%2C%20I%27m%20interested%20in%20homes%20in%20Spain" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_SVG}</a>'
            f'\n{PING}\n{NAV_JS}\n</body>\n</html>')

def cta(who="", place=""):
    who_txt = (who + "%20") if who else ""
    where = f"in {place} and the towns around it" if place else "in quiet, beautiful parts of Spain"
    return ('<div class="cta"><h2>' + (f'Want us to find your home in {e(place)}?' if place else 'Want us to find your home in Spain?') + '</h2>'
            f'<p>We search for homes {e(where)}, research the area for you and negotiate the price on your behalf. '
            'You only pay us if you buy, and our fee comes out of the discount we negotiate. We answer in English.</p>'
            f'<div class="btns"><a class="btn" href="https://wa.me/34641188959?text=Hi%2C%20I%27m%20{who_txt}interested%20in%20homes%20in%20Spain" target="_blank" rel="noopener">WhatsApp us</a>'
            '<a class="btn ghost" href="/properties/">See properties</a></div></div>')

from article_images import ART_IMG

def gcard(p):
    if p.get("slug") in ART_IMG:
        pic = f'<img src="/img/articles/{p["slug"]}-s.jpg" alt="{e(ART_IMG[p["slug"]])}" loading="lazy">'
    elif p.get("img"):
        pic = f'<img src="/img/villablino-{p["img"]}.jpg" alt="{e(IMG_ALT[p["img"]])}" loading="lazy">'
    else:
        pic = f'<div class="ph">{e(TOPICS.get(p.get("topic"), "Buyers guide"))}</div>'
    return f'<a class="gcard" href="{p["url"]}"><div>{pic}</div><div class="t"><b>{e(p["h1"])}</b><span>{e(p["desc"][:110])}…</span></div></a>'

def article(p, related, section, section_url, who):
    url = BASE + p["url"]
    faq_html = "".join(f"<details><summary>{e(q)}</summary><p>{a}</p></details>" for q, a in p["faq"])
    src_html = "".join(f'<li><a href="{u}" rel="nofollow noopener" target="_blank">{e(t)}</a></li>' for t, u in p["sources"])
    cover = ""
    if p.get("slug") in ART_IMG:
        cover = (f'<figure class="cover"><img src="/img/articles/{p["slug"]}.jpg" alt="{e(ART_IMG[p["slug"]])}" fetchpriority="high">'
                 f'<figcaption>{e(ART_IMG[p["slug"]])}. AI-generated illustration.</figcaption></figure>')
    elif p.get("img"):
        cover = (f'<figure class="cover"><img src="/img/villablino-{p["img"]}.jpg" alt="{e(IMG_ALT[p["img"]])}" fetchpriority="high">'
                 f'<figcaption>{e(IMG_ALT[p["img"]])}.</figcaption></figure>')
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in p["faq"]]}
    art_ld = {"@context": "https://schema.org", "@type": "Article", "headline": p["h1"], "description": p["desc"], "inLanguage": "en",
              "datePublished": UPDATED, "dateModified": UPDATED, "mainEntityOfPage": url,
              "author": {"@type": "Organization", "name": "La Comercial Inmobiliaria"},
              "publisher": {"@type": "Organization", "name": "Hidden Spain Bargains by La Comercial Inmobiliaria"}}
    if p.get("slug") in ART_IMG:
        art_ld["image"] = f'{BASE}/img/articles/{p["slug"]}.jpg'
    elif p.get("img"):
        art_ld["image"] = f'{BASE}/img/villablino-{p["img"]}.jpg'
    crumbs_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": section, "item": BASE + section_url},
        {"@type": "ListItem", "position": 3, "name": p["h1"], "item": url}]}
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (art_ld, faq_ld, crumbs_ld))
    og = '<meta property="og:type" content="article">' + (f'<meta property="og:image" content="{BASE}/img/articles/{p["slug"]}.jpg">' if p.get("slug") in ART_IMG else f'<meta property="og:image" content="{BASE}/img/villablino-{p["img"]}.jpg">' if p.get("img") else "")
    return (head(p["title"], p["desc"], url, og + ld) +
            f'<div class="wrap crumbs"><a href="/">Home</a> › <a href="{section_url}">{e(section)}</a></div>'
            f'<header class="head"><div class="kicker">{e(p["kicker"])}</div><h1>{e(p["h1"])}</h1><p class="lead">{p["lead"]}</p>'
            f'<p class="meta">By La Comercial Inmobiliaria · Legal and tax figures checked {UPDATED_TXT} · {p.get("mins", 6)} min read</p></header>'
            f'{cover}<article class="body">{p["body"]}{cta(who)}<h2>Frequently asked questions</h2>{faq_html}'
            f'<h2>Sources</h2><ul class="src">{src_html}</ul>'
            '<p class="src">Rules and figures change. We re-check them every time we update this site, but always confirm with a Spanish lawyer, tax adviser or the consulate before you act.</p></article>'
            f'<section class="related"><div class="wrap"><h2>Keep reading</h2><div class="cards">{"".join(gcard(q) for q in related)}</div></div></section>' + footer())

def load(pattern):
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "tools", pattern))):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        out += m.POSTS
    return out

def write(rel, content):
    path = os.path.join(SITE, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        fh.write(content)

def guides_hub(posts):
    blocks = []
    for code, name in TOPICS.items():
        ps = [p for p in posts if p.get("topic") == code]
        if ps:
            blocks.append(f'<h2 id="{code}">{e(name)}</h2><div class="cards">{"".join(gcard(p) for p in ps)}</div>')
    if not blocks:
        blocks.append('<p>New articles are on their way.</p>')
    items = [{"@type": "ListItem", "position": i + 1, "url": BASE + p["url"], "name": p["h1"]} for i, p in enumerate(posts)]
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "name": "Moving to Spain: articles", "url": BASE + "/guides/", "mainEntity": {"@type": "ItemList", "itemListElement": items}}, ensure_ascii=False) + '</script>'
    jump = " · ".join(f'<a href="#{c}">{e(n)}</a>' for c, n in TOPICS.items())
    return (head("Moving to Spain: Articles on Homes, Visas, Work & Retirement", "Honest articles about moving to Spain: home prices, cost of living, remote work, retirement, visas and quiet mountain life in north-west Spain.", BASE + "/guides/", ld) +
            '<header class="head"><div class="kicker">Articles</div><h1>A new life in Spain</h1>'
            '<p class="lead">Home prices, visas, remote work, retirement and everyday life, explained simply, with figures we check every time we update the site.</p>'
            f'<p class="meta">{jump}</p></header><section class="related" style="border:0;padding-top:10px"><div class="wrap">{"".join(blocks)}</div></section>' + footer())

PROP_CSS = '''<style>
.search{background:#fff;border:1px solid var(--line);padding:18px;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:18px 0 8px}
.search select,.search input{width:100%;font:inherit;font-size:16px;padding:11px 12px;border:1px solid #cfc6ba;border-radius:6px;background:#fff;color:var(--ink)}
.search .go{grid-column:1/-1;font-size:17px;padding:13px}
.count{color:var(--muted);margin:14px 0}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:20px}
.pcard{display:block;background:#fff;border:1px solid var(--line);text-decoration:none;color:var(--ink)}
.pcard:hover{border-color:var(--accent)}
.pimg{position:relative}.pimg img{width:100%;aspect-ratio:4/3;object-fit:cover}
.badge{position:absolute;top:10px;left:10px;background:var(--accent);color:#fff;font-size:12px;font-weight:600;padding:4px 10px;border-radius:4px;text-transform:uppercase;letter-spacing:.05em}
.pt{padding:14px 16px 18px;display:flex;flex-direction:column;gap:5px}
.ploc{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.pt b{font-family:var(--serif);font-weight:600;font-size:21px;line-height:1.2}
.pt em{font-style:normal;font-family:var(--serif);font-weight:800;font-size:26px;color:var(--accent)}
.pk{color:var(--muted)}
.ptags i{font-style:normal;font-size:12px;background:#F3EEE6;padding:3px 8px;border-radius:12px;margin-right:4px;display:inline-block;margin-top:4px}
.provs{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin:14px 0}
.prov{display:block;background:#fff;border:1px solid var(--line);padding:16px;text-decoration:none;color:var(--ink)}
.prov b{font-family:var(--serif);font-size:20px;display:block}.prov span{font-size:14px;color:var(--muted)}
.prov.soon{opacity:.6}
.req{background:#fff;border:1px solid var(--line);border-left:4px solid var(--accent);padding:22px;margin:30px 0}
.req form{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
.req input,.req select,.req textarea{width:100%;font:inherit;font-size:16px;padding:10px 12px;border:1px solid #cfc6ba;border-radius:6px;background:#fff}
.req .full{grid-column:1/-1}
@media(max-width:700px){.search{grid-template-columns:1fr 1fr}.req form{grid-template-columns:1fr}}
</style>'''

def request_form():
    return ('<div class="req" id="request"><h2 style="font-family:var(--serif);font-weight:600;font-size:26px">Tell us what you are looking for</h2>'
            '<p>We list only a few hand-picked homes. Tell us your budget and what you need and we will search for you, including homes not listed here.</p>'
            '<form name="property-request" method="POST" action="/thanks.html" data-netlify="true" netlify-honeypot="company">'
            '<input type="hidden" name="form-name" value="property-request"><p style="display:none"><label>Company <input name="company"></label></p>'
            '<input name="name" placeholder="Name" aria-label="Name" required><input type="email" name="email" placeholder="Email" aria-label="Email" required>'
            '<input type="tel" name="phone" placeholder="Phone or WhatsApp (optional)" aria-label="Phone"><input name="country" placeholder="Your country" aria-label="Country">'
            '<select name="budget" aria-label="Budget"><option value="">Budget</option><option>Under €50,000</option><option>€50,000–100,000</option><option>€100,000–200,000</option><option>Over €200,000</option></select>'
            '<select name="bedrooms" aria-label="Bedrooms"><option value="">Bedrooms</option><option>1+</option><option>2+</option><option>3+</option><option>4+</option></select>'
            '<select name="goal" aria-label="Goal"><option value="">Goal</option><option>Main home</option><option>Holiday home</option><option>Remote-work base</option><option>Retirement</option><option>Investment</option></select>'
            '<select name="lifestyle" aria-label="Lifestyle"><option value="">Lifestyle</option><option>Mountain</option><option>Coast</option><option>Countryside</option><option>Town or city</option></select>'
            '<textarea class="full" name="message" placeholder="Anything else? Areas, timing, must-haves…" aria-label="Message"></textarea>'
            '<label class="full" style="font-size:13px;color:var(--muted)"><input type="checkbox" name="consent" value="yes" required style="width:auto"> I agree that my details are used to answer this request, as explained in the <a href=\"/privacy.html\">privacy policy</a>.</label>'
            '<button class="btn full" type="submit" style="font-size:16px;padding:13px">Send my search</button></form></div>')

def properties_index():
    data = json.dumps([{k: p[k] for k in ("ref", "province", "town", "type", "status", "price", "m2", "beds", "baths", "lifestyle")} | {"html": card_html(p)} for p in PROPERTIES], ensure_ascii=False)
    def opts(vals):
        return "".join(f'<option value="{e(v)}">{e(l)}</option>' for v, l in vals)
    prov_opts = opts([(p["slug"], p["name"]) for p in PROVINCES if p["active"]])
    town_opts = opts(sorted({(p["town"], p["town"]) for p in PROPERTIES}))
    type_opts = opts(sorted({(p["type"], p["type"]) for p in PROPERTIES}))
    life_opts = opts(sorted({(l, l) for p in PROPERTIES for l in p["lifestyle"]}))
    prices = [25000, 50000, 75000, 100000, 150000, 200000, 300000]
    pm = opts([(v, f"€{v:,}") for v in prices])
    provs = "".join((f'<a class="prov" href="/properties/{p["slug"]}/"><b>{e(p["name"])}</b><span>{e(p["region"])} · {sum(1 for x in PROPERTIES if x["province"]==p["slug"])} home(s)</span></a>' if p["active"]
                     else f'<div class="prov soon"><b>{e(p["name"])}</b><span>{e(p["region"])} · coming soon</span></div>') for p in PROVINCES)
    js = ('<script>(function(){var D=' + data + ',f=document.getElementById("sf"),g=document.getElementById("res"),c=document.getElementById("cnt");'
          'function v(n){return f.elements[n].value}'
          'function run(ev){if(ev)ev.preventDefault();var r=D.filter(function(p){'
          'if(v("province")&&p.province!==v("province"))return false;if(v("town")&&p.town!==v("town"))return false;'
          'if(v("type")&&p.type!==v("type"))return false;if(v("status")&&p.status!==v("status"))return false;'
          'if(v("beds")&&p.beds<+v("beds"))return false;if(v("baths")&&p.baths<+v("baths"))return false;'
          'if(v("pmin")&&p.price<+v("pmin"))return false;if(v("pmax")&&p.price>+v("pmax"))return false;'
          'if(v("amin")&&p.m2<+v("amin"))return false;if(v("amax")&&p.m2>+v("amax"))return false;'
          'if(v("life")&&p.lifestyle.indexOf(v("life"))<0)return false;'
          'if(v("ref")&&p.ref.toLowerCase().indexOf(v("ref").toLowerCase().trim())<0)return false;return true});'
          'g.innerHTML=r.map(function(p){return p.html}).join("");c.textContent=r.length+(r.length==1?" home found":" homes found");'
          'if(!r.length)g.innerHTML="<p>No homes match yet. <a href=\\"#request\\">Tell us what you are looking for</a> and we will search for you.</p>"}'
          'f.addEventListener("submit",run);f.addEventListener("change",run);run()})();</script>')
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "ItemList", "name": "Homes for sale in Spain – Hidden Spain Bargains",
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": BASE + prop_url(p), "name": p["title"]} for i, p in enumerate(PROPERTIES)]}, ensure_ascii=False) + '</script>'
    return (head("Homes for Sale in Spain: Hand-Picked Bargains | Search", "Search hand-picked homes for sale in Spain by province, town, price, bedrooms and lifestyle. Personal-shopper service for buyers from abroad.", BASE + "/properties/", PROP_CSS + ld) +
            '<div class="wrap" style="padding-top:26px;padding-bottom:40px"><div class="kicker">Buy</div>'
            '<h1 style="font-family:var(--serif);font-weight:800;font-size:clamp(34px,5vw,54px);line-height:1.05;margin:10px 0 12px">Homes for sale in Spain</h1>'
            '<p class="lead" style="max-width:760px">Hand-picked homes in quiet, well-served parts of Spain. For every home we research the area for you and negotiate the price on your behalf. Search below, or tell us what you need.</p>'
            '<form class="search" id="sf">'
            f'<select name="province" aria-label="Province"><option value="">All provinces</option>{prov_opts}</select>'
            f'<select name="town" aria-label="Town"><option value="">All towns</option>{town_opts}</select>'
            f'<select name="type" aria-label="Type"><option value="">All types</option>{type_opts}</select>'
            '<select name="status" aria-label="Status"><option value="">All status</option><option>For sale</option><option>Reserved</option></select>'
            '<select name="beds" aria-label="Bedrooms"><option value="">Bedrooms</option><option value="1">1+</option><option value="2">2+</option><option value="3">3+</option><option value="4">4+</option></select>'
            '<select name="baths" aria-label="Bathrooms"><option value="">Bathrooms</option><option value="1">1+</option><option value="2">2+</option></select>'
            f'<select name="pmin" aria-label="Min. price"><option value="">Min. price</option>{pm}</select>'
            f'<select name="pmax" aria-label="Max. price"><option value="">Max. price</option>{pm}</select>'
            '<input name="amin" type="number" inputmode="numeric" placeholder="Min. area m²" aria-label="Min. area">'
            '<input name="amax" type="number" inputmode="numeric" placeholder="Max. area m²" aria-label="Max. area">'
            f'<select name="life" aria-label="Lifestyle"><option value="">Any lifestyle</option>{life_opts}</select>'
            '<input name="ref" placeholder="Property ID (e.g. HSB-VB-001)" aria-label="Property ID">'
            '<button class="btn go" type="submit">Search</button></form>'
            '<p class="count" id="cnt"></p><div class="pgrid" id="res"></div>'
            '<h2 id="provinces" style="font-family:var(--serif);font-weight:600;font-size:30px;margin-top:40px">Browse by province</h2>'
            f'<div class="provs" id="coming-soon">{provs}</div>'
            + request_form() + '</div>' + js + footer())

def province_page(pv):
    ps = [p for p in PROPERTIES if p["province"] == pv["slug"]]
    url = f'{BASE}/properties/{pv["slug"]}/'
    return (head(f'Homes for Sale in {pv["name"]}, Spain | Hidden Spain Bargains', f'Hand-picked homes for sale in {pv["name"]} province ({", ".join(pv["areas"])}), with area guides and price negotiation for buyers from abroad.', url, PROP_CSS) +
            f'<div class="wrap crumbs"><a href="/">Home</a> › <a href="/properties/">Properties</a> › {e(pv["name"])}</div>'
            '<div class="wrap" style="padding-top:14px;padding-bottom:40px"><div class="kicker">' + e(pv["region"]) + '</div>'
            f'<h1 style="font-family:var(--serif);font-weight:800;font-size:clamp(32px,5vw,52px);line-height:1.05;margin:10px 0 12px">Homes for sale in {e(pv["name"])}</h1>'
            f'<p class="lead" style="max-width:760px">{e(pv["intro"])}</p>'
            f'<p class="count">{len(ps)} home(s) · Areas: {e(", ".join(pv["areas"]))} · <a href="/areas/villablino/">Read the Villablino area guide</a></p>'
            f'<div class="pgrid">{"".join(card_html(p) for p in ps)}</div>' + request_form() + '</div>' + footer())


HOME_CSS = """<style>
.hhero{position:relative;min-height:78vh;display:flex;align-items:flex-end;color:#fff;background:#222;overflow:hidden}
.hhero .mosaic{position:absolute;inset:0;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:3px}
.hhero .mosaic a{position:relative;display:block;overflow:hidden}
.hhero .mosaic img{width:100%;height:100%;object-fit:cover;display:block}
.hhero .mosaic span{position:absolute;top:10px;left:10px;font-size:12px;letter-spacing:.08em;text-transform:uppercase;background:rgba(0,0,0,.45);padding:3px 8px;color:#fff;z-index:2}
.hhero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.05) 15%,rgba(0,0,0,.55) 55%,rgba(0,0,0,.82) 100%);pointer-events:none}
.hhero .wrap{pointer-events:none}.hhero .wrap a{pointer-events:auto}
.hhero .mosaic a:nth-child(n+4) span{display:none}
.photocred{font-size:12px;color:var(--muted);padding-top:6px;padding-bottom:4px}.photocred a{color:var(--muted)}
@media(max-width:800px){.hhero .mosaic{grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr)}.hhero .mosaic a:nth-child(n+3) span{display:none}}
.hhero .wrap{position:relative;z-index:2;padding-bottom:60px;width:100%}
.hhero h1{font-family:var(--serif);font-weight:800;font-size:clamp(36px,6vw,74px);line-height:1.03;margin:10px 0 14px;max-width:900px;text-shadow:0 3px 18px rgba(0,0,0,.35)}
.hhero p{font-size:20px;max-width:640px;text-shadow:0 2px 10px rgba(0,0,0,.5)}
.hhero .btns{display:flex;gap:12px;flex-wrap:wrap;margin-top:22px}
.hhero .btn.ghost{color:#fff;border-color:#fff}
.trust{background:#fff;border-bottom:1px solid var(--line)}
.trust ul{list-style:none;display:grid;grid-template-columns:repeat(4,1fr);margin:0;padding:0}
.trust li{padding:18px 14px;border-right:1px solid var(--line);font-size:15px;text-align:center}
.trust li b{display:block;font-family:var(--serif);color:var(--accent);font-size:18px}
.hsec{padding:56px 0;border-bottom:1px solid var(--line)}
.hsec h2{font-family:var(--serif);font-weight:600;font-size:clamp(28px,4vw,40px);line-height:1.1;margin:8px 0 16px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:10px}
.step{background:#fff;border:1px solid var(--line);padding:22px}
.step b{font-family:var(--serif);font-size:34px;color:var(--accent);display:block}
.step h3{font-size:19px;margin:6px 0}
.who{display:grid;grid-template-columns:1fr 1.4fr;gap:40px;align-items:center}
.who img{width:100%;aspect-ratio:4/3;object-fit:cover}
.topics{display:flex;flex-wrap:wrap;gap:10px;margin:8px 0 22px}
.topics a{border:1px solid var(--accent);border-radius:30px;padding:8px 16px;text-decoration:none;font-weight:500}
.cform{display:grid;grid-template-columns:1fr 1fr;gap:10px;max-width:720px}
.cform input,.cform textarea{width:100%;font:inherit;font-size:16px;padding:11px 12px;border:1px solid #cfc6ba;border-radius:6px;background:#fff}
.cform .full{grid-column:1/-1}
@media(max-width:800px){.trust ul{grid-template-columns:1fr 1fr}.steps,.who{grid-template-columns:1fr}.cform{grid-template-columns:1fr}.hhero{min-height:70vh}}
</style>"""

HERO_TILES = [("ferrol", "Ferrol · Atlantic coast"), ("avila", "Ávila · medieval walls"), ("lepe", "Lepe · Costa de la Luz"),
              ("ponferrada", "El Bierzo · mountains"), ("merida", "Mérida · Roman heritage"), ("zamora", "Zamora · the Duero")]


def hero_mosaic():
    import areagen
    tiles = []
    for slug, label in HERO_TILES:
        if not areagen.IMGS.get(slug, {}).get("ok"):
            continue
        tiles.append(f'<a href="/areas/{slug}/" tabindex="-1"><img src="/img/areas/{slug}-s.jpg" alt="{e(label)}" '
                     f'{"" if len(tiles) < 2 else "loading=" + chr(34) + "lazy" + chr(34)}><span>{e(label)}</span></a>')
    return f'<div class="mosaic" aria-hidden="true">{"".join(tiles)}</div>'


def hero_credits():
    import areagen
    parts = []
    for slug, label in HERO_TILES:
        i = areagen.IMGS.get(slug, {})
        if i.get("ok"):
            parts.append(f'<a href="{e(i["page"])}" rel="nofollow noopener" target="_blank">{e(label.split(" · ")[0])}</a> ({e(i["artist"] or "Wikimedia Commons")}, {e(i["license"])})')
    return '<div class="wrap photocred">Cover photos via Wikimedia Commons: ' + "; ".join(parts) + '.</div>' if parts else ""


def homepage(guides):
    from sitedata import PROPERTIES
    props = "".join(card_html(p) for p in PROPERTIES[:3])
    latest = [g for g in guides if g.get("pillar")][:3] + [g for g in guides if g.get("topic") in ("cost", "life") and not g.get("pillar")][:3]
    faqs = [("How does your home search work?", "Tell us what you need, we send you a shortlist with area guides, the owner shows you the home in person or by video call, and we negotiate the price for you."),
            ("How much do you charge?", "You only pay if you buy. Our fee comes out of the discount we negotiate, and we explain the exact terms in writing before you see any property."),
            ("Can I buy without travelling to Spain?", "Yes. You can view by video call and sign through a power of attorney. You will need an NIE, the tax number every foreign buyer needs.")]
    faq_html = "".join(f"<details><summary>{e(q)}</summary><p>{a}</p></details>" for q, a in faqs)
    ld = [{"@context": "https://schema.org", "@type": "RealEstateAgent", "name": "Hidden Spain Bargains by La Comercial Inmobiliaria", "url": BASE + "/",
           "telephone": "+34641188959", **({"email": CONTACT_EMAIL} if CONTACT_EMAIL else {}), "areaServed": ["León", "El Bierzo", "Villablino", "Spain"], "knowsLanguage": ["en", "es"]},
          {"@context": "https://schema.org", "@type": "WebSite", "name": "Hidden Spain Bargains", "url": BASE + "/"},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}]
    ldh = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    og = f'<meta property="og:type" content="website"><meta property="og:image" content="{BASE}/img/villablino-laciana-valley.jpg">'
    topics = "".join(f'<a href="/guides/#{c}">{e(n)}</a>' for c, n in TOPICS.items())
    return (head("Homes for Sale in Spain, Found and Negotiated for You", "Hand-picked homes in quiet, beautiful parts of Spain. We research the area and negotiate the price for you. You only pay if you buy.", BASE + "/", PROP_CSS + HOME_CSS + og + ldh) +
        f'<section class="hhero">{hero_mosaic()}<div class="wrap"><div class="eyebrow">Your property shopper in Spain</div>'
        '<h1>Your home in Spain, found and negotiated for you.</h1>'
        '<p>We find hidden bargains in quiet, beautiful parts of Spain, explain the area like a local, and negotiate the price on your behalf. You only pay if you buy.</p>'
        '<div class="btns"><a class="btn" href="/properties/">See homes</a><a class="btn ghost" href="https://wa.me/34641188959?text=Hi%2C%20I%27m%20interested%20in%20homes%20in%20Spain" target="_blank" rel="noopener">WhatsApp us</a></div></div></section>' + hero_credits() +
        '<section class="trust"><ul><li><b>You pay only if you buy</b>Fee from the saving we get</li><li><b>We work for you</b>Not for the seller</li><li><b>Checked figures</b>Official sources, dated</li><li><b>In English</b>From first message to keys</li></ul></section>'
        '<section class="hsec"><div class="wrap"><div class="kicker">For sale now</div><h2>Hand-picked homes</h2>'
        f'<div class="pgrid">{props}</div><p style="margin-top:18px"><a href="/properties/">Search all homes →</a> · <a href="/properties/#request">Tell us what you are looking for →</a></p></div></section>'
        '<section class="hsec"><div class="wrap"><div class="kicker">How it works</div><h2>Three steps to your home in Spain</h2><div class="steps">'
        '<div class="step"><b>1</b><h3>Tell us what you need</h3><p>Budget, bedrooms, lifestyle and timing. A short form or a WhatsApp is enough.</p></div>'
        '<div class="step"><b>2</b><h3>See the homes and the area</h3><p>A shortlist with photos, video and a guide to each town. The owner shows you the home in person or by video call.</p></div>'
        '<div class="step"><b>3</b><h3>We negotiate, you decide</h3><p>We talk to the seller in Spanish and push the price down. You sign at a notary, in person or by power of attorney.</p></div>'
        '</div><p style="margin-top:16px"><a href="/buyers-guide/how-we-work.html">More about how we work →</a></p></div></section>'
        '<section class="hsec"><div class="wrap who"><img src="/img/villablino-town.jpg" alt="Villablino town centre surrounded by mountains" loading="lazy"><div><div class="kicker">Who is behind it</div><h2>Hi, I\'m Antonio</h2>'
        '<p>I have worked as an independent real estate agent in Spain for more than 8 years, and I speak English fluently. Most agents work for the seller. I work for you: I find the home, check the area and push the price down.</p>'
        '<p>Our fee comes out of the saving, so we only win when you do. You can follow our homes and area guides on TikTok at <a href="https://www.tiktok.com/@lacomercialrealestate" target="_blank" rel="noopener">@lacomercialrealestate</a>.</p></div></div></section>'
        '<section class="hsec"><div class="wrap"><div class="kicker">Articles</div><h2>A new life in Spain, explained</h2>'
        f'<div class="topics">{topics}</div><div class="cards">{"".join(gcard(g) for g in latest)}</div><p style="margin-top:18px"><a href="/guides/">All articles →</a></p></div></section>'
        '<section class="hsec"><div class="wrap who"><div><div class="kicker">Area guide</div><h2>Villablino and the Laciana Valley</h2>'
        f'<p>A mountain town in a UNESCO Biosphere Reserve, with fibre internet, a health centre, schools and two airports within reach. Homes cost around {facts.F("price_villablino")}.</p>'
        '<p><a class="btn" href="/areas/villablino/">Read the area guide</a> <a class="btn ghost" href="/areas/">More hidden places</a></p></div><img src="/img/villablino-nature.jpg" alt="Autumn forests and mountains in the Laciana Valley" loading="lazy"></div></section>'
        '<section class="hsec" id="contact"><div class="wrap"><div class="kicker">Contact</div><h2>Tell us about the home you want</h2><p>We answer in English, usually within 24 hours.</p>'
        '<form class="cform" name="contact" method="POST" action="/thanks.html" data-netlify="true" netlify-honeypot="company"><input type="hidden" name="form-name" value="contact"><p style="display:none"><label>Company <input name="company"></label></p>'
        '<input name="name" placeholder="Name" aria-label="Name" required><input type="email" name="email" placeholder="Email" aria-label="Email" required>'
        '<input name="country" placeholder="Your country" aria-label="Country"><input name="budget" placeholder="Budget (e.g. €60,000)" aria-label="Budget">'
        '<textarea class="full" name="message" aria-label="Message" placeholder="What are you looking for?"></textarea>'
        '<label class="full" style="font-size:13px;color:var(--muted)"><input type="checkbox" name="consent" value="yes" required style="width:auto"> I agree that my details are used to answer me, as explained in the <a href="/privacy.html">privacy policy</a>.</label>'
        '<button class="btn full" type="submit" style="font-size:16px;padding:13px">Send message</button></form>'
        '<p style="margin-top:14px">Or WhatsApp / call <a href="https://wa.me/34641188959">+34 641 18 89 59</a>' + (f' · <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>' if CONTACT_EMAIL else '') + '</p></div></section>'
        f'<section class="hsec"><div class="wrap" style="max-width:780px"><div class="kicker">FAQ</div><h2>Questions buyers ask us</h2>{faq_html}</div></section>'
        + footer())

def legal_page(slug, title, body):
    from legal import LEGAL_NOTICE, PRIVACY
    return (head(title + " | Hidden Spain Bargains", title + " of Hidden Spain Bargains.", f"{BASE}/{slug}.html", '<meta name="robots" content="noindex,follow">') +
            f'<header class="head"><div class="kicker">Legal</div><h1>{e(title)}</h1><p class="meta">Last updated {UPDATED_TXT}</p></header><article class="body legal">{body}</article>' + footer())

def inject_nav(rel):
    path = os.path.join(SITE, rel)
    s = open(path).read()
    nav = nav_html()
    if "<!--NAV-->" in s:
        s = re.sub(r"<!--NAV-->.*?<!--/NAV-->", lambda m: nav, s, flags=re.S)
    else:
        s, n = re.subn(r'<nav class="nav">.*?</nav>', lambda m: nav, s, count=1, flags=re.S)
        if n == 0:
            s = re.sub(r"<body([^>]*)>", lambda m: m.group(0) + "\n" + nav, s, count=1)
    if NAV_HEAD not in s:
        s = s.replace("</head>", NAV_HEAD + "\n</head>", 1)
    if NAV_JS not in s:
        s = s.replace("</body>", NAV_JS + "\n</body>", 1)
    open(path, "w").write(s)

def main():
    facts.check()
    guides = load("posts_*.py")
    buyers = load("buyers_*.py")
    for p in guides:
        p["url"] = f'/guides/{p["slug"]}.html'
        body = p["body"].replace("<!--CLOSER-->", closer(p["topic"], p["country"])).replace("§HW§", home_word(p["country"]))
        parts = body.split("<h2>")
        if len(parts) > 2:
            body = parts[0] + "<h2>" + parts[1] + mid_card(p["country"]) + "<h2>" + "<h2>".join(parts[2:])
        p["body"] = body
    for p in buyers:
        p["url"] = f'/buyers-guide/{p["slug"]}.html'
    for p in guides + buyers:
        assert len(p["title"]) <= 65, (p["slug"], len(p["title"]))
        assert len(p["desc"]) <= 160, (p["slug"], len(p["desc"]))
    for p in guides:
        same = ([q for q in guides if q["country"] == p["country"] and q is not p] + [q for q in guides if q.get("topic") == p.get("topic") and q["country"] != p["country"]])[:3]
        write(f'guides/{p["slug"]}.html', article(p, same + buyers[:3], "Articles", "/guides/", ""))
    for p in buyers:
        rel = [q for q in buyers if q is not p] + [q for q in guides if q.get("pillar")][:3]
        write(f'buyers-guide/{p["slug"]}.html', article(p, rel[:6], "Buyers guide", "/buyers-guide/how-we-work.html", ""))
    write("guides/index.html", guides_hub(guides))
    write("properties/index.html", properties_index())
    for pv in PROVINCES:
        if pv["active"]:
            write(f'properties/{pv["slug"]}/index.html', province_page(pv))
    import areagen
    area_urls = areagen.build(dict(e=e, BASE=BASE, head=head, footer=footer, cta=cta, write=write, UPDATED=UPDATED, UPDATED_TXT=UPDATED_TXT))
    write("index.html", homepage(guides))
    # Legal notice and privacy pages are static (site/legal-notice.html, site/privacy.html), edited by hand.
    for rel in ["thanks.html", "areas/villablino/index.html"] + [prop_url(p)[1:] for p in PROPERTIES]:
        inject_nav(rel)
    urls = ["/", "/areas/villablino/"] + area_urls + ["/properties/", "/guides/"] + [f'/properties/{pv["slug"]}/' for pv in PROVINCES if pv["active"]] + [prop_url(p) for p in PROPERTIES] + [p["url"] for p in buyers + guides]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join(f"<url><loc>{BASE}{u}</loc><lastmod>{UPDATED}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    bots = ["*", "GPTBot", "ChatGPT-User", "OAI-SearchBot", "ClaudeBot", "Claude-User", "Claude-SearchBot", "Google-Extended", "PerplexityBot", "Bingbot"]
    write("robots.txt", "".join(f"User-agent: {b}\nAllow: /\nDisallow: /stats\n\n" for b in bots) + f"Sitemap: {BASE}/sitemap.xml\n")
    L = ["# Hidden Spain Bargains — by La Comercial Inmobiliaria", "",
         "> English-language property search and guides for people moving to Spain from the UK, US, Canada, Australia and New Zealand. Personal-shopper service: we select homes, research the area and negotiate the price; the buyer pays only if they buy.", "",
         "## Homes for sale"]
    L += [f'- [{p["title"]} — €{p["price"]:,}]({BASE}{prop_url(p)}): {p["m2"]} m², {p["beds"]} bedrooms, {p["baths"]} bathroom, {p["town"]} ({prov_name(p["province"])}). Ref {p["ref"]}.' for p in PROPERTIES]
    L += ["", "## Area guide", f"- [Living in Villablino, Spain]({BASE}/areas/villablino/): UNESCO Laciana Valley, services, schools, distances to airports."] + areagen.llms(BASE) + ["", "## Buyers guide"]
    L += [f'- [{p["h1"]}]({BASE}{p["url"]}): {p["desc"]}' for p in buyers]
    for code, name in TOPICS.items():
        ps = [p for p in guides if p.get("topic") == code]
        if ps:
            L += ["", f"## {name}"] + [f'- [{p["h1"]}]({BASE}{p["url"]}): {p["desc"]}' for p in ps]
    L += ["", "## Contact", "- Agency: La Comercial Inmobiliaria", "- WhatsApp / phone: +34 641 18 89 59", "- Web: https://lacomercial.app.link"]
    write("llms.txt", "\n".join(L) + "\n")
    proofcheck.run(strict=True)
    print(f"built: {len(guides)} articles, {len(buyers)} buyers-guide pages, {len(PROPERTIES)} properties")

if __name__ == "__main__":
    main()
