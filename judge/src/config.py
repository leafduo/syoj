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

import configparser
import os

class Config:
    """Do some operations related to configure."""
    def __init__(self):
        self.__global = configparser.SafeConfigParser()
        self.__global.read('./config/global.conf')
        self.__lang = configparser.SafeConfigParser()
        self.__lang.read('./config/lang.conf')
        self.__library = configparser.SafeConfigParser()
        self.__library.read('./config/problem.conf')
    def pathToLibrary(self):
        """return the path to library."""
        library.get('location', 'path')
    def setPid(self, pid):
        """Set problem id & problem config."""
        self.__pid = pid
        self.__problem = configparser.SafeConfigParser()
        pathToProblem = os.path.expanduser(os.path.join( \
                self.__pathToLibrary(), str(self.pid), '.config'
                ))
        self.__problem.read(pathToProblem)




if __name__ == '__main__':
    print('Why run me as __main__?')
