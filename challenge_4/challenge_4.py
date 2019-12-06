import unittest

from proj_options.base import Challenge
from proj_options.util import Fibo


class Challenge4(Challenge):

    fibo = None

    def setUp(self) -> None:
        """
        Override setUp to perform the same tasks
        As before, with some additional commands
        """
        super(Challenge4, self).setUp()
        self.fibo = Fibo(21)

    def test_challenge4(self):
        """
        Challenge 4:
        1. Calculate fibonacci sequence
        2. Display the numbers
        3. Display the string representation of the number
        """
        pass


if __name__ == '__main__':
    unittest.main()
