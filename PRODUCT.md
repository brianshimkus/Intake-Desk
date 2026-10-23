# Intake Desk product brief

## Customer

Lakefront Legal is a fictional five-person law office in Chicago. It is a small general practice: employment, family, business, estate, and real estate inquiries all land in the same inbox.

It is not an employment boutique. The demo and the 50-case evaluation use several matter types, and a five-person firm that only did employment would make those samples a plot hole. Mixed work also gives the extractor something real to classify, and something real to leave as `unknown`.

## User

An intake coordinator. They review a new inquiry before an attorney decides what to do with it.

## Current problem

Inquiries arrive as unstructured email and form text. The coordinator copies names, dates, and the other party into a CRM, checks whether a phone number or deadline is missing, and looks for an obvious name overlap with a current client. Nothing in that process shows where each typed value came from. An AI that filled the form and wrote the record would sound sure, and the same gap would remain.

## Version-one promise

Turn fictional inquiry text into a source-grounded proposed record, flag missing or potentially conflicting details, and require human approval before a safe demo CRM changes.

## Non-goals

- Legal advice
- Definitive conflict checks
- Automatic acceptance or rejection
- Automatic messages
- Real customer data
- Real CRM access
- Multi-tenancy

## Release evidence

- Public synthetic demo
- 50-case labeled evaluation
- pytest and Playwright results
- Accessibility checklist
- Architecture diagram
- Two-minute video
