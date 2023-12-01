from Member import Member
from Provider import Provider
from Service import Service
from Record import Record
from datetime import datetime, timedelta
from Encryption import *
import os

class Terminal():
    def __init__(self, records: list, services: dict, members: dict, providers: dict, managerPasses: dict, providerPasses: dict):

        if not ((type(records) == list) and
                (type(services) == dict) and
                (type(members) == dict) and
                (type(providers) == dict) and
                (type(managerPasses) == dict) and
                (type(providerPasses) == dict)): 
            raise ValueError

        self.records = records
        self.services = services
        self.members = members
        self.providers = providers
        self.managerPasses = managerPasses
        self.providerPasses = providerPasses

    def run(self):
        print("Welcome to ChocAn!")
        running = True
        while (running):     
            print("\nOptions:")
            print("1: Manager Mode")
            print("2: Provider Mode")
            print("3: Quit")

            choice = 0
            try:
                choice = int(input("Select your mode: "))
            except:
                print("\nOnly numeric characters allowed!")

            if (choice == 1):
                user = input("\nEnter your username: ")
                password = input("Enter your password: ")

                try:
                    if (self.managerPasses[user] == encrypt(password)):
                        # manager(self.providers, self.members, self.records).welcome()
                        self.managerMode(user)
                    else:
                        print("\nIncorrect password!")
                except:
                    print("\nIncorrect username!")

            elif (choice == 2):
                provNum = 0
                provPass = 0
                try:
                    provNum = int(input("\nEnter your provider ID: "))
                    provPass = input("Enter your password: ")
                except:
                    print("\nOnly numeric characters allowed!")

                try:
                    if (self.providerPasses[provNum] == encrypt(provPass)):
                        self.providerMode(provNum)
                    
                    else:
                        print("\nIncorrect password!")
                except:
                    print("\nNo provider with that ID found!")

            elif (choice == 3):
                print("\nExiting terminal...\nSee you again soon!\n")
                running = False

            else:
                print("Invalid option selected.\n")

        return

    def providerMode(self, provID: int):
        print(f"\nWelcome to provider mode: {self.providers[provID].name}")
        running = True
        
        while (running):
            print("\nOptions:")
            print("1: Verify member ID")
            print("2: Print Records")
            print("3: Create a record")
            print("4: Display services")
            print("5: Change your password")
            print("6: Log out")

            choice = 0
            try:
                choice = int(input("Select an option: "))
            except:
                print("\nOnly numeric characters allowed!")

            if (choice == 1):
                self.verifyID()

            elif (choice == 2):
                self.printRecords(provID)

            elif (choice == 3):
                self.createRecords(provID)

            elif (choice == 4):
                self.displayServices(provID)

            elif (choice == 5):
                self.updateProviderPassword(provID)

            elif (choice == 6):
                running = False
                print("\nLogging out...")

            else:
                print("\nInvalid option")

        return

    def displayServices(self, provID: int):
        provider = self.providers.get(provID)
        if (provider is None):
            print("\nNo provider found with that ID!")
            return

        print("\n" + "-" * 100)
        for serviceCode in provider.serviceCodes:
            service = self.services.get(serviceCode)
            if (service is None):
                print("\nFatal error!")
                return
            service.display()
            print("\n" + "-" * 100)

        return

    def verifyID(self):
        ID = int(input("\nEnter the ID of the member: "))

        if self.members.get(ID) is not None:
            print(f"\n{self.members[ID].name} status:")
            if (self.members[ID].status == False):
                print("Suspended")
            else:
                print("Validated")
        else:
            print("\nInvalid ID number")

    def printRecords(self, provID: int):
        print("\n" + "-" * 100)

        found = False
        for key in self.records:
            if key.providerID == provID:
                found = True
                key.display()
                print("\n" + "-" * 100)
        
        if not found:
            print("\nNo Records found for the given provider ID.")

    def removeRecordFile(self, time: str):
        scriptDir = os.path.dirname(__file__)
        recordDir = scriptDir + "/Records/"

        filename = f"{time}.rec"
        filepath = os.path.join(recordDir, filename)

        # Remove the file if it exists
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"\nCorresponding .rec file ({filename}) removed.")
        else:
            print(f"\nCorresponding .rec file not found: {filename}")

    def writeRecordToFile(self, record: Record, oldTime: str = ""):
        scriptDir = os.path.dirname(__file__)
        recordDir = scriptDir + "/Records/"

        # Create a filename based on the timestamp
        filename = f"{record.currentTime.strftime('%Y_%m_%d_%H_%M_%S')}.rec"
        filepath = os.path.join(recordDir, filename)

        if (oldTime != ""):
            self.removeRecordFile(oldTime)

        # Open the file for writing
        with open(filepath, "w") as file:
            # Write record data to the file
            file.write(f"{record.serviceDate.strftime('%Y_%m_%d')}\n")
            file.write(f"{record.providerID:09d}\n")
            file.write(f"{record.memberID:09d}\n")
            file.write(f"{record.serviceCode:09d}\n")
            file.write(f"{record.bill:.2f}\n")

            if (record.comments is not None):
                file.write(f"{record.comments}\n")

            print(f"\nCorresponding .rec file created: {filename}")
        
    def createRecords(self, provID: int = -1):
        print("\nYou're creating a record, please follow instructions below")
                
        try:
            if (provID == -1):
                provID = int(input("Enter a provider ID: "))
                if (self.providers.get(provID) is None):
                    raise ValueError

            serviceDate = datetime.strptime(str(input("Enter Service Date (YYYY/MM/DD): ")), '%Y/%m/%d')

            memberId = int(input("Enter Member ID: "))
            if self.members.get(memberId) is  None:
                print("Invalid member ID!")
                raise ValueError

            serviceCode = int(input("Enter Service Code: "))
            if self.services.get(serviceCode) is  None:
                print("Invalid service code!")
                raise ValueError

            bill = self.services[serviceCode].cost

            print("Enter any comments. For no comments type \"none\".")
            comments = str(input())
            if (comments == "none"):
                comments = None

            newRecord = Record(None, serviceDate, provID, memberId, serviceCode, bill, comments)
            self.records.append(newRecord)
            self.writeRecordToFile(newRecord)
        except Exception as e:
            print(f"An error ({e}) has occured.\nRecord will not be created.")

    def editRecord(self):
        try:
            dateIn = input("\nEnter the date/time record was created (YYYY/MM/DD HH:MM:SS): ")
            recordDate = datetime.strptime(dateIn, "%Y/%m/%d %H:%M:%S")
            found = False

            for record in self.records:
                if (recordDate == record.currentTime):
                    found = True
                    record.display()

                    print("\nOptions:")
                    print("1: Edit creation time")
                    print("2: Edit service date")
                    print("3: Edit provider ID")
                    print("4: Edit member ID")
                    print("5: Edit service code (changes bill)")
                    print("6: Edit bill (overrides service cost)")
                    print("7: Edit comments")

                    choice = int(input("Select an option: "))

                    if (choice == 1):
                        timeStr = input("\nEnter new date & time (YYYY/MM/DD HH:MM:SS): ")
                        time = datetime.strptime(timeStr, "%Y/%m/%d %H:%M:%S")
                        record.setTime(time)
                    elif (choice == 2):
                        dateStr = input("\nEnter new date (YYYY/MM/DD): ")
                        date = datetime.strptime(dateStr, "%Y/%m/%d")
                        record.setDate(date)
                    elif (choice == 3):
                        provID = int(input("\nEnter new provider ID: "))
                        if (self.providers.get(provID) is not None):
                            record.setProv(provID)
                        else:
                            print("\nThat provider doesn't exist!")
                            return
                    elif (choice == 4):
                        memberID = int(input("\nEnter new member ID: "))
                        if (self.members.get(memberID) is not None):
                            record.setMem(memberID)
                        else:
                            print("\nThat member doesn't exist!")
                            return                   
                    elif (choice == 5):
                        serviceCode = int(input("\nEnter new service code: "))
                        if (self.services.get(serviceCode) is not None):
                            record.setMem(serviceCode)
                            record.setBill(self.services[serviceCode].cost)
                        else:
                            print("\nThat service doesn't exist!")
                            return   
                    elif (choice == 6):
                        bill = float(input("\nEnter new bill: "))
                        record.setBill(bill)
                    elif (choice == 7):
                        comments = input("\nEnter new comments (enter for none): ")
                        if (comments == ""):
                            comments = None
                        record.setComments(comments)
                    else:
                        print("\nInvalid option selected!")
                        return

                    oldTime = datetime.strftime(recordDate, "%Y_%m_%d_%H_%M_%S")
                    self.writeRecordToFile(record, oldTime)

            if (found != True):
                print("\nNo record found for that time!")

        except Exception as e:
            print(f"An error ({e}) has occured.\nRecord will not be edited.")
        
        return

    def removeRecord(self):
        try:
            dateIn = input("\nEnter the date/time record was created (YYYY/MM/DD HH:MM:SS): ")
            recordDate = datetime.strptime(dateIn, "%Y/%m/%d %H:%M:%S")
            found = False

            for record in self.records:
                if (recordDate == record.currentTime):
                    found = True
                    record.display()

                    affirm = input("Are you sure you would like to remove? (y/n): ")
                    if (affirm == 'y'):
                        self.records.remove(record)
                        time = datetime.strftime(recordDate, "%Y_%m_%d_%H_%M_%S")
                        self.removeRecordFile(time)

                    elif (affirm == "n"):
                        print("\nNot removed.")
                    else:
                        print("\nInvalid Input. Not removed.")                  

            if (found != True):
                print("\nNo record found for that time!")

        except Exception as e:
            print(f"An error ({e}) has occured.\nRecord will not be edited.")


        return

    def updatePasswords(self):
        scriptDir = os.path.dirname(__file__)
        passDir = scriptDir + "/Passwords/"
        
        managerFile = os.path.join(passDir, "managers.pass")
        providerFile = os.path.join(passDir, "providers.pass")
    
        os.remove(managerFile)
        os.remove(providerFile)

        with open(managerFile, "w") as file:
            for user, password in self.managerPasses.items():
                file.write(f"{user}:{password}\n")
        
        with open(providerFile, "w") as file:
            for user, password in self.providerPasses.items():
                file.write(f"{user:09d}:{password}\n")

    def updateManagerPassword(self, user: str):
        newUser = True
        if (self.managerPasses.get(user) is not None):
            newUser = False
            affirm = input(f"\nWould you like to view the current password for \"{user}\"? (y/n): ")
            if (affirm == 'y'):
                print(f"Current password for \"{user}\": \"" + decrypt(self.managerPasses.get(user)) + "\"")
        
        password = input("Enter your new password (0 to cancel): ")
        try:
            password = encrypt(password)
            self.managerPasses[user] = password
            if (newUser):
                print(f"\nManager \"{user}\" added successfully!")
            else:
                print(f"\nPassword for \"{user}\" changed successfully!")
        except Exception as e:
                print(f"\bUnable to edit due to error ({e})")

        
        self.updatePasswords()
        return

    def updateProviderPassword(self, provID: int):
        affirm = input("\nWould you like to view your current password? (y/n): ")
        if (affirm == 'y'):
            print(f"Current password for provider ({provID}): \"" + decrypt(self.providerPasses.get(provID)) + "\"")
        try:
            self.providerPasses.pop(provID)
            password = input("Enter new password (0 to cancel): ")
            self.providerPasses[provID] = encrypt(password)
        except Exception as e:
                print(f"Unable to edit due to error ({e})")

        self.updatePasswords()
        return

    

    def managerMode(self, userName: str):
        print(f"\nWelcome to manager mode: {userName}")
        running = True

        while (running):
            print("\nOptions:")

            print(" 1: Add member")
            print(" 2: Edit member")
            print(" 3: Remove Member")
    
            print(" 4: Add provider")
            print(" 5: Edit provider")
            print(" 6: Remove provider")
            
            print(" 7: Add service")
            print(" 8: Edit service")
            print(" 9: Remove service")

            print("10: Add record")
            print("11: Edit record")
            print("12: Remove record")

            print("13: Generate reports")

            print("14: Change your password")
            print("15: Change provider password")
            print("16: Add new manager")

            print("17: Log out")

            choice = 0
            try:
                choice = int(input("Select an option: "))
            except:
                print("\nOnly numeric characters allowed!")

            if (choice == 1):
                self.addMember()
            
            elif (choice == 2):
                self.editMember()

            elif (choice == 3):
                self.removeMember()
            
            elif (choice == 4):
                self.addMember(True)

            elif (choice == 5):
                self.editMember(True)
            
            elif (choice == 6):
                self.removeMember(True)
            
            elif (choice == 7):
                self.addService()

            elif (choice == 8):
                self.editService()

            elif (choice == 9):
                self.removeService()

            elif (choice == 10):
                self.createRecords()

            elif (choice == 11):
                self.editRecord()

            elif (choice == 12):
                self.removeRecord()

            elif (choice == 13):
                self.generateReports()

            elif (choice == 14):
                self.updateManagerPassword(userName)

            elif (choice == 15):
                try:
                    provID = int(input("\nEnter a provider ID: "))
                    if (self.providers.get(provID) is not None):
                        self.updateProviderPassword(provID)
                    else:
                        raise ValueError
                except Exception as e:
                    print(f"Unable to change password due to error ({e})")
            
            elif (choice == 16):
                user = input("\nEnter a new username: ")
                if (self.managerPasses.get(user) is None):
                    self.updateManagerPassword(user)
                else:
                    print("Already have a manager with that username!")

            elif (choice == 17):
                running = False
                print("\nLogging out...")
            
            else:
                print("\nInvalid option selected.")

        return

    # Function to remove the corresponding .mem file
    def removeMemberFile(self, ID: int):
        scriptDir = os.path.dirname(__file__)
        memberDir = scriptDir + "/Members/"

        # Create a filename based on the member number
        filename = f"{ID:09d}.mem"
        filepath = os.path.join(memberDir, filename)

        # Remove the file if it exists
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"\nCorresponding .mem file ({filename}) removed.")
        else:
            print(f"\nCorresponding .mem file not found: {filename}")

    def writeMemberToFile(self, member: Member, oldId: int = -1):
        scriptDir = os.path.dirname(__file__)
        memberDir = scriptDir + "/Members/"

        if (oldId != -1):
            self.removeMemberFile(oldId)

        # Create a filename based on the member number
        filename = f"{member.number:09d}.mem"
        filepath = os.path.join(memberDir, filename)

        # Open the file for writing
        with open(filepath, "w") as file:
            # Write member data to the file
            file.write(f"{member.name}\n")
            file.write(f"{member.number:09d}\n")
            file.write(f"{member.address}\n")
            file.write(f"{member.city}\n")
            file.write(f"{member.state}\n")
            file.write(f"{member.zipCode}\n")
            file.write(f"{int(member.status)}")

        print(f"\nCorresponding .mem file created: {filename}")

        return

    # Function to remove the corresponding .prov file
    def removeProviderFile(self, ID: int):
        scriptDir = os.path.dirname(__file__)
        providerDir = scriptDir + "/Providers/"

        # Create a filename based on the provider number
        filename = f"{ID:09d}.prov"
        filepath = os.path.join(providerDir, filename)

        # Remove the file if it exists
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"\nCorresponding .prov file ({filename}) removed.")
        else:
            print(f"\nCorresponding .prov file not found: {filename}")

    def writeProviderToFile(self, provider: Provider, oldId: int = -1):
        scriptDir = os.path.dirname(__file__)
        providerDir = scriptDir + "/Providers/"

        if (oldId != -1):
            self.removeProviderFile(oldId)

        # Create a filename based on the provider number
        filename = f"{provider.number:09d}.prov"
        filepath = os.path.join(providerDir, filename)

        # Open the file for writing
        with open(filepath, "w") as file:
            # Write provider data to the file
            file.write(f"{provider.name}\n")
            file.write(f"{provider.number:09d}\n")
            file.write(f"{provider.address}\n")
            file.write(f"{provider.city}\n")
            file.write(f"{provider.state}\n")
            file.write(f"{provider.zipCode}\n")
            file.write("0\n")
            for service in provider.serviceCodes:
                file.write(f"{service:09d},")

        print(f"\nCorresponding .prov file created: {filename}")

        return

    def editMember(self, providerMode: bool = False):
        editing = None
        ID = 0

        try:
            if (providerMode):
                ID = int(input("\nEnter the ID of the provider: "))
                editing = self.providers.get(ID)
            else:
                ID = int(input("\nEnter the ID of the member: "))
                editing = self.members.get(ID)
        except Exception as e:
            print(f"Unable to edit due to error ({e})")

        if editing is not None:
            editing.display()

            print("\nOptions:")
            print("1: Edit name")
            if (not providerMode):
                print("2: Edit member ID")
            else:
                print("2: Edit provider ID")
            print("3: Edit address")
            print("4: Edit city")
            print("5: Edit state")
            print("6: Edit zip code")
            if (not providerMode):
                print("7: Edit status")
            else:
                print("7: Add service to list")
                print("8: Remove service from list")

            choice = 0
            try:
                choice = int(input("Select an option: "))
            except:
                print("\nOnly numeric characters allowed!")

            try:
                if (choice == 1):
                    name = input("Please enter the new name: ")
                    editing.setName(name)

                elif (choice == 2):
                    newID = int(input("Please enter in the new ID number: "))

                    if (providerMode and self.providers.get(newID) is not None):
                        print("\nAnother provider has this ID!")
                        raise ValueError
                    elif (not providerMode and self.members.get(newID) is not None):
                        print("\nAnother member has this ID!")
                        raise ValueError

                    editing.setNumber(newID)

                elif (choice == 3):
                    address = input("Please enter in the new address: ")
                    editing.setAddr(address)

                elif (choice == 4):
                    city = input("Please enter in the name of the new city: ")
                    editing.setCity(city)

                elif (choice == 5):
                    state = input("Please enter in the name of the new state: ")
                    editing.setState(state)

                elif (choice == 6):
                    zip = int(input("Please enter the new zip code: "))
                    editing.setZip(zip)
                
                elif (choice == 7 and not providerMode):
                    status = input("Enter \"Valid\" or \"Suspended\": ")
                    if (status == "Valid"):
                        editing.setStatus(True)
                    elif (status == "Suspended"):
                        editing.setStatus(False)
                    else:
                        print("\nInvalid status entered!")
                
                elif (choice == 7 or choice == 8 and providerMode):
                    serviceCode = 0
                    if choice == 7:
                        serviceCode = int(input("Enter service code you'd like to add: "))
                    else: 
                        serviceCode = int(input("Enter service code you'd like to remove: "))

                    service = self.services.get(serviceCode)

                    if (service is not None):
                        if choice == 7:
                            editing.addService(serviceCode)
                        else:
                            editing.removeService(serviceCode)
                    else:
                        print("\nInvalid service code")

                else:
                    print("\nInvalid option selected!")
                    return
                
                if (providerMode):
                    self.providers.pop(ID)
                    self.providers[editing.number] = editing
                    self.writeProviderToFile(editing, ID)

                    temp = self.providerPasses[ID]
                    self.providerPasses.pop(ID)
                    self.providerPasses[editing.number] = temp
                    self.updatePasswords()
                else:
                    self.members.pop(ID)
                    self.members[editing.number] = editing
                    self.writeMemberToFile(editing, ID)

            except Exception as e:
                print(f"Unable to edit due to error ({e})")
        else:
            print("\nInvalid ID number")
        
        return

    def addMember(self, providerMode: bool = False):
        adding = None
        if (providerMode):
            adding = Provider()
        else:
            adding = Member()
        
        if (adding is not None):
            try:
                name = input("\nPlease enter the name: ")
                adding.setName(name)

                newID = int(input("Please enter in the ID number: "))
                adding.setNumber(newID)

                address = input("Please enter in the address: ")
                adding.setAddr(address)

                city = input("Please enter in the name of the city: ")
                adding.setCity(city)

                state = input("Please enter in the name of the state: ")
                adding.setState(state)

                zip = int(input("Please enter the zip code: "))
                adding.setZip(zip)
            
                if (not providerMode):
                    status = input("Enter status as \"Valid\" or \"Suspended\": ")
                    if (status == "Valid"):
                        adding.setStatus(True)
                    elif (status == "Suspended"):
                        adding.setStatus(False)
                    else:
                        print("\nInvalid status entered!")
                
                else:
                    running = True
                    while (running):
                        print("\nIf done enter \"done\"")
                        serviceCode = input("Enter a service code to add: ")
                        if (serviceCode == "done"):
                            running = False
                        else:
                            try:
                                code = int(serviceCode)
                                if (self.services.get(code) is not None):
                                    if (adding.addService(code) == True):
                                        print("Service added.")
                                else:
                                    print("Invalid service code! Not added to provider.")
                            except:
                                print("\nOnly numeric characters allowed!")
                
                if (providerMode):
                    if (self.providers.get(adding.number) is None):
                        self.providers[adding.number] = adding
                        self.writeProviderToFile(adding)

                        self.providerPasses[adding.number] = encrypt("password")
                        self.updatePasswords()
                    else:
                        print("Provider with this ID already exists!")
                else:
                    if (self.members.get(adding.number) is None):
                        self.members[adding.number] = adding
                        self.writeMemberToFile(adding)
                    else:
                        print("Member with this ID already exists!")

            except Exception as e:
                print(f"Unable to add due to error ({e})")

        return

    def removeMember(self, providerMode: bool = False):
        removing = None
        ID = 0
        
        try:
            if (providerMode):
                ID = int(input("\nEnter the ID of the provider: "))
                removing = self.providers.get(ID)
            else:
                ID = int(input("\nEnter the ID of the member: "))
                removing = self.members.get(ID)

            if removing is not None:
                removing.display()

                affirm = input("Are you sure you would like to remove? (y/n): ")
                if (affirm == 'y'):
                    if(providerMode):
                        self.providers.pop(ID)
                        self.removeProviderFile(ID)

                        self.providerPasses.pop(ID)
                        self.updatePasswords()
                    else:
                        self.members.pop(ID)
                        self.removeMemberFile(ID)

                elif (affirm == "n"):
                    print("\nNot removed.")
                else:
                    print("\nInvalid Input. Not removed.")
        except Exception as e:
                print(f"Unable to remove due to error ({e})")

        return

    # Function to remove the corresponding .svc file
    def removeServiceFile(self, ID: int):
        scriptDir = os.path.dirname(__file__)
        serviceDir = scriptDir + "/Services/"

        # Create a filename based on the service code
        filename = f"{ID:09d}.svc"
        filepath = os.path.join(serviceDir, filename)

        # Remove the file if it exists
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"\nCorresponding .svc file ({filename}) removed.")
        else:
            print(f"\nCorresponding .svc file not found: {filename}")

    def writeServiceFile(self, service: Service, oldId: int = -1):
        scriptDir = os.path.dirname(__file__)
        serviceDir = scriptDir + "/Services/"

        if (oldId != -1):
            self.removeServiceFile(oldId)

        # Create a filename based on the member number
        filename = f"{service.code:09d}.svc"
        filepath = os.path.join(serviceDir, filename)

        # Open the file for writing
        with open(filepath, "w") as file:
            # Write member data to the file
            file.write(f"{service.code:09d}\n")
            file.write(f"{service.name}\n")
            file.write(f"{service.desc}\n")
            file.write(f"{service.cost:.2f}")

        print(f"\nCorresponding .svc file created: {filename}")

        return
        
    def addService(self):
        adding = Service()
        try:
            name = input("\nEnter service name: ")
            adding.setName(name)

            code = int(input("Enter service code: "))
            adding.setCode(code)

            desc = input("Enter service description: ")
            adding.setDesc(desc)

            cost = float(input("Enter service cost: "))
            adding.setCost(cost)

            if (self.services.get(code) is None):
                self.services[code] = adding
                self.writeServiceFile(adding)
            else:
                print("\nService with that code already exists!")

        except Exception as e:
                print(f"Unable to add due to error ({e})")

        return

    def editService(self):
        editing = None
        try:
            ID = int(input("\nEnter the service code: "))
            editing = self.services.get(ID)
        except Exception as e:
            print(f"Unable to edit due to error ({e})")
        

        if editing is not None:
            editing.display()

            print("\nOptions:")
            print("1: Edit name")
            print("2: Edit code")
            print("3: Edit description")
            print("4: Edit cost")

            choice = 0
            try:
                choice = int(input("Select an option: "))
            except:
                print("\nOnly numeric characters allowed!")

            try:
                if (choice == 1):
                    name = input("Please enter the new name: ")
                    editing.setName(name)

                elif (choice == 2):
                    code = int(input("Please enter in the new service code: "))
                    
                    if (self.services.get(code) is not None):
                        print("\nAnother service has this code!")
                        raise ValueError
                    
                    editing.setCode(code)

                elif (choice == 3):
                    desc = input("Please enter in the new description: ")
                    editing.setDesc(desc)

                elif (choice == 4):
                    cost = float(input("Please enter in the cost: "))
                    editing.setCost(cost)

                else:
                    print("\nInvalid option selected!")
                    return
                

                self.services.pop(ID)
                self.services[editing.code] = editing
                self.writeServiceFile(editing, ID)

            except Exception as e:
                print(f"Unable to edit due to error ({e})")
        else:
            print("\nInvalid ID number")
        return

    def removeService(self):
        removing = None

        try:
            ID = int(input("\nEnter the service code: "))
            removing = self.services.get(ID)

            if removing is not None:
                removing.display()

                affirm = input("Are you sure you would like to remove? (y/n): ")
                if (affirm == 'y'):
                    self.services.pop(ID)
                    self.removeServiceFile(ID)

                elif (affirm == "n"):
                    print("\nNot removed.")
                else:
                    print("\nInvalid Input. Not removed.")
        except Exception as e:
                print(f"Unable to remove due to error ({e})")

        return

    def generateReports(self):
        print("\n1: Generate Provider summary report")
        print("2: Generate Member summary report")
        print("3: Generate a Provider EFT report")
        
        choice = 0
        try:
            choice = int(input("Select an option: "))
        except:
            print("\nOnly numeric characters allowed!")
        
        currentDate = datetime.now()

        if choice == 1:  # Provider summary report
            self.generateProviderSummaryReport(currentDate)
        elif choice == 2:  # Member summary report
            self.generateMemberSummaryReport(currentDate)
        elif choice == 3:  # Provider EFT report
            self.generateProviderEFTReport(currentDate)
        else:
            print("Invalid input. No report generated.")

    def generateProviderSummaryReport(self, currentDate):
        for providerID, provider in self.providers.items():
            providerRecords = self.getProviderRecords(providerID, currentDate)

            if providerRecords:
                reportData = f"Provider summary report generated for {provider.name} on {currentDate.strftime('%Y-%m-%d')}\n\n"
                reportData += f"Provider Name: {provider.name}\n"
                reportData += f"Provider Number: {provider.number}\n"
                reportData += f"Provider Address: {provider.address}, {provider.city}, {provider.state} {provider.zipCode}\n\n"

                for record in providerRecords:
                    reportData += f"Date of Service: {record.serviceDate}\n"
                    reportData += f"Date and Time Data Inputted to Computer: {record.currentTime}\n"
                    reportData += f"Member Name: {self.members[record.memberID].name}\n"
                    reportData += f"Member Number: {record.memberID}\n"
                    reportData += f"Service Code: {record.serviceCode}\n"
                    reportData += f"Fee: {record.bill}\n\n"

                reportData += "\n" + "=" * 50 + "\n"

                self.writeReportToFile(currentDate, f"Provider_Summary_Report_{provider.number}", reportData) 

    def generateMemberSummaryReport(self, currentDate):
        for memberID, member in self.members.items():
            memberRecords = self.getMemberRecords(memberID, currentDate)

            if memberRecords:
                reportDataHeader = f"Member summary report generated for {member.name} on {currentDate.strftime('%Y-%m-%d')}\n\n"
                reportData = f"{reportDataHeader}Member Name: {member.name}\n"
                reportData += f"Member Number: {member.number}\n"
                reportData += f"Member Address: {member.address}, {member.city}, {member.state} {member.zipCode}\n\n"

                for record in memberRecords:
                    providerName = self.providers[record.providerID].name if record.providerID in self.providers else "Unknown Provider"
                    serviceName = self.services[record.serviceCode].name if record.serviceCode in self.services else "Unknown Service"

                    reportData += f"Date of Service: {record.serviceDate}\n"
                    reportData += f"Provider Name: {providerName}\n"
                    reportData += f"Service Name: {serviceName}\n\n"

                reportData += "\n" + "=" * 50 + "\n"

                filename = f"Member_Summary_Report_{member.name}_{currentDate.strftime('%Y-%m-%d')}.txt"
                self.writeReportToFile(currentDate, filename, reportData)

    def generateProviderEFTReport(self, currentDate):
        for providerID, provider in self.providers.items():
            providerRecords = self.getProviderRecords(providerID, currentDate)

            if providerRecords:
                totalAmount = sum(record.bill for record in providerRecords)
                reportData = f"Provider EFT report generated for {provider.name} on {currentDate.strftime('%Y-%m-%d')}\n"
                reportData += f"Total Amount to be Transferred: ${totalAmount}\n"
                
                self.writeReportToFile(currentDate, f"Provider_EFT_Report_{provider.name}", reportData)

    def writeReportToFile(self, currentDate, reportName, reportData):
        reports_dir = "Reports"
        os.makedirs(reports_dir, exist_ok=True)

        reportFilename = f"{reportName}_{currentDate.strftime('%Y_%m_%d_%H_%M_%S')}.txt"
        report_filepath = os.path.join(reports_dir, reportFilename)

        with open(report_filepath, "w") as report_file:
            report_file.write(reportData)

    def getProviderRecords(self, providerID, currentDate):
        # Filter self.records for the last week for a specific provider
        providerRecords = [record for record in self.records if record.providerID == providerID
                            and currentDate - timedelta(days=7) <= record.currentTime <= currentDate]
        return providerRecords

    def getMemberRecords(self, memberID, currentDate):
        # Filter self.records for the last week for a specific member
        memberRecords = [record for record in self.records if record.memberID == memberID
                            and currentDate - timedelta(days=7) <= record.currentTime <= currentDate]

        return memberRecords
