from selenium import webdriver


class WebDriverManager(object):

    _driver = None

    @classmethod
    def get_web_driver(cls, browser):
        if cls._driver is None:
            if (browser.lower()) == "chrome":
                cls._driver = webdriver.Chrome("/home/soumen/software/chromedriver/chromedriver")

        return cls._driver