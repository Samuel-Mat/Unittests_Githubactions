import pytest
import calculator
import unittest


def test_add(self):
    # Given: I want to add a to-do with a date
    x = 3
    y = 2
    expectedResult = 5

    # When: I add the item
    realresult = calculator.add(x,y)

    # Then: The most recently added to-do should have a date
    self.assertEqual(expectedResult, realresult)
