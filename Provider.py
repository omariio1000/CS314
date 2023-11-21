#Provider class

from Member import Member


class Provider(Member):
    #constructor, defaults to member not provider
    def __init__(self, inName: str = None, inNumber: int = None, inAddress: str = None,
                 inCity: str = None, inState: str = None, inZip: int = None, inStatus: int = None):
        
        Member.__init__(self, inName, inNumber, inAddress, inCity, inState, inZip, inStatus)
        self.services = []

    def addService(self, inService: int) -> bool:
        if (inService < 0):
            print("Fatal error")
            return False
        
        self.services.append(inService)
        return True

    def removeService(self, inCode: int) -> bool:
        try:
            self.services.remove(inCode)
        except ValueError as ve:  
            print("The provider doesn't offer this service")
            return False
        
        print("Service removed")
        return True
    
    #Add setter functions here#