from playwright.sync_api import Page


def test_buttons__layout(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/buttons/")
    assert_snapshot(page.screenshot(full_page=True))


def test_buttons__click_add_button(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/buttons/")
    page.locator("button[id=id_add]").click()
    assert_snapshot(page.screenshot(full_page=True))


def test_buttons__disabled_button(live_server, page: Page):
    page.goto(f"{live_server.url}/components/buttons/")
    assert page.locator("button[id=id_win]").is_disabled()
