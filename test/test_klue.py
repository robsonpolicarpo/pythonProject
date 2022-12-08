from time import time, sleep

import pytest
from selene.support.conditions import have
from selene.support.shared import browser
from urllib3.util import timeout

from pages.google_page import GooglePage
from pages.klue_page import KluePage


@pytest.mark.smoke
def test_cn01_check_klue(web):
    google_page = GooglePage()
    google_page.navigate_to_google()
    google_page.search("Klue")
    google_page.click_klue_result()

    klue_page = KluePage()
    # klue_page.navigate()
    klue_page.access_blog()
    # klue_page.access_menu('Blog')
    klue_page.blog_search('growing')
    card_title = 'Klue Named One of the Fastest-Growing Companies in Deloitte Technology Fast 50'
    klue_page.check_card(card_title)
    klue_page.click_card(card_title)
    klue_page.check_section_50_list()
    klue_page.breadcrumb_blog.click()
    assert browser.config.driver.current_url == 'https://klue.com/blog'


@pytest.mark.smoke
def test_cn02_check_klue_in_first_place_in_google(web):
    google_page = GooglePage()
    google_page.navigate_to_google()
    google_page.search("Klue")
    first_res = google_page.get_first_result()
    assert first_res == 'Klue | Competitive Enablement for every department of every ...'
    # sleep(10)

