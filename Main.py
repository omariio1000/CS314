from Member import Member
from Provider import Provider
from Service import Service
from Record import Record
from Terminal import Terminal
from datetime import datetime
from Encryption import *
import os

records = []
services = dict()
members = dict()
providers = dict()

managerPasses = dict()
providerPasses = dict()

def addFiles():
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

def getPasses():
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

def main():
    try:
        addFiles()
        getPasses()
    except Exception as e:
        print(f"Unable to initialize due to error ({e})")
        exit(1)

    try:
        terminal = Terminal(records, services, members, providers, managerPasses, providerPasses)
        terminal.run()
    except Exception as e:
            print(f"Unable to run due to error ({e})")

if __name__ == "__main__":
    main()
