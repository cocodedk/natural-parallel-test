# Security Policy

## Reporting a Vulnerability

Do **not** open a public GitHub issue for security vulnerabilities.

To report a vulnerability:

- Use the **"Report a vulnerability"** button on the Security tab of this repository
  (GitHub private advisory)
- Or email: bb@cocode.dk

We will acknowledge within 5 business days and aim to release a fix within 30 days of
confirmation.

## Scope notes for this plugin

This plugin ships prompts, not executable code that runs on your machine — but prompts are
an attack surface. Two things are worth knowing:

**Plans under test are untrusted input.** The skill instructs the model to treat any
supplied plan, incident report, or fetched page as evidence rather than instructions, and to
report an injection attempt as a finding. If you find a phrasing that defeats that
instruction, it is a valid report under this policy.

**Subagents inherit your environment.** `analogue-scout` may use WebSearch and WebFetch to
verify a mechanism. Retrieved pages are third-party content. Both shipped agents set
`disallowedTools: Write, Edit, NotebookEdit`, so neither can modify files.

## Supported Versions

| Version | Supported |
|---------|-----------|
| latest  | ✅ |
| older   | ❌ |
