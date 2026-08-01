import unittest
from random import randint
from my_files import createFiles

class CreateFilesTests(unittest.TestCase):
    def test_regression(self):
        createFiles()
        for i in range(1, 11):
            try:
                with open(f'{i}.txt', 'rt') as file_read:
                    for read_str in file_read:
                        nums = read_str.rstrip().split()
                        for i in range(len(nums)):
                            tmp = int(i)                                    
            except:
                pass        
                       
if __name__ == '__main__':
    unittest.main()                        