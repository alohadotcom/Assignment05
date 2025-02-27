#Assigment Header
# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Rich Sialana,26 Feb 2025, Program Completed
# ------------------------------------------------------------------------------------------ #

#My Data Constant
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
#My Data Constant
FILE_NAME: str = 'Enrollments.json'

import json

#My variables and constant
student_first_name: str = '' # Holds the first name of a student entered by the user
student_last_name: str = '' # Holds the last name of a student entered by the user
course_name: str = '' # Holds the name of a course entered by the user
student_data: list = [] # one row of student data (TODO: Change this to a Dictionary)
students: list = [] # a table of student data
#csv.data: str = '' # Holds combined CSV data. Note: Remove later since it is NOT needed with the JSON File
json_data: str = '' # Holds combined string data in a json format
menu_choice: str #Hold the choice made by the user

#When the program starts, read the file data into a list of lists (table)
#Extract the data from the file
try:
    file = open(FILE_NAME, 'r') #read from file
    students = json.load(file) #JSON file
    file.close()
except FileNotFoundError as e: #e generate exception object
    print('Error: File not found.  Please check file location')
    print('--- Technical Error Message ---') #Error message for developer
    #print(e) # Print the exception object (typically includes the error message)
    #print(type(e)) # Print the type of exception object
    print(e.__doc__) # Print the documentation string of the exception type
    print(e.__str__()) # Print the string representation of exception

#Present and Process the data
while (True):
    #Present the menu of choice
    print(MENU)
    menu_choice = input('What would you like to do: ')

    #Input user data
    if menu_choice =='1': #This will not work if it is an integer!
        while True:
            try:
                student_first_name = input('Enter the student\'s first name: ')
                if not student_first_name.isalpha(): #isalpha returns True only \n
                #if all the characters in the input string are alha
                    raise ValueError('Error: Student name should be only letters')

            except ValueError as e:
                print(e) # Print the exception object (typically includes the error message)
                print('--- Technical Error Message ---')
                print(e.__doc__) # Print the documentation string of the exception type
                print(e.__str__()) # Print the string representation of exception

            except Exception as e:
                print('Error: Issue with the data you entered')
                print('--- Technical Error Message ---')
                print(e.__doc__)  # Print the documentation string of the exception type
                print(e.__str__())  # Print the string representation of exception

            else:
                break

        while True:
            try:
                student_last_name = input('Enter the student\'s last name: ')
                if not student_last_name.isalpha():
                    raise ValueError ('Error: Student name should be only letters')

            except ValueError as e:
                print(e) #Print the exception object (typically includes the error message)
                print('--- Technical Error Message ---')
                print(e.__doc__)  # Print the documentation string of the exception type
                print(e.__str__())  # Print the string representation of exception

            except Exception as e:
                print('Error: Issue with the data you entered')
                print('--- Technical Error Message ---')
                print(e.__doc__)  # Print the documentation string of the exception type
                print(e.__str__())  # Print the string representation of exception

            else:
                break
        course_name = input('Please enter the name of course: ')
        student_data = {'FirstName': student_first_name, 'LastName': student_last_name,\
                        'CourseName': course_name}
        students.append(student_data)
        print(f'You have registered {student_first_name} {student_last_name} for {course_name}.')
        for row in students:
            print(row)
        continue

    #Present the current data
    elif menu_choice == '2':

        #Present the current data
        for student in students:
            print(f'Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}')

            print('-'*50)
            continue

    #Save the data to a file
    elif menu_choice == '3':
        try:
            file = open(FILE_NAME, 'w')
            json.dump(students, file)
            file.close()
            print('The following data was saved to file!')
            for students in students:
                print(f'Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}')
                      #{student['CourseName']}')
            continue

        except Exception as e:
            if file.closed == False:
                file.close()
            print('Error: Not able to write your file')
            print('--- Technical Error Message ---')
            print(e.__doc__)
            print(e.__str__())

    #Stop the loop
    elif menu_choice == '4':
        break #out of the loop
    else:
        print('Please only choose option 1, 2, 3, or 4')

print('Program Ended. Good Bye')










