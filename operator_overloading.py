class Vector:
    def __init__(self,d):
        if type(d) is list:
            self._coords = [0] * (len(d))
            for i in range(self.__len__()):
                self._coords[i] = d[i]
        else:
            self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, key, value):
        self._coords[key] = value

    def __mul__(self, other):
        new_vector = Vector(self.__len__())
        for i in range(len(self._coords)):
            new_vector[i] = self._coords[i]*other
        return new_vector

a = Vector(5)
for i in range(5):
    a[i] = i+1
b = a*3
c=Vector([3,4,5,6])
print(c[1])