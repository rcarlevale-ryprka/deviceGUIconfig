#/ @debug.py
#/ Purpose: Has variables that pass through it that create logs for error finding and debugging.

#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

from datetime import datetime


#/
#/ @Classes
#/ Purpose: Define classes in this file.

#/ @class_debug
#/ Purpose: Main class for debug.py, this file, holds debug methods.

class class_debug:

    #/ @func_getTime
    #/ Purpose: Gets time for debug logging.
    def func_getTime():
        currTime = datetime.now()
        return (currTime.strftime("[%H:%M:%S]"))


    #/ @func_debugOut
    #/ Purpose: Temporary debug method meant to output a variable.
    def func_debugOut(var1):
        print(class_debug.func_getTime() + " " + var1)


#///
#/ End of Code