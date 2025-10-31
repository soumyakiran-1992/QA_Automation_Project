# conftest.py
from typing import Any
import pytest
import config as config
from playwright.sync_api import sync_playwright
import time


@pytest.fixture(scope="session")
def browser():
    """Launch browser once per session."""
    with sync_playwright() as p:
        browser_type = getattr(p, config.BROWSER)
        browser = browser_type.launch(headless=config.HEADLESS)
        yield browser
        browser.close()

@pytest.fixture
def page(browser: Any):
    """Create a new page for each test."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


def pytest_configure(config):
    if config.option.htmlpath and "%(ts)s" in config.option.htmlpath:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        config.option.htmlpath = config.option.htmlpath.replace("%(ts)s", timestamp)
