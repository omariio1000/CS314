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
