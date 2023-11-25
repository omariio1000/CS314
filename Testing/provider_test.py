from Provider import Provider
import pytest

def test_addService_positive():
    test = Provider()
    assert test.addService(5) == True
    assert test.services.__contains__(5) == True


def test_addService_incorrect():
    test = Provider()
    with pytest.raises(TypeError):
        test.addService("29") 