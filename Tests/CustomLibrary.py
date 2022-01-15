from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from Selenium2Library import Selenium2Library
from selenium import webdriver


# class CustomLibrary(Selenium2Library):


def get_webdriver_instance():
    se2lib = BuiltIn().get_library_instance('Selenium2Library')
    print("I am driver", se2lib.driver)
    return se2lib.driver


def get_web_driver(url, driver):
    print("I am driver", driver)
    if driver == "Chrome":
        driver = webdriver.Chrome("/home/soumen/software/chromedriver/chromedriver")
        driver.get(url)
    elif driver == "Firefox":
        driver = webdriver.firefox("/home/soumen/software/geckodriver")
    #    return driver

def search_for_hotels_draft():
    get_webdriver_instance().find_element("//a[contains(@class,'widgetSearchBtn')]").click()


# def get_web_driver(url, driver, browser):
#     if browser == "Chrome":
#         driver = webdriver.Chrome("/home/soumen/software/chromedriver/chromedriver")
#         driver.get(url)
#     elif browser == "Firefox":
#         driver = webdriver.firefox("/home/soumen/software/geckodriver")
# #    return driver


# WebDriverManager.Open_Home_Page("https://www.google/com","Chrome")

#ab = CustomSeleniumLibrary().get_webdriver_instance()

