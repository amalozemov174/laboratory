import unittest
from random import randint
from sortArray import sortArray

class SortArrayTests(unittest.TestCase):
    
    def test_regression(self):
        self.assertEqual(sortArray([3, 2, 1]), [1, 2, 3])
        
    def test_random(self):
        m1 = []
        m2 = []
        for i in range(10000):
          x = randint(-25,+25)
          m1.append(x)
          m2.append(x)
        res_my = sortArray(m1)
        m2.sort()
        self.assertEqual(res_my, m2)    
       
    def test_null(self):
        m1 = []
        m2 = []
        res_my = sortArray(m1)
        m2.sort()
        self.assertEqual(res_my, m2)   
        
    def test_max(self):
          self.assertEqual(sortArray([9223372036854775808, -2, -999999999, 0, 999999999]), [-999999999, -2, 0, 999999999, 9223372036854775808])
          
    def test_strange(self):
        try:
            strng = [9223372036854775808, "-2", -999999999, 0, 999999999]
            res = sortArray(strng)
            self.assertTrue(False) # fail
        except:
              pass # success      
        
if __name__ == '__main__':
    unittest.main()