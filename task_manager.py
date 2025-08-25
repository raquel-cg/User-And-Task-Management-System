# Compulsory Task 1

#=====importing libraries===========
import datetime

#====Login Section====
# Empty dictionary to store the usernames and passwords.
user = {}

# Reads the users data for the text file.   
with open("user.txt", "r") as file:
    for line in file:
        username, password = line.strip().split(", ")  # Splits the username and password.
        user[username] = password

# Ask the user for a username and a password.
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Checks if the username and password is correct.
    if username not in user:
        print("\nInvalid username. Please enter again!\n")
    elif user[username] != password:
        print("\nInvalid password. Please enter again!\n")
    else:
        print(f"\nWelcome {username}!")
        break  # Exits the loop after a successful login.

while True:
    # Compulsory Task 2
    # This displays the new menu only for admin.
    if username == 'admin':
        menu = input('''\nSelect one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
vs - view statistics
e - exit
: ''').lower()
    # This will be displayed for other types of usesrs.
    else:
        menu = input('''\nSelect one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r':
        # Compulsory Task 2
        # This only allows admin to register new users.
        if username != "admin":
            print("\nYou are not authorized to register new users!")
            continue

        while True:
        # Asks user to enter the new username.
            new_username = input("\nEnter a new username: ")

        # This checks if the username entered already exists.
            if new_username in user:
                print("\nThe username entered already exists. Please enter another username!")
                continue

        # Asks the user to enter a new password and then confirm the new password.
            new_password = input("Enter a new password: ")
            confirm_password = input("Confirm your new password: ")

        # This checks if the passwords are the same.
            if new_password == confirm_password:
                with open("user.txt", "a") as file:
                    file.write(f"\n{new_username}, {new_password}")
                user[new_username] = new_password
                print("\nThe new user has successfully registered!")
                break
            else:
                print("\nPasswords do not match. Please enter again!")

    elif menu == 'a':
        # Ask the user to enter all the details.
        t_assigned_to = input("\nEnter the username of the person the task is assigned to: ")
        t_title = input("Enter the title of the task: ")
        t_description = input("Enter the description of the task: ")
        t_due_date = input("Enter the due date of the task: ")

        # This gets the current date (Used Stack Overflow).
        current_date = datetime.datetime.now().strftime("%d %b %Y")

        # Default task completion status.
        completed = "No"

        # This adds all the information to the task text file.
        with open("tasks.txt", "a") as f:
            f.write(f"\n{t_assigned_to}, {t_title}, {t_description}, {current_date}, {t_due_date}, {completed}")
        
        # This lets the user know that the task has been added.
        print("\nThe task has been successfully added!")

    elif menu == 'va':
        with open("tasks.txt", "r") as f:
            # Reads each task line by line.
            for line in f:
                # This splits the line into seperate parts.
                t_details = line.strip().split(", ")

                # This extracts each part of the task.
                t_assigned_to = t_details[0]
                t_title = t_details[1]
                t_description = t_details[2]
                current_date = t_details[3]
                t_due_date = t_details[4]
                completed = t_details[5]

                # This will display the task details the same way as Output 2.
                print("\n--------------------------------------------------------------------------")
                print(f"Task:\t\t\t{t_title}")
                print(f"Assigned to:\t\t{t_assigned_to}")
                print(f"Date assigned:\t\t{current_date}")
                print(f"Due date:\t\t{t_due_date}")
                print(f"Task Complete?\t\t{completed}")
                print(f"Task description:\t{t_description}")
                print("--------------------------------------------------------------------------")

    elif menu == 'vm':
        with open("tasks.txt", "r") as f:
            # Reads each task line by line.
            for line in f:
                # Splits the line into seperate parts.
                t_details = line.strip().split(", ")

                # This extracts each part of the task.
                t_assigned_to = t_details[0]
                t_title = t_details[1]
                t_description = t_details[2]
                current_date = t_details[3]
                t_due_date = t_details[4]
                completed = t_details[5]

                # Checks if tasks is assigned to current user.
                if t_assigned_to == username:
                    print("\n--------------------------------------------------------------------------")
                    print(f"Task:\t\t\t{t_title}")
                    print(f"Assigned to:\t\t{t_assigned_to}")
                    print(f"Date assigned:\t\t{current_date}")
                    print(f"Due date:\t\t{t_due_date}")
                    print(f"Task Complete?\t\t{completed}")
                    print(f"Task description:\t{t_description}")
                    print("--------------------------------------------------------------------------")
    
    # Compulsory Task 2
    # This menu option is only visible to admin.
    elif menu == 'vs' and username == 'admin':
        # Admin menu option to show statistics.
        with open("tasks.txt", "r") as f:
            total_tasks = sum(1 for line in f)  # Counts total tasks.

        total_users = len(user)  # Counts total users in the user dictionary.

        print("\n--------------------------------------------------------------------------")
        print("Statistics:")
        print(f"Total number of tasks: {total_tasks}")
        print(f"Total number of users: {total_users}")
        print("--------------------------------------------------------------------------")
   
    elif menu == 'e':
        print('\nGoodbye!!!')
        exit()

    else:
        print("\nYou have entered an invalid input. Please try again")

        