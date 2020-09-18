# -*- coding: utf-8 -*-
"""Test cases for Calculators.

- Author: Hyungseok Shin
- Contact: hsshin@jmarple.ai
"""

import pytest

from src.calculator import Adder, Calculator, Divider, Multiplier, Subtractor


class TestCalculator:
    def test_abstract_calculator(self):
        with pytest.raises(NotImplementedError):
            assert Calculator().operate(0, 0)


class TestAdder:
    def test_zeros(self):
        assert Adder().operate(0, 0) == 0

    def test_neg(self):
        assert Adder().operate(-1, 2) == 1


#    def test_dummy(self):
#        """A dummy test for varifying pre-push hook."""
#        assert Adder().operate(11, 13) == 0


class TestSubtractor:
    def test_zeros(self):
        assert Subtractor().operate(0, 0) == 0

    def test_neg(self):
        assert Subtractor().operate(-1, 2) == -3

    def test_standard(self):
        assert Subtractor().operate(2, 1) == 1


class TestMultiplier:
    def test_multiply_zero(self):
        assert Multiplier().operate(1, 0) == 0

    def test_standard(self):
        assert Multiplier().operate(2, 3) == 6

    def test_neg(self):
        assert Multiplier().operate(-2, 1) == -2

    def test_neg_x_neg_is_pos(self):
        assert Multiplier().operate(-1, -2) == 2


class TestDivider:
    def test_standard(self):
        assert Divider().operate(2, 1) == 2

    def test_nonzero_remainder(self):
        assert Divider().operate(3, 2) == 1

    def test_neg_numerator_nonzero_remainder(self):
        assert Divider().operate(-2, 4) == -1

    def test_neg_denominator_nonzero_remainder(self):
        assert Divider().operate(3, -2) == -2

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            Divider().operate(2, 0)
