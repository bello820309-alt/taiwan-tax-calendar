Tax Deadline Data Dictionary

This document explains the fields used in "tax_deadlines.csv".

CSV Fields

Field| Description
"id"| Unique identifier for each tax deadline record.
"tax_type"| Tax category, such as business tax or income tax.
"title"| Short description of the filing obligation.
"applicable_to"| Taxpayers or entities to which the rule applies.
"deadline_rule"| Description of the filing deadline.
"source_url"| Official source URL supporting the record.
"last_verified"| Date the source and rule were last reviewed, in "YYYY-MM-DD" format.
"status"| Review status of the record.

Data Quality Rules

- Use official Taiwan government sources whenever possible.
- Verify both the source URL and the applicable filing rule before marking a record as verified.
- Use "YYYY-MM-DD" for dates.
- Keep each record on one CSV row.
- Do not treat a source link as proof that every detail in a record has been verified.

Status Values

- "source_checked_rule_needs_review": The source has been located, but the filing rule still needs further review.
- "verified": The source and applicable filing rule have been checked.
- "needs_review": The record needs further verification or correction.

Contributions

When adding or editing a record, explain the change and include an official source. If a deadline varies by tax year or taxpayer type, document the applicable conditions clearly.
