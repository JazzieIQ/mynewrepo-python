# Coder: Matthew Gutierrez
# CIT 95 Giraffe Academy

import math

# Input Variable Prooram
print("\nMac MAc's Python Program")
print("Welcome to my user input program")
name = input("\nPlease input name user: ")
print("\nUser name is " + name + ".")
print("Great! Thank You. \n\nMy inquiry will now continue.")

 # Boolean Program

print("\nAre you a student?")

student_status = input("Please type yes or no: ")
status_string = "You are a student: "
while student_status.lower() not in ("yes", "no"):
    student_status = input("Please type yes or no: ")
else:
    if student_status == "yes":
        print(status_string + student_status)
    else:
        print(status_string + student_status)

# list array

user_info = [name, student_status]
users = [user_info]
print("I have logged this info. " + str(users))

try:
    print("\n\nWould you like to enter another user to my list?")
    continue_list = input("Please respond with 'Y' or 'N': ")
    while continue_list.upper() not in ("Y", "N"):
        continue_list = input("Please respond with 'Y' or 'N': ")
    else:
        if continue_list == ("Y"):
            name = input("\nPlease input name user: ")
            print("\nUser name is " + name + ".")
            print(status_string)
            student_status = input("Please type yes or no: ")
            while student_status.lower() not in ("yes", "no"):
                student_status = input("Please type yes or no: ")
            else:
                if student_status == "yes":
                    print(status_string + student_status)
                    user_info = [name, student_status]
                    users.append(user_info)
                else:
                    student_status = "no"
                    print(status_string + student_status)
                    user_info = [name, student_status]
                    users.append(user_info)
            print("Here is the existing list" + str(users)+ ". Thank You I will terminate now.")

        else:
            print("Here is the existing list" + str(users) + ". Thank You I will terminate now.")
except:
    print("Oops something happened.I'm sorry i'm a fragile inquiry program. I must terminate.")
