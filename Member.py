#Member class

class Member():
    #constructor, defaults to member not provider
    def __init__(self, inName: str = None, inNumber: int = None, inAddress: str = None,
                 inCity: str = None, inState: str = None, inZip: int = None, inStatus: bool = None):
        
        self.name = None
        self.number = None
        self.address = None
        self.city = None
        self.state = None
        self.zipCode = None
        self.status = inStatus

        ret = True
        ret = (ret and self.setName(inName))
        ret = (ret and self.setNumber(inNumber))
        ret = (ret and self.setAddr(inAddress))
        ret = (ret and self.setCity(inCity))
        ret = (ret and self.setState(inState))
        ret = (ret and self.setZip(inZip))
        
        if not (ret):
            raise ValueError
    
    #Set name
    def setName(self, inName: str) -> bool:
        if(inName):
            if (len(inName) > 25):
                print("Name must be <= 25 characters!")
                return False
        
        self.name = inName
        return True
    
    #Set member/provider number
    def setNumber(self, inNumber: int) -> bool:
        if(inNumber):
            if (0 > inNumber > 999999999):
                print("Member number must be maximum 9 digits long!")
                return False

        self.number = inNumber
        return True
    
    #Set address
    def setAddr(self, inAddr: str) -> bool:
        if(inAddr):
            if (len(inAddr) > 25):
                print("Address must be <= 25 characters!")
                return False
        
        self.address = inAddr
        return True

    #Set city
    def setCity(self, inCity: str) -> bool:
        if(inCity):
            if (len(inCity) > 14):
                print("City must be <= 14 characters!")
                return False
        self.city = inCity
        return True
    
    #Set state abbreviation
    def setState(self, inState: str) -> bool:
        if(inState):
            if (len(inState) != 2):
                print("State must be 2 characters long (abbreviation)!")
                return False
        self.state = inState
        return True
    
    #Set zip code
    def setZip(self, inZip: int) -> bool:
        if(inZip):
            if (0 > inZip > 99999):
                print("Zip code must be 5 digits long!")
                return False
        
        self.zipCode = inZip
        return True
    
    #Set status
    def setStatus(self, inStatus: bool) -> None:     
        self.status = inStatus

    #Display
    def display(self):
        print("\nMember Information:")
        print(f"Name: {self.name}")
        print(f"Number: {self.number}")
        print(f"Address: {self.address}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Zip Code: {self.zipCode}")
