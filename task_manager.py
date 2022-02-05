# This program will create a program that will help a small bussiness manage
# tasks assigned to each member of the team.
# Working with two text files, user.txt and tasks.txt.

# Importing required functions for getting the date and comparing two dates.
from datetime import date
import calendar

# Used throughout the code to keep track of the tasks, users usernames and
# passwords.
tasks = []
users_names = []
users_password = []

# This function is used to get the date of today to be used later in the code.
def get_date():
    todays_date = date.today()
    current_year = todays_date.year
    current_month = todays_date.month
    current_day = todays_date.day
    month_abbr = calendar.month_abbr[current_month]
    
    return f"{current_day} {month_abbr} {current_year}"

# This function is called if the user is has selected 'r' from the menu
# returning different outputs depending on if the user is admin or not, Also
# depending on if the user already exists.
def reg_user(current_user, current_usernames):
    print("You have selected: Register a new user.\n")
    if current_user == "admin":
        new_username = input("Please enter the new username: ")
        new_password = input("Please enter the new password: ")
        confirm_new_password = input("Please confirm the new password: ")
        
        while new_username in current_usernames:
            new_username = input("Sorry That user already exists please enter "
            "a different username: ")

        if new_password == confirm_new_password:
            users_names.append(new_username)
            users_password.append(new_password)
            with open('user.txt', 'w', encoding='utf-8') as write_user:
                for index in range(len(users_names)):
                    write_user.write(f"{users_names[index]}, "
                                        f"{users_password[index]}\n")

            print("New user added successfully.\n")

        else:
            print("The new password does not match what you entered as the "
                    "confirmation password, Please try again.")

    else:
        print("Sorry only the admin may register new users. Please "
                "Choose a different option from the menu.\n")

# This function will allow the user to add a new task to 'tasks.txt' and is
# called when the user selects 'a' from the menu.
def add_task():
    print("You have selected: Add new task.\n")
    new_task_user = input("Please enter the user for the new task: ")
    new_task_title = input("Please enter the task title for the new "
                            "task: ")
    new_task_des = input("Please enter the task description for the new "
                            "task: ")
    new_task_date = get_date()
    new_task_due = input("Please enter the task due date for the new "
                            "task in this format '06 Jan 2022': ")
    new_task_status = "No"

    new_task = f"{new_task_user}, {new_task_title}, {new_task_des}, "\
                f"{new_task_date}, {new_task_due}, {new_task_status}"

    tasks.append(new_task)
    
    with open('tasks.txt', 'w', encoding='utf-8') as write_tasks:
        for index in range(len(tasks)):
                write_tasks.write(f"{tasks[index]}\n")

# This is used later in the code to update 'tasks.txt' with the current tasks.
def update_tasks():
    with open('tasks.txt', 'r+', encoding='utf-8') as update_tasks:
        for index in range(len(tasks)):
                update_tasks.write(f"{tasks[index]}\n")

# This function allow the user to view all the tasks assigned to all users when
# when they select 'va' from the menu.
def view_all():
    print("You have selected: View all tasks.\n")

    for task in tasks:
        task = task.split(", ")

        print(f"Assigned to:\t{task[0]}\nTask title:\t{task[1]}\n"
            f"Task description:\t{task[2]}\nAssigned date:\t{task[3]}\n"
            f"Due date:\t{task[4]}\nTask completed:\t{task[5]}\n")

# This function allows the user to view all of the tasks that is assigned to
# them and also select individual tasks from the list of tasks assigned to them,
# which they can then select different options to update the task.
def view_mine():
    print("You have selected: View my tasks.\n")

    for index, task in enumerate(tasks):
        task = task.split(",")

        if task[0] == username:
            print(f"Assigned to:\t{task[0]}\nTask title:\t{task[1]}\n"
                f"Task description:\t{task[2]}\nAssigned date:\t{task[3]}\n"
                f"Due date:\t{task[4]}\nTask completed:\t{task[5]}\n"
                f"Current task selection number:\t{index}\n")

    selected_task = int(input("From selection of tasks above enter one of the "
                            "'Current task selection number' in order to "
                            "select that task to be marked as completed or"
                            " to edit the task. If you would like to "
                            "return to the main menu enter '-1': "))

    current_task = tasks[selected_task]
    
    print("")

    if current_task[-3:] != "Yes":
        if selected_task != -1:
            user_choice = input("Type 'mark' to mark the current task as "
                                "completed, Or type 'edit' to edit the current"
                                " task: ").lower()

            print("")
            
            if user_choice == "mark":
                tasks[selected_task] = tasks[selected_task].replace("No", "Yes")
                update_tasks()
                print("Current task has been marked as completed.\n")

            else:
                edit_selection = input("What would you like to edit, Type "
                    "'user' to edit the username of the person to whom the "
                    "task is assigned to. Or type 'due' to edit the due date "
                    "of the task: ").lower()

                if edit_selection == "user":
                    current_task = current_task.split(",")
                    current_user = current_task[0]

                    user_replacement = input("The current user is "
                        f"{current_user}, Who would you like to change it "
                        "to: ")

                    tasks[selected_task] = tasks[selected_task].split(", ")
                    tasks[selected_task][0] = user_replacement
                    tasks[selected_task] = ", ".join(tasks[selected_task])

                    update_tasks()
                    print("The Current task has been reassigned to "
                        f"{user_replacement}.\n")
                
                elif edit_selection == "due":
                    current_task = current_task.split(",")
                    current_due_date = current_task[4]

                    due_date_replacement = input("The current due date is "
                        f"{current_due_date}, What would you like to change it "
                        "to e.g. '20 Jan 2022'. Please use that format: ")

                    tasks[selected_task] = tasks[selected_task].split(', ')
                    tasks[selected_task][4] = due_date_replacement
                    tasks[selected_task] = ", ".join(tasks[selected_task])

                    update_tasks()
                    print("The current tasks due date has been changed from"
                        f"{current_due_date} to {due_date_replacement}\n")

                else:
                    return print("Sorry please choose only 'user' or 'due' to"
                        " edit the selected task.\n")

    else:
        print("Sorry you can only edit tasks that have not been marked as "
                "completed yet.\n")

# This is used later in the code to compare if the tasks and return the amount
# that are overdue and uncompleted.
def compare_date(user_tasks):
    current_date = get_date() 
    current_date_split = current_date.split(" ")
    current_year = current_date_split[2]
    current_month = current_date_split[1]
    current_day = current_date_split[0]
    current_month_as_num = list(calendar.month_abbr).index(current_month)
    compare_current_date = date(int(current_year), int(current_month_as_num), int(current_day))

    total_overdue_uncompleted = 0

    for task in user_tasks:
        task = task.split(", ")
        if task[-1] == "No":
            due_date = task[-2]
            due_date_split = due_date.split(" ")

            due_year = due_date_split[2]
            due_month = due_date_split[1]
            due_day = due_date_split[0]
            due_month_as_num = list(calendar.month_abbr).index(due_month)
            compare_due_date = date(int(due_year), int(due_month_as_num), int(due_day))
            
            is_overdue_uncompleted = compare_current_date > compare_due_date

            if is_overdue_uncompleted == True:
                total_overdue_uncompleted += 1

    return total_overdue_uncompleted

# This is used to compare the date of each user and return the amount of tasks
# that are overdue and uncompleted for each user and not just for all the task.
def compare_users_date():
    current_date = get_date() 
    current_date_split = current_date.split(" ")
    current_year = current_date_split[2]
    current_month = current_date_split[1]
    current_day = current_date_split[0]
    current_month_as_num = list(calendar.month_abbr).index(current_month)
    current_date = date(int(current_year), int(current_month_as_num), int(current_day))

    users_dict = {}
     
    with open('tasks.txt', 'r', encoding='utf-8') as f:
        for task in f:
            
            task = task.replace("\n", "")
            task = task.split(", ")

            due_date = task[-2]
            due_date_split = due_date.split(" ")

            due_year = due_date_split[2]
            due_month = due_date_split[1]
            due_day = due_date_split[0]
            due_month_as_num = list(calendar.month_abbr).index(due_month)
            due_date = date(int(due_year), int(due_month_as_num), int(due_day))

            if (task[-1] == "No") and (current_date > due_date): 
                user = task[0]
                if user in users_dict:
                    users_dict[user] += 1
                else:
                    users_dict[user] = 1

    return users_dict

# This generates the 'task_overview.txt' file with the required information
# when the user enters 'gr' or 'ds' in the menu.
def generate_task_overview():
    total_tasks = 0
    total_completed_tasks = 0
    total_uncompleted_tasks = 0
    total_uncompleted_overdue_tasks = compare_date(tasks)

    for task in tasks:
        task = task.split(", ")
        total_tasks += 1

        if task[-1] == "Yes":
            total_completed_tasks += 1
        elif task[-1] == "No":
            total_uncompleted_tasks += 1

    percentage_incomplete = (total_uncompleted_tasks/total_tasks) * 100
    percentage_overdue = (total_uncompleted_overdue_tasks/total_tasks) * 100

    with open('task_overview.txt', 'w', encoding='utf-8') as write_task_overview:
        write_task_overview.write("The total number of tasks that have been "
            f"generated and tracked: {total_tasks}\nThe total number of "
            f"completed tasks: {total_completed_tasks}\nThe total number of "
            f"uncompleted tasks: {total_uncompleted_tasks}\nThe total number "
            "of tasks that haven't been completed and that are overdue: "
            f"{total_uncompleted_overdue_tasks}\nThe percentage of tasks that "
            f"are incomplete: {percentage_incomplete}%\nThe percentage of tasks"
            f" that are overdue: {percentage_overdue}%\n")

    print("Task overview has been generated in 'task_overview.txt'.\n")

# This generates the 'user_overview.txt' file with the required information
# when the user enters 'gr' or 'ds' in the menu.
def generate_user_overview():
    total_tasks = len(tasks)
    total_users = len(users_names)
    users_with_tasks = []
    overdue_tasks = compare_users_date()

    with open('user_overview.txt', 'w', encoding='utf-8') as write_user_overview:
        write_user_overview.write(f"The total number of users: {total_users}\n"
            f"The total number of tasks: {total_tasks}\n")

        for user in users_names:
            write_user_overview.write(f"User: {user}\n")
            total_tasks_for_user = []
            total_completed_tasks_for_user = []
            total_uncompleted_tasks_for_user = []

            for task in tasks:
                task = task.split(", ")
                if task[0] == user:
                    total_tasks_for_user.append(task)
                    users_with_tasks.append(user)
                    if task[-1] == "Yes":
                        total_completed_tasks_for_user.append(task)
                    elif task[-1] == "No":
                        total_uncompleted_tasks_for_user.append(task)
                    
            if user in overdue_tasks:
                users_overdue_tasks = overdue_tasks[user]

            percentage_assigned_to_user = round((len(total_tasks_for_user)/total_tasks) * 100, 2)

            if len(total_tasks_for_user) != 0:
                percentage_task_completed = round((len(total_completed_tasks_for_user)/len(total_tasks_for_user)) * 100, 2)
                percentage_task_uncompleted = round((len(total_uncompleted_tasks_for_user)/len(total_tasks_for_user)) * 100, 2)
                percentage_overdue_uncompleted = round((users_overdue_tasks/len(total_tasks_for_user)) * 100, 2)
            elif len(total_tasks_for_user) == 0:
                percentage_task_completed = 0
                percentage_task_uncompleted = 0
                percentage_overdue_uncompleted = 0

            write_user_overview.write("The total number of tasks assigned to "
                f"{user}: {len(total_tasks_for_user)}\nThe percentage of tasks"
                f" assigned to {user}: {percentage_assigned_to_user}%\nThe "
                f"percentage of tasks assigned to {user} that has been completed: "
                f"{percentage_task_completed}%\nThe percentage of tasks assigned"
                f" to {user} that must still be completed: {percentage_task_uncompleted}%\n"
                f"The percentage of tasks assigned to {user} that not yet been"
                f" completed and are overdue: {percentage_overdue_uncompleted}%\n")

    print("Users overview has been generated in 'user_overview.txt'.\n")
       
# This is used when the user selects 'ds' and reads the 'task_overview.txt'
# file and lets the user see the information in a readable format.
def read_task_overview():
    with open('task_overview.txt', 'r', encoding='utf-8') as read_task_overview:
        print("Below find the statistics for all the tasks.")
        for line in read_task_overview:
            line = line.strip("\n")
            line = line.split(": ")
            print(line[0] + ":" + "\t" + line[1])
        print("")

# This is used when the user selects 'ds' and reads the 'user_overview.txt'
# file and lets the user see the information in a readable format.
def read_user_overview():
    with open('user_overview.txt', 'r', encoding='utf-8') as read_user_overview:
        print("Below find the statistics for all the users tasks.")
        check_str = "overdue"
        for line in read_user_overview:
            line = line.strip("\n")
            line = line.split(": ")
            print(line[0] + ":" + "\t" + line[1])
            
            if line[0] == "The total number of tasks":
                print("")

            elif line[0][-7:] == check_str:
                print("")
        print("")

# 'read_tasks' will open and read the contents of 'tasks.txt' and store it in
# 'tasks'
with open('tasks.txt', 'r', encoding='utf-8') as read_tasks:
    for task in read_tasks:
        task = task.strip("\n")
        tasks.append(task)

# 'read_user' will open and read the contents of 'user.txt' storing the
# usernames in 'user_name' and the password in 'user_password' for each user.
with open('user.txt', 'r', encoding='utf-8') as read_user:
    for user in read_user:
        user = user.replace(",", "")
        user = user.strip("\n")
        user = user.split(" ")
        users_names.append(user[0])
        users_password.append(user[1])

# 'logged_in' is used to run the two while loops below.
logged_in = False

# This while loop will run as long as 'logged_in' is set to False and will ask
# the user to log in with correct credentials and once logged in, it will set
# logged_in to True.
while not logged_in:
    print("Please Login with your username and password.")
    username = input("Enter username: ")
    password = input("Enter password: ")

    while username not in users_names:
        username = input("Invalid username entered please try again: ")

    user_index = users_names.index(username)

    print("")

    if (username == users_names[user_index]) and (password ==
        users_password[user_index]):
        logged_in = True
        print("User logged in with correct username and password.\n")

    elif (username == users_names[user_index]) and (password !=
            users_password[user_index]):
        print("User not logged in, Correct username entered with incorrect "
                "password.")

    elif (username not in users_names) and (password in users_password):
        print("User not logged in, Incorrect username entered with correct "
                "password.")

    elif (username not in users_names) and (password not in users_password):
        print("User not logged in, Incorrect username entered with incorrect "
                "password.")

# This while loop runs while the user is logged in.
while logged_in:
    # This block is for checking if the user is logged in as admin and if so
    # the user is given an additional option called 'ds - display statistics',
    # while the user that is not admin does not have that option.
    if username == "admin":
        user_selection = input("Please select one of the following options:\n"
                "r - register user\na - add task\nva - view all tasks\nvm -"
                " view my tasks\ngr - generate reports\nds - display statistics"
                "\ne - exit\nPlease select from the above options: ").lower()

    else:
        user_selection = input("Please select one of the following options:\n"
                "r - register user\na - add task\nva - view all tasks\nvm -"
                " view my tasks\ne - exit\nPlease select from the above "
                "options: ").lower()

    # Blank to create space on print screen.
    print("")

    # If the user selects this option it will call the 'reg_user()' function, 
    # which will return the correct information depending on the outcome of
    # the function.
    if user_selection == "r":
        reg_user(username, users_names)

    # If the user selects 'a' it will call 'add_task()' allowing the user to
    # add a new task.
    elif user_selection == "a":
        add_task()
    
    # This runs if the user has selected 'va' calling the 'view_all()' function
    # letting the user view all the tasks assigned to them.
    elif user_selection == "va":
        view_all()

    # This option runs if 'vm' has been selected which will call the 'view_mine' 
    # function allowing the user to view all the tasks assigned to them and
    # also gives them options depending on the tasks.
    elif user_selection == "vm":
        view_mine()

    # This option is only visible to the admin and allows the admin to generate
    # the 'user_overview.txt' and 'task_overview.txt' files by calling the
    # 'generate_task_overview()' and 'generate_user_overview()' functions.
    elif user_selection == "gr":

        generate_task_overview()
        generate_user_overview()

    # This option is only available if the user is logged in as admin which
    # uses the data stored in 'user_overview.txt' and 'task_overview.txt' to
    # return statistics for all the tasks and user by calling
    # 'read_task_overview()' and 'read_user_overview()' to read the files and
    # give the correct information back to the user.
    # If the files do not exist yet then it first generates them.
    elif user_selection == "ds":
        print("You have selected: Display statistics.\n")
        
        generate_task_overview()
        generate_user_overview()

        read_task_overview()
        read_user_overview()

    # This ends the program if the user has selected 'e'
    elif user_selection == "e":
        print("You have selected: Exit.\n")
        logged_in = False
        print("You have typed 'e' to exit the selections list.")
    
    # This happens if the user has selected an option that is not on the list,
    # telling them to try again.
    else:
        print("Something was entered that isn't on the list, Please try to "
                "enter your selection again.")

# Used this to figure out how to compare two dates:
#https://www.delftstack.com/howto/python/python-compare-dates/#use-the-time-module-to-compare-two-dates-in-python

# Used this link from stackoverflow to convert from month name to month as a number.
#https://stackoverflow.com/questions/3418050/month-name-to-month-number-and-vice-versa-in-python/3418092