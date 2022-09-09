
import ctypes


class DynamicArray(object):
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.Arr = self.make_array(self.capacity)

    def __len__(self):
        return self.size

    def __getitem__(self, k):
        if 0 <= k < self.size:
            return self.arr[k]
        return IndexError("Out of bounds!")

    def append(self, element):
        if self.size == self.capacity:
            self._resize(2*self.capacity)
        self.Arr[self.size]= element
        self.size += 1

    def insertAt(self, item, index):
        if not 0<=index<self.size:
            return IndexError("Out of bounds!")
        if self.size == self.capacity:
            self._resize(2*self.capacity)
        for i in range(index,self.size):
            self.arr[i+1] = self.arr[i]
        self.arr[index] = item
        self.size += 1

    def delete(self):
        if self.size == 0:
            return IndexError("Array is empty")
        self.size -= 1

    def removeAt(self,idx):
        if self.size == 0:
            return IndexError("Array is empty")
        if not 0<=idx<self.size:
            return IndexError("Index out of bounds")
        for i in range(idx,self.Arr):
            self.arr[i] = self.arr[i+1]
        self.Arr[self.size] = 0
        self.size -= 1

    def _resize(self, new_cap):
        new_Arr = self.make_array(new_cap)
        for i in range(self.size):
            new_Arr[i] = self.Arr[i]

        self.Arr = new_Arr
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap*ctypes.py_object) ()

    def print_arr(self):
        for i in range(self.size):
            print(self.Arr[i])
