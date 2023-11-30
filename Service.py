#Service class
class Service():
    def __init__(self, inCode: int = None, inName: str = None, inDesc: str = None, inCost: float = None):
        self.code = None
        self.name = None
        self.desc = None
        self.cost = None

        if (inCode == None and inName == None and inDesc == None and inCost == None):
            return

        ret = True
        ret = (ret and self.setCode(inCode))
        ret = (ret and self.setName(inName))
        ret = (ret and self.setDesc(inDesc))
        ret = (ret and self.setCost(inCost))
        
        if not (ret):
            raise ValueError

    def setCode(self, inCode: int) -> bool:
        if (0 > inCode or inCode > 999999999):
            print("Service code must be 9 digits long!")
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
        if (len(inDesc) > 100):
            print("Description must be <= 100 characters!")
            return False
        
        self.desc = inDesc
        return True
    
    def setCost(self, inCost: float) -> bool:
        if (0 > inCost or inCost > 999.99):
            print("Can't cost that much!")
            return False
        
        self.cost = inCost
        return True
    
    def display(self):
        print("\nService Information:")
        print(f"Name: {self.name}")
        print(f"Service code: {self.code:09d}")
        print(f"Description: {self.desc}")
        print(f"Cost: {self.cost:.2f}")

        return
    