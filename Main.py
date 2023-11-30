from Member import Member
from Provider import Provider
from Service import Service
from Record import Record
from datetime import datetime, timedelta
from Encryption import *
import os

records = []
services = dict()
members = dict()
providers = dict()

managerPasses = dict()
providerPasses = dict()

def providerMode(provID: int):
    print(f"\nWelcome to provider mode: {providers[provID].name}")
    running = True
    
    while (running):
        print("\nOptions:")
        print("1: Verify member ID")
        print("2: Print Records")
        print("3: Create a record")
        print("4: Change your password")
        print("5: Log out")

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
            updateProviderPassword(provID)

        elif (choice == 5):
            running = False
            print("\nLogging out...")

        else:
            print("\nInvalid option")

    return

def verifyID():
    ID = int(input("\nEnter the ID of the member: "))

    if members.get(ID) is not None:
        print(f"\n{members[ID].name} status:")
        if (members[ID].status == False):
            print("Suspended")
        else:
            print("Validated")
    else:
        print("\nInvalid ID number")

def printRecords(provID: int):
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

def writeRecordToFile(record):
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
    
def createRecords(provID: int):
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

def updatePasswords():
    scriptDir = os.path.dirname(__file__)
    passDir = scriptDir + "/Passwords/"
    
    managerFile = os.path.join(passDir, "managers.pass")
    providerFile = os.path.join(passDir, "providers.pass")
   
    os.remove(managerFile)
    os.remove(providerFile)

    with open(managerFile, "w") as file:
        for user, password in managerPasses.items():
            file.write(f"{user}:{password}\n")
    
    with open(providerFile, "w") as file:
        for user, password in providerPasses.items():
            file.write(f"{user:09d}:{password}\n")

def updateAdminPassword(user: str):
    newUser = True
    if (managerPasses.get(user) is not None):
        newUser = False
        affirm = input("\nWould you like to view your current password? (y/n): ")
        if (affirm == 'y'):
            print(f"Current password for user ({user}): \"" + decrypt(managerPasses.get(user)) + "\"")
    
    password = input("Enter your new password (0 to cancel): ")
    try:
        managerPasses[user] = encrypt(password)
        if (newUser):
            print("\nUser added successfully!")
        else:
            print("\nPassword set successfully!")
    except Exception as e:
            print(f"\bUnable to edit due to error ({e})")

    
    updatePasswords()
    return

def updateProviderPassword(provID: int):
    affirm = input("\nWould you like to view your current password? (y/n): ")
    if (affirm == 'y'):
        print(f"Current password for provider ({provID}): \"" + decrypt(providerPasses.get(provID)) + "\"")
    try:
        providerPasses.pop(provID)
        password = input("Enter new password (0 to cancel): ")
        providerPasses[provID] = encrypt(password)
    except Exception as e:
            print(f"Unable to edit due to error ({e})")

    updatePasswords()
    return

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

def managerMode(userName: str):
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

        print("10: Generate reports")

        print("11: Change your password")
        print("12: Change provider password")
        print("13: Add new admin user")

        print("14: Log out")

        choice = 0
        try:
            choice = int(input("Select an option: "))
        except:
            print("\nOnly numeric characters allowed!")

        if (choice == 1):
            addMember()
        
        elif (choice == 2):
            editMember()

        elif (choice == 3):
            removeMember()
        
        elif (choice == 4):
            addMember(True)

        elif (choice == 5):
            editMember(True)
        
        elif (choice == 6):
            removeMember(True)
        
        elif (choice == 7):
            addService()

        elif (choice == 8):
            editService()

        elif (choice == 9):
            removeService()

        elif (choice == 10):
            generateReports()

        elif (choice == 11):
            updateAdminPassword(userName)

        elif (choice == 12):
            try:
                provID = int(input("\nEnter a provider ID: "))
                if (providers.get(provID) is not None):
                    updateProviderPassword(provID)
                else:
                    raise ValueError
            except Exception as e:
                print(f"Unable to change password due to error ({e})")
        
        elif (choice == 13):
            user = input("\nEnter a new username: ")
            if (managerPasses.get(user) is None):
                updateAdminPassword(user)
            else:
                print("Already have an admin with that username!")

        elif (choice == 14):
            running = False
            print("\nLogging out...")
        
        else:
            print("\nInvalid option selected.")

    return

# Function to remove the corresponding .mem file
def removeMemberFile(ID: int):
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

def writeMemberToFile(member: Member, oldId: int = -1):
    scriptDir = os.path.dirname(__file__)
    memberDir = scriptDir + "/Members/"

    if (oldId != -1):
        removeMemberFile(oldId)

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
def removeProviderFile(ID: int):
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

def writeProviderToFile(provider: Provider, oldId: int = -1):
    scriptDir = os.path.dirname(__file__)
    providerDir = scriptDir + "/Providers/"

    if (oldId != -1):
        removeProviderFile(oldId)

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

def editMember(providerMode: bool = False):
    editing = None
    ID = 0

    try:
        if (providerMode):
            ID = int(input("\nEnter the ID of the provider: "))
            editing = providers.get(ID)
        else:
            ID = int(input("\nEnter the ID of the member: "))
            editing = members.get(ID)
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

                if (providerMode and providers.get(newID) is not None):
                    print("\nAnother provider has this ID!")
                    raise ValueError
                elif (not providerMode and members.get(newID) is not None):
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

                temp = providerPasses[ID]
                providerPasses.pop(ID)
                providerPasses[editing.number] = temp
                updatePasswords()
            else:
                members.pop(ID)
                members[editing.number] = editing
                writeMemberToFile(editing, ID)

        except Exception as e:
            print(f"Unable to edit due to error ({e})")
    else:
        print("\nInvalid ID number")
    
    return

def addMember(providerMode: bool = False):
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
                            if (services.get(code) is not None):
                                if (adding.addService(code) == True):
                                    print("Service added.")
                            else:
                                print("Invalid service code! Not added to provider.")
                        except:
                            print("\nOnly numeric characters allowed!")
            
            if (providerMode):
                if (providers.get(adding.number) is None):
                    providers[adding.number] = adding
                    writeProviderToFile(adding)

                    providerPasses[adding.number] = encrypt("password")
                    updatePasswords()
                else:
                    print("Provider with this ID already exists!")
            else:
                if (members.get(adding.number) is None):
                    members[adding.number] = adding
                    writeMemberToFile(adding)
                else:
                    print("Member with this ID already exists!")

        except Exception as e:
            print(f"Unable to add due to error ({e})")

    return

def removeMember(providerMode: bool = False):
    removing = None
    ID = 0
    
    try:
        if (providerMode):
            ID = int(input("\nEnter the ID of the provider: "))
            removing = providers.get(ID)
        else:
            ID = int(input("\nEnter the ID of the member: "))
            removing = members.get(ID)

        if removing is not None:
            removing.display()

            affirm = input("Are you sure you would like to remove? (y/n): ")
            if (affirm == 'y'):
                if(providerMode):
                    providers.pop(ID)
                    removeProviderFile(ID)

                    providerPasses.pop(ID)
                    updatePasswords()
                else:
                    members.pop(ID)
                    removeMemberFile(ID)

            elif (affirm == "n"):
                print("\nNot removed.")
            else:
                print("\nInvalid Input. Not removed.")
    except Exception as e:
            print(f"Unable to remove due to error ({e})")

    return

# Function to remove the corresponding .svc file
def removeServiceFile(ID: int):
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

def writeServiceFile(service: Service, oldId: int = -1):
    scriptDir = os.path.dirname(__file__)
    serviceDir = scriptDir + "/Services/"

    if (oldId != -1):
        removeServiceFile(oldId)

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
    
def addService():
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

        if (services.get(code) is None):
            services[code] = adding
            writeServiceFile(adding)
        else:
            print("\nService with that code already exists!")

    except Exception as e:
            print(f"Unable to add due to error ({e})")

    return

def editService():
    editing = None
    try:
        ID = int(input("\nEnter the service code: "))
        editing = services.get(ID)
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
                
                if (services.get(code) is not None):
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
            

            services.pop(ID)
            services[editing.code] = editing
            writeServiceFile(editing, ID)

        except Exception as e:
            print(f"Unable to edit due to error ({e})")
    else:
        print("\nInvalid ID number")
    return

def removeService():
    removing = None

    try:
        ID = int(input("\nEnter the service code: "))
        removing = services.get(ID)

        if removing is not None:
            removing.display()

            affirm = input("Are you sure you would like to remove? (y/n): ")
            if (affirm == 'y'):
                services.pop(ID)
                removeServiceFile(ID)

            elif (affirm == "n"):
                print("\nNot removed.")
            else:
                print("\nInvalid Input. Not removed.")
    except Exception as e:
            print(f"Unable to remove due to error ({e})")

    return

def generateReports():
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
        generateProviderSummaryReport(currentDate)
    elif choice == 2:  # Member summary report
        generateMemberSummaryReport(currentDate)
    elif choice == 3:  # Provider EFT report
        generateProviderEFTReport(currentDate)
    else:
        print("Invalid input. No report generated.")

def generateProviderSummaryReport(currentDate):
    for providerID, provider in providers.items():
        providerRecords = getProviderRecords(providerID, currentDate)

        if providerRecords:
            reportData = f"Provider summary report generated for {provider.name} on {currentDate.strftime('%Y-%m-%d')}\n\n"
            reportData += f"Provider Name: {provider.name}\n"
            reportData += f"Provider Number: {provider.number}\n"
            reportData += f"Provider Address: {provider.address}, {provider.city}, {provider.state} {provider.zipCode}\n\n"

            for record in providerRecords:
                reportData += f"Date of Service: {record.serviceDate}\n"
                reportData += f"Date and Time Data Inputted to Computer: {record.currentTime}\n"
                reportData += f"Member Name: {members[record.memberID].name}\n"
                reportData += f"Member Number: {record.memberID}\n"
                reportData += f"Service Code: {record.serviceCode}\n"
                reportData += f"Fee: {record.bill}\n\n"

            reportData += "\n" + "=" * 50 + "\n"

            writeReportToFile(currentDate, f"Provider_Summary_Report_{provider.number}", reportData) 

def generateMemberSummaryReport(currentDate):
    for memberID, member in members.items():
        memberRecords = getMemberRecords(memberID, currentDate)

        if memberRecords:
            reportData_header = f"Member summary report generated for {member.name} on {currentDate.strftime('%Y-%m-%d')}\n\n"
            reportData = f"{reportData_header}Member Name: {member.name}\n"
            reportData += f"Member Number: {member.number}\n"
            reportData += f"Member Address: {member.address}, {member.city}, {member.state} {member.zipCode}\n\n"

            for record in memberRecords:
                providerName = providers[record.providerID].name if record.providerID in providers else "Unknown Provider"
                serviceName = services[record.serviceCode].name if record.serviceCode in services else "Unknown Service"

                reportData += f"Date of Service: {record.serviceDate}\n"
                reportData += f"Provider Name: {providerName}\n"
                reportData += f"Service Name: {serviceName}\n\n"

            reportData += "\n" + "=" * 50 + "\n"

            filename = f"Member_Summary_Report_{member.name}_{currentDate.strftime('%Y-%m-%d')}.txt"
            writeReportToFile(currentDate, filename, reportData)

def generateProviderEFTReport(currentDate):
    for providerID, provider in providers.items():
        providerRecords = getProviderRecords(providerID, currentDate)

        if providerRecords:
            reportData_header = f"Provider summary report generated for {provider.name} on {currentDate.strftime('%Y-%m-%d')}\n\n"
            totalAmount = sum(record.bill for record in providerRecords)
            reportData = f"Provider EFT report generated for {provider.name} on {currentDate.strftime('%Y-%m-%d')}\n"
            reportData += f"Total Amount to be Transferred: ${totalAmount}\n"
            
            writeReportToFile(currentDate, f"Provider_EFT_Report_{provider.name}", reportData)

def writeReportToFile(currentDate, reportName, reportData):
    reports_dir = "Reports"
    os.makedirs(reports_dir, exist_ok=True)

    reportFilename = f"{reportName}_{currentDate.strftime('%Y_%m_%d_%H_%M_%S')}.txt"
    report_filepath = os.path.join(reports_dir, reportFilename)

    with open(report_filepath, "w") as report_file:
        report_file.write(reportData)

def getProviderRecords(providerID, currentDate):
    # Filter records for the last week for a specific provider
    providerRecords = [record for record in records if record.providerID == providerID
                        and currentDate - timedelta(days=7) <= record.serviceDate <= currentDate]

    return providerRecords

def getMemberRecords(memberID, currentDate):
    # Filter records for the last week for a specific member
    memberRecords = [record for record in records if record.memberID == memberID
                        and currentDate - timedelta(days=7) <= record.serviceDate <= currentDate]

    return memberRecords

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
