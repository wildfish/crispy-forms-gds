from playwright.sync_api import Page


def test_accordion__layout(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/accordion/")
    assert_snapshot(page.screenshot(full_page=True))


def test_accordion__show_all(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/accordion/")
    page.locator("button[class=govuk-accordion__show-all]").click()
    assert_snapshot(page.screenshot(full_page=True))


def test_accordion__hide_all(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/accordion/")
    page.locator("button[class=govuk-accordion__show-all]").click()
    page.locator("button[class=govuk-accordion__show-all]").click()
    assert_snapshot(page.screenshot(full_page=True))


def test_accordion__show_section(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/accordion/")
    page.locator("button[class=govuk-accordion__section-button]").locator(
        "nth=0"
    ).click()
    assert_snapshot(page.screenshot(full_page=True))


def test_accordion__hide_section(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/accordion/")
    page.locator("button[class=govuk-accordion__section-button]").locator(
        "nth=0"
    ).click()
    page.locator("button[class=govuk-accordion__section-button]").locator(
        "nth=0"
    ).click()
    assert_snapshot(page.screenshot(full_page=True))
