import time
import unittest

from selenium.webdriver.common.by import By

from proj_options import options, helper
from proj_options.base import Challenge

# Damage Types
DAMAGE_TYPE = {
    'REAR END': 0,
    'FRONT END': 0,
    'MINOR DENT/SCRATCHES': 0,
    'UNDERCARRIAGE': 0,
    'MISC': 0,
}


class Challenge5(Challenge):

    def test_challenge5(self):
        """
        Challenge 5:
        1. Search for Porsche
        2. Change dropdown from 20 to 100
        3. Group like models together
        4. Print the results
        """
        self.driver.get(options.BASE_URL)

        # Perform search on page for porsche
        self.options_copy['search'] = 'porsche'
        helper.perform_search(self.driver, **self.options_copy)

        self.wait_for_element_load('serverSideDataTable_length', 10, By.NAME)

        # Locate and modify Dropdown
        self.driver.find_element_by_xpath(
            '//select[@name="serverSideDataTable_length"]/option[text()="100"]'
        ).click()

        # Wait for first element in table to load
        self.wait_for_element_load('//*[@id="serverSideDataTable"]/tbody/tr[1]', 10, By.XPATH)

        # Get all elements from results
        find_opt = {
            'selector': '//*[@data-uname="lotsearchLotmodel"]'
        }
        # TODO: Use a good sleep
        time.sleep(10)

        # Find lotsearchLotmodel elements
        elements = helper.find_elements_of_type(self.driver, **find_opt)

        # Change selector to look for damages
        find_opt['selector'] = '//*[@data-uname="lotsearchLotdamagedescription"]'
        # Find lotsearchLotdamagedescription
        damage_elem = helper.find_elements_of_type(self.driver, **find_opt)

        # List comprehension to save results of both finds
        results = [i.text for i in elements]
        damage_results = [i.text for i in damage_elem]

        # Loop through Damages
        for i in damage_results:
            # If one of our tracked damage types, increase count
            if i in DAMAGE_TYPE:
                DAMAGE_TYPE[i] = DAMAGE_TYPE[i] + 1
            # Otherwise increment MISC
            else:
                DAMAGE_TYPE['MISC'] = DAMAGE_TYPE['MISC'] + 1

        # Print the results
        print(helper.sort_strings(results))
        print(DAMAGE_TYPE)


if __name__ == '__main__':
    unittest.main()
