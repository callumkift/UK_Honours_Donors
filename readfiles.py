#!/usr/bin/env python
"""
Contains methods that deal with reading files and extracting data from them.
"""

import os
import string
import csv


def getpath2honours():
    """
    Reads .path2csv.txt to get the location of the transaction (csv) files are
    :return: Path to the CSV files (string)
    """
    honourspathfile = ".path2honours.txt"
    path2hon = ""

    if os.path.exists(honourspathfile):
        with open(honourspathfile, "r") as f:
            for line in f:
                line = line.strip()
                path2hon = line
        f.close()

    else:
        # Loop until given valid path
        while True:
            user_path = raw_input(
                "Cannot find the honours files.\nPlease write the path to the honours files:\n")

            if os.path.exists(user_path):
                # Need / to get into the directory later on.
                if user_path[-1] != "/":
                    user_path += "/"
                    path2hon = user_path

                    with open(honourspathfile, "w") as f:
                        f.write(path2hon)
                        f.close()
                break
            else:
                "\nError: Invalid path!\n"
                pass
    print "Check - path2honours file: %s" % path2hon
    return path2hon


def getpath2donations():
    """
    Reads .path2csv.txt to get the location of the transaction (csv) files are
    :return: Path to the CSV files (string)
    """
    donorspathfile = ".path2donors.txt"
    path2don = ""

    if os.path.exists(donorspathfile):
        with open(donorspathfile, "r") as f:
            for line in f:
                line = line.strip("\t")
                path2don = line
        f.close()

    else:
        # Loop until given valid path
        while True:
            user_path = raw_input(
                "Cannot find the donors files.\nPlease write the path to the donors files:\n")

            if os.path.exists(user_path):
                # Need / to get into the directory later on.
                if user_path[-1] != "/":
                    user_path += "/"
                    path2don = user_path

                    with open(donorspathfile, "w") as f:
                        f.write(path2don)
                        f.close()
                break
            else:
                "\nError: Invalid path!\n"
                pass
    print "Check - path2donors file: %s" % path2don
    return path2don

