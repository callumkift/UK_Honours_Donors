#!/usr/bin/env python
"""
Contains methods that deal with visualising data.
"""

import dbcalls as dbc

def mosthonours():
    """
    Gets and prints all people that have more than one honour
    :return:
    """
    print "\n-- most honours received"
    data = dbc.counthonours()

    count = 0
    for i in range(len(data)):
        if data[i][1] > 1:
            print "%d honours: %s" %(data[i][1], data[i][0])
            count += 1
    print "\n-- # that have had more than one honour: %d" %count
    return


def mostdonations():
    """
    Gets and prints the ten individual donors who have made the most donations to a political party
    :return:
    """
    print "\n-- most donations made"
    data = dbc.get_ind_mostdonations()

    for i in range(len(data)):
        print "%s has donated to the %s --%3d times" %(data[i][0], data[i][2], data[i][1])

    return

def highdonations():
    """
    Gets and prints the 10 highest individual donors to a political pasrty
    :return:
    """
    print "\n-- highest donors"
    data = dbc.get_ind_highdon()

    for i in range(len(data)):
        # print data[i]
        print "%s has donated %2d times to the %s, totally %.2f GBP" %(data[i][0], data[i][3], data[i][1], data[i][2])
    return

def honour_donors():
    """
    Gets and prints the names of people who have donated and received honours.
    :return:
    """
    print "\n--donated and has honour"
    data = dbc.get_hon_don_joints()

    for i in range(len(data)):
        print data[i]
    return