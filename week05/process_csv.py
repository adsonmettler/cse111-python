
#### Process CSV file #####

# Author: Adson Mettler do Nascimento
# This is an example for me to note and remember whenever I need it.

import csv

COMPANY_NAME_INDEX = 0
ADDRESS_INDEX = 1
PHONE_NUMBER_INDEX = 2
EMPLOYEES_INDEX = 3
PATIENTS_INDEX = 4

def main():
    with open("dentists.csv", "rt") as dentists_file:
        reader = csv.reader(dentists_file)

        next(reader)
        running_max = 0
        most_office = None

        for row_list in reader:
            company = row_list[COMPANY_NAME_INDEX]
            num_employees = int(row_list[EMPLOYEES_INDEX])
            num_patients = int(row_list[PATIENTS_INDEX])

            patients_per_employees = num_patients / num_employees

            if patients_per_employees > running_max:
                running_max = patients_per_employees
                most_office = company

    print(f"{most_office} has {running_max:.1f}"
          " patients per employee.")

if __name__ == "__main__":
    main()



