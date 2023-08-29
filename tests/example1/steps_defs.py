from hamcrest import assert_that, contains_string
from pytest_bdd import when, then
from selene import be
from selene.core.condition import Condition
from selene.support.shared import browser

from config.definitions import URL
from testlib.pages import makeup_home_page


@when('open')
def open_url():
    browser.open('https://google.com/')


@then('get url')
def get_url():
    assert_that(browser.driver.current_url, contains_string('google.com'))

@when('User goes to Makeup Home page')
def open_makeup_url():
    browser.open(URL)
    if makeup_home_page.close_popup_icon.with_(timeout=10).matching(be.visible):
        makeup_home_page.close_popup_icon.click()

@then('Makeup Home Page is opened')
def get_makeup_url():
    assert_that(browser.driver.current_url, contains_string(URL))
    makeup_home_page.main_logo.should(be.visible)
    makeup_home_page.perfume_tab.click()

