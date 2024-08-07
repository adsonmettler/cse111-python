# DICTIONARY example:
######## PROGRAM 1 - Creating a dictionary, adding, and checking items using if statement.
######## PROGRAM 2 - Finding One Item in a dictionary with compound values ###############

def main():
    # Create a dictionary with student IDs as
    # the keys and student names as the values.
    students_dict = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis"
    }
    # Add an item to the dictionary.
    students_dict["81-298-9238"] = "Sama Patel"
    # Remove an item from the dictionary.
    students_dict.pop("61-315-0160")
    # Get the number of items in the dictionary.
    length = len(students_dict)
    print(f"length: {length}")
    # Print the entire dictionary.
    print(students_dict)
    print()
    # Get a student ID from the user.
    id = input("Enter a student ID: ")
    # Check if the student ID is in the dictionary.
    if id in students_dict:
        # Find the student ID in the dictionary and
        # retrieve the corresponding student name.
        name = students_dict[id]
        # Print the student's name.
        print(name)
    else:
        print("No such student")
# Call main to start this program.
if __name__ == "__main__":
    main()


################### Finding One Item ###############

def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
    }
    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3
    # Get a student ID from the user.
    id = input("Enter a student ID: ")
    # Check if the student ID is in the dictionary.
    if id in students_dict:
        # Find the student ID in the dictionary and
        # retrieve the corresponding value, which is a list.
        value = students_dict[id]
        # Retrieve the student's given name (first name) and
        # surname (last name or family name) from the list.
        given_name = value[GIVEN_NAME_INDEX]
        surname = value[SURNAME_INDEX]
        # Print the student's name.
        print(f"{given_name} {surname}")
    else:
        print("No such student")
# Call main to start this program.
if __name__ == "__main__":
    main()