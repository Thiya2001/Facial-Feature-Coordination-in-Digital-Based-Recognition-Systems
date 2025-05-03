import sqlite3

def insertData(data):
    """
    Insert criminal data into the SQLite database.

    Args:
    - data: Dictionary containing criminal data

    Returns:
    - ID of the inserted row
    """
    rowId = 0

    db = sqlite3.connect("criminals.db")  # Connect to SQLite database
    cursor = db.cursor()
    print("Database connected")

    # Ensure the table exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS criminaldata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, father_name TEXT, mother_name TEXT, gender TEXT,
            dob TEXT, blood_group TEXT, identification_mark TEXT,
            nationality TEXT, religion TEXT, crimes_done TEXT
        )
    """)

    query = """INSERT INTO criminaldata (name, father_name, mother_name, gender,
               dob, blood_group, identification_mark, nationality, religion, crimes_done)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    try:
        cursor.execute(query, (data["Name"], data["Father's Name"], data["Mother's Name"], 
                               data["Gender"], data["DOB(yyyy-mm-dd)"], data["Blood Group"], 
                               data["Identification Mark"], data["Nationality"], data["Religion"], 
                               data["Crimes Done"]))
        db.commit()
        rowId = cursor.lastrowid
        print(f"Data stored on row {rowId}")
    except Exception as e:
        db.rollback()
        print(f"Data insertion failed: {e}")

    db.close()
    print("Connection closed")
    return rowId

def retrieveData(name):
    """
    Retrieve criminal data from the SQLite database based on the name.

    Args:
    - name: Name of the criminal

    Returns:
    - Tuple containing ID and criminal data
    """
    id = None
    criminaldata = None

    db = sqlite3.connect("criminals.db")  # Connect to SQLite database
    cursor = db.cursor()
    print("Database connected")

    query = "SELECT * FROM criminaldata WHERE name=?"

    try:
        cursor.execute(query, (name,))
        result = cursor.fetchone()

        if result:
            id = result[0]
            criminaldata = {
                "Name": result[1],
                "Father's Name": result[2],
                "Mother's Name": result[3],
                "Gender": result[4],
                "DOB(yyyy-mm-dd)": result[5],
                "Blood Group": result[6],
                "Identification Mark": result[7],
                "Nationality": result[8],
                "Religion": result[9],
                "Crimes Done": result[10]
            }
            print("Data retrieved")
        else:
            print("No record found")

    except Exception as e:
        print(f"Error: Unable to fetch data: {e}")

    db.close()
    print("Connection closed")

    return id, criminaldata