import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from proj_options import options


def sleep_for_seconds(seconds):
    """
    So we don't have to import time when we sleep
    """
    time.sleep(seconds)


class Challenge(unittest.TestCase):
    """
    Base class for Challenges
    """
    options_copy = None

    def setUp(self) -> None:
        """
        Start the chromedriver session
        """
        self.driver = webdriver.Chrome(
            options.CHROME_DRIVER,
            options=options.get_chrome_options()
        )
        # Create a copy of default SEARCH_OPTIONS for each test to use
        self.options_copy = options.SEARCH_OPTIONS

    def tearDown(self) -> None:
        """
        Close the driver session
        """
        self.driver.close()

    def wait_for_element_load(self, element_id, timeout=30, by=By.ID):
        """
        Waits for an element to load before continuing to
        other parts of the test
        """
        # Perform the wait
        element = WebDriverWait(self.driver, timeout).until(
            # Wait for the provided ID to be loaded
            EC.presence_of_all_elements_located((by, element_id))
        )
