from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.definitions import BROWSER, LANGUAGE, LOCALE_CODE

browsers = {"chrome": webdriver.Chrome, "remote": webdriver.Remote}


class Driver:
    def __init__(self, **kwgs):
        self.kwgs = kwgs
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option("prefs", {"intl.accept_languages": LOCALE_CODE[LANGUAGE]})
        options.set_capability("selenoid:options", {'enableVideo': True})
        self.kwgs["options"] = options
        if BROWSER == "chrome":
            self.kwgs["service"] = Service(ChromeDriverManager().install())

        elif BROWSER == "remote":
            self.kwgs["command_executor"] = "http://54.39.83.141:4444/wd/hub"


    def start(self):
        driver = browsers[BROWSER](**self.kwgs)
        return driver
