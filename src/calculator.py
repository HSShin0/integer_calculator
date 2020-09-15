# -*- coding: utf-8 -*-
"""Basic calculation classes including add, sub, mul, and div.

- Author: Hyungseok Shin
- Contact: hsshin@jmarple.ai
"""

from abc import ABC


class Calculator(ABC):
    """An abstract class of basic computations."""

    def operate(self: "Calculator", left: int, right: int) -> int:
        """Operate the defined calcuation with two given operands."""
        raise NotImplementedError


class Adder(Calculator):
    """Addition."""

    def operate(self: "Adder", left: int, right: int) -> int:
        """Add two integers."""
        return left + right


class Subtractor(Calculator):
    """Subtraction."""

    def operate(self: "Subtractor", left: int, right: int) -> int:
        """Subtract two integers."""
        return left - right


class Multiplier(Calculator):
    """Muliplication."""

    def operate(self: "Multiplier", left: int, right: int) -> int:
        """Multiply two integers."""
        return left * right


class Divider(Calculator):
    """Division."""

    def operate(self: "Divider", left: int, right: int) -> int:
        """Divide two integers."""
        return left // right
