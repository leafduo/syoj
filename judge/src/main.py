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

import pickle
import os
import subprocess
import configparser

class Result():
    pass

result = Result()

def configInit():
    """Config initial.
    
       Read global & language configure.
    """
    configGlobal = configparser.SafeConfigParser()
    configGlobal.read("./config/global.conf")
    global configLang
    configLang = configparser.SafeConfigParser()
    configLang.read("./config/lang.conf")
    global path
    path = configGlobal.get("global","WorkingDictionary");

def unpack():
    """Unpack the source code and set language, pid, tid."""
    global lang, pid, tid
    problem = pickle.load(os.path.join(path,"problem.dat"))
    lang = problem["lang"]
    pid = problem["pid"]
    tid = problem["tid"]
    srcfile = open(path+"src."+configLang.get(lang,extension),'w')
    print(src, file = srcfile)

def compile():
    """Complie the source code."""
    compiler = subprocess.Popen( \
            [configLang.get(lang,"compiler"), \
            configLang.get(lang,"arguments")],
            )
    compiler.wait()
    if (compiler.returncode)
        print("compile error.")     #todo:log file & errer handling
    else:

