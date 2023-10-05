import Member 
import datetime

class Record():
    def __init__(self, inProvider: Member, inMember: Member):
        self.currentTime
        self.serviceDate
        self.providerNum = inProvider.number
        self.memberNum = inMember.number
        self.serviceCode
        self.comments

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
    
    def setComments(self, inComments: str) -> bool:
        if (len(str(inComments)) > 100):
            print("Max length of comments is 100!")
            return False
        
        self.comments = inComments
        return True