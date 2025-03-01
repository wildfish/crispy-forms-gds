from playwright.sync_api import Page


def test_fieldset_component__layout(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/fieldset/")
    assert_snapshot(page.screenshot(full_page=True))
