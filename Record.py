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
        return True