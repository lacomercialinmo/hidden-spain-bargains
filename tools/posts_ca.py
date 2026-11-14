from facts import F, Fc, src
from postlib import villablino, price_table, BASE_SOURCES, TOPICS

C = "ca"
POSTS = [
dict(slug="moving-to-spain-from-canada-2026", country=C, topic="visas", pillar=True, img="laciana-valley", mins=7,
  kicker=TOPICS["visas"], title="Moving to Spain from Canada in 2026: Your Options",
  h1="Moving to Spain from Canada: your three ways in",
  desc="Canadians can live in Spain on a working holiday visa up to age 35, the digital nomad visa or the non-lucrative visa. 2026 figures and home prices.",
  lead=f"Canadians have one advantage most people don't: a working holiday visa open until age 35. After that, the digital nomad and non-lucrative visas cover most people.",
  body=f"""<div class="box"><p><b>Quick answer:</b> under 36, the working holiday visa gives you {F('whv')}. Remote workers use the digital nomad visa ({F('dnv_income')}). Retirees use the non-lucrative visa ({F('nlv_income')}).</p></div>
<h2>Why Canadians are looking at Spain</h2>
<p>You have probably done the maths many times. The national average home in Canada sells for {F('price_ca')}, and in the Greater Toronto Area the average is {F('price_toronto')}. In Spain, a whole flat in a mountain town can cost less than a down payment back home.</p>
{price_table([("Canada (national average)", F('price_ca')), ("Greater Toronto Area (average)", F('price_toronto')), ("Spain (average)", F('price_spain')), ("Villablino, León", F('price_villablino'))])}
<h2>The three routes</h2>
<ul><li><b>Working holiday (18–35):</b> {F('whv')}. Perfect for trying Spain before you buy.</li>
<li><b>Digital nomad visa:</b> keep your Canadian job or clients. You need {F('dnv_income')}.</li>
<li><b>Non-lucrative visa:</b> for living on savings or a pension. You need {F('nlv_income')}.</li></ul>
{villablino()}""",
  faq=[("Can Canadians work in Spain?", "Yes, with the right visa. Canadians aged 18–35 can use the working holiday visa; others can use the digital nomad visa to work remotely for foreign clients."),
       ("What is the age limit for the Spanish working holiday visa for Canadians?", "35."),
       ("How much is a home in Villablino?", "Around " + F('price_villablino') + ".")],
  sources=src("whv", "dnv_income", "nlv_income", "price_ca", "price_toronto") + BASE_SOURCES),

dict(slug="from-toronto-to-castellon", country=C, topic="cost", mins=6,
  kicker=TOPICS["cost"], title="From Toronto to Castellón: Trading Stress for the Sea",
  h1="From Toronto to Castellón: trading stress for the Mediterranean",
  desc="A Toronto home averages over C$1 million. On Spain's Castellón coast, homes average about €1,450/m², with mild winters and warm seas.",
  lead=f"You work hard, you pay a fortune and you still feel you're running to stand still. The average home in the Greater Toronto Area sells for {F('price_toronto')}. On the Mediterranean coast of Castellón, homes average {F('cs_price_prov')}.",
  body=f"""<h2>A different kind of rich</h2>
<p>Some of the happiest people we know left big, expensive cities for smaller places where life is slower. Castellón is that kind of place: a Mediterranean province between Valencia and Barcelona, with beaches, orange groves, mountain villages inland and a calm provincial capital.</p>
<h2>The numbers</h2>
{price_table([("Greater Toronto Area (average)", F('price_toronto')), ("Castellón province (per m²)", F('cs_price_prov').split(', the lowest')[0]), ("Castellón city (per m²)", F('cs_price_city'))])}
<h2>The weather you've been dreaming of in February</h2>
<p>Castellón has {F('cs_climate')}. No snow shovelling, no ice on the windscreen.</p>
<h2>How to get there legally</h2>
<p>Under 36? The working holiday visa gives you {F('whv')}. Otherwise, remote workers use the digital nomad visa ({F('dnv_income')}) and savers the non-lucrative visa. <a href="/buyers-guide/visas-to-live-in-spain.html">See all visas</a>.</p>
<h2>We are starting to look in Castellón</h2>
<p>Castellón is the next province we are opening. <a href="/properties/#request">Tell us what you want</a> and we will search there for you, or start with the mountain homes we already have in León.</p>""",
  faq=[("Is Castellón cheaper than Valencia and Alicante?", "Yes. Castellón homes averaged " + F('cs_price_prov') + "."),
       ("What is the weather like in Castellón?", Fc('cs_climate') + ".")],
  sources=src("price_toronto", "cs_price_prov", "cs_price_city", "cs_climate", "whv", "dnv_income")),

dict(slug="youth-mobility-visa-spain-for-canadians", country=C, topic="visas", img="ski", mins=5,
  kicker=TOPICS["visas"], title="Spain's Working Holiday Visa for Canadians (Up to 35)",
  h1="Spain's working holiday visa for Canadians: a year to try a new life",
  desc="Canadians aged 18 to 35 can live and work in Spain for up to a year. How the youth mobility visa works and why it is the perfect test run.",
  lead=f"If you are Canadian and 35 or younger, you hold a rare key: {F('whv')}. It is the easiest way to test a new life before you commit.",
  body=f"""<h2>Who can apply</h2>
<p>Canadian citizens aged 18 to 35. Australians and New Zealanders have the same scheme, but only up to age 30, so Canadians get five extra years.</p>
<h2>What you can do</h2>
<p>Live in Spain, work, travel and see if the life suits you. Many people use the year to learn Spanish, find the region they love and look at homes.</p>
<h2>Then make it permanent</h2>
<p>If you fall in love with Spain, you can move on to the digital nomad visa ({F('dnv_income')}) or the non-lucrative visa.</p>
<h2>Where to spend your year</h2>
<p>Snow, mountains and lakes feel like home, but with a Spanish rhythm. Leitariegos ski resort is about 15 km from Villablino.</p>
{villablino()}""",
  faq=[("What is the age limit for Canadians?", "35."),
       ("How long can I stay?", "Up to 12 months.")],
  sources=src("whv", "dnv_income") + BASE_SOURCES),

dict(slug="trade-canadian-winters-for-spanish-ones", country=C, topic="life", img="ski", mins=5,
  kicker=TOPICS["life"], title="Trade Canadian Winters for Spanish Ones: Snow, but Lighter",
  h1="Trade Canadian winters for Spanish ones",
  desc="You like real seasons but not five months of minus twenty. Spain's mountains give you snow, ski slopes and sun, with far shorter, softer winters.",
  lead=f"You don't want to give up winter, just the brutal part of it. In Villablino, in the mountains of north-west Spain, the climate has {F('vb_climate')}.",
  body=f"""<h2>Snow you can enjoy</h2>
<p>Leitariegos ski resort is about 15 km from Villablino. You can ski in the morning and be home for lunch.</p>
<h2>Summers that are actually pleasant</h2>
<p>At about {F('vb_altitude')} above sea level, Villablino stays fresher than the rest of Spain in July and August.</p>
<h2>Prefer the sea?</h2>
<p>On the Mediterranean coast, Castellón has {F('cs_climate')}. <a href="/guides/from-toronto-to-castellon.html">Read our Toronto-to-Castellón guide</a>.</p>
{villablino()}""",
  faq=[("Does it snow in Villablino?", "Yes, especially in the mountains around it. Leitariegos ski resort is about 15 km away."),
       ("What are winters like in Castellón?", Fc('cs_climate') + ".")],
  sources=src("vb_climate", "cs_climate") + BASE_SOURCES),

dict(slug="work-remotely-from-spain-for-a-canadian-company", country=C, topic="work", img="nature", mins=5,
  kicker=TOPICS["work"], title="Work Remotely from Spain for a Canadian Company",
  h1="Work remotely from Spain for a Canadian company",
  desc="Keep your Canadian job and live in Spain: the digital nomad visa income for 2026, time zones, internet in small towns and taxes to plan.",
  lead=f"Your job is already remote. The only thing tying you to an expensive city is habit. With the Spanish digital nomad visa you need {F('dnv_income')}.",
  body=f"""<h2>The visa</h2>
<p>You need {F('dnv_income')}, plus a degree or proven experience and a letter from your employer or contracts with clients.</p>
<h2>Time zone</h2>
<p>Spain is six hours ahead of Toronto. A common rhythm: your own time in the morning, Canadian meetings in the afternoon.</p>
<h2>Internet</h2>
<p>Villablino has fibre internet in town plus 4G and 5G.</p>
<h2>Taxes</h2>
<p>If you live in Spain more than 183 days a year you normally become a Spanish tax resident. Plan the move with a cross-border tax adviser.</p>
{villablino()}""",
  faq=[("What is the time difference between Toronto and Spain?", "Spain is six hours ahead of Toronto."),
       ("How much income do I need?", Fc('dnv_income') + ".")],
  sources=src("dnv_income") + BASE_SOURCES),

dict(slug="retire-in-spain-from-canada", country=C, topic="retire", img="heritage", mins=5,
  kicker=TOPICS["retire"], title="Retiring to Spain from Canada: Sun, Savings and Peace",
  h1="Retiring to Spain from Canada",
  desc="Sell a Canadian home, buy outright in Spain and keep the difference. The non-lucrative visa, healthcare and the quiet towns that make it work.",
  lead=f"You built a life in Canada. Now you can choose where to enjoy it. Sell a home worth around {F('price_ca')}, buy one in Spain outright, and keep most of the difference.",
  body=f"""<h2>The visa</h2>
<p>The non-lucrative visa is the retirement route. You need {F('nlv_income')} and private health insurance.</p>
<h2>The home</h2>
<p>In Villablino homes cost around {F('price_villablino')}; in Castellón city, {F('cs_price_city')}. Mountains or sea, the maths works.</p>
<h2>Healthcare</h2>
<p>Villablino has a health centre with an emergency service. The reference hospital is Hospital El Bierzo in Ponferrada.</p>
{villablino()}""",
  faq=[("What visa do I need to retire in Spain?", "Usually the non-lucrative visa: " + F('nlv_income') + "."),
       ("How much is a home in Spain?", "In Villablino around " + F('price_villablino') + "; in Castellón city " + F('cs_price_city') + ".")],
  sources=src("nlv_income", "price_ca", "cs_price_city") + BASE_SOURCES),
]
