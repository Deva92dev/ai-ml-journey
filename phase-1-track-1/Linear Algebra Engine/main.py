import math

# that is how you must ask questions to google, What → Why → Should → When → How


class Vector:
    #  (*args) to allow instantiation like Vector(1, 2, 3) or Vector(1, 2, 3, 4)
    def __init__(self, *args):
        if not args:
            raise ValueError("Can not create an empty Vector")
        self.components = args
        if not all(isinstance(item, (float, int)) for item in self.components):
            raise TypeError("All items must be integer or float")

    def __iter__(self):
        yield from self.components

    def __len__(self):
        return len(self.components)   

    def __getitem__(self, key):
        return self.components[key]

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return self.components == other.components

    # asterisk unpacks the list *
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Both must be of same type")
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")

        result = Vector(*[a + b for a, b in zip(self.components, other.components)])
        return result

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Both must be of same type")
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")

        result = Vector(*[a - b for a, b in zip(self.components, other.components)])
        return result

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be int or float")

        result = Vector(*[x * scalar for x in self.components])
        return result

    def __rmul__(self, scalar):
        return self * scalar

    def dot_product(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Both must be of same type")
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions")

        result = sum(a * b for a, b in zip(self.components, other.components))
        return result

    # calculates magnitudes, euclidean norm
    def norm(self):
        return math.sqrt(sum(c * c for c in self.components))

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"


v = Vector(12, 3, 45)
w = Vector(15, 5, 65)
result = v.__add__(w)
print(result)


class Matrix:
    def __init__(self, *args):
        if not args:
            raise ValueError("Can not create an empty Matrix")
        self.rows = args
        for item in self.rows:
            if not isinstance(item, tuple):
                raise TypeError("Every item must be tuple")
            if not all(isinstance(every, (int, float)) for every in item):
                raise TypeError("Every item must be int or float")
        if not all(len(row) == len(self.rows[0]) for row in self.rows):
            raise ValueError("Every row must have the same length")

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, key):
        return self.rows[key]

    def __iter__(self):
        yield from self.rows

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented

        return self.rows == other.rows

    def __repr__(self):
        return f"Matrix({', '.join(map(str, self.rows))})"

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Both must be of same type")
        if len(self.rows) != len(other.rows) and len(self.rows[0]) != len(
            other.rows[0]
        ):
            raise ValueError("Both matrices must have the same dimension and order")

        result = tuple(
            tuple(a + b for a, b in zip(t1, t2))
            for t1, t2 in zip(self.rows, other.rows)
        )
        return result

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Both must be of same type")
        if len(self.rows) != len(other.rows) and len(self.rows[0]) != len(
            other.rows[0]
        ):
            raise ValueError("Both matrices must have the same dimension and order")

        result = tuple(
            tuple(a - b for a, b in zip(t1, t2))
            for t1, t2 in zip(self.rows, other.rows)
        )
        return result

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be int or float")

        result = [[x * scalar for x in each] for each in self.rows]
        answer = tuple(tuple(row) for row in result)
        return answer

    def transpose_matrix(self):
        row = len(self.rows)
        col = len(self.rows[0])
        transposed = []

        for j in range(col):
            new = []
            for i in range(row):
                new.append(self.rows[i][j])
            transposed.append(new)

        return transposed

    def vector_multiplication(self, vect):
        if not isinstance(vect, Vector):
            raise TypeError("Vect must be type of vector")
        if len(self.rows[0]) != len(vect):
            raise ValueError("Dimensions must match")

        result = [sum(m * v for m, v in zip(rows, vect)) for rows in self.rows]
        return result

    def matrix_multiplication(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Other must be type of matrix")
        if len(self.rows[0]) != len(other.rows):
            raise ValueError("Dimensions must match")


b = Vector(1,2,3)
a = Matrix((10, 20, 30), (40, 50, 60), (70, 80, 90))
m = Matrix((1, 2, 7), (3, 4, 8), (5, 6, 9))
n = Matrix((1, 2, 7), (3, 4, 8), (5, 6, 9))
v = m.__add__(n)
w = m.__sub__(n)
x = m.__mul__(5)
news = m.vector_multiplication(b)
print("vector mult with matrix: ", news)
print(x)
print(v)
print(w)
print(m)
print(m[2][0])
for item in m.rows:
    print(item[0], item[1], item[2])

new = a.transpose_matrix()
print(new)
