# vector_inheritance.py
# Demonstrates inheritance in Python with 2D and 3D vectors

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The Vector is ({self.i}i + {self.j}j)")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)  # call parent constructor
        self.k = k

    def show(self):
        print(f"The Vector is ({self.i}i + {self.j}j + {self.k}k)")


# Object creation
a = TwoDVector(1, 2)
b = ThreeDVector(3, 4, 5)

# Displaying vectors
a.show()   # Output: The Vector is (1i + 2j)
b.show()   # Output: The Vector is (3i + 4j + 5k)
