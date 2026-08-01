import unittest
from random import randint
import random
from my_files import makeCats
from my_files import Cat

class MakeCatsTests(unittest.TestCase):
    
    def test_regression(self):
        cats_test = []
        my_cats = makeCats()
        cats_test.append(Cat('Барсик', 5.0, 75))
        for i in range(len(my_cats)):
            self.assertEqual(my_cats[i].getCatName(), cats_test[i].getCatName())
            self.assertEqual(my_cats[i].getCatWeight(), cats_test[i].getCatWeight())
            self.assertEqual(my_cats[i].getCatPurr(), cats_test[i].getCatPurr())      
            
    def test_random(self):
        test_cats_list = []
        with open(f'cats.txt', 'wt') as file:
            for i in range (10):
                test_name = 'Барсик' + str(i)
                test_weight = round(random.random() * 20, 1)
                test_purr = randint(1,1000)
                test_cats_list.append(Cat(test_name, test_weight, test_purr))
                file.write(test_name + " ")
                file.write(str(test_weight) + " ")
                file.write(str(test_purr) + "\n")
        my_cats1 = makeCats()
        for i in range(len(my_cats1)):
            self.assertEqual(my_cats1[i].getCatName(), test_cats_list[i].getCatName())
            self.assertEqual(my_cats1[i].getCatWeight(), test_cats_list[i].getCatWeight())
            self.assertEqual(my_cats1[i].getCatPurr(), test_cats_list[i].getCatPurr())     
       
    def test_null(self):
        with open(f'cats.txt', 'wt') as file:
            file.write("")
        my_cats1 = makeCats()
        self.assertEqual(len(my_cats1), 0)       
          
    def test_strange(self):
        test_cats_list = []
        with open(f'cats.txt', 'wt') as file:
            for i in range (2):
                test_name = 'Барсик' + str(i)
                test_weight = round(random.random() * 1000000000, 1)
                test_purr = randint(-10000001,100000000)
                test_cats_list.append(Cat(test_name, test_weight, test_purr))
                file.write(test_name + " ")
                file.write(str(test_weight) + " ")
                file.write(str(test_purr) + "\n")
        my_cats1 = makeCats()
        for i in range(len(my_cats1)):
            self.assertEqual(my_cats1[i].getCatName(), test_cats_list[i].getCatName())
            self.assertEqual(my_cats1[i].getCatWeight(), test_cats_list[i].getCatWeight())
            self.assertEqual(my_cats1[i].getCatPurr(), test_cats_list[i].getCatPurr())      
        
if __name__ == '__main__':
    unittest.main()