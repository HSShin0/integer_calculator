# -*- coding: utf-8 -*-
"""Basic calculation classes including add, sub, mul, and div.

- Author: Hyungseok Shin
- Contact: hsshin@jmarple.ai
"""

from abc import ABC, abstractmethod


class Calculator(ABC):
    """An abstract class of basic computations."""

    @abstractmethod
    def operate(self: "Calculator", x: int, y: int) -> int:
        """Operate the defined calcuation with two given operands.

        Args:
            x (int): left operand.
            y (int): right operand.

        Returns:
            int: Calcalated result.

        """
        pass


class Adder(Calculator):
    """Addition."""

    def operate(self: "Adder", x: int, y: int) -> int:
        """Add two integers."""
        pass


class Subtractor(Calculator):
    """Subtraction."""

    def operate(self: "Subtractor", x: int, y: int) -> int:
        """Subtract two integers."""
        pass


class Multiplier(Calculator):
    """Muliplication."""

    def operate(self: "Multiplier", x: int, y: int) -> int:
        """Multiply two integers."""
        pass


class Divider(Calculator):
    """Division."""

    def operate(self: "Divider", x: int, y: int) -> int:
        """Divide two integers."""
        pass
