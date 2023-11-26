from Service import Service
import pytest

def test_contructor_empty():
    test = Service()
    assert test.name == None
    assert test.code == None
    assert test.desc == None
    assert test.cost == None


def test_contructor_vals():
    test = Service(29, "a name", "a desc", 2.9)
    assert test.name == "a name"
    assert test.code == 29
    assert test.desc == "a desc"
    assert test.cost == 2.9

def test_wrong_type():
    with pytest.raises(TypeError):
        Service("29", "a name", "a desc", 2.9)

def test_wrong_value():
    with pytest.raises(ValueError):
        Service(29, "a name AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "a desc", 2.9)


def test_setters_name():
    test = Service()
    assert test.setName("a name") == True
    assert test.name == "a name"

def test_setters_code():
    test = Service()
    assert test.setCode(29) == True
    assert test.code == 29

def test_setters_desc():
    test = Service()
    assert test.setDesc("a desc") == True
    assert test.desc == "a desc"

def test_setters_cost():
    test = Service()
    assert test.setCost(2.9) == True
    assert test.cost == 2.9




def test_setters_name_incorrect():
    test = Service()
    with pytest.raises(TypeError):
        test.setName(29)

def test_setters_code_incorrect():
    test = Service()
    with pytest.raises(TypeError):
        test.setCode("29")

def test_setters_desc_incorrect():
    test = Service()
    with pytest.raises(TypeError):
        test.setDesc(29)

def test_setters_cost_incorrect():
    test = Service()
    with pytest.raises(TypeError):
        test.setCost("29")



def test_setters_name_incorrect_value():
    test = Service()
    assert test.setName("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") == False

def test_setters_code_incorrect_value():
    test = Service()
    assert test.setCode(1000000000) == False

def test_setters_desc_incorrect_value():
    test = Service()
    assert test.setDesc("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") == False


def test_setters_cost_incorrect_value():
    test = Service()
    assert test.setCost(2999.9) == False


