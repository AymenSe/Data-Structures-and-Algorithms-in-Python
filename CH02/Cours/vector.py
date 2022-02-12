from unittest import result


class Vector:
    """ Represent a vector in a multidimensional space """

    def __init__(self, d) -> None:
        """ Create a D-dimensional vector of zeros """
        self._coords = [0] * d

    def __len__(self) -> int:
        """ Return the dimension of the vector """
        return len(self._coords)
    
    def __getitem__(self, j) -> float:
        """ Return j-th coordinate of vector """
        return self._coords[j]
    
    def __setitem__(self, j, value) -> None:
        """ Set j-th coordinate of vector to given value """
        self._coords[j] = value
    
    def __add__(self, other):
        """ Return sum of two vectors """
        if len(self) != len(other):
            raise ValueError('dimensions must agree!')
        res = Vector(len(other))
        for j in range(len(self)):
            res[j] = self[j] + other[j]
        return res

    def __eq__(self, other) -> bool:
        """ Return True if vector has same coordinates as other """
        return self._coords == other._coords
        
    def __ne__(self, other) -> bool:
        """ Return True if vector has different coordinates from other """
        return not self == other # rely on existing __eq__ definition
    
    def __str__(self) -> str:
        """ Produce string representation of vector """
        return '<' + str(self._coords)[1:-1] + '>'
    

if __name__ == '__main__':
    v1 = Vector(3)
    v2 = Vector(3)
    v3 = Vector(4)

    
    for i in range(len(v1)):
        v1[i] = i + 1
        v2[i] = 2 * (i + 1)

    for i in range(len(v3)):
        v3[i] = 5*i
    
    v = v1 + v2
    print(v1)
    print(v2)
    print(v)

    # print(v + v3)
        
        

