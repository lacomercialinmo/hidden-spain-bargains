"""Shared building blocks for the articles."""
from facts import F, src

TOPICS = {
    "cost": "Cost of living & homes",
    "work": "Remote work",
    "retire": "Retirement",
    "visas": "Visas & paperwork",
    "life": "Nature & lifestyle",
}

def villablino():
    return (f"<h2>Where we would start looking: Villablino</h2>"
            f"<p>Villablino is a mountain town in León, north-west Spain, and the main town of the Laciana Valley, a {F('vb_unesco')}. "
            f"It has {F('vb_population')}, sits at about {F('vb_altitude')} above sea level, and has fibre internet, a health centre with an emergency service, schools, supermarkets and banks. "
            "León Airport is 98 km away and Asturias Airport 153 km, and Leitariegos ski resort is about 15 km from town.</p>"
            f"<p>Homes here cost around {F('price_villablino')}, against {F('price_spain')} for Spain as a whole. "
            "<a href=\"/properties/\">See the homes we have selected</a> or <a href=\"/\">read our full guide to Villablino</a>.</p>")

def price_table(rows):
    body = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows)
    return f'<div class="tablewrap"><table><tr><th>Place</th><th>Typical home price</th></tr>{body}</table></div>'

BASE_SOURCES = src("price_villablino", "price_spain", "vb_unesco")
