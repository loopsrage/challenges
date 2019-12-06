import unittest

import requests

from proj_options import options
from proj_options.base import Challenge


class Challenge7(Challenge):

    def test_challenge7(self):
        """
        Challenge 7:
        1. Go to Make/Models
        2. Create 2 dimensional array
        3. Store Values and Link
        4. Loop over array and validate links are valid
        """
        self.driver.get(options.BASE_URL)
        # Selector for the tab for Makes
        makes_selector = '//*[@id="tabMakes"]/div/div/ul[1]'

        # Execute the search for the selector
        tab_makes = self.driver.find_element_by_xpath(makes_selector)

        # Using list comprehension to build a list
        results = [
            {i.get_attribute('title'): i.get_attribute('href')} for i in tab_makes.find_elements_by_css_selector('a')
        ]

        status_codes = []
        link_validation_results = []
        # Loop over the list of links and assert the page goes to where it says it will
        for i in range(len(results)):
            for k in results[i].keys():
                # Get the link from array
                link = results[i][k]
                # Request the link
                response = requests.get(link)
                # Set True in status_codes if the status is 200, else False
                status_codes.append(response.status_code is 200)
                # Append overall results
                link_validation_results.append({link:response.status_code})

        # Print the status / links for all links
        print(link_validation_results)
        # Assert that all status codes are True, otherwise fail
        assert all(status_codes), 'Some links are broken.'


if __name__ == '__main__':
    unittest.main()
