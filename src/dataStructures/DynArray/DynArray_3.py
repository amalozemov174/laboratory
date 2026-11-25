import unittest
from DynArray import DynArray
#4. Напишите тесты, проверяющие работу методов insert() и delete():

class DynArrayTests(unittest.TestCase):
    
    def DynArrayToList(self, myDynArray):
        res = []
        tmp = myDynArray.count
        for el in range(myDynArray.count):
            res.append(myDynArray.__getitem__(el))
        return res

#4.1. вставка элемента, когда в итоге размер буфера не превышен (проверьте также размер буфера);
        
    def test_add_low_then_buffer(self):
        da = DynArray()        
        da.append(1)
        da.append(2)
        da.append(3)
        da.append(4)
        da.append(5)    
        da.insert(3, 99)
        self.assertEqual(self.DynArrayToList(da), [1, 2, 3, 99, 4, 5])
        self.assertEqual(da.capacity, 16)
        
#4.1.1. вставка в пустой список;
        
    def test_add_low_then_buffer(self):
        da = DynArray()        
        da.insert(0, 99)
        self.assertEqual(self.DynArrayToList(da), [99])
        self.assertEqual(da.capacity, 16)        

#4.2 вставка элемента, когда в результате превышен размер буфера (проверьте также корректное изменение размера буфера);

    def test_add_more_then_buffer(self):
        da = DynArray()        
        for i in range(30):
            da.append(i)    
        da.insert(3, 99)
        self.assertEqual(self.DynArrayToList(da), [0, 1, 2, 99, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
        self.assertEqual(da.capacity, 32)

#4.3 попытка вставки элемента в недопустимую позицию;

    def test_add_not_exist_element(self):
        da = DynArray()        
        for i in range(30):
            da.append(i)            
        try:
            da.insert(100, 99)
        except:
              pass # success      
        self.assertEqual(da.capacity, 32)

#4.4 удаление элемента, когда в результате размер буфера остаётся прежним (проверьте также размер буфера);

    def test_delete_low_then_buffer(self):
        da = DynArray()
        for i in range(5):
            da.append(i)            
        da.delete(3)
        self.assertEqual(self.DynArrayToList(da), [0, 1, 2, 4])
        self.assertEqual(da.capacity, 16)

#4.5 удаление элемента, когда в результате понижается размер буфера (проверьте также корректное изменение размера буфера);

    def test_delete_resize_buffer(self):
        da = DynArray()
        for i in range(40):
            da.append(i)
        for i in range(30):
            da.delete(0)                            
        self.assertEqual(self.DynArrayToList(da), [30, 31, 32, 33, 34, 35, 36, 37, 38, 39])
        self.assertEqual(da.capacity, 18)

#4.6 попытка удаления элемента в недопустимой позиции.

    def test_delete_not_exist_element(self):
        da = DynArray()        
        for i in range(30):
            da.append(i)            
        try:
            da.delete(100, 99)
        except:
              pass # success      
        self.assertEqual(da.capacity, 32)

if __name__ == '__main__':
    unittest.main()
    