import pytest
from app.app import dedupe, calculate_sum

def test_dedupe():
    assert list(dedupe([1,2,2,3])) == [1,2,3]
    assert list(dedupe(['a','b','a','c'])) == ['a','b','c']

def test_calculate_sum():
    assert calculate_sum([1,2,3]) == 6
    assert calculate_sum([-1,0,1]) == 0
