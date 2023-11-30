from Provider import Provider
import pytest

def test_addService_positive():
    test = Provider()
    assert test.addService(5) == True
    assert test.serviceCodes.__contains__(5) == True


def test_addService_incorrect():
    test = Provider()
    with pytest.raises(TypeError):
        test.addService("29") 

def test_addService_incorrect_below_zero():
    test = Provider()
    with pytest.raises(ValueError):
        test.addService(-5)


def test_addService_incorrect_repeat():
    test = Provider()
    assert test.addService(5) == True
    assert test.serviceCodes.__contains__(5) == True
    assert test.addService(5) == False


def test_removeService_positive():
    test = Provider()
    assert test.addService(5) == True
    assert test.serviceCodes.__contains__(5) == True
    assert test.removeService(5) == True
    assert test.serviceCodes.__contains__(5) == False

def test_removeService_incorrect():
    test = Provider()
    with pytest.raises(TypeError):
        test.removeService("29") 

def test_removeService_incorrect_not_in_list():
    test = Provider()
    assert test.serviceCodes.__contains__(1) == False
    assert test.removeService(1) == False