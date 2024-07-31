import sqlite3
from MPYdata import *


def test_MPYdata():
    # Initialize the MPYdata class
    db = MPYdata()
    
    # Test connect
    db.connect('test1.db')
    print("Connected to database.")
    
    # Test create_table
    db.create_table('test_table', 'id INTEGER PRIMARY KEY, name TEXT, age INTEGER')
    print("Table created.")
    
    # Test insert
    db.insert('test_table', '1, John, 30')
    db.insert('test_table', '2, Jane, 25')
    print("Data inserted.")
    
    # Test getall
    results = db.getall('test_table')
    print("All data:", results)
    
    # Test select
    selected = db.select('test_table', 'age > 25')
    print("Selected data:", selected)
    
    # Test update
    db.update('test_table', 'age', 35, 'id', 1)
    updated = db.select('test_table', 'id = 1')
    print("Updated data:", updated)
    
    # Test create_column
    db.create_column('test_table', 'email', 'TEXT')
    db.update('test_table', 'email', 'john@example.com', 'id', 1)
    db.update('test_table', 'email', 'jane@example.com', 'id', 2)
    print("Column created and updated.")
    
    # Test rename_column
    db.rename_column('test_table', 'email', 'contact_email')
    renamed_columns = db.getall('test_table')
    print("Renamed column data:", renamed_columns)
    
    # Test rename_table
    db.rename_table('test_table', 'renamed_table')
    renamed_table_data = db.getall('renamed_table')
    print("Renamed table data:", renamed_table_data)
    
    # Test delete
    db.delete('renamed_table', 'id = 2')
    remaining_data = db.getall('renamed_table')
    print("Remaining data after delete:", remaining_data)
    
    # Test delete_table
    db.delete_table('renamed_table')
    try:
        db.getall('renamed_table')
    except sqlite3.OperationalError as e:
        print("Table deleted, error encountered:", e)
    
    # Test setpassword and getpassword
    try:
        db.setpassword('newpassword')
        password_info = db.getpassword()
        print("Password set, password info:", password_info)
    except sqlite3.OperationalError as e:
        print("Password functions are not supported in SQLite. Error encountered:", e)
    
    # Test rollback
    db.create_table('rollback_test', 'id INTEGER PRIMARY KEY, name TEXT')
    db.insert('rollback_test', '1, RollbackTest')
    db.rollback()
    try:
        rollback_data = db.getall('rollback_test')
    except sqlite3.OperationalError as e:
        rollback_data = f"Table not found. Error encountered: {e}"
    print("Data after rollback:", rollback_data)
    
    # Test commit
    db.create_table('commit_test', 'id INTEGER PRIMARY KEY, name TEXT')
    db.insert('commit_test', '1, CommitTest')
    db.commit()
    commit_data = db.getall('commit_test')
    print("Data after commit:", commit_data)
    
    # Test disconnect
    db.disconnect()
    try:
        db.getall('commit_test')
    except ConnectionError as e:
        print("Disconnected, error encountered:", e)
    
    # Clean up
    import os
    os.remove('test1.db')
    print("Cleaned up test database.")

# Run the test
test_MPYdata()
