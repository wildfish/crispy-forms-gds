from playwright.sync_api import Page


def test_text_input__layout(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/text-input/")
    assert_snapshot(page.screenshot(full_page=True))


def test_text_input__fill_fields_and_submit(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/text-input/")
    page.locator("input[id=id_name]").fill("D. Veloper")
    page.locator("input[id=id_email]").fill("developer@crispy-forms-gds.org")
    page.locator("input[id=id_phone]").fill("555-2322")
    page.locator("input[id=id_password]").fill("password")
    page.locator("button[id=id_submit]").click()
    assert_snapshot(page.screenshot(full_page=True))


def test_text_input__leave_blank_and_submit(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/text-input/")
    page.locator("button[id=id_submit]").click()
    assert_snapshot(page.screenshot(full_page=True))
