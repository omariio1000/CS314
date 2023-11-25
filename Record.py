#Record class (to write to disk)

from datetime import datetime

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

        if (inTime == None or inServiceDate == None or inProv == None or inMem == None
            or inServ == None or inBill == None):
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
            self.currentTime = datetime.datetime.now()
            return
        
        self.currentTme = inTime
        return
    
    def setDate(self, inDate: datetime) -> bool:
        if (inDate == None):
            print("Invalid date!")
            return False
        
        self.serviceDate = inDate
        return True
    
    def setProv(self, inProv: int) -> bool:
        if (0 > inProv or inProv > 999999999):
            print("Provider ID must be 9 digits long!")
            return False
        
        self.providerID = inProv
        return True
    
    def setMem(self, inMem: int) -> bool:
        if (0 > inMem or inMem > 999999999):
            print("Member ID must be 9 digits long!")
            return False
        
        self.memberID = inMem
        return True

    def setCode(self, inCode: int) -> bool:
        if (0 > inCode or inCode > 999999999):
            print("Service code must be 9 digits long!")
            return False
        
        self.code = inCode
        return True
    
    def setBill(self, inBill: float) -> bool:
        if (0 > inBill or inBill > 999.99):
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