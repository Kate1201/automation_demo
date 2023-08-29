from selene import Config, be, query
from selene.support.shared import browser
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement


def get_scroll_position():
    return browser.execute_script("return window.scrollY")


def is_element_visible_in_viewpoint(element) -> bool:
    return browser.execute_script(
        "var elem = arguments[0],                 "
        "  box = elem.getBoundingClientRect(),    "
        "  cx = box.left + box.width / 2,         "
        "  cy = box.top + box.height / 2,         "
        "  e = document.elementFromPoint(cx, cy); "
        "for (; e; e = e.parentElement) {         "
        "  if (e === elem)                        "
        "    return true;                         "
        "}                                        "
        "return false;                            ",
        element(),
    )


def move_cursor_to_element(element):
    ActionChains(browser.driver).move_to_element(
        WebElement(parent=browser.driver, id_=element.get(query.internal_id))
    ).perform()
