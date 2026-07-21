# Euro Flow QA Automation Portfolio

Basic QA automation project for Euro Flow using Python, pytest and Playwright.

This is an independent QA automation portfolio project created to practise smoke test automation for an open-source banking/financial application.

## Goal

Create a small automation layer to support smoke testing of selected Euro Flow web flows.

## Current Scope

- Open the Euro Flow local application.
- Validate that the main page loads.
- Validate that bank connections stay blocked when Enable Banking credentials are empty.
- Capture a screenshot as test evidence.

## Tools

- Python
- pytest
- Playwright
- Chromium

## Local URLs

- UI: `http://localhost:3000`
- API health check: `http://localhost:3001/health`

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Run

```bash
source .venv/bin/activate
pytest
```

The Euro Flow application must be running before executing the tests.
Set `EUROFLOW_BASE_URL` to test another local URL.

## Current Status

- Initial Playwright + pytest structure created.
- First homepage smoke test implemented.
- Test executed successfully locally.
- `BUG-001` automated as an expected failure: Banks shows a seeded PSD2 certificate when credentials are empty.

## Notes

- No credentials, tokens, private keys or local configuration files are stored in this repository.
- Screenshots are treated as local evidence and are ignored by git.
