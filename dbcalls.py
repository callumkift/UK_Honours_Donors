#!/usr/bin/env python
"""
Contains methods that deal with making and calling the database.
"""

import sqlite3
import os
import re


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
        c.execute('''CREATE TABLE HonourType(id INTEGER PRIMARY KEY, h_order TEXT, award TEXT, level TEXT,
                        UNIQUE(h_order, award, level))''')

        c.execute('''CREATE TABLE HonourList(id INTEGER PRIMARY KEY, list TEXT, year TEXT,
                        UNIQUE(list, year))''')

        c.execute('''CREATE TABLE HonourPerson(id INTEGER PRIMARY KEY, name TEXT, citation TEXT, county TEXT,
                        hl_id INTEGER, ht_id INTEGER, FOREIGN KEY(hl_id) REFERENCES HonourList(id),
                        FOREIGN KEY(ht_id) REFERENCES HonourType(id), UNIQUE(name, citation, hl_id, ht_id))''')

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


def addhon(hondict):
    """
    Adds honours information to the corresponding tables.
    :param hondict: Dictionary of honours information
    :return:
    """

    name = hondict.values()[0]
    level = hondict.values()[1]
    citation = hondict.values()[2]
    list = hondict.values()[3]
    award = hondict.values()[4]
    county = hondict.values()[5]
    year = hondict.values()[6]
    order = hondict.values()[7]

    conn = connect()
    c = conn.cursor()

    for i in range(len(name)):

        # Fixes lettering problems
        cite = citation[i].decode("utf-8")
        person = name[i].decode("utf-8")

        # HonourType table
        try:
            c.execute("INSERT INTO HonourType(h_order, award, level) VALUES(?,?,?)", (order[i], award[i], level[i],))
            conn.commit()
            c.execute("SELECT MAX(id) FROM HonourType")
            ht_id = c.fetchall()[0][0]
        except sqlite3.IntegrityError:
            c.execute('''SELECT id FROM HonourType
                        WHERE h_order=? AND award=? AND level=?''', (order[i], award[i], level[i],))
            ht_id = c.fetchall()[0][0]

        # HonourList table
        try:
            c.execute("INSERT INTO HonourList(list, year) VALUES(?,?)", (list[i], year[i],))
            conn.commit()
            c.execute("SELECT MAX(id) FROM HonourType")
            hl_id = c.fetchall()[0][0]
        except sqlite3.IntegrityError:
            c.execute('''SELECT id FROM HonourList
                        WHERE list=? AND year=?''', (list[i], year[i],))
            hl_id = c.fetchall()[0][0]

        # HonourPerson Table
        try:
            c.execute('''INSERT INTO HonourPerson(name, citation, county, hl_id, ht_id)
                        VALUES(?,?,?,?,?)''', (person, cite, county[i], hl_id, ht_id,))
            conn.commit()
        except sqlite3.IntegrityError:
            pass

        if i % 100 == 0:
            print i

    conn.close()
    return
