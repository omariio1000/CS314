#Service class

class Service():
    def __init__(self, inCode: int = None, inName: str = None, inDesc: str = None, inCost: float = None):
        self.code = inCode
        self.name = inName
        self.desc = inDesc
        self.cost = inCost

    def setCode(self, inCode: int) -> bool:
        if (len(str(inCode)) != 6):
            print("Service code must be 6 digits long!")
            return False
        
        self.code = inCode
        return True
    
    def setName(self, inName: str) -> bool:
        if (len(inName) > 25):
            print("Name must be <= 25 characters!")
            return False
        
        self.name = inName
        return True

    def setDesc(self, inDesc: str) -> bool:
        if (len(inDesc > 100)):
            print("Description must be <= 100 characters!")
            return False
        
        self.desc = inDesc
        return True
    
    def setCost(self, inCost: float) -> bool:
        if (inCost > 999.99):
            print("Can't cost that much!")
            return False
        
        self.cost = inCost