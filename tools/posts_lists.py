import areas  # registers the area_* price facts
from facts import F, Fc, src

C = "all"

TOWNS = [  # slug, name, region, population (INE 2025), train fact, one line from our research
    ("bembibre", "Bembibre", "León, Castile and León", "8,041", "train_ponferrada",
     "A friendly market town in El Bierzo, about 20 minutes from Ponferrada, among vineyards and chestnut woods."),
    ("puertollano", "Puertollano", "Ciudad Real, Castilla-La Mancha", "45,565", "train_puertollano",
     "A real town of 45,000 people on the Madrid–Seville high-speed line, with sunny central-Spain weather."),
    ("linares", "Linares", "Jaén, Andalusia", "55,633", "train_linares",
     "A mining city with grand boom-era buildings, birthplace of the guitarist Andrés Segovia, close to UNESCO-listed Úbeda and Baeza."),
    ("arevalo", "Arévalo", "Ávila, Castile and León", "7,851", "train_arevalo",
     "A brick Mudéjar town where Isabella of Castile grew up, between Ávila, Segovia and Valladolid."),
    ("ponferrada", "Ponferrada", "León, Castile and León", "63,186", "train_ponferrada",
     "The Templar city of El Bierzo, with a hospital, a university campus and Las Médulas a short drive away."),
    ("astorga", "Astorga", "León, Castile and León", "10,305", "train_ponferrada",
     "A Roman town where two Camino routes meet, with an Episcopal Palace by Gaudí and a long chocolate tradition."),
    ("medina-del-campo", "Medina del Campo", "Valladolid, Castile and León", "20,215", "train_medina",
     "A royal market town with a great brick castle, one of Spain's largest main squares and its own hospital."),
]

def town_rows():
    rows = "".join(
        f'<tr><td><a href="/areas/{s}/"><b>{n}</b></a><br><small>{r} · {p} people</small></td><td>{F("area_" + s)}</td><td>{F(t)}</td></tr>'
        for s, n, r, p, t, _ in TOWNS)
    return ('<div class="tablewrap"><table><tr><th>Town</th><th>Flats, per m²</th><th>Train to Madrid</th></tr>'
            f'{rows}</table></div>')

def town_sections():
    out = []
    for i, (s, n, r, p, t, line) in enumerate(TOWNS, 1):
        out.append(f'<h3>{i}. {n} ({r})</h3><p>{line} Flats cost about {F("area_" + s)}. Train: {F(t)}. '
                   f'<a href="/areas/{s}/">Read our full guide to {n}</a>.</p>')
    return "".join(out)

POSTS = [
dict(slug="spanish-towns-under-1150-m2-with-a-direct-train-to-madrid", country=C, topic="cost", mins=6,
  kicker="Cost of living & homes", title="7 Towns Under €1,150/m² With a Direct Train to Madrid",
  h1="7 Spanish towns under €1,150 per m² with a direct train to Madrid",
  desc="Flats from €696 per m², less than half the Spanish average, in real towns with a direct train to Madrid. Prices, journey times and our area guides.",
  lead=f"These seven Spanish towns have flats for under €1,150 per m², against {F('area_spain')} for Spain as a whole, and every one has a direct train to Madrid. You get a real town with a station, shops and health services, not an empty village.",
  body=f"""<div class="box"><p><b>Quick answer:</b> Bembibre, Puertollano, Linares, Arévalo, Ponferrada, Astorga and Medina del Campo. The fastest link is Medina del Campo, {F('train_medina')}. The lowest prices are in Bembibre and Puertollano. Want the full cost of buying in one of them? <a href="/buyers-guide/purchase-cost-calculator.html">Try our purchase cost calculator</a>, which shows it in your own currency.</p></div>
<h2>The seven towns at a glance</h2>
{town_rows()}
<p><small>Prices: RealAdvisor municipality pages, autumn 2026. Population: INE, 2025. Train times are typical; check the timetable on renfe.com before you travel.</small></p>
<h2>Why a train to Madrid matters</h2>
<p>Madrid-Barajas has direct flights to the UK, Ireland, North America and much of the world. With a direct train you can get from your front door to the capital without a car, see family abroad without a long drive, and reach Madrid's hospitals, embassies and consulates in a day.</p>
<h2>Town by town</h2>
{town_sections()}
<h2>What the low price does and does not mean</h2>
<p>A price per m² is an average. In every one of these towns you will find flats that need work and others ready to move into. Before you buy, check the building, the community fees and the energy certificate. That is exactly what we do for our clients: we look at the home, the street and the paperwork, and we negotiate the price down.</p>
<!--CLOSER-->""",
  faq=[("Which Spanish town under €1,150 per m² is closest to Madrid by train?", "Medina del Campo: " + F('train_medina') + "."),
       ("Where are flats lowest in this list?", "Bembibre, at about " + F('area_bembibre') + ", followed by Puertollano at about " + F('area_puertollano') + "."),
       ("Do these towns have hospitals?", "Ponferrada, Linares, Puertollano and Medina del Campo have their own hospitals. Bembibre and Astorga use Hospital El Bierzo in Ponferrada and the hospitals in León; Arévalo has a health centre and uses the hospital in Ávila.")],
  sources=src("area_spain", "area_bembibre", "area_puertollano", "area_linares", "area_arevalo", "area_ponferrada", "area_astorga", "area_medina-del-campo",
              "train_medina", "train_puertollano", "train_arevalo", "train_linares", "train_ponferrada")
          + [("Ponferrada–Madrid direct train and stops – Diario de León", "https://www.diariodeleon.es/bierzo/221216/1099688/tren-madrid-coruna-tarda-vale-igual-ponferrada.html"),
             ("Population by municipality 2025 – INE", "https://www.ine.es/dynt3/inebase/index.htm?padre=525")]),
]
