import os,sys
import sys
import unittest

sys.path.append(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__),os.path.pardir)
            )
        )

from base import Challenge


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


if __name__ == '__main__':
    unittest.main()
