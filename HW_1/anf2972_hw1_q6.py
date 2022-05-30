class Vector:

    def __init__(self, d):
        if isinstance(d, list):
            self.coords = d
        else:
            self.coords = [0] * d

    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] - other[i]
        return result

    def __mul__(self, other):

        total = 0
        if isinstance(other, int):
            return Vector([i * other for i in self.coords])
        else:
            for j in range(len(self)):
               total += (other[j] * self[j])
            return total

    def __rmul__(self, other):
        return Vector([i * other for i in self.coords])

    def __neg__(self):
        new_val = Vector([-1 * x for x in self.coords])
        return new_val

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return str(self.coords)






