import pytest
from playwright.sync_api import Page


def test_textarea__layout(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/textarea/")
    assert_snapshot(page.screenshot(full_page=True))


@pytest.mark.skip(reason="This text 'pastes' the text so the word count is not updated")
def test_textarea__word_count(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/textarea/")
    page.locator("textarea[id=id_description]").fill("This is the time for...")
    assert_snapshot(page.screenshot(full_page=True))


def test_textarea__fill_and_submit(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/textarea/")
    page.locator("textarea[id=id_description]").fill("This is the time for...")
    page.locator("button[id=id_submit]").click()
    assert_snapshot(page.screenshot(full_page=True))


def test_textarea__leave_blank_and_submit(live_server, assert_snapshot, page: Page):
    page.goto(f"{live_server.url}/components/textarea/")
    page.locator("button[id=id_submit]").click()
    assert_snapshot(page.screenshot(full_page=True))
