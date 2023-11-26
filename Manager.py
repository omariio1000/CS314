from Member import Member
from Provider import Provider

# Manager Class


class manager:
    # Constructor
    def __init__(self, in_providers=None, in_members=None, in_records=None):
        self.providers = in_providers
        self.members = in_members if in_members is not None else {}
        self.records = in_records

    def welcome(self):
        # Variables
        choice = 0
        while(True):
            # Prompt User
            print("Welcome to Manager Mode\n")
            print("To edit information about members please enter 1")
            print("To edit information about providers please enter 2")
            print("To add a member please enter 3")
            print("To add a provider please enter 4")
            print("To remove a member please enter 5")
            print("To remove a provider please enter 6")
            print("To generate reports please enter 7")
            print("To exit manager mode please enter 0")
            choice = int(input())
            # Error Check
            if choice not in [0, 1, 2, 3, 4, 5, 6, 7]:
                print(f"Invalid input: {choice}")
                return 0
            elif(choice == 0):
                break
            elif (choice == 1):
                self.edit_member()
            elif (choice == 2):
                self.edit_provider()
            elif (choice == 3):
                self.add_member()
            elif (choice == 4):
                self.add_provider()
            elif (choice == 5):
                self.remove_member()
            elif (choice == 6):
                self.remove_provider()
            # elif (choice == 7):
            #     #self.display_prov()
            # elif (choice == 8):
            #     #self.display_member()
        return 1

    # Edit member info
    def edit_member(self):
        # Prompt User
        id_number = int(input("Please enter in the ID number of the member\n"))
        # Search for member
        if (self.search_member(id_number) is True):
            edit_member = self.members[id_number]
            # Prompt User
            print("\nTo edit the name of the member please enter 1")
            print("To edit the member ID please enter 2")
            print("To edit the address of the member please enter 3")
            print("To edit the city of the member please enter 4")
            print("To edit the state of the member please enter 5")
            print("To edit the zip code of the member please enter 6")
            print("To edit the status of the member please enter 7")
            temp = int(input())
            # Call setter function
            if (temp == 1):
                name = input("Please enter in the new name of the member\n")
                edit_member.setName(name)
            elif (temp == 2):
                new_id = input("Please enter in the new ID number\n")
                edit_member.setNumber(new_id)
            elif (temp == 3):
                new_add = input(
                    "Please enter in the new address of the member\n")
                edit_member.setAddr(new_add)
            elif (temp == 4):
                new_city = input("Please enter in the name of the new city\n")
                edit_member.setCity(new_city)
            elif (temp == 5):
                new_state = input(
                    "Please enter in the name of the new state\n")
                edit_member.setState(new_state)
            elif (temp == 6):
                new_zip = input(
                    "Please enter in the new zip code of the member\n")
                edit_member.setZip(new_zip)
            elif (temp == 7):
                status = int(input(
                    "Please enter in 1 to activate the member/nPlease enter 0 to deactivate the member\n"))
                edit_member.set_status(status)
            # Display updated info
            print("Updated " + edit_member.name + " info")
            return 1
        else:
            print("\nError member not found\n")
            return 0

    # Search for member in the dict
    def search_member(self, id):
        # Search for member in dictionary
        return id in self.members.keys()

    # Search for provider in the dict
    def search_provider(self, id):
        # Search for provider in dictionary
        return id in self.providers.keys()

    # Add a member to dict
    def add_member(self):
        # Variables
        temp = Member()
        # Read info
        name = input("Please enter in the name of the member\n")
        if (temp.setName(name) is False):
            self.add_member()
        new_id = int(input("Please enter in the ID number\n"))
        if (temp.setNumber(new_id) is False):
            self.add_member()
        new_add = input("Please enter in the address of the member\n")
        if (temp.setAddr(new_add) is False):
            self.add_member()
        new_city = input("Please enter in the of the new city\n")
        if (temp.setCity(new_city) is False):
            self.add_member()
        new_state = input("Please enter in the of the new state\n")
        if (temp.setState(new_state) is False):
            self.add_member()
        new_zip = int(input("Please enter in the zip code of the member\n"))
        if (temp.setZip(new_zip) is False):
            self.add_member()
        temp.setStatus(True)
        # Add to member dict
        self.members[temp.number] = temp
        return temp.number

    # Remove a member from dict
    def remove_member(self):
        id = int(
            input("\nPlease enter in the ID number of the member you'd like to remove\n"))
        if (self.search_member(id)):
            # Remove member
            self.members.pop(id)
            print("Member was successfully removed")
            return 1
        else:
            print("\nKey not found\n")
            return 0

    # Add provider to dict
    def add_provider(self):
        # Variables
        temp = Provider()
        # Read info
        name = input("Please enter in the name of the provider\n")
        if (temp.setName(name) is False):
            self.add_provider()
        new_id = int(input("Please enter in the ID number\n"))
        if (temp.setNumber(new_id) is False):
            self.add_provider()
        new_add = input("Please enter in the address of the provider\n")
        if (temp.setAddr(new_add) is False):
            self.add_provider()
        new_city = input("Please enter in the name of the city\n")
        if (temp.setCity(new_city) is False):
            self.add_provider()
        new_state = input("Please enter in the name of the provider's state\n")
        if (temp.setState(new_state) is False):
            self.add_provider()
        new_zip = int(input("Please enter in the zip code of the provider\n"))
        if (temp.setZip(new_zip) is False):
            self.add_provider()
        temp.setStatus(1)
        # Add to provider dict
        self.providers[temp.number] = temp

    # Remove provider
    def remove_provider(self):
        id = int(
            input("\nPlease enter the ID of the provider you'd like to remove\n"))
        if (self.search_provider(id)):
            # Remove provider
            self.providers.pop(id)
            print("\nProvider was successfully removed")
            return 1
        else:
            print("Provider not found\n")
            return 0

    # Edit member info
    def edit_provider(self):
        # Prompt User
        id_number = int(
            input("Please enter in the ID number of the provider\n"))
        # Search for provider
        if ((self.search_provider(id_number)) == True):
            edit_provider = self.providers[id_number]
            # Prompt User
            print("\nTo edit the name of the number please enter 1")
            print("To edit the provider ID please enter 2")
            print("To edit the address of the provider please enter 3")
            print("To edit the city of the provider please enter 4")
            print("To edit the state of the provider please enter 5")
            print("To edit the zip code of the provider please enter 6")
            print("To edit the status of the provider please enter 7")
            temp = int(input())
            # Call setter function
            if (temp == 1):
                name = input("Please enter in the new name of the provider\n")
                edit_provider.setName(name)
            elif (temp == 2):
                new_id = input("Please enter in the new ID number\n")
                edit_provider.setNumber(new_id)
            elif (temp == 3):
                new_add = input(
                    "Please enter in the new address of the provider\n")
                edit_provider.setAddr(new_add)
            elif (temp == 4):
                new_city = input("Please enter in the name of the new city\n")
                edit_provider.setCity(new_city)
            elif (temp == 5):
                new_state = input(
                    "Please enter in the name of the new state\n")
                edit_provider.setState(new_state)
            elif (temp == 6):
                new_zip = input(
                    "Please enter in the new zip code of the provider\n")
                edit_provider.setZip(new_zip)
            elif (temp == 7):
                status = int(input("Please enter in 1 to activate the provider\n" +
                                   "Please enter 0 to deactivate the provider\n"))
                if (status == 1):
                    edit_provider.set_status(True)
                elif (status == 0):
                    edit_provider.set_status(False)
            # Display updated info
            print("Updated " + edit_provider.name + " info")
            return 1
        else:
            print("\nError provider not found\n")
            return 0

    def display_prov(self):
        for key, provider in self.providers.items():
            provider.display()

    def display_member(self):
        for key, member in self.members.items():
            member.display()
