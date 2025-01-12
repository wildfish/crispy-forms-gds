from playwright.sync_api import Page


def test_tag_component__layout(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/tag/")
    assert_snapshot(page.screenshot(full_page=True))
