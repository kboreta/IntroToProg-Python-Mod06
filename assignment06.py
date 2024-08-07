# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using classes, functions, and structured error handling
# Change Log: (Who, When, What)
#   KBoreta,08/07/24,Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = ''' 
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
menu_choice: str = ''
students: list = []


class FileProcessor:
    """Processes data to and from a file"""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a file into a list of dictionary rows"""
        try:
            with open(file_name, "r") as file:
                student_data.clear()
                student_data.extend(json.load(file))
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with reading the file.", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes data from a list of dictionary rows to a file"""
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
            IO.output_student_courses(student_data)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with writing to the file.", e)


class IO:
    """Performs Input and Output operations"""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Outputs error messages to the user"""
        print(message)
        if error:
            print("-- Technical Error Message -- ")
            print(error.__doc__)
            print(error.__str__())

    @staticmethod
    def output_menu(menu: str):
        """Displays the menu to the user"""
        print(menu)

    @staticmethod
    def input_menu_choice():
        """Gets the user's menu choice"""
        return input("What would you like to do: ").strip()

    @staticmethod
    def output_student_courses(student_data: list):
        """Displays the student data"""
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """Gets student data from the user and adds it to the list"""
        try:
            first_name = input("Enter the student's first name: ").strip()
            if not first_name.isalpha():
                raise ValueError("The first name should not contain numbers or be empty.")

            last_name = input("Enter the student's last name: ").strip()
            if not last_name.isalpha():
                raise ValueError("The last name should not contain numbers or be empty.")

            course_name = input("Please enter the name of the course: ").strip()
            if not course_name:
                raise ValueError("The course name should not be empty.")

            student_data.append({
                "FirstName": first_name,
                "LastName": last_name,
                "CourseName": course_name
            })
            print(f"You have registered {first_name} {last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("Invalid input.", e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.", e)


# When the program starts, read the file data into a list of dictionary rows
FileProcessor.read_data_from_file(FILE_NAME, students)

# Present and Process the data
while True:
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(students)

    elif menu_choice == "2":
        IO.output_student_courses(students)

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)

    elif menu_choice == "4":
        break

    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
