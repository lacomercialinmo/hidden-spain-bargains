"""Shared building blocks for the articles."""
from facts import F, src

TOPICS = {
    "cost": "Cost of living & homes",
    "work": "Remote work",
    "retire": "Retirement",
    "visas": "Visas & paperwork",
    "life": "Nature & lifestyle",
}

# The current featured listing (keep in sync with sitedata.PROPERTIES)
FEATURED = dict(price="€42,000", m2=74, beds=3, url="/properties/leon/villablino-3-bedroom-flat.html",
                img="/img/villablino-flat-main-bedroom.jpg")

def home_word(country):
    return "apartment" if country in ("us", "ca") else "flat"

GUIDE = '<a href="/areas/villablino/">our full guide to Villablino</a>'

CLOSERS = {
    "cost": lambda c: (f"<h2>What your money buys in Villablino</h2>"
        f"<p>In Villablino, in León's Laciana Valley, homes cost around {F('price_villablino')}, against {F('price_spain')} for Spain as a whole. "
        f"Our current listing is a 3-bedroom, {FEATURED['m2']} m² {home_word(c)} at {FEATURED['price']}, furnished and south-facing. "
        f"<a href=\"{FEATURED['url']}\">See it here</a> or read {GUIDE}.</p>"),
    "work": lambda c: (f"<h2>A mountain office with fibre</h2>"
        f"<p>Villablino, in a {F('vb_unesco')}, has fibre internet in town plus 4G and 5G, a health centre, schools and supermarkets. "
        f"León Airport is 98 km away and Asturias Airport 153 km, and homes cost around {F('price_villablino')}. "
        f"<a href=\"/properties/\">See the homes we have selected</a> or read {GUIDE}.</p>"),
    "retire": lambda c: (f"<h2>A calm place with everything close by</h2>"
        f"<p>Villablino has {F('vb_population')}, a health centre with an emergency service, pharmacies and shops within walking distance, and Hospital El Bierzo in Ponferrada as its reference hospital. "
        f"Homes cost around {F('price_villablino')}, which lets many retirees buy outright and keep their savings. "
        f"<a href=\"/properties/\">See the homes we have selected</a> or read {GUIDE}.</p>"),
    "visas": lambda c: (f"<h2>Once the visa is sorted: where to live</h2>"
        f"<p>Many people choose a big city first and regret the rent. Villablino, in the Laciana Valley, a {F('vb_unesco')}, has fibre internet, a health centre, schools and two airports within reach, "
        f"with homes around {F('price_villablino')}. <a href=\"/properties/\">See the homes we have selected</a> or read {GUIDE}.</p>"),
    "life": lambda c: (f"<h2>Living here, not just visiting</h2>"
        f"<p>Villablino sits at about {F('vb_altitude')} in a {F('vb_unesco')}, with trails from every village and Leitariegos ski resort about 15 km away. "
        f"It is a real town of {F('vb_population')}, with fibre internet and services, and homes around {F('price_villablino')}. "
        f"<a href=\"/properties/\">See the homes we have selected</a> or read {GUIDE}.</p>"),
}

def closer(topic, country):
    return CLOSERS.get(topic, CLOSERS["life"])(country)

def villablino(*a):
    return "<!--CLOSER-->"

def mid_card(country):
    w = home_word(country)
    return (f'<a class="midcard" href="{FEATURED["url"]}"><img src="{FEATURED["img"]}" alt="Bedroom of a {FEATURED["beds"]}-bedroom {w} for sale in Villablino" loading="lazy">'
            f'<span><small>Real example · for sale now</small><b>{FEATURED["beds"]}-bedroom, {FEATURED["m2"]} m² {w} in Villablino</b>'
            f'<em>{FEATURED["price"]}</em><i>South-facing · furnished · UNESCO valley. See the home →</i></span></a>')

def price_table(rows, country="uk"):
    rows = list(rows) + [(f"<b>Our {FEATURED['beds']}-bedroom, {FEATURED['m2']} m² §HW§ in Villablino</b>", f"<b>{FEATURED['price']}</b> for the whole home")]
    body = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows)
    return f'<div class="tablewrap"><table><tr><th>Place</th><th>Typical home price</th></tr>{body}</table></div>'

BASE_SOURCES = src("price_villablino", "price_spain", "vb_unesco")
