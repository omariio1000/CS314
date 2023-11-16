from Member import Member
from Provider import Provider
from Service import Service
from Record import Record
import os

records = dict()
services = dict()
members = dict()
providers = dict()

def managerMode():
    print("\nWelcome to manager mode.")

def providerMode():
    print("\nWelcome to provider mode.")

def main():

    '''
    TO-DO LIST:
        FILE HANDLING STUFF FIRST
            CHECK SERVICE DIRECTORY FOR SERVICES
            CHECK PROVIDER DIRECTORY FOR PROVIDERS
            CHECK MEMBER DIRECTORY FOR MEMBER
            CHECK RECORD DIRECTORY FOR RECORDS

        MANAGER MODE
            ADDING/MODIFYING MEMBERS
            ADDING/MODIFYING PROVIDERS
            ADDING/MODIFYING SERVICES
            ADDING/MODIFYING RECORDS
            GENERATE REPORTS
        
        PROVIDER MODE
            VERIFY MEMBER ID
            CREATE RECORDS
            GENERATE REPORTS

        OTHER FILE HANDLING STUFF
            WRITING SERVICES TO DIRECTORY
            WRITING MEMBERS TO DIRECTORY
            WRITING PROVIDERS TO DIRECTORY
            WRITING RECORDS TO DIRECTORY

        VERY LOW PRIORITY
            MANAGER AND PROVIDER ENCRYPTED ACCESS CODES (LIBRARY FOR THIS OR BASIC CIPHER)
            BETTER UI
            DIFFERENT FILE HANDLING (.JSON, DATABSE, ETC)

    '''    
   

    print("Welcome to ChocAn!")
    running = True

    while(running):
        print("\nOptions:")
        print("1: Manager Mode")
        print("2: Provider Mode")
        print("3: Quit")

        choice = int(input("Select your mode: "))
        
        if (choice == 1):
            managerMode()

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