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
        print("Options:")
        print("1: Verify member ID")
        print("2: Print Records")
        print("3: Create a record")
        print("4: Log out")

        choice = 0
        try:
            choice = int(input("Select your mode: "))
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
            print("Logging out...")

        else:
            print("\nInvalid option")

    return

def verifyID():#TESTED
    ID = int(input("\nEnter the ID of the member: "))

    if members.get(ID) is not None:
        print(f"\n{members[ID].name} status:")
        if (members[ID].status == True):
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
            # print("{:09d}".format(int(service)))
            newProvider.addService(int(service))
        providers[number] = newProvider
    # print(providers)
    return


def main():
    addFiles()
    getPasses()

    print("Welcome to ChocAn!")
    running = True
    while (running):     
        manager_mode = manager(providers, members, records)
        print("Options:")
        print("1: Manager Mode")
        print("2: Provider Mode")
        print("3: Quit")

        choice = 0
        try:
            choice = int(input("Select your mode: "))
        except:
            print("\nOnly numeric characters allowed!")

        if (choice == 1):
            manager_mode.welcome()

        elif (choice == 2):
            provNum = int(input("\nEnter your provider ID: "))
            provPass = input("Enter your password: ")

            try:
                if (providerPasses[provNum] == encrypt(provPass)):
                    providerMode(provNum)
                
                else:
                    print("Password is incorrect!")
            except KeyError:
                print("\nNo provider with that ID found!")

        elif (choice == 3):
            print("\nExiting terminal...\nSee you again soon!\n")
            running = False

        else:
            print("Invalid option selected.\n")

    return


if __name__ == "__main__":
    main()
