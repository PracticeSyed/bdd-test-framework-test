from playwright.sync_api import Page

class Practicesoftwaretesting_ComPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practicesoftwaretesting.com/"
    
    def navigate(self):
        self.page.goto(self.url)
        return self

    def click_link_0(self):
        """Click link: Cloudflare"""
        self.page.locator("a").first.click()
        return self

    def click_link_1(self):
        """Click link: Privacy"""
        self.page.locator("a.footer-text").first.click()
        return self

    def fill_input_0(self, value):
        """Fill: """
        if self.page.locator("#cf-chl-widget-jqmts_response").count() > 0:
            self.page.locator("#cf-chl-widget-jqmts_response").first.fill(value)
        return self
