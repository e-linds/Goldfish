#this app is to count how many days I'm in office per month

from functions import add_new, add_to_db, check_monthly_numbers, print_attendance, check_ip, get_location

input1 = input('''What would you like to do? 
               1: Check monthly office numbers. 
               2: Check another location. 
               3: Add new location.
               4: See entire database.
               ''')

if input1 == "1":
    check_monthly_numbers("office")
elif input1 == "2":
    input2 = input('''Which location? Choose from:
                   1: home
                   2: Hello Darling
                   3: The Wild
                   ''')
    
    if input2 == "1":
        check_monthly_numbers("home")
    elif input2 == "2":
        check_monthly_numbers("Hello Darling")
    elif input2 == "3":
        check_monthly_numbers("The Wild")
    else:
        print("That's not one of the options! Please try again")
#still need to add in logic to send user back to question if they answer wrong

elif input1 == 3:
    print("still need to build this")
elif input1 == "4":
    print_attendance()
else:
    print("That's not one of the options, please try again!")



# add_to_db()

# check_ip()

# get_location()

# add_new()

# check_monthly_numbers("office")

# print_attendance()