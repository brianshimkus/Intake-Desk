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

Do not number posts as Day 1, Day 2, and so on. The title is a catchy claim a stranger would click. The series still groups as Intake Desk. Previous / next can follow publish date. The site currently labels series cards with `Day N`; change that when the first Intake Desk post ships, not before.
