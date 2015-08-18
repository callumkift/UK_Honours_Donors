#!/usr/bin/env python
"""
Contains methods that deal with making and calling the database.
"""

import sqlite3
import os


def createdb():
    """
    Creates database and tables if the database does not exist. Creates it in the containing directory as a
    hidden file
    :return:
    """
    dbname = ".hondonDB.sqlite"

    if os.path.exists(dbname):
        print "check -- db exists"
        return
    else:

        conn = connect()
        c = conn.cursor()

        # Honour List Tables
        c.execute("CREATE TABLE HonourType(id INTEGER PRIMARY KEY, h_order TEXT, award TEXT, level TEXT)")

        c.execute('''CREATE TABLE HonourList(id INTEGER PRIMARY KEY, list TEXT, year TEXT)''')

        c.execute('''CREATE TABLE HonourPerson(id INTEGER PRIMARY KEY, name TEXT, citation TEXT, county TEXT,
                        hl_id INTEGER, ht_id INTEGER, FOREIGN KEY(hl_id) REFERENCES HonourList(id),
                        FOREIGN KEY(ht_id) REFERENCES HonourType(id))''')

        # Donations Tables

        c.execute("CREATE TABLE DonorEntity(id INTEGER PRIMARY KEY, name TEXT, type TEXT)")

        c.execute("CREATE TABLE DonorMaker(id INTEGER PRIMARY KEY, name TEXT, status TEXT)")

        c.execute(''' CREATE TABLE DonorDetails(id INTEGER PRIMARY KEY, type TEXT, date TEXT, value REAL,
                        dm_id INTEGER, de_id INTEGER, FOREIGN KEY(dm_id) REFERENCES DonorMaker(id),
                        FOREIGN KEY(de_id) REFERENCES DonorEntity(id))''')

        conn.commit()
        conn.close()

        print "check -- db and tables created"

        return


def connect():
    """
    Connects to database
    :return: connection to sqlite database
    """
    dbname = ".hondonDB.sqlite"

    return sqlite3.connect(dbname)
