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


def readfiles(filelist):
    """
    Reads files and puts data into a list
    :param filelist: list of files
    :return: a dictionary; key = data_name, values = list_of_values_for_key
    """

    if len(filelist) != 0:
        toread = []
        filetype = filelist[0][-3:]
        prev_read = readpastfiles(filetype)
        for i in range(len(filelist)):
            # Only extracts data from files that have not been previously read.
            if filelist[i] not in prev_read:
                toread.append(filelist[i])
            else:
                print "%s -- previously read" % filelist[i]

        if len(toread) != 0:
            data_dict = {}
            keys = getkeys(toread[0], filetype)

            if len(keys) != 0:
                datalist = extractdata(toread, filetype, len(keys))
                if len(datalist) == len(keys):
                    for i in range(len(keys)):
                        data_dict[keys[i].rstrip()] = datalist[i]
                    return data_dict
                else:
                    print "\nError - #keys != #columns"
            else:
                print "No keys found"
                return {}
        else:
            print "Nothing to read"
            return {}

    else:
        print "\nError - readfiles(filelist): No files in list. Are there files in given file list?\n"
        return {}


def getkeys(firstfile, ftype):
    """
    Gets the keys for the dictionary, by reading the first line of the file.
    :param firstfile: the first file in the list of files to read.
    :param ftype: file type
    :return: list of keys
    """
    if ftype == "tsv":
        delim = "\t"
    elif ftype == "csv":
        delim = ","

    if delim:
        if os.path.exists(firstfile):
            with open(firstfile, "r") as f:
                keys = f.readline().split(delim)
            print "Check -- got keys"
            return keys
        else:
            return []
    else:
        return []


def extractdata(datafiles, ftype, ncol):
    """
    Extracts the data from the data file
    :param datafiles: file containing data
    :param ftype: filetype
    :param ncol: number of keys = number of columns in file
    :return: A list containing  data
    """
    filedata = []

    if ftype == "tsv":
        delim = "\t"
    elif ftype == "csv":
        delim = ","

    if ncol or delim:

        data2dlist = [[] for i in range(ncol)]

        for file in datafiles:
            print "Open -- %s" % file
            with open(file, "r") as f:
                f.readline()
                for line in f:
                    line = line.strip()
                    column = line.split(delim)
                    if len(column) == ncol:
                        for q in range(ncol):
                            data2dlist[q].append(column[q])
                    else:
                        print "IGNORED -- %s" % line
            add2pastreads(file, ftype)
        print "Read -- %s files" % ftype
        return data2dlist
    else:
        print "Check -- not initiated."
        return filedata


def add2pastreads(filedone, ftype):
    """
    Adds the file to read list.
    If ftype=tsv, -> adds filedone to past read honours list.
    If ftype=csv, -> adds filedone to past read donors list.
    :param filedone: file to add
    :param ftype: file type
    :return:
    """
    pastread = ""

    if ftype == "tsv":
        pastread = ".pastread_honours.txt"
    elif ftype == "csv":
        pastread = ".pastread_donors.txt"

    if pastread == "":
        return
    else:
        with open(pastread, "a") as pr:
            pr.write(filedone + "\n")
            pr.close()
            print "-- Written %s to readfile" % filedone
    return


def readpastfiles(ftype):
    """
    Reads from a file the previously read files for the specific file type. If ftype=tsv, it will
    read previously read honours list files. If ftype=csv, it will read the previously read donor
    files.
    :param ftype: File type
    :return: List of previously read files
    """

    pastread = ""
    read_files = []

    if ftype == "tsv":
        pastread = ".pastread_honours.txt"
    elif ftype == "csv":
        pastread = ".pastread_donors.txt"

    if pastread == "":
        return read_files
    else:
        if os.path.exists(pastread):
            print "Check -- Reads past read."
            with open(pastread, "r") as f:
                for line in f:
                    line = line.strip()
                    read_files.append(line)
        else:
            # creates empty file
            with open(pastread, "w") as f:
                f.close()
                print "%s -- created" % pastread

        return read_files
