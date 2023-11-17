<<<<<<< HEAD
#Record class (to write to disk)

import Member 
import datetime

class Record():
    def __init__(self, inProvider: Member, inMember: Member):
        self.currentTime = None
        self.serviceDate = None
        self.provider = inProvider
        self.member = inMember
        self.serviceCode = None
        self.bill = None
        self.comments = None

    def setTime(self, inTime: datetime) -> None:
        self.currentTime = datetime.datetime.now()
        return
    
    def setDate(self, inDate: datetime) -> None:
        self.serviceDate = inDate
        return
    
    def setCode(self, inCode: int) -> bool:
        if (len(str(inCode)) != 6):
            print("Service code must be 6 digits long!")
            return False
        
        self.code = inCode
        return True
    
    def setBill(self, inBill: float) -> bool:
        if (inBill > 999.99):
            print("Can't charge them that much!")
            return False
        elif (inBill < 0):
            print("You can't pay them!")
            return False
        
        self.bill = inBill
        return True

    def setComments(self, inComments: str) -> bool:
        if (len(str(inComments)) > 100):
            print("Max length of comments is 100!")
            return False
        
        self.comments = inComments
=======
#Record class (to write to disk)

import datetime

class Record():
    def __init__(self, inTime: datetime = None, inServiceDate: datetime = None, inProv: int = None, 
                 inMem: int = None, inServ: int = None, inBill: float = None, inComments: str = None):
        
        self.currentTime = inTime
        self.serviceDate = inServiceDate
        self.providerID = inProv
        self.memberID = inMem
        self.serviceCode = inServ
        self.bill = inBill
        self.comments = inComments

    def setTime(self, inTime: datetime) -> None:
        self.currentTime = datetime.datetime.now()
        return
    
    def setDate(self, inDate: datetime) -> None:
        self.serviceDate = inDate
        return
    
    def setProv(self, inProv: int) -> bool:
        if (len(str(inProv)) != 9):
            print("Provider ID must be 9 digits long!")
            return False
        
        self.providerID = inProv
        return True
    
    def setMem(self, inMem: int) -> bool:
        if (len(str(inMem)) != 9):
            print("Member ID must be 9 digits long!")
            return False
        
        self.memberID = inMem
        return True

    def setCode(self, inCode: int) -> bool:
        if (len(str(inCode)) != 6):
            print("Service code must be 6 digits long!")
            return False
        
        self.code = inCode
        return True
    
    def setBill(self, inBill: float) -> bool:
        if (inBill > 999.99):
            print("Can't charge them that much!")
            return False
        elif (inBill < 0):
            print("You can't pay them!")
            return False
        
        self.bill = inBill
        return True

    def setComments(self, inComments: str) -> bool:
        if (len(str(inComments)) > 100):
            print("Max length of comments is 100!")
            return False
        
        self.comments = inComments
>>>>>>> master
        return True