#5.* Реализуйте динамический массив на основе банковского метода.
import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)
        self.coins = 0

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
            self.coins -= 1
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1
        self.coins += 2

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        tmp_prev = self.array[i]
        if (self.count + 1) > self.capacity:
            self.resize(2*self.capacity)
        for index in range(i + 1, self.count + 1):
            if index == self.count:
                self.array[self.count] = tmp_prev
                self.count += 1
                #self.append(tmp_prev)
            else:
                tmp = self.array[index]
                self.array[index] = tmp_prev
                tmp_prev = tmp
        self.coins += 2        
        self.array[i] = itm

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        tmp_next = self.array[self.count - 1]
        for index in range(self.count - 2, i - 1, -1):
            t1 = self.array[index]         
            self.array[index] = tmp_next
            tmp_next = t1
        if self.count <= self.capacity * 0.5 and self.capacity > 16:
            size = int(self.capacity / 1.5)
            if size > 16:
                self.resize(size)
            else:
                self.resize(16)
        self.coins += 1
        self.count -= 1

#6.* Реализуйте многомерный динамический массив: произвольное количество измерений, при этом каждое измерение может внутри масштабироваться по потребности. В конструкторе задаётся число измерений и размер по каждому из них. Обращаться к такому массиву надо как к обычному многомерному, например: myArr[1,2,3].

import ctypes

class DynArray:
    
    def __init__(self, level, size):
        self.count = 0
        self.size = size
        self.capacity = 16
        self.level = level
        if self.level > 1:
            self.array = self.make_array(self.capacity)
            for i in range(self.size[0]):
                 self.append(DynArray(self.level - 1, self.size[1:]))
        else:
            self.array = self.make_array(self.capacity)
            for i in range(self.size[0]):
                self.append(None)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__ (self, indexes):
        if len(indexes) != self.level:
            raise IndexError('Index is out of bounds')
        current = self
        for i in range(len(indexes)):
            idx = indexes[i]
            if idx < 0 or idx >= current.count:
                raise IndexError('Index is out of bounds')
            current = current.array[idx]
        return current
   
    def __setitem__ (self, indexes, val):
        if len(indexes) != self.level:
            raise IndexError('Index is out of bounds')
        current = self
        for i in range(len(indexes)):
            idx = indexes[i]
            if i == len(indexes) - 1:
                current.array[idx] = val
            else:         
                if idx < 0 or idx >= current.count:
                    raise IndexError('Index is out of bounds')
            current = current.array[idx]

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