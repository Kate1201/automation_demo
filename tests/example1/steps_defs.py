from lib2to3.pgen2 import driver

from hamcrest import assert_that, contains_string
from pytest_bdd import when, then
from selene import be
from selene.core.condition import Condition
from selene.support.shared import browser

from config.definitions import URL, URL_REDDIT
from testlib.actions import actions
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
   # if makeup_home_page.close_popup_icon.with_(timeout=10).matching(be.visible):
    #    makeup_home_page.close_popup_icon.click()

@then('Makeup Home Page is opened')
def get_makeup_url():
    assert_that(browser.driver.current_url, contains_string(URL))
    makeup_home_page.main_logo.should(be.visible)
    makeup_home_page.perfume_tab.click()

@when('User goes to Reddit Home page')
def open_make_url():
    browser.open(URL_REDDIT)

@then('Reddit Home page is opened')
def get_makeup_url():
    assert_that(browser.driver.current_url, contains_string(URL_REDDIT))

# @when('User goes to Youtube home page')
# def open_youtube_url():
#     browser.open(URL_YOUTUBE)
#
# @then('Youtube home page is opened')
# def get_youtube_url():
#     assert_that(browser.driver.current_url, contains_string(URL_YOUTUBE))
#
# @then('Cookies popup is displayed')
# def check_cookies_popup():
#     actions.move_cursor_to_element(youtube_home_page.accept_all_cookies_button)
#     #youtube_home_page.accept_all_cookies_button.should(be.visible)
#
# @when('User accepts all cookies')
# def accept_all_cookies():
#     youtube_home_page.accept_all_cookies_button.click()
#
# @then('Cookies popup disappers')
# def cookies_popup_hidden():
#     youtube_home_page.accept_all_cookies_button.should(be.hidden)

