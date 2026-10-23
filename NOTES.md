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

## Day 1 discussion
1. **Why is the model name configuration, not a string in main.py?**
Model name, not mode name. `EXTRACTION_MODE` is fake vs openai. `OPENAI_MODEL` is which model OpenAI actually runs. Those names change (`gpt-4o`, whatever ships next). If the ID lives in main.py, every swap is a code change and the eval report cannot say which model produced the numbers. An env var keeps that outside the app.

2. **Why will production reject arbitrary pasted text?**
Real legal info is the main reason. The other reason is money: a public text box is an open tab on your OpenAI bill. Server-owned scenarios cap both.

3. **What does CORS protect, and what does it not protect?**
CORS is a browser rule, not a lock on the API. It tells the visitor’s browser: “only pages from http://localhost:3000 may read this response.” That stops a random website from using someone’s browser as a middleman.
