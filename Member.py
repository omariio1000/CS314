#Member class

class Member():
    #constructor, defaults to member not provider
    def __init__(self, inName: str = None, inNumber: int = None, inAddress: str = None,
                 inCity: str = None, inState: str = None, inZip: int = None, inStatus: int = None):
        
        self.name = inName
        self.number = inNumber
        self.address = inAddress
        self.city = inCity
        self.state = inState
        self.zipCode = inZip
        self.status = inStatus
    
    #Set name
    def setName(self, inName: str) -> bool:
        if (len(inName) > 25):
            print("Name must be <= 25 characters!")
            return False
        
        self.name = inName
        return True
    
    #Set member/provider number
    def setNumber(self, inNumber: int) -> bool:
        if (len(str(inNumber)) != 9):
            print("Member number must be 9 digits long!")
            return False

        self.number = inNumber
        return True
    
    #Set address
    def setAddr(self, inAddr: str) -> bool:
        if (len(inAddr) > 25):
            print("Address must be <= 25 characters!")
            return False
        
        self.address = inAddr
        return True

    #Set city
    def setCity(self, inCity: str) -> bool:
        if (len(inCity) > 14):
            print("City must be <= 14 characters!")
            return False
        
        self.city = inCity
        return True
    
    #Set state abbreviation
    def setState(self, inState: str) -> bool:
        if (len(inState) != 2):
            print("State must be 2 characters long (abbreviation)!")
            return False
        
        self.state = inState
        return True
    
    #Set zip code
    def setZip(self, inZip: int) -> bool:
        if (len(str(inZip)) != 5):
            print("Zip code must be 5 digits long!")
            return False
        
        self.zipCode = inZip
        return True
    
    #Set status
    def setStatus(self, inStatus: int) -> bool:
        if (inStatus > 2 or inStatus < 0):
            print("Invalid status!")
            return False
        
        self.status = inStatus
        return True