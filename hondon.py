#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#  This script was created so that one can analyse the British Honours
#  list and the donations list.s
#
#  Creator: Callum Kift
#  email: callumkift@gmail.com
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#

import readfiles as rf
import dbcalls as dbc

if __name__ == '__main__':
    p2honours = rf.getpath2honours()
    p2donors = rf.getpath2donations()

    honoursfilelist = rf.findhonfiles(p2honours)
    donorfilelist = rf.finddonfiles(p2donors)

    hon_dict = rf.readfiles(honoursfilelist)
    don_dict = rf.readfiles(donorfilelist)
    print "\n\t\t-File reading finished-"
    print "\n\t\t========================\n"

    dbc.createdb()
    print len(hon_dict)

    if len(hon_dict) != 0:
        dbc.addhon(hon_dict)