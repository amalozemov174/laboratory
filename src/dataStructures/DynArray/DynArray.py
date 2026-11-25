import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1
        
#1. Добавьте метод insert(i, itm), который вставляет в i-ю позицию объект itm, сдвигая вперёд все последующие элементы. Учтите, что новая длина массива может превысить размер буфера.
    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        tmp_prev = self.array[i]
        if (self.count + 1) > self.capacity:
            self.resize(2*self.capacity)
        for index in range(i + 1, self.count + 1):
            if index == self.count:
                self.append(tmp_prev)
            else:
                tmp = self.array[index]
                self.array[index] = tmp_prev
                tmp_prev = tmp
        self.array[i] = itm
        
#2. Добавьте метод delete(i), который удаляет объект из i-й позиции, при необходимости сжимая буфер.
    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        tmp_next = self.array[self.count - 1]
        for index in range(self.count - 2, i - 1, -1):
            t1 = self.array[index]         
            self.array[index] = tmp_next
            tmp_next = t1
        self.count -= 1
        if self.count <= self.capacity * 0.5 and self.capacity > 16:
            size = int(self.capacity / 1.5)
            if size > 16:
                self.resize(size)
            else:
                self.resize(16)
                
#3. Оцените меры сложности для этих двух методов.
# Сложность для методов insert и delete равняется O(n) в худшем и общем случае, так необходимо сдвигать массив объектов на N при удалении или добавлении элементов. В лучшем случае сложность O(1) если происходит вставка в последний элемент или удаление последнено элемента       