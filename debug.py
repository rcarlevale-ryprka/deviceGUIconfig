#/ @debug.py
#/ Purpose: Has variables that pass through it that create logs for error finding and debugging.

#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

from datetime import datetime
import json




#/
#/ @Classes
#/ Purpose: Define classes in this file.

#/ @func_settingsManage
#/ Purpose: Loads settings.json file for when this method is called.

def func_loadConfig():
    with open('config.json', 'r') as confFile:
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
        if func_loadConfig()["debugSettings"]["doLogging"] == True:
            try:
                var_logFilePath = func_loadConfig()["fileSettings"]["filePath"]
                file_logFile = open(var_logFilePath, 'a')
                file_logFile.write(class_debug.func_getTime() + " " + var_stringInp + "\r")
                file_logFile.close()
                pass
            except IOError:
                print(class_debug.func_getTime() + " (ERROR) Couldn't create file for logging.")


    #/ @func_debugOut
    #/ Purpose: Temporary debug method meant to output a variable.
    def func_debugOut(var_classID, var_funcID, var_stringInp):
        if func_loadConfig()["debugSettings"]["doDebugging"] == True:
            print("")
            if type(var_stringInp) == str and type(var_classID) == str and type(var_funcID) == str:
                class_debug.func_logFileOut(var_stringInp)
                print(class_debug.func_getTime() + 
                " [" + str(var_classID) + 
                "] [" + str(var_funcID) + 
                "] " + var_stringInp)
                pass
            else:
                raise TypeError(class_debug.func_getTime() + 
                " [" + str(var_classID) + 
                "] [" + str(var_funcID) + "]" + 
                "\r (ERROR) Debug Variable Not String")

            



#///
#/ End of Code