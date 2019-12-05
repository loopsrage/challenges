import os
import sys
import unittest

sys.path.append(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__),os.path.pardir)
            )
        )

from base import Challenge

# The base url for this challenge
BASE_URL = 'https://google.com'


class Challenge1(Challenge):
    def test_challenge1(self):
        """
        Challenge 1:
        1. Using chrome driver, get google.com
        2. Check if 'Google' is in the title of page
        """
        # Initialize the url
        self.driver.get(BASE_URL)
        # Assert 'Google' in self.driver.title
        self.assertIn('Google', self.driver.title)


if __name__ == '__main__':
    unittest.main()