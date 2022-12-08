from time import time, sleep

import pytest
from selene.support.conditions import have
from selene.support.shared import browser
from urllib3.util import timeout

from pages.google_page import GooglePage
from pages.klue_page import KluePage


@pytest.mark.smoke
def test_cn01_just_an_example(web):
    google_page = GooglePage()
    google_page.navigate_to_google()
    google_page.search("Klue")
    # sleep(10)

