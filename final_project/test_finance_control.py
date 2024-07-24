"""
Author: Adson Mettler do Nascimento

#########  CSE 111 Proposal for a Student Chosen Program ########

######### Test Finance Control Application ##########

###### Test functions you will write.
# test_creat_entry(date, description, category, value)
# test_read_entries()
# test_update_entry(entry_id, date, description, category, value)
# test_delete_entry(entry_id)
# test_generate_report(query)
"""

import pytest
import mysql.connector
import pandas as pd
from finance_control import create_entry, read_entries, update_entry, delete_entry, generate_report, get_columns

@pytest.fixture(scope='module')
def db_connection():
    """Setup a test database and provide a connection."""
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="narf1987"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS test_finance_db")
    conn.database = 'test_finance_db'
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS finance (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        date DATE,
                        description VARCHAR(255),
                        category VARCHAR(255),
                        amount DECIMAL(10, 2)
                    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS budget (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        month VARCHAR(255),
                        category VARCHAR(255),
                        amount DECIMAL(10, 2)
                    )''')
    
    yield conn  # This provides the connection to the tests

    cursor.execute("DROP DATABASE test_finance_db")
    conn.close()

def test_create_entry(db_connection):
    create_entry('finance')
    entries = read_entries('finance')
    assert len(entries) == 1

def test_read_entries(db_connection):
    create_entry('finance')
    entries = read_entries('finance')
    assert len(entries) == 1
    assert 'description' in entries[0]

def test_update_entry(db_connection):
    create_entry('finance')
    entries = read_entries('finance')
    entry_id = entries[0][0]
    update_entry('finance', entry_id, {'description': 'Updated Description', 'category': 'Updated Category', 'amount': 123.45})
    updated_entries = read_entries('finance')
    assert updated_entries[0][2] == 'Updated Description'
    assert updated_entries[0][3] == 'Updated Category'
    assert updated_entries[0][4] == 123.45

def test_delete_entry(db_connection):
    create_entry('finance')
    entries = read_entries('finance')
    entry_id = entries[0][0]
    delete_entry('finance', entry_id)
    entries_after_delete = read_entries('finance')
    assert len(entries_after_delete) == 0

def test_generate_report(db_connection):
    create_entry('finance')
    query = 'SELECT * FROM finance'
    report = generate_report(query)
    assert isinstance(report, pd.DataFrame)
    assert len(report) == 1

def test_get_columns(db_connection):
    columns = get_columns('finance')
    assert 'description' in columns
    assert 'category' in columns
    assert 'amount' in columns


if __name__ == "__main__":
    pytest.main()