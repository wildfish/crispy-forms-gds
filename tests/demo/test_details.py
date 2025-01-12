from playwright.sync_api import Page


def test_details__layout(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/details/")
    assert_snapshot(page.screenshot(full_page=True))


def test_details__show_summary(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/details/")
    page.locator("summary[class=govuk-details__summary]").click()
    assert_snapshot(page.screenshot(full_page=True))


def test_details__hide_summary(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/details/")
    page.locator("summary[class=govuk-details__summary]").click()
    page.locator("summary[class=govuk-details__summary]").click()
    assert_snapshot(page.screenshot(full_page=True))
