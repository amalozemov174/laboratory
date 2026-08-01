import unittest
from random import randint
from my_files import readFiles

class ReadFilesTests(unittest.TestCase):
    def test_regression(self):
        self.assertIsNotNone(readFiles())
                               
if __name__ == '__main__':
    unittest.main()   