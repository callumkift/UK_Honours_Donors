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
    :return: a list of extracted data from the filelist
    """

    data = []
    filetype = filelist[0][-3:]
    prev_read = readpastfiles(filetype)

    if len(filelist) != 0:
        for i in range(len(filelist)):
            # Only extracts data from files that have not been previously read.
            if filelist[i] not in prev_read:
                data.append(extractdata(filelist[i], filetype))
                add2pastreads(filetype, filelist[i])
            else:
                print "%s -- previously read" % filelist[i]

        return data
    else:
        print "\nError - readcsvfiles(csvlist): No CSV files in list. Are there CSV files in given directory?\n"
        return data


def extractdata(datafile, ftype):
    """
    Extracts the data from the data file
    :param datafile: file containing data
    :param ftype: filetype
    :return: A list containing  data
    """
    filedata = []


    if ftype == "tsv":
        ncol = 8
        delim = "\t"
    elif ftype == "csv":
        ncol = 23
        delim = ","

    if ncol or delim:
        if os.path.exists(datafile):
            print "Open -- %s" %datafile
            with open(datafile, "r") as f:
                keys = f.readline().split(delim)
            print keys
        return filedata
    else:
        print "Check -- not initiated."
        return filedata



def add2pastreads(ftype, filedone):
    """
    Adds the file to read list.
    If ftype=tsv, -> adds filedone to past read honours list.
    If ftype=csv, -> adds filedone to past read donors list.
    :param ftype:
    :param filedone:
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
            # pr.write(filedone + "\n")
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
