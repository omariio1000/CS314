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
    dateString = '09-19-2022'
    dateTest = datetime.strptime(dateString, '%m-%d-%Y').date()
    timeString = '13::55::26'
    timeTest = datetime.strptime(timeString, '%H::%M::%S').time()


    test = Record(timeTest, dateTest, 29, 2929, 292929, 2.9, "a comment")
    assert test.currentTime == timeTest
    assert test.serviceDate == dateTest
    assert test.providerID == 29
    assert test.memberID == 2929
    assert test.serviceCode == 292929
    assert test.bill == 2.9
    assert test.comments == "a comment"

def test_wrong_type():
    dateString = '09-19-2022'
    dateTest = datetime.strptime(dateString, '%m-%d-%Y').date()
    timeString = '13::55::26'
    timeTest = datetime.strptime(timeString, '%H::%M::%S').time()
    with pytest.raises(TypeError):
        Record(timeTest, dateTest, "29", 2929, 292929, 2.9, "a comment")

def test_wrong_value():
    dateString = '09-19-2022'
    dateTest = datetime.strptime(dateString, '%m-%d-%Y').date()
    timeString = '13::55::26'
    timeTest = datetime.strptime(timeString, '%H::%M::%S').time()
    with pytest.raises(ValueError):
        Record(timeTest, dateTest, 29, 2929, 292929, 2999.9, "a comment")


def test_setters_time():
    test = Record()
    timeString = '13::55::26'
    timeTest = datetime.strptime(timeString, '%H::%M::%S').time()
    test.setTime(timeTest)
    assert test.currentTime == timeTest

def test_setters_date():
    test = Record()
    dateString = '09-19-2022'
    dateTest = datetime.strptime(dateString, '%m-%d-%Y').date()
    assert test.setDate(dateTest) == True
    assert test.serviceDate == dateTest

def test_setters_provider():
    test = Record()
    assert test.setProv(29) == True
    assert test.providerID == 29

def test_setters_memberID():
    test = Record()
    assert test.setMem(2929) == True
    assert test.memberID == 2929

def test_setters_serviceCode():
    test = Record()
    assert test.setCode(292929) == True
    assert test.serviceCode == 292929

def test_setters_bill():
    test = Record()
    assert test.setBill(2.9) == True
    assert test.bill == 2.9

def test_setters_comments():
    test = Record()
    test.setComments("a comment") == True
    assert test.comments == "a comment"



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
        test.setProv("29")

def test_setters_memberID_incorrect():
    test = Record()
    with pytest.raises(TypeError):
        test.setMem("29")

def test_setters_serviceCode_incorrect():
    test = Record()
    with pytest.raises(TypeError):
        test.setCode("29")

def test_setters_bill_incorrect():
    test = Record()
    with pytest.raises(TypeError):
        test.setBill("29")

def test_setters_comments_incorrect():
    test = Record()
    with pytest.raises(ValueError):
        test.setComments(5)




def test_setters_time_incorrect_value():
    test = Record()
    with pytest.raises(AttributeError):
        test.setTime()

def test_setters_date_incorrect_value():
    test = Record()
    with pytest.raises(ValueError):
        test.setTime()

def test_setters_provider_incorrect_value():
    test = Record()
    assert test.setProv(1000000000) == False

def test_setters_memberID_incorrect_value():
    test = Record()
    assert test.setMem(1000000000) == False

def test_setters_serviceCode_incorrect_value():
    test = Record()
    assert test.setCode(1000000000) == False

def test_setters_bill_incorrect_value():
    test = Record()
    assert test.setBill(2999.9) == False

def test_setters_comments_incorrect_value():
    test = Record()
    assert test.setComments("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") == False


