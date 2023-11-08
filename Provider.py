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

    def removeService(self, inCode: int) -> bool:
        if (inCode < 0):
            print("Fatal error")
            return False
        
        for service in self.services:
            if (service.code == inCode):
                self.services.remove(service)
                return True
            
        print("The provider doesn't offer this service")
        return False