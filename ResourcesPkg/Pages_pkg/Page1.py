from ResourcesPkg.Utilities_pkg.Web import Web


class Page1(object):

    _url = "https://openweathermap.org/api"

    def __init__(self, browser):        self._web = Web(browser)

    def call_page1_open(self):
        self._web.open(self._url)

    def click_api_doc(self, category):
        self._web.get_web_element_by_xpath("//h3[contains(text(),'"+category+"')]/following-sibling::a["
                                           "contains(text(),'API doc')]").click()

    def get_list_of_api_types(self):
        return self._web.get_web_elements_by_xpath("//section[@id='one']//section")

    def close(self):
        self._web.close_all()