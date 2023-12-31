from Member import Member
import os

class Provider(Member):
    def __init__(self, inName: str = None, inNumber: int = None, inAddress: str = None,
                 inCity: str = None, inState: str = None, inZip: int = None, inStatus: int = None):
        Member.__init__(self, inName, inNumber, inAddress, inCity, inState, inZip, inStatus)
        self.serviceCodes = []  # List to store service codes

    def addService(self, inServiceCode: int) -> bool:
        if (inServiceCode < 0 or inServiceCode > 999999999):
            print("Service code must be 9 digits long!")
            raise ValueError

        if inServiceCode not in self.serviceCodes:
            self.serviceCodes.append(inServiceCode)
            return True
        else:
            print("Already offering this service.")
            raise ValueError

    def removeService(self, inServiceCode: int) -> bool:
        if (inServiceCode < 0 or inServiceCode > 999999999):
            print("Service code must be 9 digits long!")
            raise ValueError

        if inServiceCode in self.serviceCodes:
            self.serviceCodes.remove(inServiceCode)
            return True
        else:
            print("The provider doesn't offer this service.")
            raise ValueError

    def display(self):
        print("\nProvider Information:")
        print(f"Name: {self.name}")
        print(f"Number: {self.number}")
        print(f"Address: {self.address}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Zip: {self.zipCode}")
        print("Services offered: ", end='')
        for service in self.serviceCodes:
            print(f"{service:09d}", end=',')
        print("")

        return
