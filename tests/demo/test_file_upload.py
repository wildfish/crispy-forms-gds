from playwright.sync_api import Page


def test_file_upload_component__layout(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/file-upload/")
    assert_snapshot(page.screenshot(full_page=True))
