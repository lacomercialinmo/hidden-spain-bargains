from facts import F, Fc, src
from postlib import villablino, price_table, BASE_SOURCES, TOPICS

C = "nz"
POSTS = [
dict(slug="moving-to-spain-from-new-zealand-2026", country=C, topic="visas", pillar=True, img="laciana-valley", mins=6,
  kicker=TOPICS["visas"], title="Moving to Spain from New Zealand in 2026: A Kiwi's Guide",
  h1="Moving to Spain from New Zealand: a Kiwi's guide",
  desc="Visas for New Zealanders in Spain, home prices compared with NZ, and why the green mountains of north-west Spain feel surprisingly like home.",
  lead=f"Green valleys, mountains, rivers and small towns where people know each other. North-west Spain will feel familiar, except that a home costs a fraction of New Zealand's median of {F('price_nz')}.",
  body=f"""<div class="box"><p><b>Quick answer:</b> under 31, the working holiday visa gives {F('whv')}. Remote workers use the digital nomad visa ({F('dnv_income')}); retirees and savers the non-lucrative visa ({F('nlv_income')}).</p></div>
{price_table([("New Zealand (national median)", F('price_nz')), ("Spain (average)", F('price_spain')), ("Villablino, León", F('price_villablino'))])}
<h2>Your options</h2>
<ul><li><b>Working holiday (18–30):</b> {F('whv')}.</li><li><b>Digital nomad visa:</b> {F('dnv_income')}.</li><li><b>Non-lucrative visa:</b> {F('nlv_income')}.</li></ul>
{villablino()}""",
  faq=[("Can New Zealanders live in Spain?", "Yes, with a visa: working holiday (18–30), digital nomad or non-lucrative."),
       ("How much is a home in Spain compared with NZ?", "NZ's national median is " + F('price_nz') + "; in Villablino homes cost around " + F('price_villablino') + ".")],
  sources=src("whv", "dnv_income", "nlv_income", "price_nz") + BASE_SOURCES),

dict(slug="nz-house-prices-vs-spain", country=C, topic="cost", img="town", mins=5,
  kicker=TOPICS["cost"], title="NZ$763,000 Median vs a Mountain Home in Spain",
  h1="A NZ$763,000 median, or a mountain home in Spain?",
  desc=f"New Zealand's median house price is {F('price_nz').split(' (')[0]}. Here is what a home costs in a UNESCO valley in north-west Spain, with real figures.",
  lead=f"New Zealand's median house price is {F('price_nz')}. In Villablino, in Spain's Laciana Valley, homes sell for around {F('price_villablino')}.",
  body=f"""{price_table([("New Zealand (national median)", F('price_nz')), ("Spain (average, per m²)", F('price_spain')), ("Villablino (per m²)", F('price_villablino'))])}
<h2>What €42,000 buys</h2>
<p>Our current Villablino flat: three bedrooms, one bathroom, 74 m², south-facing and furnished. Add the transfer tax ({F('itp_cyl').split(' (')[0]} in Castile and León) and notary fees and it's yours outright.</p>
<h2>Running costs</h2>
<p>A yearly municipal tax (IBI), and, if you don't live in Spain, a yearly non-resident tax: {F('irnr_imputed')}. <a href="/buyers-guide/buying-costs-and-taxes.html">All costs explained</a>.</p>
{villablino()}""",
  faq=[("What is the median house price in NZ?", Fc('price_nz') + "."),
       ("How much is a home in Villablino?", "Around " + F('price_villablino') + ".")],
  sources=src("price_nz", "itp_cyl", "irnr_imputed") + BASE_SOURCES),

dict(slug="working-holiday-visa-spain-for-new-zealanders", country=C, topic="visas", img="nature", mins=4,
  kicker=TOPICS["visas"], title="Spain Working Holiday Visa for New Zealanders",
  h1="Spain's working holiday visa for New Zealanders",
  desc="Kiwis aged 18 to 30 can live and work in Spain for up to a year. How the scheme works and how to use your OE to find a place to come back to.",
  lead=f"The OE is a Kiwi tradition. Spain's version gives New Zealanders {F('whv')}.",
  body=f"""<h2>The basics</h2>
<p>The scheme gives {F('whv')}. You apply through the Spanish consulate and show savings and insurance.</p>
<h2>Beyond London</h2>
<p>Most Kiwis do their OE in London. Spain offers a different year: lower costs, sun, mountains and a language that opens up a whole continent.</p>
<h2>Staying on</h2>
<p>Afterwards you can move to the digital nomad visa ({F('dnv_income')}) or the non-lucrative visa.</p>
{villablino()}""",
  faq=[("What is the age limit for New Zealanders?", "18 to 30."),
       ("How long can I stay?", "Up to 12 months.")],
  sources=src("whv", "dnv_income") + BASE_SOURCES),

dict(slug="brown-bears-and-birch-forests", country=C, topic="life", img="nature", mins=5,
  kicker=TOPICS["life"], title="Brown Bears and Birch Forests: Wild Spain for Kiwis",
  h1="Brown bears and birch forests: the wild Spain",
  desc="New Zealand has no large native mammals. North-west Spain has brown bears and capercaillie. Where to see them, and where to live.",
  lead="New Zealand's wildlife is famous for its birds. In the mountains of north-west Spain, you share the valleys with the Cantabrian brown bear.",
  body=f"""<h2>The bears of the Cantabrian Mountains</h2>
<p>The Laciana Valley, around Villablino, is one of the strongholds of the Cantabrian brown bear and the capercaillie. The bears live in the mountains, not in town.</p>
<h2>Where to watch them</h2>
<p>Next door in Asturias, Somiedo is {F('somiedo')}.</p>
<h2>Forests you'll walk every weekend</h2>
<p>The valley has been a {F('vb_unesco')}, with peaks above 2,000 metres and some of the finest birch forests in the Iberian Peninsula.</p>
{villablino()}""",
  faq=[("Are there bears in Spain?", "Yes. The Cantabrian brown bear lives in the mountains of north-west Spain."),
       ("Where can I see bears?", "Guided bear-watching trips run in Somiedo Natural Park, Asturias.")],
  sources=src("somiedo") + BASE_SOURCES),

dict(slug="las-medulas-and-el-bierzo-landscapes", country=C, topic="life", img="heritage", mins=5,
  kicker=TOPICS["life"], title="Las Médulas and El Bierzo: Landscapes That Rival Home",
  h1="Las Médulas and El Bierzo: landscapes that rival home",
  desc="Red Roman gold mines, vineyards and mountain villages. Why El Bierzo, in north-west Spain, wins over people who grew up with New Zealand's landscapes.",
  lead=f"You grew up with some of the world's great landscapes, so you're hard to impress. Las Médulas might do it: a {F('medulas')}.",
  body=f"""<h2>Las Médulas</h2>
<p>Red peaks and tunnels carved by Roman engineers, rising from chestnut forests. It has been a {F('medulas')}.</p>
<h2>El Bierzo</h2>
<p>A green basin of vineyards around Ponferrada, a city of {F('pf_population')}. {Fc('pf_castle')}.</p>
<h2>The Laciana Valley</h2>
<p>North of Ponferrada, Villablino sits in a UNESCO Biosphere Reserve with homes around {F('price_villablino')}.</p>
{villablino()}""",
  faq=[("What is Las Médulas?", Fc('medulas') + "."),
       ("Where is El Bierzo?", "In León province, north-west Spain, around the city of Ponferrada.")],
  sources=src("medulas", "pf_population", "pf_castle") + BASE_SOURCES),

dict(slug="remote-work-from-spain-on-nz-income", country=C, topic="work", img="laciana-valley", mins=5,
  kicker=TOPICS["work"], title="Remote Work from Spain on a New Zealand Income",
  h1="Remote work from Spain on a New Zealand income",
  desc="Keep your NZ clients or employer and live in Spain: the digital nomad visa income for 2026, time zones that actually work, internet and taxes.",
  lead=f"Working with New Zealand from Spain means working while they sleep, and the other way round. With the digital nomad visa you need {F('dnv_income')}.",
  body=f"""<h2>The visa</h2>
<p>You need {F('dnv_income')}, plus a degree or proven experience.</p>
<h2>Time zones</h2>
<p>New Zealand is around ten to twelve hours ahead of Spain, depending on the season. Early mornings in Spain overlap with the NZ evening; many people build async work around it.</p>
<h2>Internet</h2>
<p>Villablino has fibre in town plus 4G and 5G.</p>
<h2>Taxes</h2>
<p>Spend more than 183 days a year in Spain and you normally become a Spanish tax resident. Get cross-border advice first.</p>
{villablino()}""",
  faq=[("What is the time difference between NZ and Spain?", "Around ten to twelve hours, depending on the season."),
       ("How much do I need for the digital nomad visa?", Fc('dnv_income') + ".")],
  sources=src("dnv_income") + BASE_SOURCES),
]
