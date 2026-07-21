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
