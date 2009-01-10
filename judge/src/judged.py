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
    """Test if the problem submitted is valid.

       A boolean is returned, True if valid and False indicates invalid.
    """
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

def receive(problem):
    """Receive a problem and return an returncode.

       0 for OK and 1 for incomplete problems.
    """
    print(problem)
    if problemTest(problem):
        pass    #call main.py
        return 0
    else:
        return 1

def buildServer():
    """build an XMLRPC Server and serve forever \
    waiting for problem to submit.
    """
    server = SimpleXMLRPCServer(("localhost",2439))
    server.register_function(receive)
    server.serve_forever()

if __name__ == "__main__":
    buildServer()
