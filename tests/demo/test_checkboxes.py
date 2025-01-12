from playwright.sync_api import Page


def test_checkboxes__layout(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/checkboxes/")
    assert_snapshot(page.screenshot(full_page=True))


def test_checkboxes__select_option_and_submit(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/checkboxes/")
    page.locator("input[id=id_method_1]").click()
    page.locator("button[id=id_submit]").click()
    assert_snapshot(page.screenshot(full_page=True))


def test_checkboxes__leave_blank_and_submit(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/checkboxes/")
    page.locator("button[id=id_submit]").click()
    assert_snapshot(page.screenshot(full_page=True))
