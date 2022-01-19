import unittest
from models import random
Random = random.Random

class RandomQuotesTest(unittest.TestCase):
    '''
    Test the behaviour of the Random class
    '''
    def setUp(self):
        self.new_quote = Random("JohnDoe", "An example of a quote")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote, Random))


if __name__ == '__main__':
    unittest.main()