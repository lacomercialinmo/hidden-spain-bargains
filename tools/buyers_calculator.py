"""Purchase cost calculator (lead magnet). Loaded by build.py through load("buyers_*.py")."""
from facts import F, Fc, src

# General ITP rate for resale homes under €250,000, by region (see facts.py for sources).
REGIONS = [
    ("Castile and León (León, Valladolid, Ávila, Palencia, Zamora, Soria, Burgos, Segovia)", 8),
    ("Madrid region", 6),
    ("Andalusia", 7),
    ("Galicia", 8),
    ("Asturias", 8),
    ("Extremadura", 8),
    ("Castilla-La Mancha", 9),
    ("Murcia", 7.75),
    ("Valencia region (Valencia, Alicante, Castellón)", 9),
]
RATES = {"GBP": 0.83559, "USD": 1.1052, "CAD": 1.5758, "AUD": 1.6288, "NZD": 1.9978}  # ECB reference rates, 13 Nov 2026

CALC = """
<style>
.calc{background:#fff;border:1px solid var(--line);border-left:4px solid var(--accent);padding:22px;margin:24px 0}
.calc label{display:block;font-size:14px;color:var(--muted);margin:12px 0 4px}
.calc input,.calc select{width:100%;font:inherit;font-size:16px;padding:10px 12px;border:1px solid #cfc6ba;border-radius:6px;background:#fff}
.calc .g{display:grid;grid-template-columns:1fr 1fr;gap:0 14px}
.calc table{margin-top:16px}.calc td:last-child{text-align:right;white-space:nowrap}
.calc .tot td{font-weight:700;border-top:2px solid var(--ink)}
@media(max-width:700px){.calc .g{grid-template-columns:1fr}}
.req{background:#fff;border:1px solid var(--line);border-left:4px solid var(--accent);padding:22px;margin:30px 0}
.req form{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
.req input,.req textarea{width:100%;font:inherit;font-size:16px;padding:10px 12px;border:1px solid #cfc6ba;border-radius:6px;background:#fff}
.req .full{grid-column:1/-1}@media(max-width:700px){.req form{grid-template-columns:1fr}}
</style>
<div class="calc" id="calc">
<div class="g">
<div><label for="cp">Price of the home (€)</label><input id="cp" type="number" min="5000" step="1000" value="60000" inputmode="numeric"></div>
<div><label for="cr">Region</label><select id="cr">%REGIONS%</select></div>
<div><label for="cl">Lawyer or gestoría, if you use one (€, optional)</label><input id="cl" type="number" min="0" step="100" value="0" inputmode="numeric"></div>
<div><label for="cc">Show totals in</label><select id="cc"><option value="GBP">British pounds (£)</option><option value="USD">US dollars (US$)</option><option value="CAD">Canadian dollars (C$)</option><option value="AUD">Australian dollars (A$)</option><option value="NZD">New Zealand dollars (NZ$)</option><option value="EUR">Euros only</option></select></div>
</div>
<table id="ct"></table>
<p style="font-size:13px;color:var(--muted)" id="cn"></p>
</div>
<script>(function(){
var R=%RATES%,S={GBP:"£",USD:"US$",CAD:"C$",AUD:"A$",NZD:"NZ$"},D="13 November 2026";
try{fetch("https://api.frankfurter.dev/v1/latest?base=EUR&symbols=GBP,USD,CAD,AUD,NZD").then(function(r){return r.json()}).then(function(j){if(j&&j.rates){R=j.rates;D=j.date;run()}}).catch(function(){})}catch(e){}
function eur(n){return "€"+Math.round(n).toLocaleString("en-GB")}
function fx(n,c){return c==="EUR"?"":" ("+S[c]+Math.round(n*R[c]).toLocaleString("en-GB")+")"}
function run(){var p=+document.getElementById("cp").value||0,r=+document.getElementById("cr").value,l=+document.getElementById("cl").value||0,c=document.getElementById("cc").value;
var itp=p*r/100,lo=p+itp+600+l,hi=p+itp+1500+l;
document.getElementById("ct").innerHTML="<tr><td>Price of the home</td><td>"+eur(p)+fx(p,c)+"</td></tr>"+
"<tr><td>Transfer tax (ITP, "+r+"%)</td><td>"+eur(itp)+fx(itp,c)+"</td></tr>"+
"<tr><td>Notary and land registry (estimate)</td><td>€600 – €1,500</td></tr>"+
(l?"<tr><td>Lawyer or gestoría</td><td>"+eur(l)+fx(l,c)+"</td></tr>":"")+
"<tr class=tot><td>Total to budget</td><td>"+eur(lo)+" – "+eur(hi)+(c==="EUR"?"":"<br><small>"+S[c]+Math.round(lo*R[c]).toLocaleString("en-GB")+" – "+S[c]+Math.round(hi*R[c]).toLocaleString("en-GB")+"</small>")+"</td></tr>";
document.getElementById("cn").textContent=(c==="EUR"?"":"Exchange rate: European Central Bank reference rate of "+D+". Your bank or transfer service will use its own rate. ")+"Resale homes under €250,000, general rate. Some buyers pay less (for example under-36s or large families) and new builds pay VAT instead.";
var h=document.getElementById("cf-sum");if(h)h.value=eur(p)+" | ITP "+r+"% | total "+eur(lo)+"-"+eur(hi)+" | "+c;}
["cp","cr","cl","cc"].forEach(function(i){document.getElementById(i).addEventListener("input",run)});run();
})();</script>
"""

FORM = """<div class="req" id="cost-check"><h2 style="font-family:var(--serif);font-weight:600;font-size:26px">Want the real figures for a specific home?</h2>
<p>Send us the town or the listing and we will check the real costs for that home: tax, notary, community fees and the yearly local tax, and whether the price can come down. Free, with no obligation.</p>
<form name="cost-check" method="POST" action="/thanks.html" data-netlify="true" netlify-honeypot="company">
<input type="hidden" name="form-name" value="cost-check"><input type="hidden" name="calculation" id="cf-sum"><p style="display:none"><label>Company <input name="company"></label></p>
<input name="name" placeholder="Name" aria-label="Name" required><input type="email" name="email" placeholder="Email" aria-label="Email" required>
<input name="country" placeholder="Your country" aria-label="Country"><input type="tel" name="phone" placeholder="Phone or WhatsApp (optional)" aria-label="Phone">
<textarea class="full" name="message" placeholder="Town, or a link to the home you like" aria-label="Town or link"></textarea>
<label class="full" style="font-size:13px;color:var(--muted)"><input type="checkbox" name="consent" value="yes" required style="width:auto"> I agree that my details are used to answer this request, as explained in the <a href="/privacy.html">privacy policy</a>.</label>
<button class="btn full" type="submit" style="font-size:16px;padding:13px">Check the costs for me</button></form></div>"""

def calc_html():
    import json
    regions = "".join(f'<option value="{r}">{n} – {r}%</option>' for n, r in REGIONS)
    return CALC.replace("%REGIONS%", regions).replace("%RATES%", json.dumps(RATES))

POSTS = [
dict(slug="purchase-cost-calculator", kicker="Buyers guide · Calculator", mins=2,
  title="Spain Home Purchase Cost Calculator, in Your Currency",
  h1="How much does it really cost to buy a home in Spain?",
  desc="Free calculator: price, transfer tax by region, notary and registry fees for a resale home in Spain, shown in pounds, dollars or euros.",
  lead=f"On a resale home in Spain you pay the price plus a regional transfer tax ({F('itp_regions')}) plus notary and land registry fees, {F('notary_registry')}. Enter a price below to see the total in your own currency.",
  body=calc_html() + f"""
<h2>What is included</h2>
<ul><li><b>Transfer tax (ITP):</b> paid by the buyer on resale homes. Each region sets its own rate; the calculator uses the general rate for homes under €250,000.</li>
<li><b>Notary and land registry:</b> regulated fees that depend on the price, {F('notary_registry')}.</li>
<li><b>Lawyer or gestoría:</b> optional, but most buyers from abroad use one. Ask for a written quote and add it above.</li></ul>
<h2>And our fee?</h2>
<p>If you use our personal shopper service, you only pay if you buy: <b>half of the saving we negotiate on the advertised price, VAT included, with a minimum of €605</b>. If we get a €60,000 flat down to €54,000, the price falls by €6,000, our fee is €3,000 and you are still €3,000 better off, even before tax: the transfer tax is also lower on the lower price. <a href="/buyers-guide/how-we-work.html">How our fee works</a>.</p>
<p>Not included: a mortgage (the bank pays most of its costs), moving, furniture and any work on the home. After you buy, you also pay a yearly local tax (IBI) and, if you live abroad, a yearly non-resident tax. <a href="/buyers-guide/buying-costs-and-taxes.html">See all the taxes explained</a>.</p>
{FORM}""",
  faq=[("How much tax do I pay to buy a resale home in Spain?", "A regional transfer tax: " + F('itp_regions') + " at the general rate, plus notary and registry fees."),
       ("Is the tax lower in the Madrid region?", "Yes. The general rate there is " + F('itp_madrid') + ", one of the lowest in Spain."),
       ("Which exchange rate does the calculator use?", "The European Central Bank reference rate of the day. Your bank or transfer service will use its own rate.")],
  sources=src("itp_regions", "itp_madrid", "itp_andalucia", "itp_valencia", "itp_cyl", "notary_registry", "ecb_rates")),
]
