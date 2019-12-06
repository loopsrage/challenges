import unittest

from proj_options import options, helper
from proj_options.base import Challenge


class Challenge2(Challenge):
    def test_challenge2(self):
        """
        Challenge 2:
        1. Load the home page
        2. Enter the Search for the term 'Exotic'
        3. Wait for page results
        4. Check each lotsearchLotmake for PORSCHE
        """
        # Make initial request to base url
        self.driver.get(options.BASE_URL)

        # Add search term to options_copy
        self.options_copy['search'] = 'exotics'

        # Use perform_search to locate, and execute a search on the page
        helper.perform_search(self.driver, **self.options_copy)

        # Wait for table to load
        self.wait_for_element_load('serverSideDataTable')

        # Get the table data using find_elements_of_type
        find_opt = {
            # Set selector, use defaults for the rest
            'selector': '//*[@data-uname="lotsearchLotmake"]',
        }
        # Perform the operation
        results = helper.find_elements_of_type(self.driver, **find_opt)

        # Hard Assert the presence of PORSCHE in results
        self.assertIn('PORSCHE', [i.text for i in results])


if __name__ == '__main__':
    unittest.main()
