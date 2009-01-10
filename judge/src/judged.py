#!/usr/bin/python3

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

from xmlrpc.server import SimpleXMLRPCServer

def problemTest(problem):
    if "src" in problem.keys() \
            and "lang" in problem.keys() \
            and "pid" in problem.keys() \
            and 'tid' in problem.keys() \
            and type(problem["src"]) == type('') \
            and type(problem["lang"]) == type('') \
            and type(problem["pid"]) == type(0) \
            and type(problem["tid"]) == type(0):
        return True
    else:
        return False

class Problem():
    pass

def receive(problem):
    print(problem)
    if problemTest(problem):
        pass    #call main.py
        return 0
    else:
        return 1

if __name__ == "__main__":
    server = SimpleXMLRPCServer(("localhost",2439))
    server.register_function(receive)
    server.serve_forever()
