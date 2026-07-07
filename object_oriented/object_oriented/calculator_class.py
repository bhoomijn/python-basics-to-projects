# calculator_class.py
# Simple Calculator class with square, cube, and square root methods

class Calculator:
    def __init__(self, number: float):
        self.number = number

    def square(self) -> float:
        """Return the square of the number"""
        return self.number ** 2

    def cube(self) -> float:
        """Return the cube of the number"""
        return self.number ** 3

    def square_root(self) -> float:
        """Return the square root of the number"""
        return self.number ** 0.5


if __name__ == "__main__":
    a = Calculator(4)
    print("Square:", a.square())        # 16
    print("Cube:", a.cube())            # 64
    print("Square Root:", a.square_root())  # 2.0
