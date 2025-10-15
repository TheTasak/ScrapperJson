import time
from typing import Any, Generator, Callable

from playwright.sync_api import sync_playwright, Page

def _playwright_pagination(page: Page, params: dict) -> str:
    scroll_amount = params.get("scroll_amount")
    delay = params.get("scroll_delay")
    content = page.content()
    page.mouse.wheel(0, scroll_amount)
    time.sleep(delay)
    return content

class PlaywrightEngine:
    def __init__(self, pagination_function: Callable, pagination_params: dict):
        self.pagination_function = pagination_function
        self.pagination_params = pagination_params
        self.context_manager = sync_playwright()
        self.browser = self.context_manager.start().chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def get_page(self) -> Page:
        return self.page

    def load(self, url: str) -> Generator[str, Any, None]:
        pagination = self.pagination_params.get("paginate")
        if pagination:
            limit = self.pagination_params.get("limit")
        else:
            limit = 1
        self.page.goto(url)

        for i in range(0, limit):
            result = self.pagination_function(self.page, self.pagination_params)
            yield result

    def stop(self):
        self.browser.close()