    # Sample code.py
    from MPYdata import MPYdata
    
    # Create an instance of the MPYdata class
    db = MPYdata()


    # Connect to the database
    print("Connecting to database...")
    db.connect('data.db')
    print("Connected successfully.")
    
    # Create a table
    print("Creating table...")
    db.create_table('test_table', 'id INTEGER PRIMARY KEY, name TEXT, age INTEGER')
    print("Table created successfully.")
    
    # Insert data into the table
    print("Inserting data...")
    db.insert('test_table', '1, John Doe, 30')
    db.insert('test_table', '2, Jane Doe, 25')
    print("Data inserted successfully.")
    
    # Retrieve and print all data from the table
    print("Retrieving data...")
    all_data = db.getall('test_table')
    print("All data in test_table:")
    for row in all_data:
        print(row)
    
    # Disconnect from the database
    print("Disconnecting from database...")
    db.disconnect()
    print("Disconnected successfully.")

