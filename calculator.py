# -*- coding: utf-8 -*-
"""Basic calculation classes including add, sub, mul, and div.

- Author: Hyungseok Shin
- Contact: hsshin@jmarple.ai
"""

from abc import ABC, abstractmethod


class Calculator(ABC):
    """An abstract class of basic computations."""

    @abstractmethod
    def operate(self: "Calculator", left: int, right: int) -> int:
        """Operate the defined calcuation with two given operands."""
        raise NotImplementedError


class Adder(Calculator):
    """Addition."""

    def operate(self: "Adder", left: int, right: int) -> int:
        """Add two integers.

        Test:
            >>> Adder().operate(0, 0)
            0
            >>> Adder().operate(-1, 2)
            1

        """
        return left + right


class Subtractor(Calculator):
    """Subtraction."""

    def operate(self: "Subtractor", left: int, right: int) -> int:
        """Subtract two integers.

        Test:
            >>> Subtractor().operate(0, 0)
            0
            >>> Subtractor().operate(-1, 2)
            -3
            >>> Subtractor().operate(2, 1)
            1

        """
        return left - right


class Multiplier(Calculator):
    """Muliplication."""

    def operate(self: "Multiplier", left: int, right: int) -> int:
        """Multiply two integers.

        Test:
            >>> Multiplier().operate(1, 0)
            0
            >>> Multiplier().operate(2, 3)
            6
            >>> Multiplier().operate(-2, 1)
            -2
            >>> Multiplier().operate(-1, -2)
            2

        """
        return left * right


class Divider(Calculator):
    """Division."""

    def operate(self: "Divider", left: int, right: int) -> int:
        """Divide two integers.

        Test:
            >>> Divider().operate(2, 1)
            2
            >>> Divider().operate(3, 2)
            1
            >>> Divider().operate(-2, 4)
            -1
            >>> Divider().operate(3, -2)
            -2
            >>> Divider().operate(2, 0)
            Traceback (most recent call last):
                ...
            ZeroDivisionError: integer division or modulo by zero

        """
        return left // right


if __name__ == "__main__":
    import doctest

    doctest.testmod()
