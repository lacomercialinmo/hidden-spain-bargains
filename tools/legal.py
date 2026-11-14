from sitedata import OWNER as O

LEGAL_NOTICE = f"""
<h2>Website owner</h2>
<p>In accordance with Spanish Law 34/2002 on Information Society Services (LSSI), the owner of this website is:</p>
<ul><li>Owner: {O['name']}, trading as {O['brand']}</li><li>Tax ID (NIF): {O['nif']}</li><li>Address: {O['address']}</li>
<li>Email: <a href="mailto:{O['email']}">{O['email']}</a></li><li>Phone / WhatsApp: {O['phone']}</li></ul>
<h2>Purpose of the website</h2>
<p>Hidden Spain Bargains provides information about living in Spain and a home-search service for buyers: we select homes, research the area and negotiate the price on the buyer's behalf. Property details are provided by the owners and may change.</p>
<h2>Information on this site</h2>
<p>We check legal, tax and market figures against the sources cited on each page and review them regularly, but the content is general information, not legal, tax or financial advice. Always confirm with a qualified professional before making decisions.</p>
<h2>Intellectual property</h2>
<p>The texts, design and our own photographs belong to the owner. Please do not reproduce them without permission. Third-party trademarks belong to their owners.</p>
<h2>Links</h2>
<p>We link to external sources so you can check our figures. We are not responsible for the content of external websites.</p>
<h2>Applicable law</h2>
<p>This website is governed by Spanish law.</p>
"""

PRIVACY = f"""
<h2>Who is responsible for your data</h2>
<p>{O['name']}, trading as {O['brand']}. NIF {O['nif']}. {O['address']}. Email: <a href="mailto:{O['email']}">{O['email']}</a>.</p>
<h2>What data we collect and why</h2>
<ul>
<li><b>Contact and search forms:</b> name, email, and optionally phone, country, budget and preferences. We use them only to answer you and to search for homes that fit what you asked for.</li>
<li><b>WhatsApp and phone:</b> if you contact us this way, we use your number and messages only to answer you.</li>
<li><b>Visit statistics:</b> we count page views with our own system. It records the page, the approximate country and city of the connection, the device type, the browser language and the website you came from. It does not store your IP address, does not use advertising cookies and does not identify you.</li>
</ul>
<h2>Legal basis</h2>
<p>Your consent when you send a form, and the steps you ask us to take before a possible contract (your home search). Statistics are based on our legitimate interest in knowing which pages are useful, and contain no personal data.</p>
<h2>How long we keep it</h2>
<p>While we are helping you with your search, and afterwards for the time required by law. You can ask us to delete it at any time.</p>
<h2>Who processes it</h2>
<p>Our website and forms are hosted by Netlify, Inc., which acts as a data processor and may process data outside the European Economic Area with the safeguards required by the GDPR. We do not sell or share your data with anyone else, and we do not pass it to sellers without your permission.</p>
<h2>Cookies</h2>
<p>This website does not use advertising cookies. Embedded Google Maps and YouTube videos come from Google and may set their own cookies when they load or you use them; YouTube runs in privacy-enhanced mode (youtube-nocookie.com).</p>
<h2>Your rights</h2>
<p>You can access, correct or delete your data, object to or restrict its use, and ask for portability by writing to <a href="mailto:{O['email']}">{O['email']}</a>. You can also complain to the Spanish Data Protection Agency (<a href="https://www.aepd.es" rel="noopener" target="_blank">www.aepd.es</a>).</p>
"""
