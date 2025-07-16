from typing import Union

Number = Union[int, float]

class Calculator:
    """
    Core calculator class. Provides basic arithmetic operations.
    """

    def add(self, a: Number, b: Number) -> Number:
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        """Return the product of a and b."""
        return a * b

    def divide(self, a: Number, b: Number) -> Number:
        """
        Return the division of a by b.
        Raises ZeroDivisionError if b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b

    def power(self, a: Number, b: Number) -> Number:
        """Return a raised to the power of b."""
        return a ** b
