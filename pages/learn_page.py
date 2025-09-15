from playwright.sync_api import Page, Locator, Response, expect
import re


class LearnPage:
    URL = "https://www.adobe.com/learn"

    def __init__(self, page: Page, timeout: int = 10_000) -> None:
        self.page = page
        self.timeout = timeout
        self.page.set_default_timeout(timeout)  # applies to all actions & waits
        self.page.set_default_navigation_timeout(timeout)  #

    # ── Navigation ────────────────────────────────────────────────────────────

    def navigate(self, url: str | None = None) -> Response | None:
        return self.page.goto(url or self.URL)

    def reload(self) -> Response | None:
        return self.page.reload()

    def go_back(self) -> Response | None:
        return self.page.go_back()

    def go_forward(self) -> Response | None:
        return self.page.go_forward()

    def wait_for_load_state(self, state: str = "load") -> None:
        """States: 'load' | 'domcontentloaded' | 'networkidle'"""
        self.page.wait_for_load_state(state)

    def wait_for_url(self, url: str | re.Pattern, **kwargs) -> None:
        self.page.wait_for_url(url, **kwargs)

    # ── Page info ─────────────────────────────────────────────────────────────

    def title(self) -> str:
        return self.page.title()

    def url(self) -> str:
        return self.page.url

    def content(self) -> str:
        """Returns the full HTML of the page."""
        return self.page.content()

    # ── Finders (return Locator) ───────────────────────────────────────────────

    def get_by_text(self, text: str, **kwargs) -> Locator:
        return self.page.get_by_text(text, **kwargs)

    def get_by_role(self, role: str, **kwargs) -> Locator:
        return self.page.get_by_role(role, **kwargs)

    def get_by_label(self, text: str, **kwargs) -> Locator:
        return self.page.get_by_label(text, **kwargs)

    def get_by_placeholder(self, text: str, **kwargs) -> Locator:
        return self.page.get_by_placeholder(text, **kwargs)

    def get_by_alt_text(self, text: str, **kwargs) -> Locator:
        return self.page.get_by_alt_text(text, **kwargs)

    def get_by_title(self, text: str, **kwargs) -> Locator:
        return self.page.get_by_title(text, **kwargs)

    def get_by_test_id(self, test_id: str) -> Locator:
        return self.page.get_by_test_id(test_id)

    def locator(self, selector: str, **kwargs) -> Locator:
        return self.page.locator(selector, **kwargs)

    def query_selector(self, selector: str):
        return self.page.query_selector(selector)

    def query_selector_all(self, selector: str):
        return self.page.query_selector_all(selector)

    # ── Actions ───────────────────────────────────────────────────────────────

    def click(self, selector: str, **kwargs) -> None:
        self.page.click(selector, **kwargs)

    def dblclick(self, selector: str, **kwargs) -> None:
        self.page.dblclick(selector, **kwargs)

    def hover(self, selector: str, **kwargs) -> None:
        self.page.hover(selector, **kwargs)

    def fill(self, selector: str, value: str, **kwargs) -> None:
        self.page.fill(selector, value, **kwargs)

    def type(self, selector: str, text: str, **kwargs) -> None:
        self.page.type(selector, text, **kwargs)

    def press(self, selector: str, key: str, **kwargs) -> None:
        self.page.press(selector, key, **kwargs)

    def select_option(self, selector: str, value: str, **kwargs) -> None:
        self.page.select_option(selector, value, **kwargs)

    def check(self, selector: str, **kwargs) -> None:
        self.page.check(selector, **kwargs)

    def uncheck(self, selector: str, **kwargs) -> None:
        self.page.uncheck(selector, **kwargs)

    def focus(self, selector: str, **kwargs) -> None:
        self.page.focus(selector, **kwargs)

    def tap(self, selector: str, **kwargs) -> None:
        self.page.tap(selector, **kwargs)

    def drag_and_drop(self, source: str, target: str, **kwargs) -> None:
        self.page.drag_and_drop(source, target, **kwargs)

    # ── Keyboard & Mouse ──────────────────────────────────────────────────────

    def keyboard_press(self, key: str) -> None:
        self.page.keyboard.press(key)

    def keyboard_type(self, text: str, **kwargs) -> None:
        self.page.keyboard.type(text, **kwargs)

    def mouse_move(self, x: float, y: float) -> None:
        self.page.mouse.move(x, y)

    def mouse_click(self, x: float, y: float, **kwargs) -> None:
        self.page.mouse.click(x, y, **kwargs)

    # ── Waiting ───────────────────────────────────────────────────────────────

    def wait_for_selector(self, selector: str, **kwargs) -> None:
        self.page.wait_for_selector(selector, **kwargs)

    def wait_for_timeout(self, ms: int) -> None:
        self.page.wait_for_timeout(ms)

    def wait_for_function(self, expression: str, **kwargs):
        return self.page.wait_for_function(expression, **kwargs)

    # ── JavaScript ────────────────────────────────────────────────────────────

    def evaluate(self, expression: str, arg=None):
        return self.page.evaluate(expression, arg)

    def evaluate_handle(self, expression: str, arg=None):
        return self.page.evaluate_handle(expression, arg)

    def add_script_tag(self, **kwargs) -> None:
        self.page.add_script_tag(**kwargs)

    # ── Network ───────────────────────────────────────────────────────────────

    def wait_for_response(self, url_or_predicate, **kwargs):
        return self.page.wait_for_response(url_or_predicate, **kwargs)

    def wait_for_request(self, url_or_predicate, **kwargs):
        return self.page.wait_for_request(url_or_predicate, **kwargs)

    def route(self, url, handler) -> None:
        self.page.route(url, handler)

    def unroute(self, url, handler=None) -> None:
        self.page.unroute(url, handler)

    # ── Screenshots & PDF ─────────────────────────────────────────────────────

    def screenshot(self, **kwargs) -> bytes:
        return self.page.screenshot(**kwargs)

    def pdf(self, **kwargs) -> bytes:
        """Chromium only."""
        return self.page.pdf(**kwargs)

    # ── Frames & Popups ───────────────────────────────────────────────────────

    def frame(self, name: str | None = None, url: str | None = None):
        return self.page.frame(name=name, url=url)

    def frames(self):
        return self.page.frames

    def frame_locator(self, selector: str):
        return self.page.frame_locator(selector)

    def expect_popup(self):
        return self.page.expect_popup()

    def expect_new_page(self):
        return self.page.context.expect_page()

    # ── Dialogs ───────────────────────────────────────────────────────────────

    def on_dialog(self, handler) -> None:
        """Register a handler: lambda d: d.accept() or d.dismiss()"""
        self.page.on("dialog", handler)

    def expect_dialog(self):
        return self.page.expect_event("dialog")

    # ── Assertions (expect wrappers) ──────────────────────────────────────────

    def expect_title(self, title: str | re.Pattern, **kwargs) -> None:
        expect(self.page).to_have_title(title, **kwargs)

    def expect_url(self, url: str | re.Pattern, **kwargs) -> None:
        expect(self.page).to_have_url(url, **kwargs)

    def expect_visible(self, selector: str, **kwargs) -> None:
        expect(self.page.locator(selector)).to_be_visible(**kwargs)

    def expect_hidden(self, selector: str, **kwargs) -> None:
        expect(self.page.locator(selector)).to_be_hidden(**kwargs)

    def expect_text(self, selector: str, text: str | re.Pattern, **kwargs) -> None:
        expect(self.page.locator(selector)).to_have_text(text, **kwargs)

    def expect_contains_text(self, selector: str, text: str, **kwargs) -> None:
        expect(self.page.locator(selector)).to_contain_text(text, **kwargs)

    def expect_enabled(self, selector: str, **kwargs) -> None:
        expect(self.page.locator(selector)).to_be_enabled(**kwargs)

    def expect_checked(self, selector: str, **kwargs) -> None:
        expect(self.page.locator(selector)).to_be_checked(**kwargs)

    def wait_for_visible(self, selector: str, timeout: int = 10_000) -> Locator:
        locator = self.page.locator(selector)
        expect(locator).to_be_visible(timeout=timeout)
        return locator

    def click_first(self, selector: str, **kwargs) -> None:
        self.page.locator(selector).first.click(**kwargs)