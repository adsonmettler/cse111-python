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
from datetime import datetime
from finance_control import create_connection, get_columns, create_entry, read_entries, update_entry, delete_entry, generate_report

# Define a fixture to handle database setup and teardown
@pytest.fixture(scope="module")
def db_setup():
    # Connect to test database
    conn = create_connection()
    cursor = conn.cursor()

    # Create a test table
    cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), value INT)")
    conn.commit()
    yield conn  # Provide the fixture value
    
    # Teardown
    cursor.execute("DROP TABLE IF EXISTS test_table")
    conn.commit()
    conn.close()

def test_get_columns(db_setup):
    columns = get_columns('test_table')
    assert 'id' in columns
    assert 'name' in columns
    assert 'value' in columns

def test_create_entry(db_setup):
    create_entry('test_table')
    entries = read_entries('test_table')
    assert len(entries) > 0  # Check that at least one entry was created

def test_update_entry(db_setup):
    create_entry('test_table')
    entries = read_entries('test_table')
    entry_id = entries[0][0]  # Assuming the ID is the first column
    update_entry('test_table', entry_id, {'name': 'Updated Name', 'value': 100})
    updated_entries = read_entries('test_table')
    updated_entry = next(entry for entry in updated_entries if entry[0] == entry_id)
    assert updated_entry[1] == 'Updated Name'
    assert updated_entry[2] == 100

def test_delete_entry(db_setup):
    create_entry('test_table')
    entries = read_entries('test_table')
    entry_id = entries[0][0]  # Assuming the ID is the first column
    delete_entry('test_table', entry_id)
    remaining_entries = read_entries('test_table')
    assert entry_id not in [entry[0] for entry in remaining_entries]

def test_generate_report(db_setup):
    create_entry('test_table')
    query = "SELECT * FROM test_table"
    df = generate_report(query)
    assert not df.empty  # Check that the DataFrame is not empty

if __name__ == "__main__":
    pytest.main()