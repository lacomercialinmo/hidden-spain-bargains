from facts import F, Fc, src

POSTS = [
dict(
  slug="how-we-work", kicker="Buyers guide", img="laciana-valley", mins=4,
  title="How Our Spanish Home Search Works | Hidden Spain Bargains",
  h1="How our home search works",
  desc="We find homes in Spain, research the area for you and negotiate the price. You only pay if you buy: half of the saving we negotiate, minimum €605 incl. VAT.",
  lead="We work for the buyer, not the seller. We find the home, explain the area and negotiate the price for you, and you only pay us if you buy.",
  body="""
<h2>What we do for you</h2>
<p>We are a personal-shopper service for people buying a home in Spain from abroad. Most agencies work for the seller and want the highest price. We work for you and want the lowest one.</p>
<ul>
<li><b>We search.</b> We look for homes that match your budget and the life you want: mountains, quiet towns, fast internet, healthcare nearby.</li>
<li><b>We explain the area.</b> Every home comes with a guide to its town: services, schools, airports, nature and what daily life is like.</li>
<li><b>We negotiate.</b> We talk to the seller in Spanish and push the price down for you.</li>
<li><b>We guide you to the notary.</b> We tell you which documents you need and who does what, so nothing surprises you.</li>
</ul>
<h2>How you pay us</h2>
<p>You only pay if you buy. <b>Our fee is half of the saving we negotiate, VAT included, with a minimum of €605 (€500 + VAT).</b> The saving is the difference between the advertised price on the day you sign our search agreement and the price you finally pay.</p>
<div class="tablewrap"><table><tr><th>Example</th><th>Advertised price</th><th>You pay</th><th>Saving</th><th>Our fee (VAT incl.)</th><th>You keep</th></tr>
<tr><td>Good negotiation</td><td>€80,000</td><td>€70,000</td><td>€10,000</td><td>€5,000</td><td>€5,000</td></tr>
<tr><td>Small discount</td><td>€60,000</td><td>€58,000</td><td>€2,000</td><td>€1,000</td><td>€1,000</td></tr>
<tr><td>No discount possible</td><td>€50,000</td><td>€50,000</td><td>€0</td><td>€605 (minimum)</td><td>—</td></tr></table></div>
<p>If you do not buy, you pay nothing. The seller pays us nothing either, so we work only for you. The terms are in a simple search agreement in English and Spanish that you sign before you see any property.</p>
<h2>Step by step</h2>
<ol>
<li><b>Tell us what you need.</b> Budget, bedrooms, lifestyle and timing. Use the form on our <a href="/properties/#request">properties page</a> or WhatsApp us.</li>
<li><b>Get a shortlist.</b> We send you homes that fit, with photos, video and the area guide.</li>
<li><b>See the home.</b> The owner shows you the home in person or on a live video call.</li>
<li><b>Make an offer.</b> We negotiate for you and agree the price and conditions.</li>
<li><b>Sign and get the keys.</b> You sign at a notary in Spain, in person or through someone you give power of attorney to.</li>
</ol>
""",
  faq=[("Do you charge the seller?", "No. We work for the buyer. The seller pays nothing to us."),
       ("What if I don't buy?", "Then you pay nothing."),
       ("Can I buy without travelling to Spain?", "Yes. You can view by video call and sign through a power of attorney. See our guide to <a href=\"/buyers-guide/buying-from-abroad.html\">buying from abroad</a>.")],
  sources=[("La Comercial Inmobiliaria", "https://lacomercial.app.link")],
),
dict(
  slug="buying-costs-and-taxes", kicker="Buyers guide · Tax in Spain", mins=8,
  title="Buying a Home in Spain: Costs & Taxes for Foreigners (2026)",
  h1="Buying a home in Spain: costs and taxes for foreigners",
  desc="The taxes you pay to buy, own and sell a home in Spain as a foreigner in 2026: transfer tax in Castile and León, non-resident tax, IBI and the 3% withholding.",
  lead="When you buy a resale home in Castile and León you pay a transfer tax of " + F("itp_cyl") + ", plus notary and land registry fees. After that, owners pay a yearly local tax, and non-residents also file a yearly income tax return.",
  body=f"""
<div class="box"><p><b>Quick answer:</b> budget the price of the home plus roughly 10% for taxes and fees when you buy. In Castile and León, where Villablino is, most of that is the transfer tax (ITP) of {F('itp_cyl')}. <a href="/buyers-guide/purchase-cost-calculator.html">Work out your total in pounds, dollars or euros with our calculator</a>.</p></div>
<h2>1. Taxes and costs when you buy</h2>
<h3>Transfer tax (ITP) on resale homes</h3>
<p>Almost every home we show is a resale home, so you pay the Impuesto de Transmisiones Patrimoniales (ITP). The rate is set by each region. In Castile and León it is {F('itp_cyl')}.</p>
<p>There are lower rates for some people buying their main home: {F('itp_cyl_reduced')}. In small rural towns the rate can drop to {F('itp_cyl_rural_young')}. Villablino has {F('vb_population')}, so it counts as a rural town for this rule, but you must meet every condition.</p>
<h3>Example</h3>
<table><tr><th>Item</th><th>Home at €42,000</th></tr>
<tr><td>Transfer tax (ITP, 8%)</td><td>€3,360</td></tr>
<tr><td>Notary and land registry</td><td>regulated fees that depend on the price; ask for a quote before you sign</td></tr>
<tr><td>Lawyer or gestoría (optional)</td><td>agreed with them</td></tr></table>
<h3>New homes</h3>
<p>New homes bought from a developer pay VAT instead of ITP, plus stamp duty (AJD) on the deed. Ask us for the figures if you are looking at a new build.</p>
<h2>2. Taxes while you own the home</h2>
<ul>
<li><b>IBI:</b> {F('ibi')}. In small towns it is usually modest. We ask the seller for the last receipt so you know the figure.</li>
<li><b>Non-resident income tax:</b> if you do not live in Spain, you pay a yearly tax on the home even if you don't rent it out: {F('irnr_imputed')}. It is filed on form Modelo 210.</li>
<li><b>Rental income:</b> if you rent the home out, non-residents pay tax on that income too (19% or 24%).</li>
</ul>
<h2>3. If you become a Spanish tax resident</h2>
<p>If you live in Spain for more than 183 days a year, or your main interests are here, you normally become a Spanish tax resident and pay Spanish income tax on your worldwide income. Your home country's tax treaty with Spain decides how pensions and other income are taxed. Get advice from a cross-border tax adviser before you move.</p>
<h2>4. When you sell</h2>
<p>If you sell while you are a non-resident, {F('sale_withholding')}. It is an advance payment towards your capital gains tax, and you can claim back any excess. The seller also usually pays the municipal plusvalía tax.</p>
""",
  faq=[("What is the transfer tax in Castile and León?", Fc("itp_cyl") + " for resale homes, with reduced rates for some main-home buyers."),
       ("Do non-residents pay tax on a home they don't rent out?", "Yes. " + Fc("irnr_imputed") + ", filed on Modelo 210."),
       ("What happens when a non-resident sells?", "The buyer withholds 3% of the price and pays it to the Spanish tax office as an advance on the seller's capital gains tax.")],
  sources=src("itp_cyl", "irnr_imputed", "sale_withholding"),
),
dict(
  slug="visas-to-live-in-spain", kicker="Buyers guide · Visas", mins=7,
  title="Visas to Live in Spain in 2026: Digital Nomad, Non-Lucrative",
  h1="Visas to live in Spain in 2026",
  desc="The main visas for people from the UK, US, Canada, Australia and NZ who want to live in Spain: digital nomad, non-lucrative and working holiday (2026).",
  lead="Buying a home in Spain does not give you the right to live here. If you are not an EU citizen you need a visa, and the three most used ones are the digital nomad visa, the non-lucrative visa and the working holiday visa.",
  body=f"""
<div class="box"><p><b>Quick answer:</b> remote workers usually choose the <b>digital nomad visa</b> ({F('dnv_income')}). Retirees and people living on savings usually choose the <b>non-lucrative visa</b> ({F('nlv_income')}). Young Australians, New Zealanders and Canadians can use the <b>working holiday visa</b>, which gives {F('whv')}.</p></div>
<h2>Digital nomad visa (remote work)</h2>
<p>This visa lets you live in Spain while you work remotely for companies or clients outside Spain. You need to show {F('dnv_income')}. The amount rises every year because it is tied to the Spanish minimum wage.</p>
<h2>Non-lucrative visa (retirees and savers)</h2>
<p>This visa is for people who want to live in Spain without working here. You need to show {F('nlv_income')}. You also need private health insurance.</p>
<h2>Working holiday visa (under 31, or under 36 for Canadians)</h2>
<p>Spain has youth mobility agreements that give {F('whv')}. It is a good way to try life in Spain before buying.</p>
<h2>UK citizens: the 90/180 rule</h2>
<p>Since Brexit, {F('uk_90_180')}. Owning a home in Spain does not change this. To stay longer you need one of the visas above.</p>
<h2>What about the golden visa?</h2>
<p>Spain closed its investor residence route (the "golden visa") for property purchases in 2025, so buying a home no longer gives you residence by itself.</p>
""",
  faq=[("How much income do I need for the Spanish digital nomad visa?", Fc("dnv_income") + "."),
       ("How much do I need for the non-lucrative visa?", Fc("nlv_income") + "."),
       ("Does buying a property in Spain give me residency?", "No. You need a visa such as the digital nomad or non-lucrative visa if you are not an EU citizen.")],
  sources=src("dnv_income", "nlv_income", "whv", "uk_90_180"),
),
dict(
  slug="buying-from-abroad", kicker="Buyers guide · Remote purchase", img="town", mins=5,
  title="How to Buy a Home in Spain Without Travelling There",
  h1="How to buy a home in Spain from abroad",
  desc="Yes, you can buy a home in Spain without flying over: get an NIE, view by video call, and sign through a power of attorney. Here is how it works step by step.",
  lead="You can buy a home in Spain without being here for every step. You need a Spanish tax number (NIE), a way to see the home, and someone to sign for you at the notary if you can't come.",
  body="""
<h2>1. Get your NIE</h2>
<p>The NIE is the identity number every foreigner needs to buy property in Spain. You can apply at a Spanish consulate in your country or in Spain. Without it, the notary cannot sign the sale.</p>
<h2>2. See the home by video</h2>
<p>We arrange a live video call with the owner so you can walk through every room, open windows and ask questions. We also send you the area guide, so you know the town before you visit.</p>
<h2>3. Check the paperwork</h2>
<p>Before you pay anything, the land registry extract (nota simple) shows who owns the home and whether it has debts or a mortgage. We ask for it and go through it with you.</p>
<h2>4. Reserve and sign</h2>
<ul>
<li><b>Deposit contract (arras):</b> you usually pay a deposit to take the home off the market. The contract says what happens if either side pulls out.</li>
<li><b>Notary:</b> the sale is signed at a notary. The buyer can choose the notary.</li>
<li><b>Power of attorney:</b> if you can't travel, you can give a power of attorney to a lawyer or person you trust. You sign it at a notary or Spanish consulate in your country, with an apostille where needed.</li>
</ul>
<h2>5. After the keys</h2>
<p>The deed is registered at the land registry in your name, the taxes are paid, and you put the utilities in your name. We tell you who to call for each one.</p>
""",
  faq=[("Do I need to travel to Spain to buy?", "No. You can view by video and sign through a power of attorney."),
       ("What is an NIE?", "The tax identity number every foreigner needs to buy property in Spain."),
       ("Who chooses the notary?", "In Spain the buyer normally has the right to choose the notary.")],
  sources=[("Comprar una propiedad en España siendo extranjero – CostaLuz Lawyers", "https://www.costaluzlawyers.com/es/comprar-propiedad-espana-extranjero-guia-legal/")],
),
]
