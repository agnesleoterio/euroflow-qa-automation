from pathlib import Path


BASE_URL = "http://localhost:3000"
EVIDENCE_DIR = Path("evidence")


def test_homepage_loads(page):
    EVIDENCE_DIR.mkdir(exist_ok=True)

    page.goto(BASE_URL)

    assert page.title()
    page.screenshot(path=EVIDENCE_DIR / "homepage.png", full_page=True)

