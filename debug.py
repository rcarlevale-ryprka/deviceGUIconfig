#/ @debug.py
#/ Purpose: Has variables that pass through it that create logs for error finding and debugging.

#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

from datetime import datetime
import json



#/ @Load Settings File
#/ Purpose: Loads manually. 
with open('settings.json', 'r') as confFile:
    doDebug = confFile["debugSettings"]["doDebugging"]
    doLogging = confFile["debugSettings"]["doLogging"]

#/
#/ @Classes
#/ Purpose: Define classes in this file.

#/ @class_settingsManage
#/ Purpose: Loads settings.json file for entire program.

class class_settingsManage:
    def class_settingsManage():
        with open('settings.json', 'r') as confFile:
            return(json.load(confFile))



#/ @class_debug
#/ Purpose: Main class for debug.py, this file, holds debug methods.

class class_debug:

    #/ @func_getTime
    #/ Purpose: Gets time for debug logging.
    def func_getTime():
        currTime = datetime.now()
        return (currTime.strftime("[%H:%M:%S]"))

    #/ @func_logFileOut
    #/ Purpose: To write and create log file.
    def func_logFileOut(var_stringInp):

        #/ Try/Catch block for seeing if logging file exists. If not, spits error.
        try:
            file_logFile = open('C:\\NDM.txt', 'a')
            file_logFile.write(class_debug.func_getTime() + " " + var_stringInp + "\r")
            file_logFile.close()
            pass
        except IOError:
            print(class_debug.func_getTime() + " (ERROR) Couldn't create file for logging.")




        



    #/ @func_debugOut
    #/ Purpose: Temporary debug method meant to output a variable.
    def func_debugOut(var_stringInp):

        
        if type(var_stringInp) == str:
            class_debug.func_logFileOut(var_stringInp)
            pass
        else:
            raise TypeError(class_debug.func_getTime() + " (ERROR) Debug Variable Not String")

        print(class_debug.func_getTime() + " " + var_stringInp)


        



#///
#/ End of Code