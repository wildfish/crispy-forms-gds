from playwright.sync_api import Page


def test_radios_conditional__layout(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/conditional_radios/")
    assert_snapshot(page.screenshot(full_page=True))


def test_radios_conditional__fill_hidden_and_submit(
    live_server, assert_snapshot, page: Page
):
    page.goto(f"{live_server.url}/components/conditional_radios/")
    page.locator("input[id=id_method_1]").click()
    page.locator("input[id=id_email_address]").fill("developer@crispy-forms-gds.org")
    page.locator("button[id=id_submit]").click()
    assert_snapshot(page.screenshot(full_page=True))


def test_radios_conditional__show_hidden_and_submit(
    live_server, assert_snapshot, page: Page
):
    page.goto(f"{live_server.url}/components/conditional_radios/")
    page.locator("input[id=id_method_1]").click()
    page.locator("button[id=id_submit]").click()
    assert_snapshot(page.screenshot(full_page=True))
