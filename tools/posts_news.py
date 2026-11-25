"""News-led articles: a current story about north-west Spain, tied back to life in Villablino."""
from facts import F, Fc, src
from postlib import TOPICS, BASE_SOURCES

C = "all"

POSTS = [
dict(slug="jesus-calleja-favourite-mountain-pena-ubina", country=C, topic="life", img="nature", mins=4,
  kicker=TOPICS["life"], title="Everest Climber's Favourite Mountain Is Next Door to Villablino",
  h1="Jesús Calleja's favourite mountain is not in Alaska. It is Peña Ubiña",
  desc="Spanish adventurer Jesús Calleja, who has climbed Everest, says his favourite mountain is Peña Ubiña, between León and Asturias, close to Villablino.",
  lead=f"Jesús Calleja is Spain's best-known adventurer and TV explorer, and he has climbed Everest. Asked about his favourite mountain, he did not pick the Himalaya or Alaska. He picked Peña Ubiña ({F('ubina')}), on the border between León and Asturias.",
  body=f"""<div class="box"><p><b>The story:</b> on 24 November 2026 the Spanish newspaper OKDIARIO reported that Calleja calls Peña Ubiña his favourite mountain: "No es Alaska, mi montaña favorita es espectacular y maravillosa" ("It's not Alaska, my favourite mountain is spectacular and wonderful"). According to the report, it is where he started climbing as a young man, where his dream of the Himalaya began, and where he still returns after his big expeditions.</p></div>
<h2>Where Peña Ubiña is</h2>
<p>Peña Ubiña rises in the Cantabrian Mountains, on the watershed between León and Asturias. On the Asturian side it sits in the Las Ubiñas-La Mesa Natural Park, {F('ubinas_rb')}. On the León side, the classic climb starts in the village of Torrebarrio, in Babia, {F('babia_rb')}.</p>
<h2>Can you climb it?</h2>
<p>Yes, but it is a serious day out. The route from Torrebarrio is {F('ubina_route')}. In summer it has no technical sections, but in winter snow, ice and wind make it a mountaineering climb, so check the forecast and go with a guide if you are not experienced. If you just want the views, the walks through the valleys and high pastures below the peak are easy and beautiful.</p>
<h2>Why this matters if you are thinking of moving here</h2>
<p>Babia is the valley next to the Laciana Valley, where Villablino is. That puts one of Spain's most loved mountains a short drive from a real town with fibre internet, a health centre, schools and shops, where homes cost around {F('price_villablino')}. Brown bears, golden eagles, the ski slopes at Leitariegos and several Biosphere Reserves are all on the doorstep.</p>
<!--CLOSER-->""",
  faq=[("Who is Jesús Calleja?", "A Spanish mountaineer, adventurer and TV presenter from León who has climbed Everest and other 8,000 m peaks."),
       ("How high is Peña Ubiña?", Fc('ubina') + "."),
       ("Where do you start the climb?", "From Torrebarrio in Babia (León) or from Tuiza de Arriba in Lena (Asturias)."),
       ("How far is it from Villablino?", "Babia, where the León-side route starts, is the valley next to the Laciana Valley, so it is a short drive.")],
  sources=[("El refugio de Jesús Calleja – OKDIARIO, 24 November 2026", "https://okdiario.com/cool/famosos/refugio-jesus-calleja-61-anos-no-alaska-montana-favorita-espectacular-maravillosa-21262169")]
          + src("ubina", "ubina_route", "ubinas_rb", "babia_rb") + BASE_SOURCES),
]
