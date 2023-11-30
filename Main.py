from Member import Member
from Provider import Provider
from Service import Service
from Record import Record
from Manager import manager
from datetime import datetime
from Manager import manager
from Encryption import *
import os

records = []
services = dict()
members = dict()
providers = dict()

managerPasses = dict()
providerPasses = dict()

def providerMode(provID: int):#TESTED
    print(f"\nWelcome to provider mode: {providers[provID].name}")
    running = True
    
    while (running):
        print("\nOptions:")
        print("1: Verify member ID")
        print("2: Print Records")
        print("3: Create a record")
        print("4: Log out")

        choice = 0
        try:
            choice = int(input("Select an option: "))
        except:
            print("\nOnly numeric characters allowed!")

        if (choice == 1):
            verifyID()

        elif (choice == 2):
            printRecords(provID)

        elif (choice == 3):
            createRecords(provID)

        elif (choice == 4):
            running = False
            print("\nLogging out...")

        else:
            print("\nInvalid option")

    return

def verifyID():#TESTED
    ID = int(input("\nEnter the ID of the member: "))

    if members.get(ID) is not None:
        print(f"\n{members[ID].name} status:")
        if (members[ID].status == False):
            print("Suspended")
        else:
            print("Validated")
    else:
        print("\nInvalid ID number")

def printRecords(provID: int):#TESTED
    print("\n" + "-" * 100)

    for key in records:
        if key.providerID == provID:
            serviceDate = key.serviceDate.strftime("%Y-%m-%d")
            print(f"Record Creation Time: {key.currentTime}")
            print(f"Service Date: {serviceDate}")
            print(f"Provider ID: {key.providerID:09d}")
            print(f"Member ID: {key.memberID:09d}")
            print(f"Service Code: {key.serviceCode:09d}")
            print(f"Bill: {key.bill:.2f}")
            if (key.comments != None):
                print(f"Comments: {key.comments}")
            else:
                print("No comments provided")
            print("-" * 100)
        else:
            print("\nNo records found for the given provider ID.")

def writeRecordToFile(record):#TESTED
        scriptDir = os.path.dirname(__file__)
        recordDir = scriptDir + "/Records/"

        # Create a filename based on the timestamp
        filename = f"{record.currentTime.strftime('%Y_%m_%d_%H_%M_%S')}.rec"
        filepath = os.path.join(recordDir, filename)

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
    
def createRecords(provID: int):#TESTED
    print("\nYou're creating a record, please follow instructions below")
    try:
        serviceDate = datetime.strptime(str(input("Enter Service Date (YYYY/MM/DD): ")), '%Y/%m/%d')

        memberId = int(input("Enter Member ID: "))
        if members.get(memberId) is  None:
            print("Invalid member ID!")
            raise ValueError

        serviceCode = int(input("Enter Service Code: "))
        if services.get(serviceCode) is  None:
            print("Invalid service code!")
            raise ValueError

        bill = services[serviceCode].cost

        print("Enter any comments. For no comments type \"none\".")
        comments = str(input())
        if (comments == "none"):
            comments = None

        newRecord = Record(None, serviceDate, provID, memberId, serviceCode, bill, comments)
        records.append(newRecord)
        writeRecordToFile(newRecord)
    except Exception as e:
        print(f"An error ({e}) has occured.\nRecord will not be created.")

def getPasses():#TESTED
    scriptDir = os.path.dirname(__file__)
    passDir = scriptDir + "/Passwords/"

    managerFile = open(passDir + "managers.pass", "r")
    providerFile = open(passDir + "providers.pass", "r")

    managerData = managerFile.readlines()
    providerData = providerFile.readlines()

    for data in managerData:
        if (data[-1] == '\n'):
            data = data[:-1]

        userPass = data.split(":")
        managerPasses[userPass[0]] = userPass[1]


    for data in providerData:
        if (data[-1] == '\n'):
            data = data[:-1]

        userPass = data.split(":")
        providerPasses[int(userPass[0])] = userPass[1]
    
    return

def addFiles():#TESTED
    scriptDir = os.path.dirname(__file__)  # absolute dir
    recordDir = scriptDir + "/Records/"
    serviceDir = scriptDir + "/Services/"
    memberDir = scriptDir + "/Members/"
    providerDir = scriptDir + "/Providers/"

    extRecords = os.listdir(recordDir)
    extServices = os.listdir(serviceDir)
    extMembers = os.listdir(memberDir)
    extProviders = os.listdir(providerDir)

    for extRecord in extRecords:
        # print(recordDir + extRecord)
        file = open(recordDir + extRecord, "r")
        fileData = file.readlines()

        # removing \n characters from strings
        count = 0
        for data in fileData:
            if (data[-1] == '\n'):
                fileData[count] = data[:-1]
            count += 1

        currentTime = datetime.strptime(extRecord[:-4], '%Y_%m_%d_%H_%M_%S')
        # print(currentTime)
        serviceDate = datetime.strptime(fileData[0], '%Y_%m_%d')
        # print(serviceDate)
        providerId = int(fileData[1])
        # print("{:09d}".format(providerId))
        memberId = int(fileData[2])
        # print("{:09d}".format(memberId))
        serviceCode = int(fileData[3])
        # print("{:09d}".format(serviceCode))
        bill = float(fileData[4])
        # print("{:.2f}".format(bill))
        comments = ""
        if (fileData[4] != fileData[-1]):
            comments = fileData[5]
            # print(comments)
        else:
            comments = None

        newRecord = Record(currentTime, serviceDate, providerId,
                           memberId, serviceCode, bill, comments)
        records.append(newRecord)

    for extService in extServices:
        # print(serviceDir + extService)
        file = open(serviceDir + extService, "r")
        fileData = file.readlines()

        # removing \n characters from strings
        count = 0
        for data in fileData:
            if (data[-1] == '\n'):
                fileData[count] = data[:-1]
            count += 1

        code = int(fileData[0])
        # print("{:09d}".format(code))
        name = fileData[1]
        # print(name)
        desc = fileData[2]
        # print(desc)
        cost = float(fileData[3])
        # print("{:.2f}".format(cost))
        newService = Service(code, name, desc, cost)
        services[code] = newService

    # print(services)

    for extMember in extMembers:
        # print(memberDir + extMember)
        file = open(memberDir + extMember, "r")
        fileData = file.readlines()

        # removing \n characters from strings
        count = 0
        for data in fileData:
            if (data[-1] == '\n'):
                fileData[count] = data[:-1]
            count += 1

        name = fileData[0]
        # print(name)
        number = int(fileData[1])
        # print("{:09d}".format(number))
        address = fileData[2]
        # print(address)
        city = fileData[3]
        # print(city)
        state = fileData[4]
        # print(state)
        zip = int(fileData[5])
        # print(zip)
        statusInt = int(fileData[6])
        # print(statusInt)
        status = True
        if (statusInt == 0):
            status = False
        # print(status)

        newMember = Member(name, number, address, city, state, zip, status)
        members[number] = newMember

    # print(members)

    for extProvider in extProviders:
        # print(providerDir + extProvider)
        file = open(providerDir + extProvider, "r")
        fileData = file.readlines()

        # removing \n characters from strings
        count = 0
        for data in fileData:
            if (data[-1] == '\n'):
                fileData[count] = data[:-1]
            count += 1

        name = fileData[0]
        # print(name)
        number = int(fileData[1])
        # print("{:09d}".format(number))
        address = fileData[2]
        # print(address)
        city = fileData[3]
        # print(city)
        state = fileData[4]
        # print(state)
        zip = int(fileData[5])
        # print(zip)
        statusInt = int(fileData[6])
        # print(statusInt)
        status = True
        if (statusInt == 0):
            status = False
        # print(status)
        newProvider = Provider(name, number, address, city, state, zip, status)
        serviceList = fileData[7].split(",")
        for service in serviceList:
            if (service != ""):
                # print("{:09d}".format(int(service)))
                newProvider.addService(int(service))
        providers[number] = newProvider
    # print(providers)
    return

def managerMode(userName: str):
    print(f"\nWelcome to manager mode: {userName}")
    running = True

    while (running):
        print("\nOptions:")
        print("1: Edit member information")
        print("2: Edit provider information")
        print("3: Add a member")
        print("4: Add a provider")
        print("5: Remove a member")
        print("6: Remove a provider")
        print("7: Generate reports")
        print("8: Log out")

        choice = 0
        try:
            choice = int(input("Select an option: "))
        except:
            print("\nOnly numeric characters allowed!")

        if (choice == 1):
            editMember()
        
        elif (choice == 2):
            editMember(True)
        
        elif (choice == 3):
            return
        
        elif (choice == 4):
            return
        
        elif (choice == 5):
            return
        
        elif (choice == 6):
            return
        
        elif (choice == 7):
            return
        
        elif (choice == 8):
            running = False
            print("\nLogging out...")
        
        else:
            print("\nInvalid option selected.")

    return

def writeMemberToFile(member: Member, oldId: int = -1):#TESTED
    scriptDir = os.path.dirname(__file__)
    memberDir = scriptDir + "/Members/"

    if (oldId != -1):
        oldFile = os.path.join(memberDir, f"{oldId:09d}.mem")
        os.remove(oldFile)

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
        file.write(f"{int(member.status)}\n")

    return

def writeProviderToFile(provider: Provider, oldId: int = -1):#TESTED
    scriptDir = os.path.dirname(__file__)
    providerDir = scriptDir + "/Providers/"

    if (oldId != -1):
        oldFile = os.path.join(providerDir, f"{oldId:09d}.prov")
        os.remove(oldFile)

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
        file.write(f"{int(provider.status)}\n")
        for service in provider.serviceCodes:
            file.write(f"{service:09d},")

    return

def editMember(providerMode: bool = False):#TESTED
    editing = None
    
    if (providerMode):
        ID = int(input("\nEnter the ID of the provider: "))
        editing = providers.get(ID)
    else:
        ID = int(input("\nEnter the ID of the member: "))
        editing = members.get(ID)


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
                status = input("Enter \"Valid\" or \"Suspended\"")
                if (status == "Valid"):
                    editing.setStatus(True)
                elif (status == "Suspended"):
                    editing.setStatus(False)
                else:
                    print("\nInvalid status entered!")
            
            elif (choice == 7 or choice == 8 and providerMode):
                serviceCode = 0
                if choice == 7:
                    serviceCode = int(input("Enter service code you'd like to add"))
                else: 
                    serviceCode = int(input("Enter service code you'd like to remove"))

                service = services.get(serviceCode)

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
                providers.pop(ID)
                providers[editing.number] = editing
                writeProviderToFile(editing, ID)
            else:
                members.pop(ID)
                members[editing.number] = editing
                writeMemberToFile(editing, ID)

        except Exception as e:
            print(f"Unable to edit due to ({e}) error")
    else:
        print("\nInvalid ID number")
    
    return

def main():
    addFiles()
    getPasses()

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
            user = input("Enter your username: ")
            password = input("Enter your password: ")

            try:
                if (managerPasses[user] == encrypt(password)):
                    # manager(providers, members, records).welcome()
                    managerMode(user)
                else:
                    print("\nIncorrect password!")
            except:
                print("\nIncorrect username!")

        elif (choice == 2):
            provNum = 0
            try:
                provNum = int(input("\nEnter your provider ID: "))
            except:
                print("\nOnly numeric characters allowed!")
            provPass = input("Enter your password: ")

            try:
                if (providerPasses[provNum] == encrypt(provPass)):
                    providerMode(provNum)
                
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


if __name__ == "__main__":
    main()
