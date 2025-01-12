from playwright.sync_api import Page


def test_inset_component__layout(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/inset/")
    assert_snapshot(page.screenshot(full_page=True))
