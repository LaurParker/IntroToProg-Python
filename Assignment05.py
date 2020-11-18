# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Lauren Parker,11.13.20,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFileName = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = ""
strPriority = ""

# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(objFileName, "w")
objFile.close()

objFile = open(objFileName, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priorities": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if not lstTable:
            print("You have no tasks!")  # Prints if user has not entered any data
        else:
            for objRow in lstTable:
                print(objRow)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        #Get User Input
        strTask = str(input("Please enter a task: "))
        strPriority = str(input("Please enter the priority level [low, med, high]: "))
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        for objRow in lstTable:
            print(objRow)
        delTask = input("What task would you like to delete? ")
        delTask = delTask
        for row in lstTable:
            if delTask == row["Task"]:
                lstTable.remove(row)
                print("Your task has been deleted!")
            else:
                if delTask not in lstTable:
                    print("Sorry, I can't do that! That task is not in your To Do List.")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(objFileName, "w")
        for row in lstTable:
            objFile.write(row["Task"].lower() + "," + row["Priority"].lower() + "\n")
        objFile.close()
        print("Your data has been saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Thank you, goodbye!")
        break  # and Exit the program

