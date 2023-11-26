import pytest
from Manager import manager


def test_constructor():
    test = manager(1, 2, 3)
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
    print("Enter invalid data")
    result = test.welcome()
    assert result == 0


def test_invlaid_edit_member():
    test = manager()
    print("Enter invalid data")
    result = test.edit_member()
    assert result == 0


def test_valid_edit_member():
    test = manager()
    print("Enter valid data 1 - 7")
    result = test.edit_member()
    assert result == 1


def test_valid_search_mem():
    test = manager()
    test.members = {123456789: "Najiib"}
    assert test.search_member(123456789) is True


def test_valid_remove_mem():
    test = manager()
    test.members = {123456789: "Najiib"}
    print("Enter 123456789 as key")
    result = test.remove_member()
    assert result == 1
    assert (123456789 in test.members) is False


def test_invalid_remove_mem():
    test = manager()
    result = test.add_member()
    assert result == 0


def test_invalid_mem():
    test = manager()
    test.members = {13456789: "Najiib"}
    assert test.search_member(123) is False


def test_add_mem():
    test = manager()
    result = test.add_member()
    assert result in test.members


def test_valid_remove_mem():
    test = manager()
    test.members = {123456789: "Najiib"}
    print("Enter this key: 123456789")
    result = test.remove_member()
    assert result == 1


def test_invalid_remove_mem():
    test = manager()
    result = test.remove_member()
    assert result == 0


def test_add_provider():
    test = manager()
    result = test.add_provider()
    assert result in test.providers
