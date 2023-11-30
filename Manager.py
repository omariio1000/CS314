from Member import Member
from Provider import Provider
from datetime import datetime, timedelta
import os
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
            elif (choice == 7):
                self.generate_reports()
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
            
            #Write edited member data to file 
            self.writeMemberToFile(edit_member)
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
    
    def writeMemberToFile(self, member):
        scriptDir = os.path.dirname(__file__)
        memberDir = scriptDir + "/Members/"

        # Create a filename based on the member number
        filename = f"{member.number}.mem"
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
        self.writeMemberToFile(temp)
        return temp.number
    # Function to remove the corresponding .mem file
    def removeMemberFile(self, member):
        scriptDir = os.path.dirname(__file__)
        memberDir = scriptDir + "/Members/"

        # Create a filename based on the member number
        filename = f"{member.number}.mem"
        filepath = os.path.join(memberDir, filename)

        # Remove the file if it exists
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"Corresponding .mem file ({filename}) removed.")
        else:
            print(f"Corresponding .mem file not found: {filename}")

    # Remove a member from dict
    def remove_member(self):
        id = int(
            input("\nPlease enter in the ID number of the member you'd like to remove\n"))
        if (self.search_member(id)):
            # Remove member
            removed_member = self.members.pop(id)
            print("Member was successfully removed")

            #rmeove the corresponding .mem file
            self.removeMemberFile(removed_member)
            return 1
        else:
            print("\nKey not found\n")
        return 0
    
    def writeProviderToFile(self, provider):
        scriptDir = os.path.dirname(__file__)
        providerDir = scriptDir + "/Providers/"

        # Create a filename based on the provider number
        filename = f"{provider.number}.prov"
        filepath = os.path.join(providerDir, filename)

        # Open the file for writing
        with open(filepath, "w") as file:
            # Write provider data to the file
            file.write(f"{provider.name}\n")
            file.write(f"{provider.number}\n")
            file.write(f"{provider.address}\n")
            file.write(f"{provider.city}\n")
            file.write(f"{provider.state}\n")
            file.write(f"{provider.zipCode}\n")
            file.write(f"{int(provider.status)}\n")
            if hasattr(provider, 'services'):
                file.write(",".join(str(service) for service in provider.services) + "\n")

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
        temp.setStatus(True)
        # Add to provider dict
        self.providers[temp.number] = temp
        # Add provider to file
        self.writeProviderToFile(temp)


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
            # Update info in corresponding .prov file
            self.writeProvidersToFile(edit_provider)
            return 1
        else:
            print("\nError provider not found\n")
            return 0
        
    # Function to remove the corresponding .prov file
    def removeProviderFile(self, provider):
        scriptDir = os.path.dirname(__file__)
        providerDir = scriptDir + "/Providers/"

        # Create a filename based on the provider number
        filename = f"{provider.number}.prov"
        filepath = os.path.join(providerDir, filename)

        # Remove the file if it exists
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"Corresponding .prov file ({filename}) removed.")
        else:
            print(f"Corresponding .prov file not found: {filename}")

    # Remove provider
    def remove_provider(self):
        id = int(
            input("\nPlease enter the ID of the provider you'd like to remove\n"))
        if (self.search_provider(id)):
            # Remove provider
            removed_provider = self.providers.pop(id)
            print("\nProvider was successfully removed")

            # Remove corresponding .prov file
            self.removeProviderFile(removed_provider)
            return 1
        else:
            print("Provider not found\n")
            return 0

    def display_prov(self):
        for key, provider in self.providers.items():
            provider.display()

    def display_member(self):
        for key, member in self.members.items():
            member.display()

    def generate_reports(self):
        print("\nTo generate a Provider summary report, enter 1")
        print("To generate a Member summary report, enter 2")
        print("To generate a Provider EFT report, enter 3")

        report_type = int(input())
        current_date = datetime.now()

        if report_type == 1:  # Provider summary report
            self.generate_provider_summary_report(current_date)
        elif report_type == 2:  # Member summary report
            self.generate_member_summary_report(current_date)
        elif report_type == 3:  # Provider EFT report
            self.generate_provider_eft_report(current_date)
        else:
            print("Invalid input. No report generated.")

    def generate_provider_summary_report(self, current_date):
        for provider_id, provider in self.providers.items():
            provider_records = self.get_provider_records(provider_id, current_date)

            if provider_records:
                report_data = f"Provider summary report generated for {provider.name} on {current_date.strftime('%Y-%m-%d')}\n\n"
                report_data += f"Provider Name: {provider.name}\n"
                report_data += f"Provider Number: {provider.number}\n"
                report_data += f"Provider Address: {provider.address}, {provider.city}, {provider.state} {provider.zipCode}\n\n"

                for record in provider_records:
                    report_data += f"Date of Service: {record.serviceDate}\n"
                    report_data += f"Date and Time Data Inputted to Computer: {record.currentTime}\n"
                    report_data += f"Member Name: {self.members[record.memberID].name}\n"
                    report_data += f"Member Number: {record.memberID}\n"
                    report_data += f"Service Code: {record.serviceCode}\n"
                    report_data += f"Fee: {record.bill}\n\n"

                report_data += "\n" + "=" * 50 + "\n"

                self.write_report_to_file(f"Provider_Summary_Report_{provider.number}", report_data)
        

    
    def generate_member_summary_report(self, current_date):
        for member_id, member in self.members.items():
            member_records = self.get_member_records(member_id, current_date)

            if member_records:
                report_data_header = f"Member summary report generated for {member.name} on {current_date.strftime('%Y-%m-%d')}\n\n"
                report_data = f"{report_data_header}Member Name: {member.name}\n"
                report_data += f"Member Number: {member.number}\n"
                report_data += f"Member Address: {member.address}, {member.city}, {member.state} {member.zipCode}\n\n"

                for record in member_records:
                    provider_name = self.providers[record.providerID].name if record.providerID in self.providers else "Unknown Provider"
                    service_name = self.services[record.serviceCode].name if record.serviceCode in self.services else "Unknown Service"

                    report_data += f"Date of Service: {record.serviceDate}\n"
                    report_data += f"Provider Name: {provider_name}\n"
                    report_data += f"Service Name: {service_name}\n\n"

                report_data += "\n" + "=" * 50 + "\n"

                filename = f"Member_Summary_Report_{member.name}_{current_date.strftime('%Y-%m-%d')}.txt"
                self.write_report_to_file(filename, report_data)


    def generate_provider_eft_report(self, current_date):
        for provider_id, provider in self.providers.items():
            provider_records = self.get_provider_records(provider_id, current_date)

            if provider_records:
                report_data_header = f"Provider summary report generated for {provider.name} on {current_date.strftime('%Y-%m-%d')}\n\n"
                total_amount = sum(record.bill for record in provider_records)
                report_data = f"Provider EFT report generated for {provider.name} on {current_date.strftime('%Y-%m-%d')}\n"
                report_data += f"Total Amount to be Transferred: ${total_amount}\n\n"
                
                self.write_report_to_file(f"Provider_EFT_Report_{provider.number}", report_data)

    
    def write_report_to_file(self, report_name, report_data):
        reports_dir = "Records"
        os.makedirs(reports_dir, exist_ok=True)

        report_filename = f"{report_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.rec"
        report_filepath = os.path.join(reports_dir, report_filename)

        with open(report_filepath, "w") as report_file:
            report_file.write(report_data)
    
    
    def get_provider_records(self, provider_id, current_date):
        # Filter records for the last week for a specific provider
        provider_records = [record for record in self.records if record.providerID == provider_id
                            and current_date - timedelta(days=7) <= record.serviceDate <= current_date]

        return provider_records

    def get_member_records(self, member_id, current_date):
        # Filter records for the last week for a specific member
        member_records = [record for record in self.records if record.memberID == member_id
                           and current_date - timedelta(days=7) <= record.serviceDate <= current_date]

        return member_records

