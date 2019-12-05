from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

CHROME_DRIVER = './chromedriver.exe'

BASE_URL = 'https://copart.com/'
SEARCH_FIELD_SELECTOR = '//*[@id="input-search"]'
SEARCH_OPTIONS = {
    'by_type': By.XPATH,
    'selector': SEARCH_FIELD_SELECTOR
}


def get_chrome_options():
    """

    """
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    return chrome_options


