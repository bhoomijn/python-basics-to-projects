"""
Unit tests for basic problems module
"""

import pytest
from exercises.basic_problems import (
    find_largest,
    sum_of_natural_numbers,
    multiplication_table,
)


class TestFindLargest:
    """Test cases for find_largest function"""

    def test_largest_of_three_positive_numbers(self):
        """Test finding largest among positive numbers"""
        assert find_largest([10, 20, 30]) == 30

    def test_largest_with_negatives(self):
        """Test finding largest with negative numbers"""
        assert find_largest([-10, -5, -20]) == -5


class TestSumOfNaturalNumbers:
    """Test cases for sum_of_natural_numbers function"""

    def test_sum_of_first_five(self):
        """Test sum of first 5 natural numbers (should be 15)"""
        assert sum_of_natural_numbers(5) == 15

    def test_sum_of_first_ten(self):
        """Test sum of first 10 natural numbers (should be 55)"""
        assert sum_of_natural_numbers(10) == 55


class TestMultiplicationTable:
    """Test cases for multiplication_table function"""

    def test_multiplication_table_of_five(self):
        """Test multiplication table of 5"""
        result = multiplication_table(5)
        assert result == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
