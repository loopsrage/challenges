import os
import unittest

from proj_options import options
from proj_options.base import Challenge

LOG_PATH = os.path.join('.\\logs', 'challenge_8.log')
BASE_URL = "{}/public/lots/search".format(options.BASE_URL)


class Challenge8(Challenge):
    def test_challenge8(self):
        """
        Challenge 8:
        1. Using copart webservice search for Toyota Camry
        2. Grab data and output to a log file
        3. https://www.copart.com/public/lots/search Is the endpoint via POST
        4. Pass query = toyota camry

        5. Repeat step 1 - 4 for 10 different searches
        """
        self.driver.get(BASE_URL)


if __name__ == '__main__':
    unittest.main()
