from Selenium2Library import Selenium2Library


def search_for_hotels(driver):
    driver.find_element("//a[contains(@class,'widgetSearchBtn')]").click()

