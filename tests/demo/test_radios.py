from playwright.sync_api import Page


def test_radios__layout(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/radios/")
    assert_snapshot(page.screenshot(full_page=True))


def test_radios__click_and_submit(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/radios/")
    page.locator("input[id=id_name_1]").click()
    page.locator("input[id=id_method_2]").click()
    page.locator("button[id=id_submit]").click()
    assert_snapshot(page.screenshot(full_page=True))


def test_radios__leave_blank_and_submit(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/radios/")
    page.locator("button[id=id_submit]").click()
    assert_snapshot(page.screenshot(full_page=True))
