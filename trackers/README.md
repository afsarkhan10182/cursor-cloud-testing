# Trackers — Google Sheets setup

The salesperson lives in these sheets. WhatsApp is not a CRM.

## Create the workbook

1. Google Drive → New → Google Sheets → name it `Digital Fuzed — Sales OS (Month 1)`.
2. File → Import each CSV in this folder (create a new sheet tab per file).
3. Freeze row 1 on every tab.
4. Share: founders = editor, salesperson = editor, nobody else.

Suggested tabs:

- `Leads`
- `Activity`
- `Content`
- `Product scoreboard`
- `Weekly review log`
- `Month-end`
- `Dropdowns` (hide after setting data validation)

## Data validation (Leads tab)

| Column | List |
| --- | --- |
| Product | Salon, Restaurant, School, Hospital, Inventory, Textile, Real Estate |
| Lead Source | Google, Google Maps, LinkedIn, Instagram, Directory, Referral, Network, Community, Website, WhatsApp, Other |
| Contact Method | Call, WhatsApp, Email, LinkedIn, Instagram, In-person, Other |
| Status | New Lead, Contacted, Replied, Qualified, Demo Booked, Demo Completed, Proposal, Negotiation, Won, Lost |
| Outcome | Open, Won, Lost |
| Lost Reason | Too expensive, Already using competitor, Missing feature, No budget, Not decision maker, Not interested, Wants one-time purchase, Wants own server/domain, Needs customization, Follow-up later, Trust issue, No response, Support concern, Other |
| Qual | A, B, C, D |

## Conditional formatting

- Status `Won` → green
- Status `Lost` → grey
- Next Follow-Up date **before today** and Outcome `Open` → red (this is the most important rule)

## Formulas (Product scoreboard)

Assume Leads columns: B = Product, K = Status, R = Outcome, P = Proposal Amount.

Put products in A2:A8. Then:

```text
Leads        =COUNTIF(Leads!B:B, A2)
Responses    =COUNTIFS(Leads!B:B, A2, Leads!K:K, "<>New Lead", Leads!K:K, "<>Contacted")
Demos        =COUNTIFS(Leads!B:B, A2, Leads!K:K, "Demo Completed")
             +COUNTIFS(Leads!B:B, A2, Leads!K:K, "Proposal")
             +COUNTIFS(Leads!B:B, A2, Leads!K:K, "Negotiation")
             +COUNTIFS(Leads!B:B, A2, Leads!K:K, "Won")
Proposals    =COUNTIFS(Leads!B:B, A2, Leads!K:K, "Proposal")
             +COUNTIFS(Leads!B:B, A2, Leads!K:K, "Negotiation")
             +COUNTIFS(Leads!B:B, A2, Leads!K:K, "Won")
Sales        =COUNTIFS(Leads!B:B, A2, Leads!R:R, "Won")
Revenue      =SUMIFS(Leads!P:P, Leads!B:B, A2, Leads!R:R, "Won")
```

Simpler demo count if you prefer: `COUNTIF` on Demo Date not blank.

## Conversion rates

```text
Response rate = Responses / Contacts
Demo rate     = Demos / Responses
Proposal rate = Proposals / Demos
Close rate    = Sales / Demos
ARPU          = Revenue / Sales
CAC           = (retainer + incentives + tools this month) / Sales
```

Contacts = rows with First Contact Date filled.

## Hygiene rules

- New row **before** first outreach when possible; immediately after if you called from Maps on the street.
- Every Open row must have Next Follow-Up.
- Won/Lost must have Outcome. Lost must have Lost Reason.
- End of each day: one row on Activity.
- End of each week: one row on Weekly review log.
