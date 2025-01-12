from playwright.sync_api import Page


def test_select__layout(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/select/")
    assert_snapshot(page.screenshot(full_page=True))


def test_select__select_item_and_submit(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/select/")
    page.locator("select[id=id_sort_by]").select_option("updated")
    page.locator("button[id=id_submit]").click()
    assert_snapshot(page.screenshot(full_page=True))
