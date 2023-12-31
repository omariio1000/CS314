#Record class (to write to disk)

from datetime import datetime
from typing import Union
class Record():
    def __init__(self, inTime: datetime = None, inServiceDate: datetime = None, inProv: int = None, 
                 inMem: int = None, inServ: int = None, inBill: float = None, inComments: str = None):
        
        self.currentTime = None
        self.serviceDate = None
        self.providerID = None
        self.memberID = None
        self.serviceCode = None
        self.bill = None
        self.comments = None

        if (inServiceDate == None and inProv == None and inMem == None
            and inServ == None and inBill == None):
                return

        ret = True
        ret = (ret and self.setDate(inServiceDate))
        ret = (ret and self.setProv(inProv))
        ret = (ret and self.setMem(inMem))
        ret = (ret and self.setCode(inServ))
        ret = (ret and self.setBill(inBill))
        
        if (inComments != None):
            ret = (ret and self.setComments(inComments))
         
        if not (ret):
            raise ValueError
        
        self.setTime(inTime)

    def setTime(self, inTime: datetime = None) -> None:
        if (inTime == None):
            self.currentTime = datetime.now()
            return
        elif not isinstance(inTime, datetime):
                  raise TypeError
        
        self.currentTime = inTime
        return
    
    def setDate(self, inDate: datetime) -> bool:
        if (inDate == None):
            print("Invalid date!")
            raise ValueError
        elif not isinstance(inDate, datetime):
                  raise TypeError
        
        self.serviceDate = inDate
        return True
    
    def setProv(self, inProv: int) -> bool:
        if (0 > inProv or inProv > 999999999):
            print("Provider ID must be 9 digits long!")
            raise ValueError
        
        self.providerID = inProv
        return True
    
    def setMem(self, inMem: int) -> bool:
        if (0 > inMem or inMem > 999999999):
            print("Member ID must be 9 digits long!")
            raise ValueError
        
        self.memberID = inMem
        return True

    def setCode(self, inCode: int) -> bool:
        if (0 > inCode or inCode > 999999999):
            print("Service code must be 9 digits long!")
            raise ValueError
        
        self.serviceCode = inCode
        return True
    
    def setBill(self, inBill: float) -> bool:
        if (0 > inBill or inBill > 999.99):
            print("Can't charge them that much!")
            raise ValueError
        elif (inBill < 0):
            print("You can't pay them!")
            raise ValueError
        
        self.bill = inBill
        return True

    def setComments(self, inComments: Union[str, None]) -> bool:
        if (inComments == None):
             self.comments = None
             return True
        
        if (len(inComments) > 100):
            print("Max length of comments is 100!")
            raise ValueError
        
        self.comments = inComments
        return True
    
    def display(self):
        serviceDate = self.serviceDate.strftime("%Y-%m-%d")
        print(f"\nRecord Creation Time: {self.currentTime}")
        print(f"Service Date: {serviceDate}")
        print(f"Provider ID: {self.providerID:09d}")
        print(f"Member ID: {self.memberID:09d}")
        print(f"Service Code: {self.serviceCode:09d}")
        print(f"Bill: {self.bill:.2f}")
        if (self.comments != None):
            print(f"Comments: {self.comments}")
        else:
            print("No comments provided.")

        return
