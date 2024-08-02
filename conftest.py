import time
from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common import WebDriverException

from helpers.literals import TEST_URL


@pytest.fixture()
def driver(request):
    before_failed = request.session.testsfailed
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(TEST_URL)
    yield driver
    if request.session.testsfailed != before_failed:
        test_name = request.node.name
        _ts = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        try:
            allure.attach(driver.get_screenshot_as_png(),
                          name=f'Crash-Screenshot-{_ts}-{test_name}',
                          attachment_type=AttachmentType.PNG)
        except WebDriverException:
            pass
    driver.quit()
