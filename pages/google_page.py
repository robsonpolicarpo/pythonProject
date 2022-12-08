from selene.api import s, ss
from selene.support.conditions import have
from selene.support.shared import browser


class GooglePage:

    def __init__(self):
        self.input_search = s('input[name="q"]')
        self.link_klue = s('a[href="https://klue.com/"]')
        self.results = ss('#rso>div h3')

    def navigate_to_google(self):
        browser.open('https://www.google.com')

    def search(self, query):
        self.input_search.set(query).press_enter()

    def click_klue_result(self):
        self.link_klue.click()

    def get_first_result(self):
        return self.results.first().text