#Provider class

import Member
import Service


class Provider(Member):
    #constructor, defaults to member not provider
    def __init__(self, inName: str = None, inNumber: int = None, inAddress: str = None,
                 inCity: str = None, inState: str = None, inZip: int = None, inStatus: int = None):
        
        Member.__init__(self, inName, inNumber, inAddress, inCity, inState, inZip, inStatus)
        self.services = []

    def addService(self, inService: Service) -> bool:
        if (Service == None):
            print("Fatal error")
            return False
        
        self.services.append(Service)
        return True

    def removeService(self, inService: Service) -> bool:
        if (self.services.__contains__(inService)):
            