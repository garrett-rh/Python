#!/usr/bin/python3

import sqlite3
    
try:
    print("""Where would you like the table to be created? Please ensure that the specified path is already created.
For example, If I want to store it at /home/user/.agenda/agenda.db make sure that /home/user/.agenda exists.""")
    db_location = str(input("Enter agenda.db location: "))
    if db_location[-9:] != "agenda.db":
        db_location = db_location + "/agenda.db"
    print(f"The agenda will be stored at this location: {db_location}")
    yes_no = str(input("Is that correct?"))
    if 'y' in yes_no.lower():
        conn = sqlite3.connect(db_location)
        c = conn.cursor()
        c.execute("""CREATE TABLE agenda(
                ID integer,
                date text,
                class text,
                assignment text,
                status text
                )"""
                )
    else:
        print("Please rerun setup.py")
finally:
    print("An error occurred. Please rerun setup.py")
