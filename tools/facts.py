"""Single source of truth for every legal, tax and market figure used on the site.

RULE: every time the site is changed, re-verify each fact against its source and update
`checked`. build.py refuses to build if any volatile fact is older than MAX_AGE_DAYS.
"""
import datetime

MAX_AGE_DAYS = 45

FACTS = {
    # --- Transfer tax (ITP) on resale homes by region, general rate for homes under €250,000 (checked 2026-11-16) ---
    "itp_madrid": dict(text="6%", src="ITP Madrid 2026 – guiafiscal.es", url="https://guiafiscal.es/patrimonio/itp/madrid/", checked="2026-11-16", volatile=True),
    "itp_andalucia": dict(text="7%", src="ITP Andalucía 2026 – guiafiscal.es", url="https://guiafiscal.es/patrimonio/itp/andalucia/", checked="2026-11-16", volatile=True),
    "itp_regions": dict(text="from 6% in the Madrid region to 10% in Catalonia", src="ITP by region 2026 – Ros Legal Abogados", url="https://roslegalabogados.com/itp-por-comunidad-autonoma-2026-tabla-comparativa-de-lo-que-pagas-al-comprar-vivienda/", checked="2026-11-16", volatile=True),
    "itp_valencia": dict(text="9% (since 1 June 2026)", src="ITP Comunitat Valenciana – TaxDown", url="https://taxdown.es/informacion-impuestos/itp-comunidad-valenciana", checked="2026-11-16", volatile=True),
    "notary_registry": dict(text="usually about €600 to €1,500 together, depending on the price", src="Impuestos y gastos al comprar vivienda 2026 – Gibobs", url="https://www.gibobs.com/blog/sabes_impuestos_comprar_vivienda/", checked="2026-11-16", volatile=True),
    "ecb_rates": dict(text="13 November 2026", src="European Central Bank – euro reference rates", url="https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html", checked="2026-11-16", volatile=True),
    # --- Direct trains to Madrid (timetable aggregators, checked 2026-11-16) ---
    "train_puertollano": dict(text="about 1 h 10 min to 1 h 20 min by high-speed train, with more than 15 direct trains a day", src="Puertollano–Madrid trains – Omio", url="https://www.omio.es/trenes/puertollano", checked="2026-11-16", volatile=True),
    "train_medina": dict(text="about 55 minutes on the fastest direct trains to Madrid Chamartín", src="Medina del Campo–Madrid Chamartín trains – Omio", url="https://www.omio.es/trenes/medina-del-campo/madrid-chamartin-zufsv", checked="2026-11-16", volatile=True),
    "train_arevalo": dict(text="about 2 hours on direct regional trains to Madrid Príncipe Pío, around 7 a day", src="Arévalo–Madrid trains – Omio", url="https://www.omio.es/trenes/arevalo/madrid-dy63u", checked="2026-11-16", volatile=True),
    "train_linares": dict(text="about 3 hours to Madrid Atocha, with around 5 direct trains a day from Linares-Baeza station, about 10 km from town", src="Linares–Madrid trains – Omio", url="https://www.omio.es/trenes/linares/madrid", checked="2026-11-16", volatile=True),
    "train_ponferrada": dict(text="one direct train a day to Madrid Chamartín, taking about 4 hours, which also stops at Bembibre and Astorga", src="Madrid–Ponferrada trains – Omio; Diario de León", url="https://www.omio.es/trenes/madrid/ponferrada", checked="2026-11-16", volatile=True),

    # --- Buying taxes, Castile and León ---
    "itp_cyl": dict(text="8% (10% on the part of the price above €250,000)", src="ITP Castilla y León 2026 – TaxDown",
                    url="https://taxdown.es/informacion-impuestos/itp-castilla-leon", checked="2026-11-16", volatile=True),
    "itp_cyl_rural_young": dict(text="0.01% for buyers under 36 buying their first main home for under €150,000 in a municipality of up to 10,000 people (3,000 if within 30 km of the provincial capital); income limits apply",
                    src="Junta de Castilla y León – tax benefits (ITP)", url="https://tributos.jcyl.es/web/es/beneficios-fiscales/impuesto-sobre-transmisiones-patrimoniales.html", checked="2026-11-16", volatile=True),
    "itp_cyl_reduced": dict(text="4% on a main home for buyers under 36 (first home), large families, people with a disability of 65% or more and buyers of protected housing, with income limits",
                    src="ITP Castilla y León 2026 – TaxDown", url="https://taxdown.es/informacion-impuestos/itp-castilla-leon", checked="2026-11-16", volatile=True),
    # --- Owning as a non-resident ---
    "irnr_imputed": dict(text="1.1% of the cadastral value (2% if the town's values have not been revised since 2012), taxed at 19% for EU/EEA residents or 24% for everyone else",
                    src="Modelo 210 non-resident tax 2026 – GuiaFiscal", url="https://guiafiscal.es/irpf/modelo-210-irnr/", checked="2026-11-16", volatile=True),
    "ibi": dict(text="a yearly municipal tax on the cadastral value; the rate depends on the town hall", src="Spain property tax guide – TaxesForExpats",
                    url="https://www.taxesforexpats.com/country-guides/spain/property-tax-in-spain-non-residents.html", checked="2026-11-16", volatile=False),
    "sale_withholding": dict(text="the buyer withholds 3% of the price and pays it to the tax office (Modelo 211)", src="Non-Resident Tax in Spain 2026 – Pellicer & Heredia",
                    url="https://www.pellicerheredia.com/en/non-resident-tax-spain/", checked="2026-11-16", volatile=True),
    # --- Visas ---
    "dnv_income": dict(text="an income of €2,849 a month for a single applicant in 2026, which is 200% of the Spanish minimum wage, and no more than 20% of the work for Spanish clients",
                    src="Digital Nomad Visa income 2026 – Migratiolex", url="https://migratiolex.com/spain-digital-nomad-visa-minimum-income-requirement-for-2026/", checked="2026-11-16", volatile=True),
    "nlv_income": dict(text="€28,800 a year for the main applicant in 2026, which is 400% of the IPREM index, plus €7,200 for each family member, and you cannot work in Spain",
                    src="Non-Lucrative Visa 2026 – Pellicer & Heredia", url="https://www.pellicerheredia.com/residencia-no-lucrativa-espa%c3%b1a/", checked="2026-11-16", volatile=True),
    "whv": dict(text="up to 12 months of living and working in Spain (ages 18–30 for Australians and New Zealanders, 18–35 for Canadians)",
                    src="Working Holiday Visa Spain – Immigration Lawyers Spain", url="https://www.immigrationspain.es/en/working-holiday-visa-spain/", checked="2026-11-16", volatile=True),
    "uk_90_180": dict(text="UK passport holders can stay up to 90 days in any 180-day period in the Schengen area without a visa",
                    src="Brexit and Spain 2026 – CostaLuz Lawyers", url="https://www.costaluzlawyers.com/brexit-spain-guide-british-nationals/", checked="2026-11-16", volatile=True),
    "uk_s1": dict(text="UK State Pension recipients living in Spain may get Spanish state healthcare paid by the UK through an S1 form",
                    src="GOV.UK – Healthcare in Spain", url="https://gov.uk/healthcareinspain", checked="2026-11-16", volatile=True),
    "uk_pension_uprated": dict(text="the UK State Pension is paid in Spain and uprated every year",
                    src="Retiring in Spain from the UK – Novado", url="https://novado.es/en/guides/retiring-in-spain-from-uk/", checked="2026-11-16", volatile=True),
    # --- Home prices ---
    "price_villablino": dict(text="€539/m² (median, October 2026)", src="RealAdvisor – Villablino", url="https://realadvisor.es/es/precios-viviendas/municipio-villablino", checked="2026-11-16", volatile=True),
    "price_spain": dict(text="€2,512/m² (average, Q3 2026)", src="Colegio de Registradores – Estadística Registral Inmobiliaria Q3 2026, via Euronews", url="https://es.euronews.com/2026/11/06/compra-vivienda-extranjeros-marca-record-16-mientras-precio-alcanza-maximos-historicos", checked="2026-11-16", volatile=True),
    "price_uk": dict(text="£273,000 (UK average, August 2026)", src="ONS – Private rent and house prices, UK: October 2026", url="https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/privaterentandhousepricesuk/october2026", checked="2026-11-16", volatile=True),
    "rent_uk": dict(text="£1,406 a month (UK average private rent, September 2026)", src="ONS – Private rent and house prices, UK: October 2026", url="https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/privaterentandhousepricesuk/october2026", checked="2026-11-16", volatile=True),
    "price_us": dict(text="$416,700 (median existing-home price, October 2026)", src="National Association of Realtors", url="https://www.nar.realtor/newsroom/existing-home-sales-decreased-5-5-percent-october-nar-report", checked="2026-11-16", volatile=True),
    "price_ca": dict(text="C$666,538 (national average sale price, September 2026)", src="CREA via Advisor.ca", url="https://www.advisor.ca/economy/economic-indicators/crea-downgrades-home-sales-forecast-for-the-third-time-this-year/", checked="2026-11-16", volatile=True),
    "price_au": dict(text="A$884,855 (national median dwelling value, October 2026)", src="Cotality Home Value Index via OpenAgent", url="https://www.openagent.com.au/news/national-property-market-update-october-2026", checked="2026-11-16", volatile=True),
    "price_nz": dict(text="NZ$763,000 (national median price, October 2026)", src="REINZ via interest.co.nz", url="https://www.interest.co.nz/property/141065/reinz-october-housing-market-data-shows-24-drop-annual-nationwide-sales-volumes", checked="2026-11-16", volatile=True),
    # --- Villablino ---
    "vb_population": dict(text="7,585 residents (INE, 2025)", src="INE", url="https://www.ine.es/", checked="2026-11-16", volatile=False),
    "vb_unesco": dict(text="UNESCO Biosphere Reserve since 2003, about 23,000 hectares", src="MITECO – Valle de Laciana Biosphere Reserve", url="https://www.miteco.gob.es/es/parques-nacionales-oapn/reservas-biosfera-mab/programa-mab-espana/nuestras-reservas-de-la-biosfera/valledelaciana.html", checked="2026-11-16", volatile=False),
    "vb_altitude": dict(text="1,015 m", src="AEMET – Villablino", url="https://www.aemet.es/en/eltiempo/prediccion/municipios/villablino-id24202", checked="2026-11-16", volatile=False),
    # --- Ponferrada / El Bierzo ---
    "pf_population": dict(text="63,186 residents (INE, 2025)", src="Diario de León", url="https://www.diariodeleon.es/sociedad/251212/2069126/municipios-grandes-impulsan-poblacion-leon.html", checked="2026-11-16", volatile=False),
    "pf_castle": dict(text="the Knights Templar held the town until 1312, and the castle covers about 8,000 m²", src="Turismo Castilla y León / TerraNostrum", url="https://www.turismocastillayleon.com/es/arte-cultura-patrimonio/castillos/castillo-ponferrada", checked="2026-11-16", volatile=False),
    "pf_train": dict(text="direct trains to Madrid take around four hours", src="Railclick – Madrid to Ponferrada", url="https://railclick.com/es/train/madrid/ponferrada", checked="2026-11-16", volatile=True),
    "medulas": dict(text="UNESCO World Heritage Site since 1997 and the largest open-pit gold mine of the Roman Empire, about 25 km south-west of Ponferrada", src="Wikipedia / UNESCO", url="https://en.wikipedia.org/wiki/Las_M%C3%A9dulas", checked="2026-11-16", volatile=False),
    "somiedo": dict(text="an Asturian natural park and Biosphere Reserve (since 2000) of about 291 km², a stronghold of the Cantabrian brown bear, with guided bear-watching trips", src="MITECO – Somiedo Biosphere Reserve", url="https://www.miteco.gob.es/es/parques-nacionales-oapn/reservas-biosfera-mab/programa-mab-espana/nuestras-reservas-de-la-biosfera/somiedo.html", checked="2026-11-16", volatile=False),
    "vb_climate": dict(text="average highs of about 7°C in January and 28°C in July, with drier summers (approximate model averages)", src="WeatherAPI – Villablino climate", url="https://www.weatherapi.com/history/q/villablino-725979", checked="2026-11-16", volatile=False),
    # --- Castellón ---
    "cs_price_prov": dict(text="€1,521/m² (average, Q3 2026), the lowest of the three Valencian provinces, against €1,965 in Valencia and €2,403 in Alicante", src="Colegio de Registradores Q3 2026, via Alicante Plaza", url="https://alicanteplaza.es/alicanteplaza/plaza-inmobiliaria-alicante/alicante-registra-12111-compras-de-vivienda-en-el-tercer-trimestre-un-15-menos-y-los-precios-suben-un-6", checked="2026-11-16", volatile=True),
    "cs_price_city": dict(text="€1,423/m² (average, Q3 2026)", src="Tinsa – Castellón de la Plana", url="https://www.tinsa.es/precio-vivienda/comunitat-valenciana/castellon/castellon/", checked="2026-11-16", volatile=True),
    "cs_climate": dict(text="January highs of about 15°C, August highs of about 30°C and around 467 mm of rain in a normal year", src="AEMET – climate normals, Castellón-Almassora (1981–2010)", url="https://www.aemet.es/es/serviciosclimaticos/datosclimatologicos/valoresclimatologicos?l=8500A", checked="2026-11-16", volatile=False),
    "price_toronto": dict(text="C$1,024,108 (GTA average selling price, October 2026)", src="TRREB Market Watch", url="https://trreb.ca/wp-content/files/news_releases/news2026/nr_market_watch_1026.pdf", checked="2026-11-16", volatile=True),
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
