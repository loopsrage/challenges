import os
import time
import unittest

from selenium.common.exceptions import NoSuchElementException

from proj_options import options, helper
from proj_options.base import Challenge

SCREENSHOT_PATH = os.path.join('.challenge_6', 'screenshots', 'challenge_6.png')


class Challenge6(Challenge):

    def test_challenge6(self):
        """
        Challenge 6:
        1. Search for nissan - skyline
        2. Try and access the first result
        3. Catch exception for NoSuchelementException
        4. Take screenshot if it does not exist
        """
        self.driver.get(options.BASE_URL)

        # Set the search term
        self.options_copy['search'] = 'Nissan Skyline'
        helper.perform_search(self.driver, **self.options_copy)

        # TODO: Set good sleep here
        time.sleep(10)
        first_element_selector = '//*[@id="serverSideDataTable"]/tbody/tr/td[6]/span'
        try:
            # If the element exists, do nothing for now, test passed
            first_elem_in_table = self.driver.find_element_by_xpath(first_element_selector)

            # Assert that the result is actually a SKYLINE
            self.assertEqual(first_elem_in_table.text, 'SKYLINE', 'Results found, but wasn\'t a SKYLINE')
        except NoSuchElementException as ex:
            # If the element does not exist, throw a screenshot
            # TODO: Add timestamp to the file, so it does not overwrite the existing one
            self.driver.save_screenshot(SCREENSHOT_PATH)
            print("Screenshot saved to: {}".format(SCREENSHOT_PATH))


if __name__ == '__main__':
    unittest.main()
