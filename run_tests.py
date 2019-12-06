import unittest

from challenge_1 import challenge_1 as ch1
from challenge_2 import challenge_2 as ch2
from challenge_3 import challenge_3 as ch3
from challenge_4 import challenge_4 as ch4
from challenge_5 import challenge_5 as ch5
from challenge_6 import challenge_6 as ch6
from challenge_7 import challenge_7 as ch7
from challenge_8 import challenge_8 as ch8

test_cases = (
    unittest.TestLoader().loadTestsFromModule(ch1),
    unittest.TestLoader().loadTestsFromModule(ch2),
    unittest.TestLoader().loadTestsFromModule(ch3),
    unittest.TestLoader().loadTestsFromModule(ch4),
    unittest.TestLoader().loadTestsFromModule(ch5),
    unittest.TestLoader().loadTestsFromModule(ch6),
    unittest.TestLoader().loadTestsFromModule(ch7),
    unittest.TestLoader().loadTestsFromModule(ch8),
)
for tc in test_cases:
    unittest.TextTestRunner(verbosity=2).run(tc)


if __name__ == '__main__':
    unittest.main()
