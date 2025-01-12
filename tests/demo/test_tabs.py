from playwright.sync_api import Page


def test_tabs__layout(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/tabs/")
    assert_snapshot(page.screenshot(full_page=True))


def test_tabs__click_tab(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/tabs/")
    page.locator("a[id=tab_past-week]").click()
    assert_snapshot(page.screenshot(full_page=True))
