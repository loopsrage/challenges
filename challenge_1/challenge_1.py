import unittest

from proj_options.base import Challenge


class Challenge1(Challenge):
    def test_challenge1(self):
        """
        Challenge 1:
        1. Using chrome driver, get google.com
        2. Check if 'Google' is in the title of page
        """
        # Initialize the url
        self.driver.get('https://www.google.com/')
        # Assert 'Google' in self.driver.title
        self.assertIn('Google', self.driver.title)


if __name__ == '__main__':
    unittest.main()