"""Deep-research content per area guide (comité de research de municipios).
Every fact here has a source in research_areas.md / the 'sources' list. Restaurants and timetables change: say 'at the time of writing'.
Keys: history, see[(title, text)], square, eat[(name, text)], calendar[(when, text)], food, outdoors, services,
      transport[(mode, text)], market, budgets[(budget, text)], downsides[], nearby[(place, text)], videos[(id, title)], faq[(q, a)], sources[(title, url)]
"""

EXTRA = {
"medina-del-campo": dict(
    history=("Medina del Campo grew up in the 11th century on the <em>mota</em>, the low hill where the castle stands today. "
             "From the 15th century its two great fairs a year drew merchants and bankers from all over Europe, and much of the "
             "trade and credit of the time was agreed under the arcades of its main square. Ferdinand and Isabella used the town as "
             "one of their favourite residences, and Queen Isabella I signed her will and died here in 1504. Today it is a working town "
             "of about 20,000 people that lives from trade, farming and furniture making, which is why it is also called the City of Furniture."),
    see=[
        ("Castillo de la Mota", "A huge red-brick fortress commissioned in the mid-15th century by Juan II and Enrique IV, later a royal archive and a state prison. "
         "The guided visit (about 1 hour, €5) takes you along the walls, the underground firing gallery, the parade ground and the chapel; the 40 m keep is a separate 50-minute visit (€5, or €9 for both). "
         "Some weekends there are theatre-style tours (€8, booking needed)."),
        ("Plaza Mayor de la Hispanidad", "Built for the fairs, it is one of the largest main squares in Spain, about one and a half hectares. "
         "Around it stand the Collegiate Church of San Antolín, the town hall, the Casa de los Arcos and the 17th-century Casa del Peso, which is the tourist office (Plaza Mayor 48)."),
        ("Collegiate Church of San Antolín", "Founded in 1177 and rebuilt over the centuries. Look for the Balcón del Pópulo, an outdoor balcony from which Mass was said for the crowds at the fair, and go up the tower on a guided visit."),
        ("Palacio Real Testamentario", "The royal palace on the main square where Isabella I signed her will and died in 1504, now a museum about her life and reign."),
        ("Museo de las Ferias", "A museum unique in Spain about the fairs that made Medina one of the trading centres of Europe in the 15th and 16th centuries: coins, scales, account books and letters of exchange."),
        ("Reales Carnicerías", "The old royal meat market, a long arcaded building used today for exhibitions and as a stage during the Renaissance Week."),
        ("Saint Teresa and Saint John of the Cross", "Saint Teresa of Ávila founded her second convent here in 1567, and it was in Medina that she met the young Saint John of the Cross. "
         "Near the main square stands the chapel of San Juan de la Cruz, where he is said to have said his first Mass."),
        ("Palacio de las Salinas spa", "Four kilometres out of town, a palace-style spa hotel built in 1912 by the team behind the Magdalena Palace in Santander. Its mineral waters were declared of public benefit in 1893. It is the only spa in the province and is open to non-residents."),
        ("Sunday market", "Every Sunday from 9:00 to 14:00, about 200 stalls fill calle José Zorrilla: fruit, clothes, cooked food and household goods. It is one of the largest weekly markets in Castile and León. Go early: after 12:00 the aisles get crowded."),
    ],
    square=("The Plaza Mayor is where Medina lives. People meet for a <em>vino</em> before lunch and again in the evening, and the square fills with terraces in good weather. "
            "Every bar is known for something: mussels at Alegría, prawns and <em>tigres</em> (stuffed mussels) at El Casino, prawns at Mónaco 1962. "
            "A small tip from visitors: on Thursdays many bars close, so check before you go."),
    eat=[
        ("Mónaco 1962 (Plaza Mayor)", "Home cooking and one of the best-rated places in town; a weekday set menu of about €17 with four or five choices per course."),
        ("Bar Casino (Plaza Mayor)", "Popular for its low prices, prawns and stuffed mussels."),
        ("Alegría (Plaza Mayor)", "Sharing plates and mussels on a terrace facing the square."),
        ("Gloria (Plaza Mayor)", "Castilian dishes with some modern touches, in two dining rooms."),
        ("Tapería La Plaza", "Creative tapas based on seasonal and Mediterranean produce."),
        ("Mesón La Plaza", "In the cellar of the Casa del Peso, open for more than 50 years."),
        ("El Mortero", "Toasts with local ingredients, and roast suckling pig."),
        ("Taberna Mohíno", "Large and busy; known for its <em>cocido</em> (chickpea stew) on the set menu."),
    ],
    calendar=[
        ("Every Sunday", "Big street market on calle José Zorrilla, 9:00–14:00."),
        ("March or April", "Holy Week, declared of International Tourist Interest. Its processions of discipline go back to 1411 and are considered the oldest in Spain; 17 processions, and the Miserere sung in the Plaza Mayor. In 2026 it ran from 27 March to 5 April."),
        ("Early May", "D.O. Rueda Wine Fair in the Plaza Mayor, with more than 20 wineries, tastings and local food, followed by the Spring Fair (8–10 May in 2026)."),
        ("August", "Renaissance Week and the Imperiales y Comuneros Fair: a 16th-century market with around 200 stalls, thousands of people in period dress, camps, concerts and the re-enactment of the burning of Medina in 1520. In 2026: 18–21 August."),
        ("September", "Ferias y Fiestas de San Antolín, the town's main festival, with traditional bull runs declared of Regional Tourist Interest."),
    ],
    food=("The classic meal is <em>lechazo</em>, milk-fed lamb roasted in a wood oven, with a white wine from the D.O. Rueda, whose vineyards start at the edge of town. "
          "Also look for Castilian <em>cocido</em>, garlic soup and game, and for dessert the local <em>cocadas</em>, small coconut sweets."),
    outdoors=("The land around Medina is a flat plain of cereal fields, pine woods and vineyards, crossed by the river Zapardiel. It is easy cycling country: "
              "a 32 km loop runs through the villages of Moraleja de las Panaderas and Gomeznarro, and an 83 km 'Route of the Castles' links Medina, Íscar and Olmedo. "
              "For a river landscape, the Riberas de Castronuño–Vega del Duero nature reserve is a short drive north."),
    services=("Hospital de Medina del Campo (calle Peñaranda 24) serves more than 53,000 people in the south of the province, with A&amp;E, paediatrics, obstetrics, cardiology, "
              "trauma, ophthalmology and other specialities, and works with the Hospital Clínico Universitario in Valladolid. There are two health centres (Medina urbano and Medina rural). "
              "Sport: the Pablo Cáceres sports centre and the municipal stadium. The population was 20,314 at the 2021 census; about 29% are over 60."),
    transport=[
        ("Train to Madrid", "About 12 direct trains a day (AVE, Alvia, Avlo and regional), from roughly 55 minutes to Madrid Chamartín; tickets from about €12. Slower regional trains go to Príncipe Pío in about 2 h 20."),
        ("Train to Valladolid", "Around 28 trains a day, 25–35 minutes, from about €4. Easy for a daily commute."),
        ("Train to Salamanca", "About 7 direct trains a day, 40–45 minutes, from about €5."),
        ("Stations", "The classic station is about 700 m from the centre; high-speed trains also stop at Medina del Campo AV."),
        ("Bus", "About 8 buses a day to Valladolid (La Regional, about 40 minutes, from €5; first around 7:00, last around 21:15). "
         "To Madrid, 4–8 a day with Monbus and others (about 2 hours, from €12), from calle Ronda Gracia Plazuela. Buses also go to Lugo and Galicia (Alsa)."),
        ("Road", "On the A-6 Madrid–A Coruña motorway, exits 156, 157, 160 and 161. Madrid is about 140–160 km away: the A-6 is toll-free from Medina to Adanero, then the AP-6 toll section crosses the Guadarrama mountains. "
         "Valladolid is 47 km by the old road or 53 km by motorway via Tordesillas (35–40 minutes); the A-62 to Salamanca and Burgos starts 25 km north at Tordesillas."),
        ("Airports", "Valladolid–Villanubla is about 49 km away and Salamanca–Matacán about 60 km. For most international flights, Madrid-Barajas is reached by train via Chamartín."),
        ("Six capitals within 100 km", "Valladolid, Salamanca, Zamora, Ávila, Segovia and Palencia are all under 100 km away."),
    ],
    market=("In October 2026 the average asking price in Medina del Campo was €1,102 per m² (flats €1,137, houses €1,001), "
            "up 12.2% in a year and 28% in three years (RealAdvisor). Another portal, Indomio, gave €898 per m² in July 2026, up 11.3%. "
            "Typical prices by size: a studio from about €67,000, a 2-bedroom flat €72,000–108,000, a 3-bedroom flat €90,000–135,000 and a 4-bedroom flat €120,000–180,000. "
            "The villages within the municipality are cheaper (around €878 per m² for flats in postcode 47492). "
            "Rents: a median of about €784 a month for a flat on RealAdvisor, while Indomio puts asking rents at €3.90 per m² a month; gross yields therefore range from roughly 5% to 8% depending on the source and the property."),
    budgets=[
        ("€60,000–75,000", "A studio or a small flat to update, or a village house in one of the outlying hamlets."),
        ("€100,000", "A 2–3 bedroom flat in town, walking distance to the station and the main square."),
        ("€150,000", "A large 4-bedroom flat or a house with some outdoor space."),
    ],
    downsides=["A continental climate: cold, foggy winters and hot, dry summers. You will want good heating.",
               "Midweek the centre can be quiet, and many bars close on Thursdays.",
               "Prices have risen fast (about 12% in a year), so negotiation matters more than it did.",
               "Outside the tourist sites, expect to need some Spanish for daily life."],
    nearby=[("Rueda (about 12 km)", "The capital of Rueda white wine, with wineries to visit and a fine baroque church."),
            ("Tordesillas (about 25 km)", "Where the Treaty of Tordesillas was signed in 1494; Royal Monastery of Santa Clara and a medieval bridge over the Duero."),
            ("Olmedo (about 25 km)", "Mudéjar churches, a thermal spa and a park of scale models of Mudéjar monuments, good with children."),
            ("Coca (about 40 km)", "Coca Castle, often called the most impressive Mudéjar building in Spain."),
            ("Valladolid (about 50 km)", "A city of 300,000 with shopping, culture and the regional university hospital, 25 minutes by train."),
            ("Salamanca (about 80 km)", "One of Spain's most beautiful cities, 40 minutes by train.")],
    videos=[("gaPa8yrN9q4", "Castillo de la Mota, Spain (aerial, 8K)"),
            ("o452VSjJDGI", "Medina del Campo: castle, collegiate church, palace and main square")],
    faq=[("How long is the train from Medina del Campo to Madrid?", "The fastest trains take about 55 minutes to Madrid Chamartín, with around 12 direct trains a day; tickets start at about €12."),
         ("Is there a hospital in Medina del Campo?", "Yes. The Hospital de Medina del Campo has A&amp;E and the main specialities and serves more than 53,000 people; the university hospital in Valladolid is 25 minutes away by train."),
         ("Can I live in Medina del Campo without a car?", "In town, yes: the centre, the station, the hospital and the shops are close together, and there are frequent trains to Valladolid, Madrid and Salamanca. A car helps for the villages and wineries around."),
         ("What is there to do in the evening?", "Life centres on the Plaza Mayor: terraces, tapas bars and restaurants, with special evenings during Holy Week, the May wine fair, the Renaissance Week in August and the San Antolín fiestas in September."),
         ("What does a flat cost in Medina del Campo?", None),
         ("What rental return can I expect?", "Gross yields range roughly from 5% to 8% depending on the property and the source, with a median flat rent of about €784 a month on RealAdvisor (October 2026).")],
    sources=[("Turismo Castilla y León – Medina del Campo", "https://www.turismocastillayleon.com/es/patrimonio-cultura/medina-campo"),
             ("Turismo Castilla y León – Plaza Mayor", "https://www.turismocastillayleon.com/es/patrimonio-cultura/plazas-mayores/plaza-mayor-medina-campo"),
             ("Spain.info – Holy Week in Medina del Campo", "https://www.spain.info/es/agenda/semana-santa-medina-campo"),
             ("Terranostrum – Castillo de la Mota visit and prices", "https://www.terranostrum.es/actividades/visita-guiada-castillo-de-la-mota"),
             ("Terranostrum – What to see in Medina del Campo", "https://www.terranostrum.es/turismo/ruta-medina-del-campo-y-alrededores"),
             ("Sacyl – Hospital de Medina del Campo", "https://www.saludcastillayleon.es/HMedinaCampo/en/area-influencia"),
             ("Festivales de España – Imperiales y Comuneros 2026", "https://www.festivalesdeespana.com/festival/feria-renacentista-imperiales-y-comuneros-medina-del-campo"),
             ("Mercadillos.org – Sunday market", "https://mercadillos.org/mercadillo-medina-del-campo"),
             ("Fascinating Spain – Eating in Medina del Campo", "https://www.fascinatingspain.com/articulo/where-to-eat-in-castile-and-leon/where-to-eat-in-medina-del-campo/20170523212121068967.html"),
             ("Gastroranking – restaurants in Medina del Campo", "https://gastroranking.es/restaurantes/valladolid/medina-del-campo"),
             ("Omio – trains from Medina del Campo (timetables are indicative)", "https://www.omio.es/trenes/medina-del-campo"),
             ("Omio – buses from Medina del Campo (indicative)", "https://www.omio.es/autobuses/medina-del-campo"),
             ("Indomio – Valladolid province market", "https://www.indomio.es/mercado-inmobiliario/castilla-y-leon/valladolid-provincia/"),
             ("RealAdvisor – Medina del Campo villages (47492)", "https://realadvisor.es/es/precios-viviendas/47492-medina-del-campo")],
),
"medina-de-rioseco": dict(
    history=("Medina de Rioseco is called the City of the Admirals: from the 15th century it belonged to the Enríquez family, Admirals of Castile, and its merchants grew rich enough to fill a town of a few thousand people with four huge churches. "
             "In the 18th century it became the end of the Canal de Castilla, the great engineering project of the Spanish Enlightenment, built to carry the wheat of Tierra de Campos towards the sea. "
             "In 1808 a battle of the Peninsular War was fought here; the French victory opened the road to Madrid for Joseph Bonaparte. The old town has been a protected historic ensemble since 1965. "
             "About 4,600 people live here today, and around 4,300 of them belong to one of its Holy Week brotherhoods."),
    see=[
        ("Rúa Mayor", "The backbone of the old town: a long street lined with wooden porticoes held up by stone and timber columns, with traditional family shops, bakeries and bars underneath. It is the best place to start, and the stage of the Holy Week processions."),
        ("Santa María de Mediavilla", "The largest of the 'four cathedrals', a late Gothic church with Renaissance spirit. Inside, the Benavente chapel is one of the jewels of the Spanish Renaissance, with work by Juan de Juni."),
        ("Santiago and Santa Cruz", "Santiago is the other great hall church of the town. Santa Cruz, a 16th-century church on the Rúa Mayor with a sober Herrerian façade, is now the Holy Week Museum, where you can see the processional floats up close all year."),
        ("Museo de San Francisco", "A former convent turned museum, with terracotta sculptures by Juan de Juni and an outstanding collection of 17th-century Hispano-Filipino ivories."),
        ("Capilla de los Pasos Grandes", "The museum that keeps the two giant floats of the Crucifixion and the Descent from the Cross, known in town as 'El Longinos' and 'La Escalera'."),
        ("Canal de Castilla dock", "Medina de Rioseco is where the Campos branch of the canal ends, in a large dock surrounded by old warehouses. Walk or cycle the towpath, and take the tourist boat 'Antonio de Ulloa', which runs along the canal between the dock and the sixth lock near Tamariz de Campos."),
        ("San Antonio flour mill", "Beside the dock, a 19th-century flour mill turned museum, with its turbines and machinery: a real witness of the industrial revolution the canal brought to the area."),
        ("Teatro Principal and El Torno", "Two civil buildings worth a look: the town theatre, and El Torno, the old public granary of the Admirals."),
    ],
    square=("Life in Medina de Rioseco happens under the porticoes of the Rúa Mayor and in the tapas area of calle Lázaro Alonso and the Plaza de Santo Domingo. "
            "It is a small, friendly town where the barman soon knows your order, and where an aperitif with a tapa is part of the daily routine. "
            "Do not leave without visiting a cake shop: bollos de baño and bollos de aceite, pelusas, marinas, abisinios and tortas de chicharrón are local specialities."),
    eat=[
        ("La Rúa (calle San Juan)", "A classic in town: restaurant since 1988, in a family business that started as a tavern in 1972. Traditional seasonal cooking; a weekday set menu of about €13."),
        ("El Rincón de Unamuno", "A popular bar with a terrace and well-known croquetas, prawns, tortilla and pinchos."),
        ("España", "A charming bar for a drink, with tapas of egg and black pudding."),
        ("Pasos", "A restaurant with medieval-style décor and a long menu of Castilian dishes."),
        ("La Era (Plaza Mayor 9)", "A restaurant right on the main square."),
        ("Casa Manolo", "One of the best-rated places in town, with more than 1,400 reviews."),
        ("Confitería Cubero", "Pastries and cakes, and a good stop for the local sweets."),
    ],
    calendar=[
        ("5 January", "The Three Kings arrive by boat, on the 'Antonio de Ulloa', to the canal dock: a parade declared of Tourist Interest of Castile and León."),
        ("March or April", "Holy Week, declared of International Tourist Interest (2009) and Intangible Heritage (BIC, 2019). Seventeen brotherhoods and more than twenty floats carved by 16th- and 17th-century masters are carried on shoulders through the narrow streets; the exit of El Longinos and La Escalera is the most famous moment. In 2026 it started on 27 March."),
        ("All year", "The tourist boat on the Canal de Castilla, the museums and the Holy Week Museum."),
    ],
    food=("The cooking is that of Tierra de Campos: roast suckling lamb, pulses, game, local cheeses and the wines of nearby Cigales and Toro. "
          "The sweet tradition is especially strong, with its bollos, pelusas, marinas and abisinios."),
    outdoors=("Medina de Rioseco sits on the wide, open plains of Tierra de Campos, at the foot of the Montes Torozos. The Canal de Castilla towpath is flat and perfect for walking and cycling, and the canal and its locks attract birds and anglers. "
              "Big skies, sunsets over the wheat fields and very little traffic."),
    services=("The health centre is on the Plaza Mayor and is being fully rebuilt with more than €5 million: the new building will have 14 consulting rooms, including one for paediatric nursing, and will serve about 6,600 people in the area. "
              "During the works, which started in July 2025 and last about 18 months, care continues in the Casino de Recreo. The nearest hospitals are in Valladolid, about 40 km away. "
              "The town belongs to the World Health Organization's network of age-friendly cities (since 2021); about 32% of residents are over 60."),
    transport=[
        ("Bus to Valladolid", "Around 17 buses a day (Linecar and Alsa), 20–40 minutes, from about €3. Some go to Valladolid airport. Buses leave from the bus station on calle La Estación."),
        ("Bus to León", "About 9 Alsa buses a day, from about €9.60; the first leaves around 1:30 and the last around 20:55."),
        ("Train", "There is no passenger railway in town. Valladolid, 40 km away, has fast trains to Madrid Chamartín in about an hour."),
        ("Road", "On the N-601 Valladolid–León road: Valladolid is about 40 km (about 30 minutes). The road is being upgraded to the A-60 motorway in stages; the Villanubla–Medina de Rioseco section has its environmental approval. The A-6 Madrid–A Coruña motorway is reached at exits 216–217 (Villardefrades, Medina de Rioseco)."),
        ("Airports", "Valladolid–Villanubla airport is on the N-601, between Medina de Rioseco and Valladolid. For most international flights, use Madrid-Barajas via the train from Valladolid."),
        ("Car", "Useful: with no train and a hospital 40 km away, most residents drive, although the buses to Valladolid are frequent."),
    ],
    market=("In October 2026 the average price in Medina de Rioseco was €969 per m² (flats €1,140, houses €645), with flats up 8.4% in a year and 27.4% in three years (RealAdvisor). "
            "Typical flat prices: a studio about €53,000, a 2-bedroom flat about €66,000, a 3-bedroom flat about €86,000 and a 4-bedroom flat about €114,000. "
            "Houses are larger and cheaper per square metre: village houses with big rooms and yards are common. "
            "This is a small market with few homes for sale at any one time, and the portals disagree (Indomio gave an asking price of €462 per m² in July 2026), so real comparables matter. "
            "Rental data for a town this size is thin; ask us for current rents before you plan an investment."),
    budgets=[
        ("€55,000–70,000", "A studio or a 2-bedroom flat, often to update."),
        ("€85,000–100,000", "A 3-bedroom flat in town, close to the Rúa Mayor and the bus station."),
        ("€110,000–150,000", "A large 4-bedroom flat, or a village house with outdoor space that may need work."),
    ],
    downsides=["No train: you depend on the bus or the car, although Valladolid is only 30 minutes away.",
               "No hospital in town; the nearest are in Valladolid, about 40 km away.",
               "Cold, foggy winters and hot summers on the open plain.",
               "A small town of about 4,600 people: quiet outside Holy Week and the summer.",
               "The health centre is being rebuilt until about 2027, with care in temporary premises."],
    nearby=[("Valladolid (about 40 km)", "Regional capital with shopping, culture, university hospitals and fast trains to Madrid."),
            ("Canal de Castilla and Tamariz de Campos", "Follow the Campos branch of the canal to its locks by boat, bike or on foot."),
            ("Urueña", "A walled hilltop village known as Spain's 'book town', with bookshops and wide views over Tierra de Campos."),
            ("Montes Torozos", "The plateau of oak woods and moors between Medina de Rioseco and Valladolid, good for walking and cycling."),
            ("León (about 100 km)", "Cathedral, Gaudí's Casa Botines and a lively tapas quarter, along the N-601.")],
    videos=[("lLIyzwIemfw", "What not to miss in Medina de Rioseco, the City of the Admirals"),
            ("b6PsboSPzGA", "Medina de Rioseco, Tierra de Campos (Valladolid)")],
    faq=[("How do I get from Medina de Rioseco to Valladolid?", "By bus (about 17 a day, 20–40 minutes, from about €3) or by car on the N-601 (about 40 km, 30 minutes)."),
         ("Is there a train station in Medina de Rioseco?", "No. The nearest station with fast trains is Valladolid, about 40 km away, with trains to Madrid in about an hour."),
         ("Is there a doctor in Medina de Rioseco?", "Yes. The health centre on the Plaza Mayor serves about 6,600 people and is being rebuilt with 14 consulting rooms; the nearest hospitals are in Valladolid."),
         ("When is the best time to visit?", "Holy Week, declared of International Tourist Interest, is the highlight of the year; 5 January is special too, when the Three Kings arrive by boat on the canal."),
         ("What does a flat cost in Medina de Rioseco?", None),
         ("Is Medina de Rioseco a good place to retire?", "For people who want a quiet, walkable historic town with a health centre, frequent buses to Valladolid and low prices, yes; it belongs to the WHO network of age-friendly cities. People who need a hospital nearby every week may prefer Valladolid or Medina del Campo.")],
    sources=[("Turismo Castilla y León – Holy Week in Medina de Rioseco", "https://www.turismocastillayleon.com/es/semanasanta/interes-turistico-internacional/semana-santa-medina-rioseco"),
             ("Turismo Castilla y León – Culture and traditions", "https://www.turismocastillayleon.com/es/patrimonio-cultura/medina-rioseco/cultura-tradiciones"),
             ("Terranostrum – What to see in Medina de Rioseco", "https://www.terranostrum.es/turismo/valladolid/ruta-medina-de-rioseco-y-alrededores"),
             ("El Español – Holy Week and brotherhoods (2025)", "https://elespanol.com/castilla-y-leon/region/valladolid/20250412/pueblo-medieval-cofrades-habitantes-famoso-semana-santa/1003743705340_0.html"),
             ("Sacyl – New health centre in Medina de Rioseco (2025)", "https://www.saludcastillayleon.es/HRHortega/es/actualidad/reforma-centro-salud-medina-rioseco-permitira-contar-consul"),
             ("WHO – Age-friendly world: Medina de Rioseco", "https://extranet.who.int/agefriendlyworld/network/medina-de-rioseco/"),
             ("Fascinating Spain – Eating in Medina de Rioseco", "https://www.fascinatingspain.com/articulo/where-to-eat-in-castile-and-leon/where-to-eat-in-medina-de-rioseco/20170523212122068966.html"),
             ("Gastroranking – restaurants in Medina de Rioseco", "https://gastroranking.es/restaurantes/valladolid/medina-de-rioseco/"),
             ("Omio – Medina de Rioseco to Valladolid (indicative)", "https://www.omio.es/viajes/medina-de-rioseco/valladolid"),
             ("Movelia – Medina de Rioseco to León bus (indicative)", "https://www.movelia.es/ca/node/2098"),
             ("BOE – A-60 motorway, Villanubla–Medina de Rioseco (2023)", "https://boe.gob.es/boe/dias/2023/07/15/pdfs/BOE-A-2023-16454.pdf"),
             ("Indomio – Valladolid province market", "https://www.indomio.es/mercado-inmobiliario/castilla-y-leon/valladolid-provincia/")],
),
}
