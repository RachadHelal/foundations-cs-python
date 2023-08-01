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
print(admin_tickets) #####################################################################################################

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

def adminBookTicket(): #O(N) N being the length of the list
  print()
  max_ticket_num = 0 #we assign a variable in order to compare it with actual ticket number and in order
  #to use it later on when auto incrementing ticket ID number.
  for ticket in admin_tickets: #O(N) N being the length of the list
    latest_ticket_num = int(ticket[0][4:]) #we are casting the ticket number into an integer so we are able to auto increment it later.
    if max_ticket_num < latest_ticket_num:
      max_ticket_num = latest_ticket_num #we compare the ticket id number in the matrix with the the variable assigned at the beginning of the function. 
      #This way we get the highest ticket number in the matrix and then auto increment from that last higher ticket number.

  print("You are about to book a ticket for an existing event.")
  is_event = False #we add this boolean in order to break out thr while loop when the event date and event number is found in the matrix.
  while not is_event:
    username = input("Please enter username: ")
    event_id = input("Please enter event ID ('ev001'): ")
    event_date = input("Please enter event date (YYYYMMDD): ")
    priority_num = input("Please enter priority number: ")
    for ticket in admin_tickets:
      if event_id and event_date in ticket: #checking if event id and date are in the tickets we are iterating through.
        is_event = True #if the boolean is true, then the event date and number are found, which will allow us to book a new ticket.
        lst = ["tick" + str(max_ticket_num + 1), event_id, username, event_date, priority_num] #creating the ticket in order to add 
        #it to the matrix (list of tickets) after booking it. 
    if not is_event: #if the event id and date are not in the list of tickets, then the below will be printed and we 
      #repeat the process of booking a ticket until the event date and Id input by the user matches the ones in the ticket lists.
      print("The event date or event ID does not exist, please try again.")

  admin_tickets.append(lst) #we are adding the newly booked ticket to the matrix of tickets.
  print()
  print("The added ticket is: ", lst)
  print()
  print("Tickets updated are: ", admin_tickets)
  print()

def showAllTickets(): #O(N^2) N being the length of the list
  print()
  pending_events = [] #we create an empty list to showcase all event that will take place today or in the future.
  old_events = [] #we create an empty list to showcase all event that already took place.
  today = datetime.now().date() #we are creating a today variable where we can compare the event date with today's date. I got this from google.
  for ticket in admin_tickets: #O(N) N being the length of the list
    event_date = datetime.strptime(ticket[3], "%Y%m%d").date() #we are assigning the index 3 of each ticket as a date in order to 
    #compare it with today's date. 
    #https://stackoverflow.com/questions/3278999/how-can-i-compare-a-date-and-a-datetime-in-python
    if event_date >= today: #if the event's date is either TODAY or in the future, then that ticket will be appended
      # to the pending_events list
      pending_events.append(ticket)
    else: #if the event's date is in the past, then that ticket will be appended to the old_events list
      old_events.append(ticket)
  print("The old events are: ", old_events)
  print()
  print("The pending events are: ", pending_events)
  print()
  bubbleSort(pending_events, 3) #O(N^2) N being the length of the list. Here we are sorting based on event date (index 3)
  bubbleSort(pending_events, 1) #O(N^2) N being the length of the list. Here we are sorting based on event ID (index 1)
  print("The pending events sorted by event date and id are: ", pending_events)
  print()

def changePriority(): #O(N) N being the length of the list
  print()
  print("You are about to change the priority of a ticket")
  is_ticket = False #we set the boolean as false so it turns true when the ticket ID matches witht the input ticket id number 
  #from the user and this will allows us to change the priority of any ticket the user inputs as long as it is in the matrix.
  while not is_ticket:
    ticket_id = input("Enter ticket ID to change ('tick101'): ")
    for ticket in admin_tickets: #O(N) N being the length of the list
      if ticket_id in ticket:
        is_ticket = True #we iterate through evey ticket and we check if the ticketID of every ticket matches with
        #the ticket number input by the user, if they match, then the boolean becomes true, which will allows us to move on 
        # and change the priority of the ticket, and then the while loop will automatically break.
        new_priority = input("Enter a new priority number for the ticket: ")
        ticket[4] = new_priority #setting the new priority number
        print("The modified ticket is: ", ticket)
    if not is_ticket:
      print("The ticket you are searching for was not found, please try again")
  print()

def removeTicket(): #O(N) N being the length of the list
  print()
  print("You are about to remove a ticket from the system.")
  is_ticket = False #we set the boolean as false so it turns true when the ticket ID matches witht the input ticket id number
  while not is_ticket:
    ticket_id = input("Enter the ticket ID to remove the ticket ('tick101'): ")
    print()
    for ticket in admin_tickets: #O(N) N being the length of the list
      if ticket_id in ticket:  #we iterate through evey ticket and we check if the ticketID of every ticket matches with
        #the ticket number input by the user, if they match, then the boolean becomes true, which will allows us to move on 
        #and remove the ticket from the matrix using the remove function below (.remove()). The while loop will automatically break after this.
        is_ticket = True
        print("The ticket to be removed is: ", ticket)
        admin_tickets.remove(ticket)
    if not is_ticket:
      print("The ticket you are searching for was not found, please try again")
  print()
  print("The remaining tickets are: ", admin_tickets)
  print()

def displayEvents(): #O(N^2) N being the length of the list
  print()
  todays_events = [] #we are creating an empty list to add todays tickets in them, and sort them.
  today = datetime.now().date() #we are creating a today variable where we can compare the event date with today's date.
  for ticket in admin_tickets: #O(N) N being the length of the list
    event_date = datetime.strptime(ticket[3], "%Y%m%d").date()
    ticket[4] = int(ticket[4])
    if event_date == today:
      todays_events.append(ticket)
      reverseBubbleSort(todays_events, 4) #O(N^2) N being the length of the list
      # today_tickets.sort(key=lambda ticket: ticket[4]) 
      #https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
      #The above sorts the list based on the fourth element in the ticket, which is the ticket priority. The time complexity
      # of this function is O(N*logN) which is better than the bubble sort being O(n^2). I prefered doing the bubble sort 
      # to practice, but I would choose the sort function above for a better time complexity.
  for ticket in todays_events: #O(N) N being the length of the list
    if ticket in admin_tickets: #if the tickets from today's events are in the main matrix (admin_tickets), they will be removed
      admin_tickets.remove(ticket)
  print("Today's events sorted by priority are: ", todays_events)
  print()
  print("The remaining tickets are: ", admin_tickets)
  print()

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