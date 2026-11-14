from facts import F, Fc, src
from postlib import villablino, price_table, BASE_SOURCES, TOPICS

C = "au"
POSTS = [
dict(slug="moving-to-spain-from-australia-2026", country=C, topic="visas", pillar=True, img="laciana-valley", mins=7,
  kicker=TOPICS["visas"], title="Moving to Spain from Australia in 2026: Where to Start",
  h1="Moving to Spain from Australia: where to start",
  desc="Visas for Australians in Spain (working holiday, digital nomad, non-lucrative), home prices vs Australia, and why the north-west surprises people.",
  lead=f"You grew up a long way from everything. Spain puts you in the middle of it: Europe's history, food and cities a short trip away, and homes that cost a fraction of an Australian median of {F('price_au')}.",
  body=f"""<div class="box"><p><b>Quick answer:</b> under 31, the working holiday visa gives {F('whv')}. Remote workers use the digital nomad visa ({F('dnv_income')}); retirees and savers the non-lucrative visa ({F('nlv_income')}).</p></div>
<h2>What your money buys</h2>
{price_table([("Australia (national median dwelling)", F('price_au')), ("Spain (average)", F('price_spain')), ("Villablino, León", F('price_villablino'))])}
<h2>Your visa options</h2>
<ul><li><b>Working holiday (18–30):</b> {F('whv')}.</li>
<li><b>Digital nomad visa:</b> {F('dnv_income')}.</li>
<li><b>Non-lucrative visa:</b> {F('nlv_income')}.</li></ul>
<h2>The Spain most Australians never see</h2>
<p>Everyone knows Barcelona and the beaches. Fewer people know the green north-west: Templar castles, Roman gold mines, wine valleys and mountains with brown bears. <a href="/guides/ponferrada-templar-city-of-history.html">Start with Ponferrada</a>.</p>
{villablino()}""",
  faq=[("Can Australians work in Spain?", "Yes, Australians aged 18–30 can use the working holiday visa; others can work remotely for foreign clients on the digital nomad visa."),
       ("How much is a home in Spain compared with Australia?", "Australia's national median dwelling value is " + F('price_au') + "; in Villablino homes cost around " + F('price_villablino') + ".")],
  sources=src("whv", "dnv_income", "nlv_income", "price_au") + BASE_SOURCES),

dict(slug="priced-out-in-australia-own-a-home-in-spain", country=C, topic="cost", img="town", mins=5,
  kicker=TOPICS["cost"], title="Priced Out in Australia? You Can Still Own a Home in Spain",
  h1="Priced out in Australia? You can still own a home",
  desc=f"Australia's median dwelling is worth {F('price_au').split(' (')[0]}. In a Spanish mountain town, a three-bedroom flat costs a fraction of that, with no mortgage.",
  lead=f"Rate rises, auctions you can't win, a deposit that keeps moving away. Australia's national median dwelling value is {F('price_au')}. Owning a home doesn't have to be a lifetime project.",
  body=f"""{price_table([("Australia (national median dwelling)", F('price_au')), ("Spain (average, per m²)", F('price_spain')), ("Villablino (per m²)", F('price_villablino'))])}
<h2>A real example</h2>
<p>Our current flat in Villablino has three bedrooms, 74 m², south-facing rooms and furniture included, listed at €42,000. Add the transfer tax ({F('itp_cyl')}) and notary fees, and that is the full price of owning it outright.</p>
<h2>No auction, no bidding war</h2>
<p>In Spain you negotiate. That is our job: we talk to the seller in Spanish and push the price down for you.</p>
{villablino()}""",
  faq=[("What is Australia's median home value?", Fc('price_au') + "."),
       ("Can foreigners buy property in Spain?", "Yes. You need an NIE (foreigner tax number). Buying does not give you residence; for that you need a visa.")],
  sources=src("price_au", "itp_cyl") + BASE_SOURCES),

dict(slug="working-holiday-visa-spain-for-australians", country=C, topic="visas", img="nature", mins=5,
  kicker=TOPICS["visas"], title="Spain Working Holiday Visa for Australians: A Year in Spain",
  h1="Spain's working holiday visa for Australians",
  desc="Australians aged 18 to 30 can live and work in Spain for up to a year. How it works and how to use it to find the place you'll come back to.",
  lead=f"If you are an Australian aged 18 to 30, Spain gives you {F('whv')}. It's the gap year that turns into a plan.",
  body=f"""<h2>The basics</h2>
<p>The scheme gives {F('whv')}. You apply at the Spanish consulate in Australia and must show savings and insurance.</p>
<h2>Use the year well</h2>
<ul><li>Learn Spanish properly.</li><li>Live in more than one region: the north is green and mountainous, the south dry and sunny.</li><li>Look at homes and talk to locals about prices.</li></ul>
<h2>When the year is up</h2>
<p>To stay, move on to the digital nomad visa ({F('dnv_income')}) or the non-lucrative visa.</p>
{villablino()}""",
  faq=[("What is the age limit for Australians?", "18 to 30."),
       ("How long does the visa last?", "Up to 12 months.")],
  sources=src("whv", "dnv_income") + BASE_SOURCES),

dict(slug="ponferrada-templar-city-of-history", country=C, topic="life", mins=6,
  kicker=TOPICS["life"], title="Ponferrada: A Templar City for Australians Who Love History",
  h1="Ponferrada: a Templar city for people who love history",
  desc="A Templar castle, the Camino de Santiago, Roman gold mines and a wine valley: why Ponferrada, in north-west Spain, wins over visitors from far away.",
  lead=f"Some places have stories older than whole countries. In Ponferrada, {F('pf_castle')}. Pilgrims on the Camino de Santiago still walk past its walls.",
  body=f"""<h2>A castle that is the city's heart</h2>
<p>Ponferrada's castle is one of the great fortresses of north-west Spain. {Fc('pf_castle')}. You don't visit it once; you walk past it on your way to buy bread.</p>
<h2>Roman gold and a wine valley</h2>
<p>Las Médulas is a {F('medulas')}. Around Ponferrada, El Bierzo is a green valley of vineyards and orchards.</p>
<h2>A real city, not a museum</h2>
<p>Ponferrada has {F('pf_population')}, the region's reference hospital (Hospital El Bierzo) and a train station: {F('pf_train')}.</p>
<h2>Mountains next door</h2>
<p>An hour from Ponferrada, Villablino sits in a UNESCO Biosphere Reserve with homes around {F('price_villablino')}. City life and mountain life, a short drive apart.</p>
<p><a href="/properties/">See our homes in León province</a>.</p>""",
  faq=[("Where is Ponferrada?", "In El Bierzo, León province, north-west Spain."),
       ("What is Las Médulas?", Fc('medulas') + "."),
       ("How far is Ponferrada from Madrid by train?", Fc('pf_train') + ".")],
  sources=src("pf_castle", "medulas", "pf_population", "pf_train", "price_villablino")),

dict(slug="living-in-the-middle-of-europe", country=C, topic="life", img="town", mins=4,
  kicker=TOPICS["life"], title="From the Edge of the World to the Middle of Europe",
  h1="From the edge of the world to the middle of Europe",
  desc="Long-haul flights for every holiday? Living in Spain puts Europe's cities, history and food a short trip away. Here's how connected north-west Spain is.",
  lead="From Australia, Europe is a 20-hour journey. From Spain, it's a weekend. Living here changes what a holiday means.",
  body=f"""<h2>Connected, even from the mountains</h2>
<p>Villablino is 98 km from León Airport and 153 km from Asturias Airport. From Ponferrada, {F('pf_train')}, and Madrid's airport connects to the whole of Europe.</p>
<h2>Same time zone as Paris and Rome</h2>
<p>Spain runs on Central European Time, so calls with friends in London, Paris or Berlin are easy. Calls home need planning: eastern Australia is around eight to ten hours ahead of Spain, depending on the season.</p>
<h2>A base that costs little</h2>
<p>With homes in Villablino around {F('price_villablino')}, you can own your base in Europe outright and spend on travel instead of rent.</p>
{villablino()}""",
  faq=[("What is the time difference between Spain and Sydney?", "Around eight to ten hours, depending on the season."),
       ("How far is Villablino from an airport?", "León Airport is 98 km and Asturias Airport 153 km.")],
  sources=src("pf_train") + BASE_SOURCES),

dict(slug="christmas-in-the-snow-seasons-reversed", country=C, topic="life", img="ski", mins=4,
  kicker=TOPICS["life"], title="Christmas in the Snow: Living the Seasons the Other Way Round",
  h1="Christmas in the snow: the seasons, the other way round",
  desc="A white Christmas, a ski slope 15 km away and fresh summers: the seasons in north-west Spain for people raised down under.",
  lead="You've seen it on cards all your life. In the mountains of north-west Spain, Christmas really can be white, and summer arrives in July.",
  body=f"""<h2>Winter</h2>
<p>Leitariegos ski resort is about 15 km from Villablino. The climate has {F('vb_climate')}.</p>
<h2>Summer without the burn</h2>
<p>At about {F('vb_altitude')} above sea level, summer days are warm and nights cool. Rivers, forests and long evenings in the village squares.</p>
<h2>Four real seasons</h2>
<p>Green spring meadows, golden autumn birch forests, snow in winter. The valley is a {F('vb_unesco')}.</p>
{villablino()}""",
  faq=[("Does it snow at Christmas in Villablino?", "Snow is common in the mountains in winter; Leitariegos ski resort is about 15 km away."),
       ("Are summers hot?", "Warm by day and cool at night, thanks to the altitude of about " + F('vb_altitude') + ".")],
  sources=src("vb_climate", "vb_altitude") + BASE_SOURCES),
]
