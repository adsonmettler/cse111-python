

import csv

ID_NUMBER = 0
NAME = 1

def main():

    students_dic = read_dictionary("students.csv", ID_NUMBER)
    print(students_dic)

    user_query = input("Enter the I-Number you want to search: ")

    if user_query in students_dic:
        value = students_dic[user_query]
        name = value[NAME]
        print(f"The student name is {name}")
    else:
        print("No such student")



def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary

# Call main to start this program.
if __name__ == "__main__":
    main()
