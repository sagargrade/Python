#--------------------------------------------------------------------
# Start Function - To decide the flow the the program
#--------------------------------------------------------------------
def start():
    print("""
    \nYou are in a hall. There are two doors in the hall.\n
    1. One door on your left hand
    2. Another door on your right hand
    \nWhich door would you like to enter?
    """)
    choice = int(input("> "))

    if choice == 1:
        bear_room()
    elif choice == 2:
        tiger_room()
    else:
        print("Looks like you dont want to try. Exit the game.")
#--------------------------------------------------------------------
# Bear Room function - This function allow us to define the bear room
#--------------------------------------------------------------------
def bear_room():
    print("Bear Room")
#--------------------------------------------------------------------
# Tiger Room function - This function allow us to define the tiger
# room
#--------------------------------------------------------------------
def tiger_room():
    print("Tiger Room")
#--------------------------------------------------------------------
# Gold Room function - This function allow us to define the gold
# room
#--------------------------------------------------------------------
def gold_room():
    print("Gold Room")
#--------------------------------------------------------------------
# Actual Processing of the Program
#--------------------------------------------------------------------
start()
