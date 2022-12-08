from selene import query
from selene.api import s, ss
from selene.support import by
from selene.support.conditions import have, be
from selene.support.shared import browser


class KluePage:

    def __init__(self):
        self.menus = ss('#menu-main-nav>li')
        self.new_menu = s('//*[@id="menu-super-nav-1"]')
        self.input_search = s('#search')
        self.results = ss('#card-listings>div')
        self.section_50_list = s('#Deloittes_Fast_50_List')
        self.breadcrumb_blog = s('a[href="/blog"]')

    def navigate(self):
        browser.open('https://klue.com/')

    def access_menu(self, menu_completed: str):
        menu_list = menu_completed.split('>')
        for item in self.menus:
            if item.s('a').get(query.text).casefold() \
                    == menu_list[0].casefold().strip():
                item.click()
                if len(menu_list) > 1:
                    submenus = item.ss('li')
                    for submenu in submenus:
                        if submenu.s('a').get(query.text).casefold() \
                                == menu_list[1].casefold().strip():
                            submenu.click()
                            return
                return
        raise ValueError(f"'{menu_list}' not found")

    def access_blog(self):
        s('.//a[contains(text(),"Resources")]').click()
        self.new_menu.s('.//p[text()="Our Blog"]').click()

    def blog_search(self, text):
        self.input_search.set(text).press_enter()

    def check_card(self, title):
        if self.get_result_by_title(title) is None:
            raise ValueError(f"Card not found. Title:\n{title}")

    def click_card(self, title):
        item = self.get_result_by_title(title)
        item.s('a[class="newbutton"]').click()

    def get_result_by_title(self, title):
        for item in self.results:
            if item.s('h3').get(query.text) \
                    .casefold().__contains__(title.casefold()):
                return item

    def check_section_50_list(self):
        self.section_50_list.with_(timeout=10).should(be.visible)


