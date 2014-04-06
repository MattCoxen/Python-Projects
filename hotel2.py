import random
import pickle
guest_list = {}
#guest_list = pickle.load(open( "save.p", "rb" ) )
rooms = {}
    
print("Welcome to the hotel registration system!")

#Let's start by asking the user what he wants to do
#The user must choose 'EXIT' if they want to save the guest list
def asknewguest():
    choice = input("Would you like to ADD or VIEW a guest, VIEW ALL guests, or EXIT?")
    if choice == "ADD":
        enter_new_guest()
    elif choice == "VIEW":
        callinfo()
    elif choice == "VIEW ALL":
        print(guest_list)
        asknewguest()
    elif choice == "EXIT":
        byebye()
    else:
        print("Sorry, I didn't understand that. Please try again.")
        asknewguest()

#If the user wants to VIEW information, we call it up by ID number
#An ID number is used because it is unique, rather than names which can sometimes be the same
def callinfo():
    choice = input("Please enter the guest ID number:")
    choice = int(choice)
    print (guest_list[choice])
    choice2 = input("Would you like to edit this information? Y/N")
    if choice2 == "Y":
        # send the guestID to edit info
        editinfo(choice)
    else:
        asknewguest()

#If the user wants to edit a guest's info, they can do it here
def editinfo(guest):
    #where `guest` is the guestID, to edit the guest, we will use guest_list[guest]
    choice = input("Which data would you like to do? Edit a guest's NAME, or BREAKFAST, or DELETE their file?")
    if choice == "NAME":
        print("Name is currently set to:", guest_list[guest][0],)
        new_name = input("Please type in the new name.")
        guest_list[guest][0] = new_name
        print("The new name is:", guest_list[guest][0])
        asknewguest()
    elif choice == "DELETE":
        #and this is why, it will allow us to delete the guest by their ID easier
        # for things like this, you ususally want to pass the unique ID instead of the data/guest itself
        del guest_list[guest]
        asknewguest()
    else:
        print("The guest's breakfast option is set to:", guest_list[guest][2])
        breakchange = input("Would you like to change this? Y/N")
        if breakchange == "Y":
            if guest_list[guest][2] == True:
                guest_list[guest][2] = False
                print("The guest's breakfast has been successfully cancelled.")
                asknewguest()
            else:
                guest_list[guest][2] = True
                print("The guest's breakfast has been successfully booked!")
                asknewguest()
        else:
            asknewguest()

#When the user chooses ADD at the beginning, they are directed here
#The guest is automatically assigned an ID and room number
#A directory of specific rooms with specific properties will come later,
#as will code to check if the number was already assigned
def enter_new_guest():
    guest_name = input("What is the name of the new guest?")
    guest_breakf = input("Would the guest like breakfast? Y/N")
    if guest_breakf == "Y":
        guest_breakfast = True
    else:
        guest_breakfast = False
    guest_id = random.randint(1000,9999)
    guest_room = random.randint(100,501)
    guest_list[guest_id] = [guest_name, guest_room, guest_breakfast]
    print ("Thanks. I have assigned the guest, ", guest_name, ", the ID number",guest_id)
    print ("Their room number is:", guest_room)
    if guest_breakfast == True:
        print ("The guest has booked breakfast")
    else:
        print ("The guest has chosen not to book breakfast")
    print (guest_list)
    asknewguest()

#Here's a rough way of saving the guest list
#It's executed by choosing EXIT when prompted
def byebye():
    pickle.dump(guest_list, open( "save.p", "wb" ) )
    print("Goodbye!")

asknewguest()
