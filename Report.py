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
    
    #add a record to the list
    def addRecord(self, inRecord: Record) -> bool:
        if (self.provider != inRecord.provider):
            print("Not your appointment")
            return False
        
        if (self.totalConsultations >= 999):
            print("Too many consultations for the week!")
            return False
        
        if (self.totalFee + inRecord.bill >= 99999.99):
            print("Too much income this week!")
            return False

        if (self.recordList == None):
            self.recordList = [inRecord]
        else:
            self.recordList.append(inRecord)
        
        self.totalConsultations += 1
        self.totalFee += inRecord.bill

        return True