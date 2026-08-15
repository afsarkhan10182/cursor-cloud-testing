#!/usr/bin/env python3
"""Generate static product landing pages. Run from repo root: python3 website/generate.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

PAGES = [
    {
        "file": "salon.html",
        "nav": "Salon",
        "kicker": "Salon management",
        "h1": "Stop running the salon from a diary and WhatsApp.",
        "lede": "Appointments clash, commissions are guesswork, and product stock disappears. Digital Fuzed puts bookings, billing, staff and inventory in one place.",
        "software": "Software for salon and spa owners who need the floor to run when they are with a client — not a custom IT project.",
        "features": [
            ("Appointments", "Book, move, and avoid double-booking without a paper diary."),
            ("Billing", "Services and retail products on one invoice."),
            ("Staff", "See who did the work. Keep commission simple."),
            ("Inventory", "Colours, creams, and retail — know what is left."),
            ("Client history", "Last visit, preferred service, notes."),
            ("Packages", "Memberships and packages if you sell them."),
        ],
        "demo": "We demonstrate the live product, not a slide deck. If your build is on a private URL, the founder joins the first demos.",
        "demo_url": None,
    },
    {
        "file": "restaurant.html",
        "nav": "Restaurant",
        "kicker": "Restaurant management",
        "h1": "Orders should not get lost between the table and the kitchen.",
        "lede": "Digital Fuzed Restaurant POS handles tables, KOT, QR menus and payments so you are not reconciling shouting with a cash drawer.",
        "software": "Built for independent restaurants, cafes, QSR and small groups — not a hotel chain RFP.",
        "features": [
            ("KOT", "Kitchen tickets from the order, not from memory."),
            ("Tables", "Floor plan, seating, and reservations."),
            ("QR menu", "Guests order without reprinting a board every week."),
            ("Payments", "Gateway-ready billing (Razorpay / Stripe style)."),
            ("Menu", "Change rates without a printer fight."),
            ("Owner view", "What sold today, not next week in Excel."),
        ],
        "demo": "Live product:",
        "demo_url": "https://restaurant.digitalfuzed.com",
    },
    {
        "file": "school-erp.html",
        "nav": "School ERP",
        "kicker": "School ERP",
        "h1": "Fees, attendance and parents should not live in Excel.",
        "lede": "Digital Fuzed School ERP helps private schools and coaching institutes collect fees, mark attendance, and update parents without a Sunday spreadsheet.",
        "software": "For principals and office staff. Not a university tender pack.",
        "features": [
            ("Attendance", "Mark a class; parents can actually see it."),
            ("Fees", "Pending list and SMS reminders instead of chasing."),
            ("Parent portal", "Live updates instead of rumours."),
            ("Report cards", "Digital cards, less printing panic."),
            ("Staff", "Payroll and leave when you need it."),
            ("Records", "One student file, not five registers."),
        ],
        "demo": "Live product:",
        "demo_url": "https://school.digitalfuzed.com",
    },
    {
        "file": "hospital.html",
        "nav": "Hospital",
        "kicker": "Hospital management",
        "h1": "A queue should be a list, not a crowd in the lobby.",
        "lede": "Digital Fuzed Hospital Management helps clinics and small hospitals move patients, billing, pharmacy and doctor schedules without hunting for files.",
        "software": "For owners and admins of clinics, nursing homes, and compact hospitals.",
        "features": [
            ("Queue", "Tokens and flow instead of lobby chaos."),
            ("Appointments", "Doctor schedule that staff can trust."),
            ("Billing", "Charge the visit without a missing file."),
            ("Pharmacy", "Stock alerts before the shelf is empty."),
            ("Insurance", "Track claims instead of a pile of papers."),
            ("Owner reports", "Today’s OPD and collection, plainly."),
        ],
        "demo": "Live product:",
        "demo_url": "https://hospital.digitalfuzed.com",
    },
    {
        "file": "inventory.html",
        "nav": "Inventory",
        "kicker": "Inventory management",
        "h1": "Know what is in stock before the customer is at the counter.",
        "lede": "Digital Fuzed Inventory replaces notebooks, WhatsApp photos, and month-end Excel for shops and small trading businesses.",
        "software": "For SME retail and distribution. Not SAP.",
        "features": [
            ("Items", "A master list with units and prices."),
            ("Stock in/out", "Purchases and sales that match the shelf."),
            ("Alerts", "Low stock before it is an embarrassment."),
            ("Bills", "Simple purchase and sales documents."),
            ("Slow movers", "See what is not selling."),
            ("Owner view", "A week of movement without a fight."),
        ],
        "demo": "Book a demo with the founder until the public demo environment is complete. Do not send buyers to a placeholder page.",
        "demo_url": None,
    },
    {
        "file": "textile.html",
        "nav": "Textile",
        "kicker": "Textile software",
        "h1": "Lots, job work and billing should not live in three registers.",
        "lede": "Digital Fuzed Textile is for traders, job-work units and small manufacturers who need to answer “where is this lot?” without a phone tree.",
        "software": "We map the demo to your register columns. We do not pretend you are a grocery shop.",
        "features": [
            ("Orders", "What was promised, to whom."),
            ("Lots", "Identify goods the way you already do."),
            ("Job work", "Issued vs received."),
            ("Stock", "Position by the units you actually use."),
            ("Billing", "Invoices and outstanding."),
            ("Owner view", "Open orders instead of night-time Excel."),
        ],
        "demo": "Demo is scheduled with a founder until a public subdomain is ready. Do not book a tour you cannot run.",
        "demo_url": None,
    },
    {
        "file": "real-estate.html",
        "nav": "Real estate",
        "kicker": "Real-estate management",
        "h1": "Leads should not die in a WhatsApp archive.",
        "lede": "Digital Fuzed Real Estate CRM helps brokers, small builders and agencies follow properties, site visits and clients as a team.",
        "software": "For local agencies and builders. Not a national portal.",
        "features": [
            ("Inventory", "Units and properties in one list."),
            ("Leads", "Capture and assign instead of forwarding chats."),
            ("Site visits", "Scheduled, not remembered."),
            ("Follow-up", "Reminders when a lead goes quiet."),
            ("Pipeline", "Enquiry to close, visible to the owner."),
            ("Team view", "What each person actually did."),
        ],
        "demo": "Live product:",
        "demo_url": "https://realestate.digitalfuzed.com",
    },
]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Digital Fuzed</title>
  <meta name="description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,650&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="wrap">
    <nav class="nav">
      <a class="brand" href="index.html">Digital Fuzed</a>
      <a class="nav-cta" href="https://wa.me/918459148396">WhatsApp +91 8459148396</a>
    </nav>
"""

FOOT = """
    <footer>
      <p>Digital Fuzed · Mumbai · info@digitalfuzed.com · +91 8459148396</p>
      <p class="products">{links}</p>
    </footer>
  </div>
</body>
</html>
"""

CTA = """
    <section class="cta-band" id="demo">
      <h2>Book a free demo / Contact us for pricing</h2>
      <p>We show the actual software. We quote after we understand your workflow — monthly, annual, or your own server.</p>
      <div class="actions">
        <a class="btn btn-primary" href="https://wa.me/918459148396?text=I%20want%20a%20demo%20of%20{nav}">WhatsApp to book a demo</a>
        <a class="btn btn-ghost" href="mailto:info@digitalfuzed.com?subject=Demo%20{nav}">Email info@digitalfuzed.com</a>
      </div>
    </section>
"""


def features(items):
    cards = "\n".join(
        f'<article class="card"><h3>{t}</h3><p>{d}</p></article>' for t, d in items
    )
    return f'<section><h2>Key features</h2><div class="grid">{cards}</div></section>'


def page(p, links):
    demo = p["demo"]
    if p["demo_url"]:
        demo_html = f'<p>{demo} <a href="{p["demo_url"]}">{p["demo_url"]}</a></p>'
    else:
        demo_html = f"<p>{demo}</p>"
    body = f"""
    <header class="hero">
      <p class="kicker">{p['kicker']}</p>
      <h1>{p['h1']}</h1>
      <p class="lede">{p['lede']}</p>
      <div class="actions">
        <a class="btn btn-primary" href="#demo">Book a free demo / Contact us for pricing</a>
        <a class="btn btn-ghost" href="https://wa.me/918459148396">WhatsApp</a>
      </div>
    </header>
    <section>
      <h2>The software</h2>
      <p>{p['software']}</p>
    </section>
    {features(p['features'])}
    <section>
      <h2>See it</h2>
      {demo_html}
      <div class="shot">Screenshot / 60-second demo video goes here.<br>Record the real product. Do not use stock office photos.</div>
    </section>
    {CTA.format(nav=p['nav'].replace(' ', '%20'))}
"""
    title = f"{p['nav']} software"
    html = HEAD.format(title=title, desc=p["lede"]) + body + FOOT.format(links=links)
    (ROOT / p["file"]).write_text(html, encoding="utf-8")


def index(links):
    items = []
    for p in PAGES:
        items.append(
            f'<a href="{p["file"]}"><strong>{p["nav"]}</strong><span>{p["h1"]}</span></a>'
        )
    body = f"""
    <header class="hero">
      <p class="kicker">Product pages</p>
      <h1>One page per product. Not “we build everything.”</h1>
      <p class="lede">Internal preview. Publish each file to its own URL. CTA is the same on every page.</p>
    </header>
    <div class="index-list">{''.join(items)}</div>
"""
    html = HEAD.format(title="Product pages", desc="Digital Fuzed product page drafts") + body + FOOT.format(links=links)
    (ROOT / "index.html").write_text(html, encoding="utf-8")


def main():
    links = " · ".join(f'<a href="{p["file"]}">{p["nav"]}</a>' for p in PAGES)
    for p in PAGES:
        page(p, links)
    index(links)
    print(f"Wrote {len(PAGES) + 1} HTML files in {ROOT}")


if __name__ == "__main__":
    main()
