from Member import Member
import pytest

def test_contructor_empty():
    test = Member()
    assert test.name == None
    assert test.number == None
    assert test.address == None
    assert test.city == None
    assert test.state == None
    assert test.zipCode == None
    assert test.status == None


def test_contructor_vals():
    test = Member("a name",29, "a address", "a city", "OR", 97000, True)
    assert test.name == "a name"
    assert test.number == 29
    assert test.address == "a address"
    assert test.city == "a city"
    assert test.state == "OR"
    assert test.zipCode == 97000
    assert test.status == True

def test_wrong_type():
    with pytest.raises(TypeError):
        Member("a name", "29", "a address", "a city", "OR", 97000, True)

def test_wrong_value():
    with pytest.raises(ValueError):
        Member("a name", 29, "a address", "a city", "a state", 97000, True)


def test_setters_name():
    test = Member()
    assert test.setName("a name") == True
    assert test.name == "a name"

def test_setters_number():
    test = Member()
    assert test.setNumber(29) == True
    assert test.number == 29

def test_setters_address():
    test = Member()
    assert test.setAddr("a address") == True
    assert test.address == "a address"

def test_setters_city():
    test = Member()
    assert test.setCity("a city") == True
    assert test.city == "a city"

def test_setters_state():
    test = Member()
    assert test.setState("OR") == True
    assert test.state == "OR"

def test_setters_zip_code():
    test = Member()
    assert test.setZip(97000) == True
    assert test.zipCode == 97000

def test_setters_status():
    test = Member()
    test.setStatus(True)
    assert test.status == True



def test_setters_name_incorrect():
    test = Member()
    with pytest.raises(TypeError):
        test.setName(29)

def test_setters_number_incorrect():
    test = Member()
    with pytest.raises(TypeError):
        test.setNumber("29")

def test_setters_address_incorrect():
    test = Member()
    with pytest.raises(TypeError):
        test.setAddr(29)

def test_setters_city_incorrect():
    test = Member()
    with pytest.raises(TypeError):
        test.setCity(29)

def test_setters_state_incorrect():
    test = Member()
    with pytest.raises(TypeError):
        test.setState(29)

def test_setters_zip_code_incorrect():
    test = Member()
    with pytest.raises(TypeError):
        test.setZip("29")

#def test_setters_status_incorrect():
#    test = Member()
#    with pytest.raises(TypeError):
#        test.setStatus(5)




def test_setters_name_incorrect_value():
    test = Member()
    assert test.setName("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") == False

#def test_setters_number_incorrect_value():
#    test = Member()
#   assert test.setNumber(1000000000) == False

def test_setters_address_incorrect_value():
    test = Member()
    assert test.setAddr("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") == False

def test_setters_city_incorrect_value():
    test = Member()
    assert test.setCity("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") == False

def test_setters_state_incorrect_value():
    test = Member()
    assert test.setState("AAA") == False

#def test_setters_zip_code_incorrect_value():
#    test = Member()
#    assert test.setStatus(1000000000) == False

#def test_setters_status_incorrect_value():
#    test = Member()
#    with pytest.raises(TypeError):
#        test.setStatus("29")

