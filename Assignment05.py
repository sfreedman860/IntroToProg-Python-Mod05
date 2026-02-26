# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Steve Freedman, 2/20/2026, Created script
#
# ------------------------------------------------------------------------------------------ #

# Import the json and _io modules
import json


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
#FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
#student_data: list = []  # one row of student data (Change this to a Dictionary)
student_data: dict = {}
students: list = []  # a table of student data
#csv_data: str = ''  # Holds combined CSV data. Note: Remove later since it is NOT needed with the JSON File
file = None  # Holds a reference to an opened file. (Change this to use _io.TextIOWrapper instead of None)
menu_choice: str  # Hold the choice made by the user.

try:
# "When the program starts, the contents of the "Enrollments.json" are automatically read into the students
# two-dimensional list of dictionary rows using the json.load() function."
# Extract the data from the file
    file = open(FILE_NAME, "r")

    students = json.load(file)

except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file is not None and file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")
    # "On menu choice 1, the program prompts the user to enter the student's first name and last name,
    # followed by the course name, using the input() function and stores the inputs in the respective variables."
    # "Data collected for menu choice 1 is added to a dictionary named student_data. Next,
    # student_data is added to the students two-dimensional list of dictionaries rows."

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            # Check that the input does not include numbers
            student_first_name = input("Enter the student's first name: ")
            if student_first_name.isnumeric():# Is there a difference between doing this vs doing "if not ***.isalpha()?
                raise ValueError("The first name should not contain numbers.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        try:
            # Check that the input does not include numbers
            student_last_name = input("Enter the student's last name: ")
            if student_last_name.isnumeric(): # Is there a difference between doing this vs doing "if not ***.isalpha()?
                raise ValueError("The last name should not contain numbers.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')

        # Don't really need a try here
        course_name = input("Please enter the name of the course: ")

        student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "CourseName": course_name}
        # Load it into our collection (list of lists)
        students.append(student_data)
        #print(students) #for troubleshooting
        continue

    # Present the current data
    # "On menu choice 2, the presents a string by formatting the collected data using the print() function."
    # "On menu choice 2, the program uses the print() function to show a string of comma-separated values
    # for each row collected in the students variable"

    elif menu_choice == "2":

        # Process the data to create and display a custom message

        print("-"*50)
        print(students) #this doesn't produce a clean print, but its accurate
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            #for student in students:
            json.dump(students, file)

        except FileNotFoundError as e:
            print("Text file must exist before running this script!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file is not None and file.closed == False:
                file.close()

        print("The following data was saved to file!")
        #for student in students:
        #    print(f"Student {students[0]} {students[1]} is enrolled in {students[2]}")
        #students.append(student_data)
        print(students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        print("Program Ended")
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, 3, or 4") 



