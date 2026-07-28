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
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")

        result = Vector(*[a + b for a, b in zip(self.components, other.components)])
        return result

    def __sub__(self, other):
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
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions")

        result = sum(a * b for a, b in zip(self.components, other.components))
        return result

    # calculates magnitudes, euclidean norm
    def norm(self):
        return math.sqrt(sum(c * c for c in self.components))

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"


class Matrix:
    def __init__(self, rows):
        self.rows = rows
        self.cols = rows[0]
