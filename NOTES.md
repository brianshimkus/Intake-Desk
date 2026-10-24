# Notes

Lab notebook for Intake Desk. Each entry is a miss, a boundary, or a choice that would be easy to forget later.

The public write-up lives on [brianshimkus.com](https://www.brianshimkus.com). Draft posts in chat first. Do not add files under `Brian-Shimkus-Portfolio` until they are ready to publish.

| | |
| --- | --- |
| [Decisions](#decisions) | Product and publishing rules |
| [Lab notes](#lab-notes) | What broke or surprised me while building |
| [Interview answers](#interview-answers) | Explain-it-back questions, tightened after discussion |

---

## Decisions

### Lakefront Legal is a general practice

The published case study called it an employment office. The sample inquiries and seeded CRM contacts span employment, family, business, estate, and real estate.

A five-person employment firm would not usually take all of those, and a hiring manager would notice.

> **Rule:** Version one treats Lakefront Legal as a small Chicago general practice so the demo, the eval, and the story match.

### Blog titles are claims, not session numbers

Do not number posts as Day 1, Day 2, and so on. The title is a catchy claim a stranger would click.

| Surface | How it reads |
| --- | --- |
| Series | Intake Desk |
| Card label | `Intake Desk`, not `Intake Desk · Day N` |
| Previous / next | Publish date |
| First post | [I built the empty office first](https://www.brianshimkus.com/blog/intake-desk-empty-office) |

---

## Lab notes

### `uv run` is the Python that matters

The API needs Python 3.12. The system `python3` on this machine is 3.9.

> **Rule:** Use `uv run`, not `python`.

### Tailwind is on, unused on purpose

The web app is Next.js 16 with the App Router, TypeScript, and Tailwind. The first page does not use Tailwind. It stays because `create-next-app` puts it there, and because it can be explained: utility CSS for later layout, plus plain CSS when the queue exists.

### The model name is configuration

`OPENAI_MODEL` is an environment variable, currently `gpt-6-astra`. The name will change.

> **Rule:** Do not hard-code a model in the app.

### Seed data is not ORM rows

The three fictional existing clients are stored as dictionaries. `seed_demo_crm` builds a new `DemoContact` only when it inserts.

If those were live SQLModel objects at import time, the test database and the app database would fight over the same Python object.

---

## Interview answers

### Why is the model name configuration, not a string in `main.py`?

**Model name, not mode name.**

| Variable | Meaning |
| --- | --- |
| `EXTRACTION_MODE` | `fake` vs `openai` |
| `OPENAI_MODEL` | Which model OpenAI actually runs |

Those model IDs change (`gpt-4o`, whatever ships next). If the ID lives in `main.py`, every swap is a code change, and the eval report cannot say which model produced the numbers.

> An env var keeps the model outside the app.

### Why will production reject arbitrary pasted text?

Two reasons:

1. **Safety.** A public text box would invite real legal information.
2. **Cost.** That same box is an open tab on the OpenAI bill.

Server-owned fictional scenarios cap both.

### What does CORS protect, and what does it not protect?

CORS is a **browser** rule, not a lock on the API. It tells the visitor’s browser: only pages from `http://localhost:3000` may *read* this response. That stops a random website from using someone’s browser as a middleman.

| CORS does | CORS does not |
| --- | --- |
| Limit which websites can read the response in a browser | Stop `curl`, Postman, or another server |
| | Identify a person (it is not a login) |
| | Replace `DEMO_MODE` or later server checks |

### Why is a possible name match not a definitive conflict?

The match is not “two law firms with the same name.” It is: **the other party in this inquiry has the same name as someone already in Lakefront Legal’s files.**

Northstar is already a client. A new message says the dispute is *with* Northstar. That might be a real problem (you cannot represent both sides), or it might be a different company, a typo, or an old name.

Exact name matching cannot tell those apart. A conflict check is a legal conclusion this product is not allowed to make.

> The system only says **possible**. A person looks.

Same name and different email is one reason a match can be wrong. It is not the only reason, and email is not how version one compares.

### Why is the original source stored separately from `final_record`?

Approval is **not** the reason they are separate. They stay separate after approval too.

| Field | Meaning |
| --- | --- |
| `raw_text` | What the person wrote. It never changes. |
| `extraction` | The model’s draft. It can be wrong. |
| `final_record` | What the reviewer saved. They may have edited it. |

If you overwrite the original with the approved form, you can no longer prove a quote was in the message, and you cannot see what the prospect said versus what the firm stored.

### Why must a seed function be idempotent?

“So it can seed twice” is the behavior, not the reason.

The API process starts over and over: every `fastapi dev`, every reload, every deploy, every test. Without the early return, each start would insert another Northstar, Evelyn, and Apex. The demo CRM would fill with duplicates, and “three existing clients” would be a lie.

> First start creates three rows. Every later start sees they exist and stops.
