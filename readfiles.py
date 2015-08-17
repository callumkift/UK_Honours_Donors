#!/usr/bin/env python
"""
Contains methods that deal with reading files and extracting data from them.
"""

import os


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
    print "Check -- path2honours file: %s" % path2hon
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
    print "Check -- path2donors file: %s" % path2don
    return path2don


def findhonfiles(path2files):
    """
    Method finds the honour TSV files to read and extract data.
    :param path2files: Path to directory that contains honour files
    :return: A list of the honour files to read.
    """

    honfiles = []

    if os.path.isdir(path2files):
        for file in os.listdir(path2files):
            if file.endswith(".tsv"):
                honfiles.append(path2files + str(file))

        if len(honfiles) != 0:
            for i in range(len(honfiles)):
                print "Honour files -- %s" % honfiles[i]
            return honfiles
        else:
            print "\nError - findhonfiles(path2files): No honour files found in given directory.\n"
            return
    else:
        print "\nError - findhonfiles(path2files): Directory does not exist.\n"
        return honfiles

def finddonfiles(path2files):
    """
    Method finds the donor CSV files to read and extract data.
    :param path2files: Path to directory that contains honour files
    :return: A list of the donor files to read.
    """

    donfiles = []

    if os.path.isdir(path2files):
        for file in os.listdir(path2files):
            if file.endswith(".csv"):
                donfiles.append(path2files + str(file))

        if len(donfiles) != 0:
            for i in range(len(donfiles)):
                print "Donor files -- %s" % donfiles[i]
            return donfiles
        else:
            print "\nError - finddonfiles(path2files): No donor files found in given directory.\n"
            return
    else:
        print "\nError - finddonfiles(path2files): Directory does not exist.\n"
        return donfiles