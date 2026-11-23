from facts import F, Fc, src
from postlib import villablino, price_table, BASE_SOURCES, TOPICS

C = "us"
POSTS = [
dict(slug="moving-to-spain-from-the-us-2026", country=C, topic="visas", pillar=True, img="laciana-valley", mins=7,
  kicker=TOPICS["visas"], title="Moving to Spain from the US in 2026: Visas That Work",
  h1="Moving to Spain from the US: the visas that actually work",
  desc="Americans can live in Spain with the digital nomad or non-lucrative visa. Income needed in 2026, healthcare, taxes and what a home costs.",
  lead=f"Americans can stay in Spain as tourists for up to 90 days. To live here you need a visa, and the two that fit most people are the digital nomad visa ({F('dnv_income')}) and the non-lucrative visa ({F('nlv_income')}).",
  body=f"""<h2>Option 1: digital nomad visa</h2>
<p>For remote employees of US companies and freelancers with clients outside Spain. You need {F('dnv_income')}.</p>
<h2>Option 2: non-lucrative visa</h2>
<p>For retirees and people living on savings, investments or pensions, with no work in Spain. You need {F('nlv_income')}. You also need private health insurance.</p>
<h2>Taxes: the American exception</h2>
<p>The US taxes its citizens on worldwide income wherever they live, and Spain taxes its residents too. The US–Spain tax treaty helps avoid paying twice, but you need a cross-border tax adviser before you move.</p>
<h2>What a home costs</h2>
{price_table([("United States (median existing home)", F('price_us')), ("Spain (average)", F('price_spain')), ("Villablino, León", F('price_villablino'))])}
{villablino()}""",
  faq=[("Can Americans live in Spain?", "Yes, with a visa such as the digital nomad visa or the non-lucrative visa."),
       ("How much income do I need for the Spanish digital nomad visa?", Fc('dnv_income') + "."),
       ("Do Americans in Spain still file US taxes?", "Yes. US citizens file US returns wherever they live; a tax treaty helps avoid double taxation.")],
  sources=src("dnv_income", "nlv_income", "price_us") + BASE_SOURCES),

dict(slug="us-home-prices-vs-spain", country=C, topic="cost", img="town", mins=5,
  kicker=TOPICS["cost"], title="A $416,700 Median Home vs a Paid-Off Home in Spain",
  h1="A $416,700 median home, or a paid-off home in Spain?",
  desc=f"The median US existing home costs {F('price_us').split(' (')[0]}. In a Spanish mountain town a three-bedroom apartment costs a small fraction of that, with no mortgage.",
  lead=f"The median existing-home price in the US is {F('price_us')}. In Villablino, north-west Spain, homes sell for around {F('price_villablino')}.",
  body=f"""{price_table([("United States (median existing home)", F('price_us')), ("Spain (average, per m²)", F('price_spain')), ("Villablino (per m²)", F('price_villablino'))])}
<h2>No mortgage, no HOA, no property-tax shock</h2>
<p>Our three-bedroom, 74 m² apartment in Villablino is listed at €42,000. You pay a one-off transfer tax of {F('itp_cyl')} and notary fees, then a modest yearly local tax (IBI).</p>
<h2>What you trade</h2>
<p>A big American house and a two-car commute, for a compact town where shops, the health centre and schools are close together, surrounded by mountains.</p>
{villablino()}""",
  faq=[("What is the median home price in the US?", Fc('price_us') + "."),
       ("What does a home cost in Villablino?", "Around " + F('price_villablino') + ".")],
  sources=src("price_us", "itp_cyl") + BASE_SOURCES),

dict(slug="remote-work-in-spain-on-us-income", country=C, topic="work", img="nature", mins=6,
  kicker=TOPICS["work"], title="Remote Work in Spain on a US Salary: Visa, Taxes, Hours",
  h1="Remote work in Spain on a US salary",
  desc="Keep your US remote job and live in Spain: digital nomad visa income for 2026, the 20% rule, time zones and the US tax filing you can't skip.",
  lead=f"With the Spanish digital nomad visa you can live in Spain and keep working for a US company. You need {F('dnv_income')}.",
  body=f"""<h2>The visa</h2>
<p>You need {F('dnv_income')}. You also need a degree or proven experience in your field, and a letter from your employer or contracts with your clients.</p>
<h2>Time zones</h2>
<p>Spain is six hours ahead of New York and nine ahead of California. Many remote workers in Spain work mornings for themselves and afternoons and evenings overlapping US hours.</p>
<h2>Taxes</h2>
<p>As a US citizen you keep filing US returns. If you live in Spain more than 183 days a year you also become a Spanish tax resident. Get cross-border advice before you move.</p>
<h2>Internet</h2>
<p>Villablino has fibre in town plus 4G and 5G coverage.</p>
{villablino()}""",
  faq=[("Can I work for a US company while living in Spain?", "Yes, with the digital nomad visa, if most of your income comes from outside Spain."),
       ("What income do I need?", Fc('dnv_income') + ".")],
  sources=src("dnv_income") + BASE_SOURCES),

dict(slug="early-retirement-in-spain-for-americans", country=C, topic="retire", img="heritage", mins=6,
  kicker=TOPICS["retire"], title="Early Retirement in Spain for Americans: A 2026 Guide",
  h1="Early retirement in Spain for Americans",
  desc="Retire early in Spain on savings or a pension: the non-lucrative visa, private health insurance and a home bought outright in the mountains.",
  lead=f"If you want to stop working and live on savings or a pension, the non-lucrative visa is the usual route. You need {F('nlv_income')}.",
  body=f"""<h2>The non-lucrative visa</h2>
<p>You need {F('nlv_income')}. You also need private health insurance and a clean criminal record. After five years of legal residence you can apply for long-term residence.</p>
<h2>Make your money last</h2>
<p>The biggest cost in retirement is housing. With homes in Villablino at around {F('price_villablino')}, many retirees buy outright and live without rent or a mortgage.</p>
<h2>Healthcare</h2>
<p>Visa applicants need private health insurance. Villablino has a health centre with an emergency service, and the reference hospital for the area is Hospital El Bierzo in Ponferrada.</p>
{villablino()}""",
  faq=[("How much do I need to retire in Spain?", "For the non-lucrative visa: " + F('nlv_income') + "."),
       ("Can I work on a non-lucrative visa?", "No. It is for people who live on their own means without working in Spain.")],
  sources=src("nlv_income") + BASE_SOURCES),

dict(slug="small-town-spain-vs-american-suburbs", country=C, topic="life", img="town", mins=5,
  kicker=TOPICS["life"], title="Small-Town Spain vs the American Suburbs: Daily Life",
  h1="Small-town Spain vs the American suburbs",
  desc="Walk to the pharmacy, the bakery and the health centre. What daily life is like in a Spanish mountain town compared with a car-dependent suburb.",
  lead="In a Spanish town, daily life happens on foot. The pharmacy, the supermarket, the bank and the health centre are a short walk from home.",
  body=f"""<h2>A town built for walking</h2>
<p>Villablino has {F('vb_population')}. Shops, pharmacies, banks, schools and the health centre are all in town, so most errands don't need a car.</p>
<h2>Nature on the doorstep</h2>
<p>The town sits in a {F('vb_unesco')}. Trails start from the villages, Leitariegos ski resort is about 15 km away, and a greenway of around 14 km follows the old mining railway.</p>
<h2>Slower, but connected</h2>
<p>Fibre internet, two airports within reach (León 98 km, Asturias 153 km) and trains to Madrid from Ponferrada: {F('pf_train')}.</p>
{villablino()}""",
  faq=[("Do I need a car in Villablino?", "Not for daily errands in town. A car helps for trips to the mountains and airports."),
       ("How far is Villablino from an airport?", "León Airport is 98 km and Asturias Airport 153 km.")],
  sources=src("pf_train") + BASE_SOURCES),

dict(slug="healthcare-in-spain-explained-for-americans", country=C, topic="retire", img="health", mins=5,
  kicker=TOPICS["retire"], title="Healthcare in Spain Explained for Americans",
  h1="Healthcare in Spain, explained for Americans",
  desc="How Spain's public and private healthcare works for foreign residents, what visa applicants need, and what is available in Villablino.",
  lead="Spain has a public health system for people who live and work here, and a large private sector. If you move on a visa, you will usually start with private insurance.",
  body=f"""<h2>Public healthcare</h2>
<p>People who work and pay social security in Spain are covered by the public system. Pensioners from some countries are covered through agreements with their home country.</p>
<h2>Private insurance for visa holders</h2>
<p>Applicants for the non-lucrative visa need private health insurance valid in Spain. Many digital nomads also start with private cover.</p>
<h2>What is near Villablino</h2>
<p>The town has a health centre with an emergency service and pharmacies. The reference hospital is Hospital El Bierzo in Ponferrada, 62 km away.</p>
{villablino()}""",
  faq=[("Do I need private health insurance to move to Spain?", "For the non-lucrative visa, yes. Check the requirements of your visa."),
       ("Is there a hospital near Villablino?", "Hospital El Bierzo in Ponferrada, 62 km away, is the reference hospital.")],
  sources=src("nlv_income") + BASE_SOURCES),
]
