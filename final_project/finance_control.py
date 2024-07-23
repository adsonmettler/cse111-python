
"""
Author: Adson Mettler do Nascimento

#########  CSE 111 Proposal for a Student Chosen Program ########

######### Finance Control Application ##########

# This is a personal project intended to contribute to a real-world project
# that my friends invited me to join last week. The real customer needs a
# finance control system that can function as a database with CRUD (Create,
# Read, Update, Delete) operations. With this database, the customer can
# perform queries to generate reports.

# In this project I beleive that I will use the following modules: csv,
# math, pandas, pytest, mysql.connector

##### Program Functions to develop:

# create_connection() # function to connect Python to MySQL server
# creat_entry(date, description, category, value)
# read_entries()
# update_entry(entry_id, date, description, category, value)
# delete_entry(entry_id)
# generate_report(query)

###### Test functions you will write.
# test_creat_entry(date, description, category, value)
# test_read_entries()
# test_update_entry(entry_id, date, description, category, value)
# test_delete_entry(entry_id)
# test_generate_report(query)
"""

import mysql.connector
import pandas as pd
from datetime import datetime



def main():

    ######### Before running the CRUD functions the program will create a database in my localhost
    # to simulate a database to perform entries, reading, updates, and delete operations.

    # Connect to MySQL server
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="narf1987"
    )

    cursor = conn.cursor()

    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS finance_db")

    # Connect to the new database
    conn.database = 'finance_db'

    # Create finance table
    cursor.execute('''CREATE TABLE IF NOT EXISTS finance (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        date DATE,
                        description VARCHAR(255),
                        category VARCHAR(255),
                        amount DECIMAL(10, 2)
                    )''')

    # Create budget table
    cursor.execute('''CREATE TABLE IF NOT EXISTS budget (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        month VARCHAR(255),
                        category VARCHAR(255),
                        amount DECIMAL(10, 2)
                    )''')

    conn.commit()
    conn.close()



    while True:
        print()
        print("1. Add entry")
        print("2. View entries")
        print("3. Update entry")
        print("4. Delete entry")
        print("5. Generate report")
        print("6. Exit")
        choice = input("Choose an option: ")
        print()

        if choice in ['1', '3', '4']:
            table = input("Enter table name (type finance or budget): ").lower()
        
        if choice == '1':
            create_entry(table)
        elif choice == '2':
            table = input("Enter table name (type finance or budget): ").lower()
            entries = read_entries(table)
            for entry in entries:
                print(entry)
        elif choice == '3':
            entry_id = int(input("Enter entry ID to update: "))
            columns = input("Enter columns to update (comma separated): ").split(',')
            values = [input(f"Enter new {column}: ") for column in columns]
            data = dict(zip(columns, values))
            update_entry(table, entry_id, data)
        elif choice == '4':
            entry_id = int(input("Enter entry ID to delete: "))
            delete_entry(table, entry_id)
        elif choice == '5':
            query = input("Enter SQL query for report (ex: SELECT * FROM finance): ")
            report = generate_report(query)
            print(report)
            print()
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")



##### Program Functions to develop:


# function to connect Python to MySQL server
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="narf1987",
        database="finance_db"
    )

def get_columns(table):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"DESCRIBE {table}")
    columns = [row[0] for row in cursor.fetchall()]
    conn.close()
    return columns

# function to enter new data to database finance_db
def create_entry(table):
    columns = get_columns(table)
    data = {}
    
    # Automatically add current date to the data dictionary for 'finance' table if date column exists
    if table == 'finance' and 'date' in columns:
        data['date'] = datetime.now().date()
    
    print(f"Enter data for table '{table}':")
    for column in columns:
        if column == 'id':  # Skip ID if it's auto-incremented
            continue
        if column == 'date':  # Skip date input if it's auto-filled
            continue
        value = input(f"Enter {column}: ")
        data[column] = value
    
    # To Build SQL statement to insert data into table
    conn = create_connection()
    cursor = conn.cursor()
    placeholders = ', '.join(['%s'] * len(data))
    columns_str = ', '.join(data.keys())
    sql = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
    cursor.execute(sql, list(data.values()))
    conn.commit()
    conn.close()

# function to read data from database finance_db.
def read_entries(table):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    rows = cursor.fetchall()
    conn.close()
    return rows
# function to update date from database finance_db.
def update_entry(table, entry_id, data):
    conn = create_connection()
    cursor = conn.cursor()
    placeholders = ', '.join([f"{key} = %s" for key in data.keys()])
    sql = f"UPDATE {table} SET {placeholders} WHERE id = %s"
    cursor.execute(sql, list(data.values()) + [entry_id])
    conn.commit()
    conn.close()
# function to delete specific data in an specific table from database finance_db.
def delete_entry(table, entry_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {table} WHERE id = %s', (entry_id,))
    conn.commit()
    conn.close()

import pandas as pd
# function to generate report from database finance_db.
def generate_report(query):
    conn = create_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df




if __name__ == "__main__":
    main()