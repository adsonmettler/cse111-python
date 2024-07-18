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


def main():
    while True:
        print("1. Add entry")
        print("2. View entries")
        print("3. Update entry")
        print("4. Delete entry")
        print("5. Generate report")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice in ['1', '3', '4']:
            table = input("Enter table name: ")
        
        if choice == '1':
            columns = input("Enter columns (comma separated): ").split(',')
            values = [input(f"Enter {column}: ") for column in columns]
            data = dict(zip(columns, values))
            create_entry(table, data)
        elif choice == '2':
            table = input("Enter table name: ")
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
            query = input("Enter SQL query for report: ")
            report = generate_report(query)
            print(report)
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
# function to enter new data
def create_entry(table, data):
    conn = create_connection()
    cursor = conn.cursor()
    placeholders = ', '.join(['%s'] * len(data))
    columns = ', '.join(data.keys())
    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    cursor.execute(sql, list(data.values()))
    conn.commit()
    conn.close()
# function to read data
def read_entries(table):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    rows = cursor.fetchall()
    conn.close()
    return rows
# function to update date
def update_entry(table, entry_id, data):
    conn = create_connection()
    cursor = conn.cursor()
    placeholders = ', '.join([f"{key} = %s" for key in data.keys()])
    sql = f"UPDATE {table} SET {placeholders} WHERE id = %s"
    cursor.execute(sql, list(data.values()) + [entry_id])
    conn.commit()
    conn.close()
# function to delete specific data in an specific table from database
def delete_entry(table, entry_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {table} WHERE id = %s', (entry_id,))
    conn.commit()
    conn.close()

import pandas as pd
# function to generate report
def generate_report(query):
    conn = create_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df




if __name__ == "__main__":
    main()