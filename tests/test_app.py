import pytest
from app.app import dedupe, calculate_sum

# 测试去重功能
def test_dedupe():
    assert dedupe([1,2,2,3]) == [1,2,3]
    assert dedupe([]) == []
    assert dedupe(["a","b","a"]) == ["a","b"]

# 测试求和功能
def test_calculate_sum():
    assert calculate_sum([1,2,3]) == 6
    assert calculate_sum([0, -1, 1]) == 0
