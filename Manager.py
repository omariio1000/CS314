#Manager Class
class manager:
    #Constructor
    def __init__(self, providers = None, members = None, records = None):
        self.providers = providers
        self.members = members
        self.records = records
    def welcome(self):
        #Variables
        choice = 0
        member_id = 0
        try:
            #Prompt User
            print("Welcome to Manager Mode\n")
            print("To edit information about members please enter 1")
            print("To edit information about providers please enter 2")
            print("To generate reports please enter 3")
            choice = int(input())
            #Error Check
            if choice not in [1,2,3]:
                raise choice
            elif(choice == 1):
                self.edit_member()
                
            return 1
        except:
            print(f"Invlaid input: {choice}")
            return 0

    def edit_member(self):
        #Prompt User
        id_number = input("Please enter in the ID number of the member\n")
        #Search for member
        if(self.search_member(id_number)):
            member = self.members[id_number]
            #Prompt User
            print("To edit the name of the number please enter 1")
            print("To edit the member ID please enter 2")
            print("To edit the address of the member please enter 3")
            print("To edit the city of the member please enter 4")
            print("To edit the state of the member please enter 5")
            print("To edit the zip code of the member please enter 6")
            print("To edit the status of the member please enter 7")
            temp = int(input())
            #Call setter function
            if(temp == 1):
                name = input("Please enter in the new name of the member")
                member.setName(name)
            elif(temp == 2):
                new_id = input("Please enter in the new ID number")
                member.setNumber(new_id)
            elif(temp == 3):
                new_add = input("Please enter in the new address of the member")
                member.setAddr(new_add)
            elif(temp == 4):
                new_city = input("Please enter in the name of the new city")
                member.setCity(new_city)
            elif(temp == 5):
                new_state = input("Please enter in the name of the new state")
                member.setState(new_state)
            elif(temp == 6):
                new_zip = input("Please enter in the new zip code of the member")
                member.setZip(new_zip)
            elif(temp == 7):
                status = int(input("Please enter in 1 to activate the member/nPlease enter 0 to deactivate the member"))
                member.set_status(status)
            #Display updated info
            print("Updated " + member.name + " info")
            print(member)
            return 1
        else:
            return 0
    def search_member(self, id):
        #Search for member in dictionary
        if id in self.members:
            return True
        else:
            print("\nError: Member not found")
            return False

