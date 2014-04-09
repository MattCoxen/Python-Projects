import random
import pickle
import time
guest_list = {}
guest_list = pickle.load(open( "save.p", "rb" ) )
rooms = {}
    
print("Welcome to the hotel registration system!")
print("Today's date is:", time.strftime("%d/%m/%Y"))

#To do:
#Print list of all guests who have booked breakfast and their rooms
#Create dict with rooms and their properties
#Generate leaving date by asking 'how many nights?'
#Add code to ensure script checks if an ID was already taken
#If pickle file does not exist, create pickle file
#If input is not correct format, return an error (such as an ID number with letters)

#Let's start by asking the user what he wants to do
#The user must choose 'EXIT' if they want to save the guest list
def asknewguest():
    choice = input("Would you like to ADD or VIEW a guest, VIEW ALL guests, or EXIT?").upper()
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
    choice2 = input("Would you like to edit this information? Y/N").upper()
    if choice2 == "Y":
        # send the guestID to edit info
        editinfo(choice)
    else:
        asknewguest()

#If the user wants to edit a guest's info, they can do it here
def editinfo(guest):
    #where `guest` is the guestID, to edit the guest, we will use guest_list[guest]
    choice = input("Which data would you like to do? Edit a guest's NAME, or BREAKFAST, NIGHTS or DELETE their file?").upper()
    if choice == "NAME":
        print("Name is currently set to:", guest_list[guest][0],)
        new_name = input("Please type in the new name.")
        guest_list[guest][0] = new_name
        print("The new name is:", guest_list[guest][0])
        asknewguest()
    elif choice == "NIGHTS":
        new_nights = int(input("How many nights would the guest like to stay?"))
        guest_list[guest][3] = new_nights
        print("The guest will stay for", guest_list[guest][3], "nights.")
        asknewguest()
    elif choice == "DELETE":
        #and this is why, it will allow us to delete the guest by their ID easier
        # for things like this, you ususally want to pass the unique ID instead of the data/guest itself
        print("All records for guest number",guest,"have been deleted!")
        del guest_list[guest]
        asknewguest()
    else:
        print("The guest's breakfast option is set to:", guest_list[guest][2])
        breakchange = input("Would you like to change this? Y/N").upper()
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
    guest_breakf = input("Would the guest like breakfast? Y/N").upper()
    if guest_breakf == "Y":
        guest_breakfast = True
    else:
        guest_breakfast = False
    guest_id = random.randint(1000,9999)
    guest_room = random.randint(100,501)
    guest_nights = int(input("How many nights would the guest like to stay for?"))
    guest_list[guest_id] = [guest_name, guest_room, guest_breakfast, guest_nights]
    print ("Thanks. I have assigned the guest, ", guest_name, ", the ID number",guest_id)
    print ("Their room number is:", guest_room)
    if guest_breakfast == True:
        print ("The guest has booked breakfast")
    else:
        print ("The guest has chosen not to book breakfast")
    print ("The guest is staying for", guest_nights,"nights.")
    print (guest_list)
    asknewguest()

#Here's a rough way of saving the guest list
#It's executed by choosing EXIT when prompted
def byebye():
    pickle.dump(guest_list, open( "save.p", "wb" ) )
    print("All your changes have now been saved. Goodbye!")

asknewguest()
