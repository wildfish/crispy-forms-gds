from playwright.sync_api import Page


def test_date_input__layout(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/date-input/")
    assert_snapshot(page.screenshot(full_page=True))


def test_date_input__enter_date_and_submit(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/date-input/")
    page.locator("input[id=id_date_0]").fill("25")
    page.locator("input[id=id_date_1]").fill("12")
    page.locator("input[id=id_date_2]").fill("2024")
    page.locator("button[id=id_submit]").click()
    assert_snapshot(page.screenshot(full_page=True))


def test_date_input__leave_blank_and_submit(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/date-input/")
    page.locator("button[id=id_submit]").click()
    assert_snapshot(page.screenshot(full_page=True))
