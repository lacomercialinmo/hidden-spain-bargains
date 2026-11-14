"""Shared site data: menu, provinces and property listings for Hidden Spain Bargains."""
import html, json

BASE = "https://hiddenspainbargains.netlify.app"

# Provinces. active=True when there are homes listed; the rest show as "coming soon".
PROVINCES = [
    {"slug": "leon", "name": "León", "region": "Castile and León", "active": True,
     "areas": ["Laciana Valley", "El Bierzo"],
     "intro": "León province, in north-west Spain, is where we start: the Laciana Valley, a UNESCO Biosphere Reserve in the Cantabrian Mountains, and El Bierzo, a green wine-growing basin around the city of Ponferrada.",
     "lifestyle": ["Mountain", "Nature", "Remote work"]},
    {"slug": "asturias", "name": "Asturias", "region": "Asturias", "active": False, "areas": [], "intro": "", "lifestyle": ["Coast", "Mountain"]},
    {"slug": "a-coruna", "name": "A Coruña", "region": "Galicia", "active": False, "areas": [], "intro": "", "lifestyle": ["Coast"]},
    {"slug": "cordoba", "name": "Córdoba", "region": "Andalusia", "active": False, "areas": [], "intro": "", "lifestyle": ["Sun", "Countryside"]},
    {"slug": "huelva", "name": "Huelva", "region": "Andalusia", "active": False, "areas": [], "intro": "", "lifestyle": ["Coast", "Sun"]},
    {"slug": "castellon", "name": "Castellón", "region": "Valencian Community", "active": False, "areas": [], "intro": "", "lifestyle": ["Coast", "Sun"]},
]

PROPERTIES = [
    {"ref": "HSB-VB-001", "slug": "villablino-3-bedroom-flat", "province": "leon", "town": "Villablino", "area": "Laciana Valley",
     "title": "3-bedroom flat in Villablino", "type": "Flat", "price": 42000, "m2": 74, "beds": 3, "baths": 1,
     "lifestyle": ["Mountain", "Nature", "Remote work"], "tags": ["South-facing", "Furnished", "Heating"],
     "img": "/img/villablino-flat-main-bedroom.jpg", "status": "For sale"},
]

GUIDE_COUNTRIES = [("cost", "Cost of living & homes"), ("work", "Remote work"), ("retire", "Retirement"), ("visas", "Visas & paperwork"), ("life", "Nature & lifestyle")]

def e(s):
    return html.escape(str(s), quote=True)

def prop_url(p):
    return f"/properties/{p['province']}/{p['slug']}.html"

def nav_html():
    prov = "".join(
        f'<li><a href="/properties/{p["slug"]}/">{e(p["name"])}</a></li>' if p["active"]
        else f'<li><a class="soon" href="/properties/#coming-soon">{e(p["name"])}<em>soon</em></a></li>'
        for p in PROVINCES)
    guides = "".join(f'<li><a href="/guides/#{c}">{e(l)}</a></li>' for c, l in GUIDE_COUNTRIES)
    return ('<!--NAV--><header class="snav"><div class="in">'
            '<a class="logo" href="/">Hidden Spain Bargains<small>by La Comercial Inmobiliaria</small></a>'
            '<button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>'
            '<ul class="menu">'
            '<li><button aria-expanded="false">Buy</button><ul class="sub">'
            '<li><a href="/properties/">Search all properties</a></li><li><span class="lab">By province</span></li>' + prov +
            '</ul></li>'
            '<li><button aria-expanded="false">Move to Spain</button><ul class="sub">'
            '<li><a href="/guides/">All articles</a></li><li><span class="lab">By topic</span></li>' + guides +
            '</ul></li>'
            '<li><button aria-expanded="false">Buyers guide</button><ul class="sub">'
            '<li><a href="/buyers-guide/how-we-work.html">How our home search works</a></li>'
            '<li><a href="/buyers-guide/buying-costs-and-taxes.html">Buying costs &amp; taxes</a></li>'
            '<li><a href="/buyers-guide/visas-to-live-in-spain.html">Visas to live in Spain</a></li>'
            '<li><a href="/buyers-guide/buying-from-abroad.html">Buying from abroad</a></li>'
            '</ul></li>'
            '<li><button aria-expanded="false">Area guides</button><ul class="sub">'
            '<li><span class="lab">León</span></li><li><a href="/">Villablino &amp; Laciana Valley</a></li>'
            '</ul></li>'
            '<li><a href="/guides/">Articles</a></li>'
            '<li><a class="cta" href="/#contact">Contact</a></li>'
            '</ul></div></header><!--/NAV-->')

NAV_HEAD = '<link rel="stylesheet" href="/css/menu.css">'
NAV_JS = '<script src="/js/menu.js" defer></script>'

def card_html(p):
    tags = " · ".join([f"{p['m2']} m²", f"{p['beds']} bed", f"{p['baths']} bath"])
    return (f'<a class="pcard" href="{prop_url(p)}"><div class="pimg"><img src="{p["img"]}" alt="{e(p["title"])}" loading="lazy">'
            f'<span class="badge">{e(p["status"])}</span></div><div class="pt"><span class="ploc">{e(p["town"])} · {e(prov_name(p["province"]))}</span>'
            f'<b>{e(p["title"])}</b><em>€{p["price"]:,}</em><span class="pk">{tags}</span>'
            f'<span class="ptags">{" ".join("<i>"+e(t)+"</i>" for t in p["lifestyle"])}</span></div></a>')

def prov_name(slug):
    return next(p["name"] for p in PROVINCES if p["slug"] == slug)
