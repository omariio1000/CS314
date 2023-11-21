from Member import Member
from Provider import Provider
from Service import Service
from Record import Record
from datetime import datetime
from Manager import manager
import os

records = []
services = dict()
members = dict()
providers = dict()

def providerMode():
    print("\nWelcome to provider mode.")
    return

def addFiles():
    scriptDir = os.path.dirname(__file__) #absolute dir
    recordDir =  scriptDir + "/Records/"
    serviceDir =  scriptDir + "/Services/"
    memberDir =  scriptDir + "/Members/"
    providerDir =  scriptDir + "/Providers/"

    extRecords = os.listdir(recordDir)
    extServices = os.listdir(serviceDir)
    extMembers = os.listdir(memberDir)
    extProviders = os.listdir(providerDir)

    for extRecord in extRecords:
        # print(recordDir + extRecord)
        file = open(recordDir + extRecord, "r")
        fileData = file.readlines()
        
        #removing \n characters from strings
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
        # print("{:06d}".format(providerId))
        
        memberId = int(fileData[2])
        # print("{:06d}".format(memberId))
        
        serviceCode = int(fileData[3])
        # print("{:06d}".format(serviceCode))

        bill = float(fileData[4])
        # print("{:.2f}".format(bill))

        comments = ""
        if (fileData[4] != fileData[-1]):
            comments = fileData[5]
            # print(comments)
        else:
            comments = None

        newRecord = Record(currentTime, serviceDate, providerId, memberId, serviceCode, bill, comments)
        records.append(newRecord)


    for extService in extServices:
        # print(serviceDir + extService)
        file = open(serviceDir + extService, "r")
        fileData = file.readlines()
        
        #removing \n characters from strings
        count = 0
        for data in fileData:
            if (data[-1] == '\n'):
                fileData[count] = data[:-1]
            count += 1

        code = int(fileData[0])
        # print("{:06d}".format(code))

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
        
        #removing \n characters from strings
        count = 0
        for data in fileData:
            if (data[-1] == '\n'):
                fileData[count] = data[:-1]
            count += 1

        name = fileData[0]
        # print(name)

        number = int(fileData[1])
        # print("{:06d}".format(number))

        address = fileData[2]
        # print(address)

        city = fileData[3]
        # print(city)

        state = fileData[4]
        # print(state)

        zip = int(fileData[5])
        # print(zip)

        status = int(fileData[6])
        # print(status)

        newMember = Member(name, number, address, city, state, zip, status)
        members[number] = newMember

    # print(members)

    for extProvider in extProviders:
        # print(providerDir + extProvider)
        file = open(providerDir + extProvider, "r")
        fileData = file.readlines()
        
        #removing \n characters from strings
        count = 0
        for data in fileData:
            if (data[-1] == '\n'):
                fileData[count] = data[:-1]
            count += 1

        name = fileData[0]
        # print(name)

        number = int(fileData[1])
        # print("{:06d}".format(number))

        address = fileData[2]
        # print(address)

        city = fileData[3]
        # print(city)

        state = fileData[4]
        # print(state)

        zip = int(fileData[5])
        # print(zip)

        status = int(fileData[6])
        # print(status)

        newProvider = Provider(name, number, address, city, state, zip, status)

        serviceList = fileData[7].split(",")
        for service in serviceList:
            # print("{:06d}".format(int(service)))
            newProvider.addService(int(service))

        providers[number] = newProvider

    # print(providers)

    return

def main():
    addFiles()

    '''
    TO-DO LIST:
        FILE HANDLING STUFF FIRST - DONE
            CHECK SERVICE DIRECTORY FOR SERVICES - DONE
            CHECK PROVIDER DIRECTORY FOR PROVIDERS - DONE
            CHECK MEMBER DIRECTORY FOR MEMBER - DONE
            CHECK RECORD DIRECTORY FOR RECORDS - DONE

        MANAGER MODE - NAJIIB
            ADDING/MODIFYING MEMBERS
            ADDING/MODIFYING PROVIDERS
            ADDING/MODIFYING SERVICES
            ADDING/MODIFYING RECORDS
            GENERATE REPORTS
        
        PROVIDER MODE - ABDIRIZAK
            VERIFY MEMBER ID
            CREATE RECORDS
            GENERATE REPORTS

        OTHER FILE HANDLING STUFF - LAYAAL
            WRITING SERVICES TO DIRECTORY
            WRITING MEMBERS TO DIRECTORY
            WRITING PROVIDERS TO DIRECTORY
            WRITING RECORDS TO DIRECTORY

        VERY LOW PRIORITY - OMAR
            MANAGER AND PROVIDER ENCRYPTED ACCESS CODES (LIBRARY FOR THIS OR BASIC CIPHER)
            BETTER UI
            DIFFERENT FILE HANDLING (.JSON, DATABSE, ETC) - really not tryna do this

        TESTING - ADAM + ABDIRIZAK

    '''    

    print("Welcome to ChocAn!")
    running = True
    while(running):
       #print(members[1].number)
        manager_mode = manager(providers, members, records)
        print("\nOptions:")
        print("1: Manager Mode")
        print("2: Provider Mode")
        print("3: Quit")

        choice = int(input("Select your mode: "))
        
        if (choice == 1):
            manager_mode.welcome()

        elif (choice == 2):
            providerMode()

        elif (choice == 3):
            print("\nExiting terminal...\nSee you again soon!\n")
            running = False

        else:
            print("Invalid option selected.\n")

    return

if __name__ == "__main__":
    main()