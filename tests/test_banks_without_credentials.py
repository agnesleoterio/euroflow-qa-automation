import os
from pathlib import Path

import pytest


BASE_URL = os.getenv("EUROFLOW_BASE_URL", "http://localhost:3000")
EVIDENCE_DIR = Path("evidence")


@pytest.mark.xfail(
    reason="BUG-001: Banks uses seeded certificate data when credentials are empty",
    strict=True,
)
def test_banks_blocks_connection_without_enable_banking_credentials(page):
    """Bank connection must stay blocked until PSD2 credentials are configured."""
    EVIDENCE_DIR.mkdir(exist_ok=True)

    page.goto(f"{BASE_URL}/banks")
    page.get_by_text("Bank connections", exact=True).wait_for()
    page.screenshot(
        path=EVIDENCE_DIR / "banks-without-credentials.png",
        full_page=True,
    )

    missing_certificate = page.get_by_text(
        "NO PSD2 CERTIFICATE — bank connections are disabled.",
        exact=True,
    )
    search_input = page.get_by_role("textbox")

    assert missing_certificate.is_visible()
    assert search_input.is_disabled()


@pytest.mark.xfail(
    reason=(
        "BUG-002: bank search reaches the API without Enable Banking credentials "
        "and gives the user no actionable error"
    ),
    strict=True,
)
def test_bank_search_without_credentials_is_blocked_before_api_call(page):
    """An unconfigured bank search must be blocked without calling the API."""
    EVIDENCE_DIR.mkdir(exist_ok=True)
    bank_requests = []

    page.on(
        "request",
        lambda request: bank_requests.append(request.url)
        if "/api/banks" in request.url
        else None,
    )

    page.goto(f"{BASE_URL}/banks")
    page.get_by_text("Bank connections", exact=True).wait_for()

    search_input = page.get_by_placeholder("Bank name (e.g. N26, Revolut, ING…)")
    search_input.fill("N26")
    page.wait_for_timeout(1_000)
    page.screenshot(
        path=EVIDENCE_DIR / "bank-search-without-credentials.png",
        full_page=True,
    )

    assert bank_requests == [], (
        f"Bank search reached the API without credentials: {bank_requests}"
    )
    assert page.get_by_text(
        "NO PSD2 CERTIFICATE — bank connections are disabled.",
        exact=True,
    ).is_visible()
