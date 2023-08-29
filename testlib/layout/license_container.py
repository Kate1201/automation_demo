from selene.core.entity import Element
from selene.support.shared import browser


class LicenseContainer(Element):

    def __init__(self, locator):
        super().__init__(locator, browser.config)

    def get_license_type(self):
        return self.element('./div/a[not(@class)]')

    def get_license_badge(self):
        return self.element('./div/p[@class="badge"]')

    def get_license_price(self):
        return self.element('./div/p[@class="price"]')

    def get_license_buy_button(self):
        return self.element('./div/a[@class]')
