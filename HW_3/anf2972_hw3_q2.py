import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0

    def __len__(self):
        return self.n

    def insert(self, index, val):
        if index < -self.n or index > self.n:
            raise IndexError
        else:
            if self.n == self.capacity:
                self.resize(2 * self.capacity)
            for i in range(self.n, index, -1):
                self.data_arr[i] = self.data_arr[i - 1]
            self.data_arr[index] = val
            self.n+=1

    def pop(self, index = -1):
        if self.n == 0 or (index < -self.n or index > self.n):
             raise IndexError
        else:
            if index == -1:
                temp = self.data_arr[self.n - 1]
                self.data_arr[self.n-1] = None
                self.n -= 1
                if ((self.n) < (self.capacity // 4)):
                    self.resize(self.capacity // 2)
                return temp
            else:
                temp = self.data_arr[index]
                self.data_arr[index] = None
                for j in range (index+1, self.n):
                    self.data_arr[j-1] = self.data_arr[j]
                self.n -= 1
                if ((self.n) < (self.capacity // 4)):
                    self.resize(self.capacity // 2)
                return temp

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size


    def __getitem__(self, ind):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        return self.data_arr[ind]


    def __setitem__(self, ind, val):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        self.data_arr[ind] = val


    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]


    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)



