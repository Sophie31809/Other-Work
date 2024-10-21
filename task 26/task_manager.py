from datetime import date #adding a module to get the current date and time. Found on https://www.geeksforgeeks.org/get-current-date-using-python/
from os.path import exists

#taking username as input and saving to a variable
username = input("Please enter your username:")

#writing all of the usernames and passwords to lists within one big list.
#[0] indexes are username and [1] indexes are the corresponding passwords. 
u = open('user.txt', 'r')
valid_logins = []
for line in u:
    valid_logins.append(line.strip('\n').split(", "))
u.close()

#checking if the username entered is correct, and if it is assigning the correct password to a variable called password
for i in valid_logins:
    if username == i[0]:
        user = True
        password = i[1]
        break
    else:
        user = False

#if the password is incorrect, go into a while loop that asks for a new username until a valid one is entered
while user == False:
    username = input("Please enter a valid username:")
    for i in valid_logins:
        if username in i:
            user = True
            password = i[1]
            break
        
#asking the user for a password now that the correct username has been entered
password_entered = input("Please enter your password:")

#checking if the password is the correct one for the user
if password_entered == password:
    user = True
else:
    user = False

#if the first password is incorrect, enter a while loop that will ask for a new password until the correct one is entered
while user == False:
    password_entered = input("Password incorrect. Please enter your password")
    if password_entered == password:
        user = True
    else:
        user = False
        
#when the while loop is exited, the user has now sucsessfully logged in
print("Welcome.")    

###### defining functions ######

#defining a reg_user function that takes the username as an argument
def reg_user(username):
    
    #checking that the user is admin (only admin can register new users)
    if username == 'admin':
    #taking input for new username, password and password confirmation, and storing them as variables.
        new_user = input("Please enter the new username:")
        f = open('user.txt', 'r')
        #testing that the user does not already exist. If it does, print a message to take new input
        for line in f:
            line = line.split(',')
            while new_user == line[0] and new_user != '0':
                new_user = input("The username already exists. Please enter a new username, or press 0 to exit. ")
        f.close()
        #exit if the user chooses not to enter a new username
        if new_user =='0':
            return
        new_password1 = input("Please enter your new password")
        new_password2 = input("Please confirm new password")
        
    #checking that the password and password confirmation match each other
        if new_password1 == new_password2:
            #if the password matches the password confirmation, user.txt is opened, and the new username and password is added to a new line. user.txt is then closed.
            u = open('user.txt', 'a')
            u.write('\n')
            u.write(new_user + ', ' + new_password1)
            u.close()
        else:
            #print a message if the passwords don't match. 
            print("Sorry, the passwords entered do not match. The new user has not been created. ")
            #if the user is not the admin, they cannot register a new user. 
    else:
        print("Sorry. Only the admin is allowed to create new users")

#defining an add task function
def add_task():
#taking the username, task title, task description, and task duedate as inputs. Fetching the current date.
    list_of_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    task_username = input("Please enter the username of the person that this task is assigned to: ")
    task_title = input("What is the title of this task: ")
    task_description = input("Enter a short description of this task: ")
    task_duedate = input("When is this task due? Please enter the date in the following format: dd 1st 3 letters of the month (1st letter capitalised), yyyy, e.g. 10 Dec 2022")
    currentdate = str(date.today()).split('-')
    current_date_formatted = currentdate[2] + ' ' + list_of_months[int(currentdate[1])-1] + ' ' + currentdate[0]

    #writing it all to the tasks.txt file in the correct format
    f = open('tasks.txt', 'a')
    f.write(f"\n{task_username}, {task_title}, {task_description}, {str(current_date_formatted)}, {task_duedate}, No")
    f.close()

#defining a view_all function

def view_all():
    #open the tasks.txt file
    f = open('tasks.txt')
    for line in f:
        #split the line by commas to seperate each section and strip out new line characters
        line = line.strip('\n').split(', ')
        #print in the nice format, using indexing
        print('\n--------------------------------------------------\n')
        print(f"Task: \t\t\t {line[1]}")
        print(f"Assigned to: \t\t {line[0]}")
        print(f"Date assigned:\t\t {line[3]}")
        print(f"Due Date:\t\t {line[4]}")
        print(f"Task Complete? \t\t {line[5]}")
        print(f"Task Description: \n {line[2]}")
    print('\n--------------------------------------------------\n')
    #close the file
    f.close()


def view_mine(username):
    f = open('tasks.txt', 'r')
    #creating a dictionary to store tasks with their corresponding number
    #also create dictionary to store other users tasks for when we rewrite everything back into the file
    tasks_dict = {}
    tasks_other_users = {}
    tasks_other_users_count = 1
    #creating a tasks count variable
    tasks_count = 1
    for line_full in f:
        line = line_full.strip('\n').split(', ')
        #check for tasks where the assigned user is equal to the username of the user who is logged in
        #print in the nice format
        if line[0] == username:
            #add task number and line into the dictionary
            tasks_dict[tasks_count] = line #line_full.strip('\n')
            print('\n--------------------------------------------------\n')
            print(f"Task number {tasks_count}")
            print(f"Task: \t\t\t {line[1]}")
            print(f"Assigned to: \t\t {line[0]}")
            print(f"Date assigned:\t\t {line[3]}")
            print(f"Due Date:\t\t {line[4]}")
            print(f"Task Complete? \t\t {line[5]}")
            print(f"Task Description: \n {line[2]}")
            tasks_count = tasks_count + 1
        elif line[0] != username:
            tasks_other_users[tasks_other_users_count] = line
            tasks_other_users_count = tasks_other_users_count + 1
    print('\n--------------------------------------------------\n')
    #create varible to store the task selection
    f.close()
    task_selection = int(input("Which task would you like to select? (Enter the task number or enter -1 to exit): "))
    #if -1 entered exit by returning the function
    if task_selection == -1:
        return
    f = open('tasks.txt', 'r+')
    for line_full in f:
        #split line into list by comma
        #ask user about what they would like todo and action it using if statements
        #if user, date or completed status is changed, update in the dictionary
        if tasks_dict[task_selection] == line_full.strip('\n').split(', '):
            task_action = input("Would you like to edit the task (enter 0) or mark the task as complete (enter 1)?")
            if task_action == '0' and tasks_dict[task_selection][5] == 'No':
                change_user = input("Would you like to change the user? y/n ")
                if change_user == 'y':
                    tasks_dict[task_selection][0] = input("Please enter new user: ")
                change_date = input("Would you like to change the due date? y/n ")
                if change_date == 'y':
                    tasks_dict[task_selection][4] = input("Please enter new due date: ")
            elif task_action == '0' and tasks_dict[task_selection][5] == 'Yes':
                print("Only incomplete tasks may be edited. ")
            elif task_action == '1':
                tasks_dict[task_selection][5] = 'Yes'
            

    f.close()
    #open and overwrite nothing into the file to clear it 
    f = open('tasks.txt', 'w')
    f.write('')
    f.close()
    #open the file and all all lines from both dictionaries to rewrite both the updated and the unchanged tasks to the file
    f = open('tasks.txt', 'a')
    for i in range(1, tasks_count):
        f.write(', '.join(tasks_dict[i]) + '\n')
    for i in range(1, tasks_other_users_count):
        f.write(', '.join(tasks_other_users[i]) + '\n')
    f.close()

def generate_reports():
    #define list of months
    list_of_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    t_o = open('task_overview.txt', 'w')

    t = open('tasks.txt', 'r')
    #define count variables for tasks, completed, incompleted and overdue
    total_tasks = 0
    completed = 0
    incomplete = 0
    overdue = 0

    #iterate through the lines
    for line in t:
        line = line.strip('\n').split(', ')
        date_due = line[4].split(' ')
        #create variables for day, month and year for the current and due date. 
        due_day = int(date_due[0])
        due_month = list_of_months.index(date_due[1]) + 1
        due_year = int(date_due[2])
                    
        currentdate = str(date.today()).split('-') #yyyy-mm-dd
        current_day = int(currentdate[2])
        current_month = int(currentdate[1])
        current_year = int(currentdate[0])

        #add to completed and incompleted task count based on what is written in the file
        total_tasks = total_tasks + 1
        if line[5] == 'Yes':
            completed = completed + 1
        elif line[5] == 'No':
            incomplete = incomplete + 1
            #if the task is incomplete, check if the due date is before the current date, and if so, add to the overdue count
            if due_year < current_year:
                overdue = overdue + 1
            elif due_year == current_year and due_month < current_month:
                overdue = overdue + 1
            elif due_year == current_year and due_month == current_month and due_day < current_day:
                overdue = overdue + 1
    t.close()
    #write the results into the file
    t_o.write(f"""There have been {total_tasks} tasks generated.
There are currently {completed} completed tasks and {incomplete} incomplete tasks.
There are currently {overdue} overdue tasks.
        
{100*(incomplete/total_tasks)}% of tasks are incomplete and {100*(overdue/total_tasks)}% of all tasks are overdue.""")      
    t_o.close()
        
    u_o = open('user_overview.txt', 'w')
    u = open('user.txt', 'r')
    #create user count variable and dictionaries for all user tasks, completed tasks for each user, and overdue tasks for each user
    users_count = 0
    user_task_dict = {}
    user_completed_tasks_dict = {}
    user_overdue_dict = {}

    #add to user count and for each user set the completed tasks and oversue tasks count to 0
    for line_u in u:
        users_count = users_count + 1
        line_u = line_u.split(', ')
        user_to_check = line_u[0]
        user_to_check_count = 0
        user_completed_tasks_count = 0
        overdue = 0

        #set values for current day, month and year
        currentdate = str(date.today()).split('-')
        current_day = int(currentdate[2])
        current_month = int(currentdate[1])
        current_year = int(currentdate[0])
                
        t = open('tasks.txt', 'r')

        #iterate through the task file and count all tasks, completed tasks, and overdue tasks for each user.  
        for line_t in t:
            line_t = line_t.strip('\n').split(', ')
            if user_to_check == line_t[0]:
                user_to_check_count = user_to_check_count + 1
                if line_t[5] == 'Yes':
                    user_completed_tasks_count = user_completed_tasks_count + 1
                elif line_t[5] == 'No':
                    date_due = line_t[4].split(' ')
                    due_day = int(date_due[0])
                    due_month = list_of_months.index(date_due[1]) + 1
                    due_year = int(date_due[2])
                        
                    if due_year < current_year:
                        overdue = overdue + 1
                    elif due_year == current_year and due_month < current_month:
                        overdue = overdue + 1
                    elif due_year == current_year and due_month == current_month and due_day < current_day:
                        overdue = overdue + 1
                       
        #add the count values for each count variable to the dictionaries as the value, with the user as the key          
        if user_completed_tasks_count > 0:            
            user_completed_tasks_dict[user_to_check] = user_completed_tasks_count
        user_task_dict[user_to_check] = user_to_check_count
        user_overdue_dict[user_to_check] = overdue
        t.close()
    users_tasks_str = ''
    #add the values into a string so that it can be written to the file in a readable way
    #the if and elif statements are to avoid zero devision - if a user has no tasks, you cannot calculate the percentage that are completed for example
    for key in user_task_dict:
        users_tasks_str = users_tasks_str + key + ': ' + str(user_task_dict[key]) + ' tasks, ' + str(100*(user_task_dict[key]/total_tasks))+ '% of all tasks \n'
        if key in user_completed_tasks_dict:
            users_tasks_str = users_tasks_str + '\t'+str(100*(user_completed_tasks_dict[key]/user_task_dict[key]))+'% are completed, '+ str(100 - (100*(user_completed_tasks_dict[key]/user_task_dict[key])))+ '% of tasks are incomplete, and  \n'            
        elif user_task_dict[key] != 0:
            users_tasks_str = users_tasks_str + '\t 0% of tasks are completed, and 100% of tasks are incomplete \n'
        if user_task_dict[key] != 0 :
            users_tasks_str = users_tasks_str + '\t'+str(100*(user_overdue_dict[key]/user_task_dict[key])) + '% of all assigned tasks are overdue. \n'
            
    #write results to file   
    u_o.write(f"""There are {users_count} registered users.
There have been {total_tasks} tasks generated.
The following shows the number of tasks shown to each user:
{users_tasks_str}""")
        
    u_o.close()
    u.close()

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if username == 'admin':
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    gr - generate reports
    s - view statistics
    e - Exit
    : ''').lower()
    else:
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()
        

    if menu == 'r':
                
        reg_user(username)


    elif menu == 'a':
        
        add_task()


    elif menu == 'va':
        
        view_all()

    elif menu == 'vm':

        view_mine(username)

    elif menu == 's' and username == 'admin':
        #only the admin can select statistics
        
        #open the user.txt file and count the number of lines. Assign it to a variable
        user_file = open('user.txt', 'r')
        number_of_users = 0
        for line in user_file:
            number_of_users = number_of_users + 1
        user_file.close()

        #do the same for the tasks file
        tasks_file = open('tasks.txt', 'r')
        number_of_tasks = 0
        for line in tasks_file:
            number_of_tasks = number_of_tasks + 1
        tasks_file.close()

        #print in a user friendly format
        print(f"There are {number_of_users} users, and {number_of_tasks} tasks")

        #getting info from task_overview and user_overview
        files_exist = exists('task_overview.txt') #assume that if one exists or doesn't exist they both do or don't exist
        if files_exist == False:
            #call the generate reports function if the files don't exist
            generate_reports()

        #print the contents of the overview files. As they are already written in a readable, user friendly way, printing by line is fine.
        t_o = open('task_overview.txt', 'r')
        u_o = open('user_overview.txt', 'r')

        for line in t_o:
            print(line)
        for line in u_o:
            print(line)

        t_o.close()
        u_o.close()
        
        

    elif menu == 'gr' and username == 'admin':

        #run generate reports function
        generate_reports()
        

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
