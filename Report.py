#report class to store provider records

import Member
import Record

class Report:
    def __init__(self, inProvider: Member) -> bool:
        if (inProvider.provider == False):
            print("Pass in a provider, not a member!")
            return False
        
        self.provider = inProvider
        self.recordList = None
        self.totalConsultations = 0
        self.totalFee = 0.0
    
    def addRecord(self, inRecord: Record) -> bool:
        if (self.provider != inRecord.provider):
            print("Not your appointment")
            return False
        
    