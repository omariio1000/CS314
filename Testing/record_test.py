from Record import Record
from datetime import datetime
import pytest

def test_contructor_empty():
    test = Record()
    assert test.currentTime == None
    assert test.serviceDate == None
    assert test.providerID == None
    assert test.memberID == None
    assert test.serviceCode == None
    assert test.bill == None
    assert test.comments == None


def test_contructor_vals():
    aDate = Date
    test = Record("a time",29, "a providerID", "a memberID", "OR", 97000, True)
    assert test.currentTime == "a time"
    assert test.serviceDate == 29
    assert test.providerID == "a providerID"
    assert test.memberID == "a memberID"
    assert test.serviceCode == "OR"
    assert test.bill == 97000
    assert test.comments == True

def test_wrong_type():
    with pytest.raises(TypeError):
        Record("a time", "29", "a providerID", "a memberID", "OR", 97000, True)

def test_wrong_value():
    with pytest.raises(ValueError):
        Record("a time", 29, "a providerID", "a memberID", "a serviceCode", 97000, True)


def test_setters_time():
    test = Record()
    assert test.setTime("a time") == True
    assert test.currentTime == "a time"

def test_setters_date():
    test = Record()
    assert test.setDate(29) == True
    assert test.serviceDate == 29

def test_setters_provider():
    test = Record()
    assert test.setProv("a providerID") == True
    assert test.providerID == "a providerID"

def test_setters_memberID():
    test = Record()
    assert test.setMem("a memberID") == True
    assert test.memberID == "a memberID"

def test_setters_serviceCode():
    test = Record()
    assert test.setCode("OR") == True
    assert test.serviceCode == "OR"

def test_setters_bill():
    test = Record()
    assert test.setBill(97000) == True
    assert test.bill == 97000

def test_setters_comments():
    test = Record()
    test.setComments(True)
    assert test.comments == True



def test_setters_time_incorrect():
    test = Record()
    with pytest.raises(TypeError):
        test.setTime(29)

def test_setters_date_incorrect():
    test = Record()
    with pytest.raises(TypeError):
        test.setDate("29")

def test_setters_provider_incorrect():
    test = Record()
    with pytest.raises(TypeError):
        test.setProv(29)

def test_setters_memberID_incorrect():
    test = Record()
    with pytest.raises(TypeError):
        test.setMem(29)

def test_setters_serviceCode_incorrect():
    test = Record()
    with pytest.raises(TypeError):
        test.setCode(29)

def test_setters_bill_incorrect():
    test = Record()
    with pytest.raises(TypeError):
        test.setBill("29")

#def test_setters_comments_incorrect():
#    test = Record()
#    with pytest.raises(ValueError):
#        test.setComments(5)




def test_setters_time_incorrect_value():
    test = Record()
    assert test.setTime("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") == False

#def test_setters_date_incorrect_value():
#    test = Record()
#   assert test.setDate(1000000000) == False

def test_setters_provider_incorrect_value():
    test = Record()
    assert test.setProv("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") == False

def test_setters_memberID_incorrect_value():
    test = Record()
    assert test.setMem("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") == False

def test_setters_serviceCode_incorrect_value():
    test = Record()
    assert test.setCode("AAA") == False

#def test_setters_bill_incorrect_value():
#    test = Record()
#    assert test.setBill(1000000000) == False

#def test_setters_comments_incorrect_value():
#    test = Record()
#    with pytest.raises(TypeError):
#        test.setComments("29")

