import unittest

from selenium.webdriver.common.by import By

from proj_options import options
from proj_options.base import Challenge


class Challenge3(Challenge):

    def test_challenge3(self):
        """
        Challenge 3:
        1. Locate Popular Items
        2. Get URL/href for each type
        3. Loop over links
        """
        # Get the initial page
        self.driver.get(options.BASE_URL)

        # Search for 'popularSearches'
        searches_elem = self.driver.find_elements(By.XPATH, '//*[@ng-if="popularSearches"]')

        # Loop over elements in popularSearches
        for elem in searches_elem:
            # Get a list of 'a' tags from popularSearches element
            links_in_popular_searches = elem.find_elements_by_tag_name('a')
            # Loop over the 'a' tags
            for link in links_in_popular_searches:
                # Format a string for output of EXAMPLE => https://example.com
                search_link = "{} => {}".format(link.text, link.get_attribute('href'))
                # Print the results
                print(search_link)


if __name__ == '__main__':
    unittest.main()
