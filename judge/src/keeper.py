#!/usr/bin/env python3

#    SYOJ - Simple Yummy Online Judge (backend)
#    Copyright (C) 2009  leafduo@gmail.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import subprocess

def keep():
    """start judged.py, and keep it running"""
    judged = subprocess.Popen("./judged.py")
    while True:
        judged.wait()
        print("judged.py(pid ",judged.pid, \
                ") is killed, return code is ", judged.returncode, \
                '.',sep='') 
        #todo:log file
        judged=subprocess.Popen("./judged.py")

if __name__=="__main__":
    keep()
