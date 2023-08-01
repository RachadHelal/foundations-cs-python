from datetime import datetime 
#https://stackoverflow.com/questions/15707532/import-datetime-v-s-from-datetime-import-datetime
f = open("FCS45-Midterm.txt", "r")
admin_tickets = []
user_tickets = []
tickets = []
for line in f: 
  #to convert each line from the txt file into a list, and then appending to the admin and user list 
  #which will create a matrix.
  #https://www.youtube.com/watch?v=hUyopAoOpG4&ab_channel=J%27sLab
  line_strip = line.strip()
  line_split = line_strip.split(", ")
  admin_tickets.append(line_split)
  user_tickets.append(line_split)

#####################################
# Program Functions
#####################################

def bubbleSort(l, num):  
  for x in range(len(l)):
    check_swap = False
    for y in range(len(l) -x -1):
      if (l[y][num] > l[y+1][num]):
        check_swap = True
        temp = l[y]
        l[y] = l[y+1]
        l[y+1] = temp

    if not check_swap:
      return l
    #defining the bubble sort algorithm that I will use later on in the program. 
    #Where l is the matrix and num is the index of the sorting element.

def reverseBubbleSort(l, num):  
  for x in range(len(l)):
    check_swap = False
    for y in range(len(l) -x -1):
      if (l[y][num] < l[y+1][num]):
        check_swap = True
        temp = l[y]
        l[y] = l[y+1]
        l[y+1] = temp

    if not check_swap:
      return l
    #defining the bubble sort algorithm that I will use later on in the program. 
    #Where l is the matrix and num is the index of the sorting element 
  
#####################################
# Admin Functions
#####################################
print(admin_tickets)

def showEventId(): #O(N) N being the length of the dict
  print()
  events_check = {}
  for ticket in admin_tickets: #O(N) N being the length of the list
    if ticket[1] in events_check:
      events_check[ticket[1]] += 1
    else:
      events_check[ticket[1]] = 1
    #Here we are checking if the first index in ticket, being the event, is in the empty dictionary. 
      #if it is, then the value of that key will be incremented by 1. If it is not, then a new dict will be created 
      #with the key as the eventID and the value of 1. This way we will have the keys in the dict as all event ID's with 
      #the value as how many ticket each event has. You can see below when the dict events_check gets printed.

  maximum_ticket_event = 0 
  event_id = ""
  #we set variables in order to compare with the dict key and value. 
  #this allows us later to store the max value of tickets with their corresponding event ID key.

  for event_number, ticket_count in events_check.items():
    if maximum_ticket_event < ticket_count:
      maximum_ticket_event = ticket_count
      event_id = event_number
  #here we are doing the comparison mentioned above and storing a new value for max tickets and getting their 
  #corresponding event ID.

  print(events_check)
  print()
  print(f"The maximum tickets are {maximum_ticket_event} for the event {event_id}")
  print()

def adminBookTicket():
  pass

def showAllTickets():
  pass

def changePriority():
  pass

def removeTicket():
  pass

def displayEvents():
  pass

#####################################
# User Functions
#####################################

def userBookTicket():
  pass

#####################################
# Admin Menu
#####################################

# def adminMenu(): #O(1)
#   print("1. Display Statistics\n2. Book a Ticket\n3. Display all Tickets\n4. Change Ticket's Priority\n5. Disable Ticket\n6. Run Events\n7. Exit")

# def userMenu(): #O(1)
#   print("1. Book a ticket\n2. Exit")

# def main(): #O(N) for N being the user input
#   admin_username = ""
#   admin_password = ""
#   user_password = ""
#   user_type = input("Welcome! Enter user type (Admin or Users): ")

#   while user_type.lower() != "admin" and user_type.lower() != "users":
#     print("Ivalid input")
#     user_type = input("Enter user type (Admin or Users): ")
    
#   is_admin = False        
#   if user_type.lower() == "admin":
#     is_admin = True
#     admin_password = input("Enter admin password: ")
#   elif user_type.lower() == "users":
#     user_password = input("Enter user password: ")

#   if is_admin == True:
#     count = 5
#     while True: 
#       if admin_password.lower() != "admin123123":
#         print("\nIncorrect Username and/or Password")
#         if count > 1:
#           count -= 1
#           print(f"You have {count} remaining trials\n")
#           admin_password = input("Enter admin password: ")
#         if count == 1:
#           print("The program has been terminated")
#           break      
     
#       elif admin_password.lower() == "admin123123":
#         adminMenu()
#         admin_choice = eval(input("Choose a number from the above menu: "))
#         while admin_choice != 7:
#           if admin_choice == 1:
#             showEventID() 
#           elif admin_choice == 2:
#             adminBookTicket()
#           elif admin_choice == 3:
#             showAllTickets()
#           elif admin_choice == 4:
#             changePriority()
#           elif admin_choice == 5:
#             removeTicket()
#           elif admin_choice == 6:
#             displayEvents()
#           else:
#             print("Invalid input\n")
#           adminMenu()
#           admin_choice = eval(input("Choose a number from the above menu: "))
#         print("End of program")
#         break
  
#   if is_admin == False:
#     while user_password != "":
#       print("Password should be empty")
#       user_password = input("Enter user password: ")

#     if user_password == "":
#       userMenu()
#       user_choice = eval(input("Choose a number from the above menu: "))
#       while user_choice != 2:
#         if user_choice == 1:
#           userBookTicket()
#         else:
#           print("Invalid input\n")
#         userMenu()
#         user_choice = eval(input("Choose a number from the above menu: "))
#       print("End of program")

# main()