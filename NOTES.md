# Notes

Build notes for Intake Desk. Each entry is something I actually saw: a miss, a boundary, or a choice that would be easy to forget later.

The public write-up lives on [brianshimkus.com](https://www.brianshimkus.com). This file is the lab notebook.

## Day 1 setup notes

The API runs on Python 3.12 through uv. The system `python3` on this machine is 3.9, so `uv run` is the command that matters, not `python`.

The web app is Next.js 16 with the App Router, TypeScript, and Tailwind on. Day 1 does not use Tailwind. It stays because create-next-app puts it there, and because we can explain it: utility CSS for later layout, plus the tutorial's plain CSS when the queue exists.

`OPENAI_MODEL` is an environment variable, currently `gpt-6-astra`. The name will change. The product must not hard-code a model.

## Lakefront Legal is a general practice

The published case study called it an employment office. The sample inquiries and seeded CRM contacts are employment, family, business, estate, and real estate. A five-person employment firm would not usually take all of those, and a hiring manager would notice. Version one treats Lakefront Legal as a small Chicago general practice so the demo, the eval, and the story match.

## Blog titles

Do not number posts as Day 1, Day 2, and so on. The title is a catchy claim a stranger would click. The series still groups as Intake Desk. Previous / next can follow publish date. Cards for this series show `Intake Desk`, not `Intake Desk · Day N`.

First post: [I built the empty office first](https://www.brianshimkus.com/blog/intake-desk-empty-office).

## Seed data is not ORM rows

The three fictional existing clients are stored as dictionaries. `seed_demo_crm` builds a new `DemoContact` only when it inserts. If those were live SQLModel objects at import time, the test database and the app database would fight over the same Python object.

## Day 1 discussion
1. **Why is the model name configuration, not a string in main.py?**
Model name, not mode name. `EXTRACTION_MODE` is fake vs openai. `OPENAI_MODEL` is which model OpenAI actually runs. Those names change (`gpt-4o`, whatever ships next). If the ID lives in main.py, every swap is a code change and the eval report cannot say which model produced the numbers. An env var keeps that outside the app.

2. **Why will production reject arbitrary pasted text?**
Real legal info is the main reason. The other reason is money: a public text box is an open tab on your OpenAI bill. Server-owned scenarios cap both.

3. **What does CORS protect, and what does it not protect?**
CORS is a browser rule, not a lock on the API. It tells the visitor’s browser: “only pages from http://localhost:3000 may read this response.” That stops a random website from using someone’s browser as a middleman.

## Day 2 discussion
1. **Why is a possible name match not a definitive conflict?**
The match is not “two law firms with the same name.” It is “the other party in this inquiry has the same name as someone already in Lakefront Legal’s files.”

Northstar is already a client. A new message says the dispute is with Northstar. That might be a real problem (you cannot represent both sides), or it might be a different company, a typo, or an old name. Exact name matching cannot tell those apart, and a conflict check is a legal conclusion this product is not allowed to make. So the system only says possible, and a person looks.

Same name and different email is one reason a match can be wrong. It is not the only reason, and email is not how version one compares.

2. **Why is the original source stored separately from `final_record`?**
Approval is not the reason they are separate. They stay separate after approval too.
> `raw_text` is what the person wrote. It never changes.
> `extraction` is the model’s draft. It can be wrong.
> `final_record` is what the reviewer saved. They may have edited it.
If you overwrite the original with the approved form, you can no longer prove a quote was in the message, and you cannot see what the prospect said versus what the firm stored.

3. **Why must a seed function be idempotent?**
“So it can seed twice” is the behavior, not the reason.

The API process starts over and over: every time you run `fastapi dev`, every reload, every deploy, every test. Without the early return, each start would insert another Northstar, Evelyn, and Apex. The demo CRM would fill with duplicates, and “three existing clients” would be a lie.

Idempotent here means: first start creates three rows. Every later start sees they exist and stops.
