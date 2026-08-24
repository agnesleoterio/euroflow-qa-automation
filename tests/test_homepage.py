import os
from pathlib import Path

from playwright.sync_api import expect


BASE_URL = os.getenv("EUROFLOW_BASE_URL", "http://localhost:3000")
EVIDENCE_DIR = Path("evidence")


def test_homepage_redirects_to_setup_wizard(page):
    EVIDENCE_DIR.mkdir(exist_ok=True)

    response = page.goto(BASE_URL)

    assert response is not None
    assert response.ok

    expect(page).to_have_url(f"{BASE_URL}/setup")
    expect(
        page.get_by_role("main").get_by_role("img", name="euroflow")
    ).to_be_visible()
    expect(
        page.get_by_text("First-run wizard", exact=True)
    ).to_be_visible()
    expect(
        page.get_by_text(
            "Protect your euroflow instance",
            exact=True,
        )
    ).to_be_visible()
    expect(
        page.get_by_role("button", name="Skip for now")
    ).to_be_visible()
    expect(
        page.get_by_role("button", name="Continue")
    ).to_be_visible()

    page.screenshot(
        path=EVIDENCE_DIR / "homepage.png",
        full_page=True,
    )
