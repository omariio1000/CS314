import pytest
from Manager import manager

def test_constructor():
    test = manager(1,2,3)
    assert test.providers == 1
    assert test.members == 2
    assert test.records == 3

def test_valid_welcome():
    test = manager()
    print("Enter valid data(1-3)\n")
    result = test.welcome()
    assert result == 1

def test_invalid_welcome():
    test = manager()
    print("Enter invalid data\n")
    result = test.welcome()
    assert result == 0
