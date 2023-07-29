f = open("FCS45-Midterm.txt", "r")
tickets = []
for line in f:
  line_strip = line.strip()
  line_split = line_strip.split(", ")
  tickets.append(line_split)
print(tickets)
print(f.read())

def showEventID():
  ticket_event_counter = {}
  for ticket in tickets:
    event_id = ticket[1]
  
    if event_id in ticket_event_counter:
      ticket_event_counter[event_id] += 1
    else:
      ticket_event_counter[event_id] = 1
  
  max_event_number = None
  max_ticket_count = 0
  for event_number, ticket_count in ticket_event_counter.items():
    if ticket_count > max_ticket_count:
      max_ticket_count = ticket_count
      max_event_number = event_number

  print("The event id", max_event_number, "has the highest number of tickets, that are:", max_ticket_count)

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

def adminMenu():
  print("1. Display Statistics\n2. Book a Ticket\n3. Display all Tickets\n4. Change Ticket's Priority\n5. Disable Ticket\n6. Run Events\n7. Exit")

def userMenu():
  print("1. Book a ticket\n2. Exit")

def main():
  admin_username = ""
  admin_password = ""
  user_password = ""
  user_type = input("Enter user type (Admin or Users): ")

  while user_type.lower() != "admin" and user_type.lower() != "users":
    print("Ivalid input")
    user_type = input("Enter user type (Admin or Users): ")
    
  is_admin = False        
  if user_type.lower() == "admin":
    is_admin = True
    admin_username = input("Enter admin username: ")
    admin_password = input("Enter admin password: ")
  elif user_type.lower() == "users":
    user_password = input("Enter user password: ")


  if is_admin == True:
    count = 5
    while True: 
      if admin_username.lower() != "admin" or admin_password.lower() != "admin123123":
        print("\nIncorrect Username and/or Password")
        if count > 1:
          count -= 1
          print(f"You have {count} remaining trials\n")
          admin_username = input("Enter admin username: ")
          admin_password = input("Enter admin password: ")
        if count == 1:
          print("The program has been terminated")
          break
          
  
    
      elif admin_username.lower() == "admin" and admin_password.lower() == "admin123123":
        adminMenu()
        admin_choice = eval(input("Choose a number from the above menu: "))
        while admin_choice != 7:
          if admin_choice == 1:
            showEventID() 
          elif admin_choice == 2:
            adminBookTicket()
          elif admin_choice == 3:
            showAllTickets()
          elif admin_choice == 4:
            changePriority()
          elif admin_choice == 5:
            removeTicket()
          elif admin_choice == 6:
            displayEvents()
          else:
            print("Invalid input\n")
          adminMenu()
          admin_choice = eval(input("Choose a number from the above menu: "))
        print("End of program")
        break
  
  if is_admin == False:
    while user_password != "":
      print("Password should be empty")
      user_password = input("Enter user password: ")

    if user_password == "":
      userMenu()
      user_choice = eval(input("Choose a number from the above menu: "))
      while user_choice != 2:
        if user_choice == 1:
          userBookTicket()
        else:
          print("Invalid input\n")
        userMenu()
        user_choice = eval(input("Choose a number from the above menu: "))
      print("End of program")

main()

      
      


    