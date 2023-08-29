import os
from time import sleep
import pytest
import selenium

from config import driver as driver_setup
from selene.support.shared import browser
from selenium.common.exceptions import WebDriverException


def set_pytest_plugins_by_os(path_to_project):
    plugins = []
    path_separator = chr(92) if os.name == "nt" else "/"
    for root, dirs, files in os.walk(os.path.join(path_to_project, "tests"), topdown=False):
        for file in files:
            if file.split(".")[0] == "steps_defs" and "pycache" not in root:
                plugins.append(
                    f"{root[root.find(f'{path_separator}tests') + 1:].replace(path_separator, '.')}.{file.split('.')[0]}"
                )
    return plugins


pytest_plugins = set_pytest_plugins_by_os(path_to_project=os.path.dirname(__file__))


@pytest.fixture(scope="function", autouse=True)
def session():
    return {}


@pytest.fixture(scope="function", autouse=True)
def setup_browser(session):
    try:
        ui_driver = driver_setup.Driver().start()
    except selenium.common.exceptions.SessionNotCreatedException:
        sleep(1)
        ui_driver = driver_setup.Driver().start()
    browser.config.timeout = 2
    browser.config.driver = ui_driver
    session["browser_windows"] = {
        "main_window_handle": browser.driver.current_window_handle,
        "window_handles": browser.driver.window_handles,
    }
    yield
    try:
        browser.config.driver.quit()
    except WebDriverException:
        print("Driver is already closed")
