from facts import F, src
from postlib import villablino, price_table, BASE_SOURCES, TOPICS

C = "uk"
POSTS = [
dict(slug="moving-to-spain-from-the-uk-2026", country=C, topic="visas", pillar=True, img="laciana-valley", mins=7,
  kicker=TOPICS["visas"], title="Moving to Spain from the UK in 2026: The Honest Guide",
  h1="Moving to Spain from the UK in 2026: the honest guide",
  desc="Visas after Brexit, the 90/180 rule, healthcare, pensions and home prices: what Britons need to know before moving to Spain in 2026.",
  lead=f"Since Brexit, {F('uk_90_180')}. To live here you need a visa, but the routes are clear, and a home in Spain can cost a fraction of one in Britain.",
  body=f"""<div class="box"><p><b>Quick answer:</b> remote workers use the digital nomad visa ({F('dnv_income')}); retirees and savers use the non-lucrative visa ({F('nlv_income')}). State pensioners can get Spanish public healthcare through the S1 form.</p></div>
<h2>Why so many Britons are looking at Spain</h2>
<p>The average UK home costs {F('price_uk')} and the average private rent is {F('rent_uk')}. Many people pay that rent for years and still can't buy. In much of rural Spain you can own a home outright for the price of a deposit in Britain.</p>
{price_table([("United Kingdom (average)", F('price_uk')), ("Spain (average)", F('price_spain')), ("Villablino, León", F('price_villablino'))])}
<h2>The visa you need</h2>
<ul><li><b>Working for a UK employer or clients:</b> the digital nomad visa. You need {F('dnv_income')}.</li>
<li><b>Retired or living on savings:</b> the non-lucrative visa. You need {F('nlv_income')}.</li></ul>
<p>Owning a home does not give you residence on its own. <a href="/buyers-guide/visas-to-live-in-spain.html">See our visa guide</a>.</p>
<h2>Healthcare and pensions</h2>
<p>{F('uk_s1').capitalize()}. And {F('uk_pension_uprated')}.</p>
{villablino()}""",
  faq=[("Can I live in Spain after Brexit?", "Yes, with a visa. " + F('uk_90_180').capitalize() + "."),
       ("Is the UK State Pension paid in Spain?", "Yes. " + F('uk_pension_uprated').capitalize() + "."),
       ("How much does a home cost in rural Spain?", "In Villablino around " + F('price_villablino') + ".")],
  sources=src("uk_90_180", "dnv_income", "nlv_income", "uk_s1", "uk_pension_uprated", "price_uk", "rent_uk") + BASE_SOURCES),

dict(slug="retire-in-spain-on-a-uk-state-pension", country=C, topic="retire", img="heritage", mins=6,
  kicker=TOPICS["retire"], title="Retiring to Spain on a UK State Pension: What You Need",
  h1="Retiring to Spain on a UK State Pension",
  desc="How British pensioners retire to Spain in 2026: the non-lucrative visa, S1 healthcare, pension uprating and a home bought outright in a quiet mountain town.",
  lead=f"Retiring to Spain is still very possible after Brexit. {F('uk_pension_uprated').capitalize()}, and {F('uk_s1')}.",
  body=f"""<h2>Step 1: the non-lucrative visa</h2>
<p>This is the visa for people who will not work in Spain. You need {F('nlv_income')}. A State Pension on its own is often not enough, but most retirees combine it with a workplace or private pension, or savings.</p>
<h2>Step 2: healthcare with the S1</h2>
<p>{F('uk_s1').capitalize()}. Before you reach State Pension age, plan for private health insurance.</p>
<h2>Step 3: a home with no mortgage</h2>
<p>Retiring without rent or a mortgage changes everything. With homes in Villablino at around {F('price_villablino')}, many people can buy outright with the money from selling a UK home, and keep the rest as savings.</p>
<h2>Why a mountain town and not the Costas?</h2>
<p>Green valleys, four seasons, stone villages and no tourist crowds. Life is quiet, but the town has a health centre, pharmacies and shops within walking distance.</p>
{villablino()}""",
  faq=[("How much do I need for the non-lucrative visa?", F('nlv_income').capitalize() + "."),
       ("Will I get free healthcare in Spain as a UK pensioner?", F('uk_s1').capitalize() + ".")],
  sources=src("nlv_income", "uk_s1", "uk_pension_uprated") + BASE_SOURCES),

dict(slug="uk-house-prices-vs-spain", country=C, topic="cost", img="town", mins=5,
  kicker=TOPICS["cost"], title="UK House Prices vs Spain: What Your Money Buys in 2026",
  h1="UK house prices vs Spain: what your money buys",
  desc=f"The average UK home costs {F('price_uk').split(' (')[0]}. In a Spanish mountain town a three-bedroom flat can cost a small fraction of that. Here are the figures.",
  lead=f"The average UK home costs {F('price_uk')}. In Villablino, in north-west Spain, homes sell for around {F('price_villablino')}.",
  body=f"""{price_table([("United Kingdom (average home)", F('price_uk')), ("Spain (average, per m²)", F('price_spain')), ("Castile and León (per m²)", F('price_cyl')), ("Villablino (per m²)", F('price_villablino'))])}
<h2>What that means in practice</h2>
<p>Our current flat in Villablino has three bedrooms and 74 m² and is listed at €42,000. Add the regional transfer tax ({F('itp_cyl')}) and notary fees, and you have the full cost of owning a home with no mortgage.</p>
<h2>The catch? There isn't one, but there is a trade-off</h2>
<p>You won't be in a big city. You will be in a real town of {F('vb_population')}, surrounded by mountains, with fibre internet and services. For many people that is exactly the point.</p>
{villablino()}""",
  faq=[("How much is the average home in the UK?", F('price_uk').capitalize() + "."),
       ("How much is a home in Villablino?", "Around " + F('price_villablino') + ".")],
  sources=src("price_uk", "price_cyl", "itp_cyl") + BASE_SOURCES),

dict(slug="stop-renting-in-the-uk-own-a-home-in-spain", country=C, topic="cost", img="pool", mins=5,
  kicker=TOPICS["cost"], title="Tired of UK Rent? How Owning in Spain Changes the Maths",
  h1="Tired of UK rent? How owning a home in Spain changes the maths",
  desc=f"The average UK rent is {F('rent_uk').split(' (')[0]}. Here is how buying a home outright in rural Spain compares, with real figures for 2026.",
  lead=f"The average private rent in the UK is {F('rent_uk')}. At that rate, a little over two years of rent would pay for our three-bedroom flat in Villablino.",
  body=f"""<h2>Rent vs own: a simple comparison</h2>
<p>At {F('rent_uk')}, a tenant pays around £16,700 a year. Our three-bedroom flat in Villablino is listed at €42,000. That is less than three years of average UK rent, and then the home is yours.</p>
<h2>What owning still costs</h2>
<ul><li>The transfer tax when you buy: {F('itp_cyl')} in Castile and León.</li>
<li>A yearly municipal tax (IBI), usually modest in small towns.</li>
<li>If you don't live in Spain, a yearly non-resident tax: {F('irnr_imputed')}.</li></ul>
<p>See every cost in our <a href="/buyers-guide/buying-costs-and-taxes.html">costs and taxes guide</a>.</p>
{villablino()}""",
  faq=[("What is the average rent in the UK?", F('rent_uk').capitalize() + "."),
       ("What taxes do I pay to buy in Castile and León?", "A transfer tax of " + F('itp_cyl') + ", plus notary and registry fees.")],
  sources=src("rent_uk", "itp_cyl", "irnr_imputed") + BASE_SOURCES),

dict(slug="work-remotely-from-spain-for-a-uk-company", country=C, topic="work", img="nature", mins=6,
  kicker=TOPICS["work"], title="Working Remotely from Spain for a UK Company (2026 Guide)",
  h1="Working remotely from Spain for a UK company",
  desc="Keep your UK job and live in the Spanish mountains: the digital nomad visa, the income you need in 2026, internet and time zone.",
  lead=f"The Spanish digital nomad visa lets you live in Spain while you work for a UK employer or clients. You need {F('dnv_income')}.",
  body=f"""<h2>Who the visa is for</h2>
<p>Employees of foreign companies and freelancers with foreign clients. Most of your work must come from outside Spain: {F('dnv_income')}.</p>
<h2>Time zone</h2>
<p>Spain is one hour ahead of the UK all year, so your working day lines up almost exactly with your colleagues'.</p>
<h2>Internet in the mountains</h2>
<p>Villablino has fibre internet in town plus 4G and 5G. For homes in the smaller villages we check the connection at the exact address before you decide.</p>
<h2>Taxes</h2>
<p>If you live in Spain more than 183 days a year you normally become a Spanish tax resident. Talk to a cross-border tax adviser before you move. <a href="/buyers-guide/buying-costs-and-taxes.html">Read our tax overview</a>.</p>
{villablino()}""",
  faq=[("How much do I need to earn for the Spanish digital nomad visa?", F('dnv_income').capitalize() + "."),
       ("What is the time difference between the UK and Spain?", "Spain is one hour ahead of the UK.")],
  sources=src("dnv_income") + BASE_SOURCES),

dict(slug="green-spain-for-brits-who-dont-want-the-costas", country=C, topic="life", img="nature", mins=5,
  kicker=TOPICS["life"], title="Green Spain: For Britons Who Don't Want the Costas",
  h1="Green Spain: for Britons who don't want the Costas",
  desc="Mountains, forests, four seasons and stone villages: the Spain most British buyers never see, and why the Laciana Valley could suit you.",
  lead="Not everyone dreams of a beach bar. North-west Spain is green, mountainous and quiet, more Lake District than Benidorm, but with more sun and much lower prices.",
  body=f"""<h2>What it is like</h2>
<p>The Laciana Valley is a {F('vb_unesco')}, with peaks above 2,000 metres, birch forests and rivers. The weather has four real seasons: {F('vb_climate')}.</p>
<h2>Wildlife</h2>
<p>The mountains around the valley are home to the Cantabrian brown bear and the capercaillie. They live in the mountains, not in town. Next door, Somiedo is {F('somiedo')}.</p>
<h2>Winter sports and walking</h2>
<p>Leitariegos ski resort is about 15 km from Villablino, and trails start from the villages of the valley.</p>
{villablino()}""",
  faq=[("Is north-west Spain rainy?", "It is greener and wetter than southern Spain, with drier summers: " + F('vb_climate') + "."),
       ("Are there bears near Villablino?", "Yes, in the surrounding mountains, not in town.")],
  sources=src("vb_climate", "somiedo") + BASE_SOURCES),
]
