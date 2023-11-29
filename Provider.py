from Member import Member
from Service import Service
import os

class Provider(Member):
    def __init__(self, inName: str = None, inNumber: int = None, inAddress: str = None,
                 inCity: str = None, inState: str = None, inZip: int = None, inStatus: int = None):
        Member.__init__(self, inName, inNumber, inAddress, inCity, inState, inZip, inStatus)
        self.service_codes = []  # List to store service codes

    def writeServicesToFile(self, serviceDict):
        scriptDir = os.path.dirname(__file__)
        serviceDir = scriptDir + "/Services/"

        for serviceCode in self.service_codes:
            service = serviceDict.get(serviceCode)
            if service:
                filename = f"{serviceCode:09d}.svc"
                filepath = os.path.join(serviceDir, filename)

                with open(filepath, "w") as file:
                    file.write(f"{service.code}\n")
                    file.write(f"{service.name}\n")
                    file.write(f"{service.desc}\n")
                    file.write(f"{service.cost}\n")
            else:
                print(f"Service with code {serviceCode} not found.")

    def addService(self, inServiceCode: int) -> bool:
        if inServiceCode not in self.service_codes:
            self.service_codes.append(inServiceCode)
            return True
        else:
            print("Already offering this service.")
            return False

    def removeService(self, inServiceCode: int) -> bool:
        if inServiceCode in self.service_codes:
            self.service_codes.remove(inServiceCode)
            return True
        else:
            print("The provider doesn't offer this service.")
            return False

    def display(self):
        print("\nProvider Information:")
        print(f"Name: {self.name}")
        print(f"Number: {self.number}")
        print(f"Address: {self.address}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Zip: {self.zipCode}")
        print(f"Status: {self.status}")
