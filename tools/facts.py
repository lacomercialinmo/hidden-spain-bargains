"""Single source of truth for every legal, tax and market figure used on the site.

RULE: every time the site is changed, re-verify each fact against its source and update
`checked`. build.py refuses to build if any volatile fact is older than MAX_AGE_DAYS.
"""
import datetime

MAX_AGE_DAYS = 45

FACTS = {
    # --- Buying taxes, Castile and León ---
    "itp_cyl": dict(text="8% (10% on the part of the price above €250,000)", src="ITP Castilla y León 2026 – TaxDown",
                    url="https://taxdown.es/informacion-impuestos/itp-castilla-leon", checked="2026-11-14", volatile=True),
    "itp_cyl_rural_young": dict(text="0.01% for buyers under 36 buying their first main home for under €150,000 in a municipality of up to 10,000 people (income limits apply)",
                    src="ITP Castilla y León 2026 – TaxDown", url="https://taxdown.es/informacion-impuestos/itp-castilla-leon", checked="2026-11-14", volatile=True),
    "itp_cyl_reduced": dict(text="4% for some main-home buyers (under 36, large families, disability of 65% or more, protected housing), with income limits",
                    src="ITP Castilla y León 2026 – TaxDown", url="https://taxdown.es/informacion-impuestos/itp-castilla-leon", checked="2026-11-14", volatile=True),
    # --- Owning as a non-resident ---
    "irnr_imputed": dict(text="1.1% of the cadastral value (2% if it has not been revised in the last ten years), taxed at 19% for EU/EEA residents or 24% for everyone else",
                    src="Non-resident tax in Spain 2026 – TaxesForExpats", url="https://www.taxesforexpats.com/country-guides/spain/property-tax-in-spain-non-residents.html", checked="2026-11-14", volatile=True),
    "ibi": dict(text="a yearly municipal tax on the cadastral value; the rate depends on the town hall", src="Spain property tax guide – TaxesForExpats",
                    url="https://www.taxesforexpats.com/country-guides/spain/property-tax-in-spain-non-residents.html", checked="2026-11-14", volatile=False),
    "sale_withholding": dict(text="the buyer withholds 3% of the price and pays it to the tax office (Modelo 211)", src="Non-Resident Tax in Spain 2026 – Pellicer & Heredia",
                    url="https://www.pellicerheredia.com/en/non-resident-tax-spain/", checked="2026-11-14", volatile=True),
    # --- Visas ---
    "dnv_income": dict(text="€2,849 a month for a single applicant in 2026 (200% of the Spanish minimum wage), with no more than 20% of work for Spanish clients",
                    src="Digital Nomad Visa income 2026 – Migratiolex", url="https://migratiolex.com/spain-digital-nomad-visa-minimum-income-requirement-for-2026/", checked="2026-11-14", volatile=True),
    "nlv_income": dict(text="€28,800 a year for the main applicant in 2026 (400% of IPREM), plus €7,200 for each family member; no work allowed in Spain",
                    src="Non-Lucrative Visa 2026 – Pellicer & Heredia", url="https://www.pellicerheredia.com/residencia-no-lucrativa-espa%c3%b1a/", checked="2026-11-14", volatile=True),
    "whv": dict(text="up to 12 months for citizens of Australia and New Zealand aged 18–30 and Canada aged 18–35",
                    src="Working Holiday Visa Spain – Immigration Lawyers Spain", url="https://www.immigrationspain.es/en/working-holiday-visa-spain/", checked="2026-11-14", volatile=True),
    "uk_90_180": dict(text="UK passport holders can stay up to 90 days in any 180-day period in the Schengen area without a visa",
                    src="Brexit and Spain 2026 – CostaLuz Lawyers", url="https://www.costaluzlawyers.com/brexit-spain-guide-british-nationals/", checked="2026-11-14", volatile=True),
    "uk_s1": dict(text="UK State Pension recipients living in Spain may get Spanish state healthcare paid by the UK through an S1 form",
                    src="GOV.UK – Healthcare in Spain", url="https://gov.uk/healthcareinspain", checked="2026-11-14", volatile=True),
    "uk_pension_uprated": dict(text="the UK State Pension is paid in Spain and uprated every year",
                    src="Retiring in Spain from the UK – Novado", url="https://novado.es/en/guides/retiring-in-spain-from-uk/", checked="2026-11-14", volatile=True),
    # --- Home prices ---
    "price_villablino": dict(text="€539/m² (median, October 2026)", src="RealAdvisor – Villablino", url="https://realadvisor.es/es/precios-viviendas/municipio-villablino", checked="2026-11-14", volatile=True),
    "price_spain": dict(text="€2,429/m² (average, Q1 2026)", src="Colegio de Registradores – Estadística Registral Inmobiliaria, via Última Hora", url="https://www.ultimahora.es/noticias/comunidades/2026/05/07/2624541/precio-vivienda-sube-comunitat-valenciana-primer-trimestre-hasta-1963-euros-m2.html", checked="2026-11-14", volatile=True),
    "price_uk": dict(text="£273,000 (UK average, July 2026)", src="ONS UK House Price Index via Mortgage Solutions", url="https://www.mortgagesolutions.co.uk/mortgage-news/2026/09/16/house-price-growth-persists-despite-stubborn-inflation-and-rising-rates-ons/", checked="2026-11-14", volatile=True),
    "rent_uk": dict(text="£1,393 a month (UK average private rent, July 2026)", src="ONS via MPA", url="https://www.mpamag.com/uk/mortgage-types/residential/uk-house-prices-up-annually-but-growth-slows-for-second-month/586643", checked="2026-11-14", volatile=True),
    "price_us": dict(text="$417,500 (median existing-home price, September 2026)", src="National Association of Realtors", url="https://www.nar.realtor/newsroom/existing-home-sales-increased-1-5-in-september-according-to-nar-report", checked="2026-11-14", volatile=True),
    "price_ca": dict(text="C$666,538 (national average sale price, September 2026)", src="CREA via Advisor.ca", url="https://www.advisor.ca/economy/economic-indicators/crea-downgrades-home-sales-forecast-for-the-third-time-this-year/", checked="2026-11-14", volatile=True),
    "price_au": dict(text="A$884,855 (national median dwelling value, October 2026)", src="Cotality Home Value Index via OpenAgent", url="https://www.openagent.com.au/news/national-property-market-update-october-2026", checked="2026-11-14", volatile=True),
    "price_nz": dict(text="NZ$755,000 (national median price, September 2026)", src="REINZ via MPA", url="https://www.mpamag.com/nz/specialty/residential/south-island-outshines-north-as-nz-house-sales-slide/593272", checked="2026-11-14", volatile=True),
    # --- Villablino ---
    "vb_population": dict(text="7,585 residents (INE, 2025)", src="INE", url="https://www.ine.es/", checked="2026-11-14", volatile=False),
    "vb_unesco": dict(text="UNESCO Biosphere Reserve since 2003, about 22,000 hectares", src="Spain.info – Laciana Valley", url="https://www.spain.info/en/nature/valle-laciana-biosphere-reserve", checked="2026-11-14", volatile=False),
    "vb_altitude": dict(text="1,015 m", src="AEMET – Villablino", url="https://www.aemet.es/en/eltiempo/prediccion/municipios/villablino-id24202", checked="2026-11-14", volatile=False),
    # --- Ponferrada / El Bierzo ---
    "pf_population": dict(text="63,186 residents (INE, 2024)", src="Diario de León", url="https://www.diariodeleon.es/sociedad/251212/2069126/municipios-grandes-impulsan-poblacion-leon.html", checked="2026-11-14", volatile=False),
    "pf_castle": dict(text="the Templar knights held Ponferrada until 1312; the castle covers about 8,000 m²", src="Turismo Castilla y León / TerraNostrum", url="https://www.turismocastillayleon.com/es/arte-cultura-patrimonio/castillos/castillo-ponferrada", checked="2026-11-14", volatile=False),
    "pf_train": dict(text="direct trains to Madrid take around four hours", src="Railclick – Madrid to Ponferrada", url="https://railclick.com/es/train/madrid/ponferrada", checked="2026-11-14", volatile=True),
    "medulas": dict(text="UNESCO World Heritage Site since 1997 and the largest open-pit gold mine of the Roman Empire, about 25 km south-west of Ponferrada", src="Wikipedia / UNESCO", url="https://en.wikipedia.org/wiki/Las_M%C3%A9dulas", checked="2026-11-14", volatile=False),
    "somiedo": dict(text="an Asturian natural park and Biosphere Reserve (since 2000) of 283 km², a stronghold of the Cantabrian brown bear, with guided bear-watching trips", src="Turismo Asturias", url="https://www.turismoasturias.es/en/descubre/naturaleza/reservas-de-la-biosfera/parque-natural-de-somiedo", checked="2026-11-14", volatile=False),
    "vb_climate": dict(text="average highs of about 7°C in January and 28°C in July, with drier summers (approximate model averages)", src="WeatherAPI – Villablino climate", url="https://www.weatherapi.com/history/q/villablino-725979", checked="2026-11-14", volatile=False),
    # --- Castellón ---
    "cs_price_prov": dict(text="€1,443/m² (average, Q1 2026), the lowest of the three Valencian provinces, against €1,843 in Valencia and €2,214 in Alicante", src="Colegio de Registradores, via Última Hora", url="https://www.ultimahora.es/noticias/comunidades/2026/05/07/2624541/precio-vivienda-sube-comunitat-valenciana-primer-trimestre-hasta-1963-euros-m2.html", checked="2026-11-14", volatile=True),
    "cs_price_city": dict(text="€1,317/m² (average, Q1 2026)", src="Tinsa – Castellón de la Plana", url="https://www.tinsa.es/precio-vivienda/comunitat-valenciana/castellon/castellon/", checked="2026-11-14", volatile=True),
    "cs_climate": dict(text="January highs of about 14°C, August highs of about 31°C and around 444 mm of rain in a normal year", src="Climate-Data.org / Snowy (AEMET station, 1991–2020)", url="https://es.climate-data.org/location/2097/", checked="2026-11-14", volatile=False),
    "price_toronto": dict(text="C$1,024,108 (GTA average selling price, October 2026)", src="TRREB Market Watch", url="https://trreb.ca/wp-content/files/news_releases/news2026/nr_market_watch_1026.pdf", checked="2026-11-14", volatile=True),
}

def F(key):
    return FACTS[key]["text"]

def src(*keys):
    seen, out = set(), []
    for k in keys:
        f = FACTS[k]
        if f["url"] not in seen:
            seen.add(f["url"]); out.append((f["src"], f["url"]))
    return out

def check():
    today = datetime.date.today()
    stale = [k for k, f in FACTS.items() if f["volatile"] and (today - datetime.date.fromisoformat(f["checked"])).days > MAX_AGE_DAYS]
    if stale:
        raise SystemExit("Re-verify these facts before building: " + ", ".join(stale))

def Fc(key):
    t = FACTS[key]["text"]
    return t[:1].upper() + t[1:]
