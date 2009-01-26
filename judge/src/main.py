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

import pickle
import os
import sys
import subprocess
import configparser
import time

class Result():
    pass

class Test():
    pass

result = Result()

def configInit():
    """Config initial.
    
       Read global, language & problem configure.
    """
    configGlobal = configparser.SafeConfigParser()
    configGlobal.read("./config/global.conf")
    global configLang
    configLang = configparser.SafeConfigParser()
    configLang.read("./config/lang.conf")
    global configProblemGlobal
    configProblemGlobal = configparser.SafeConfigParser()
    configProblemGlobal.read("./config/problem.conf")
    global workingDict
    workingDict = configGlobal.get("global","WorkingDictionary");
    #configProblem load in unpack()

def unpack():
    """Unpack the source code and set language, pid, tid."""
    global lang, pid, tid
    problem = pickle.load(open( \
            os.path.expanduser(os.path.join(workingDict, "problem.dat")), \
            "rb"))
    lang = problem["lang"]
    pid = problem["pid"]
    tid = problem["tid"]
    srcfile = open(os.path.expanduser(os.path.join(workingDict,\
            "src." +\
            configLang.get(lang, "extension"))), 'w')
    print(problem["src"], file = srcfile)
    global configProblem
    configProblem = configparser.SafeConfigParser()
    configProblem.read(os.path.expanduser(os.path.join( \
            configProblemGlobal.get("location", "path"), \
            str(pid), \
            ".config")))

def resultInit():
    """Result Initial"""
    result.tid = tid
    result.pid = pid
    result.test = [];

def compile():
    """Complie the source code."""
    os.chdir(workingDict);  #change path
    compiler = subprocess.Popen( \
            [configLang.get(lang, "compiler"), \
            configLang.get(lang, "arguments"), \
            os.path.expanduser(os.path.join(
            workingDict, "src." + configLang.get(lang, "extension")))],
            )
    compiler.wait()
    if (compiler.returncode):
        print("compiling error.")     #todo:log file
        testCase = Test()
        testCase.score = 0
        testCase.error = "Compiling Error"
        testCase.errorDesc = "Compiling Error"
        for i in range(1, configProblem.getint("point", "numberOfTest") + 1):
            testCase.id = i + 1
            result.test.append(testCase)
        send(result)
    else:
        run()

def prepare(n):
    """do some preparation.

    like linking input etc.
    """
    os.symlink(os.path.expanduser(os.path.join( \
            configProblemGlobal.get("location", "path"), \
            str(pid),
            configProblem.get("file", "input"))), \
            os.path.expanduser(os.path.join( \
            workingDict, \
            str(n) + ".in")), \
            )

def run():
    """Run the program numberOfTest times."""
    for i in range(1, configProblem.getint("point", "numberOfTest") + 1):
        preapre(i)
        os.chdir(workingDict)   #change path
        program = subprocess.Popen('./a.out');
        timeLimit = configProblem.getfloat("time", "time");
        time.sleep(timeLimit);
        if program.poll() == None: 
            #time out
            program.kill()
            testCase = Test()
            testCase.score = 0
            testCase.id = i
            testCase.error = "TLE"
            testCase.errorDesc = "TLE"
            result.test.append(testCase)
        else:
            judge(i)
        clean()
    cleanAll()
    pass

def judge():
    """Judge whether the answer is correct."""
    pass

def clean():
    """Clean the working dictionary for the next run."""

def cleanAll():
    """Clean ALL in the working dictionary."""

def send(result):
    """Send result to frontend."""
    pass


if __name__ == "__main__":
    configInit()
    unpack()
    resultInit()
    compile()
