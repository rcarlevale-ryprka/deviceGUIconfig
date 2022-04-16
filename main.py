#/ 
#/ @Project Headers
#/ Purpose: Used for referencing outside of the file to identify informaiton about the program.

__projName__ = "Network Device Manager"
__projDesc__ = "Used to automate CLI commands for cisco based devices using GUI."
__projVer__ = ["alpha", "1.0.0"]

__authors__ = ["Ryder Carlevale", "Amber Kovacs"]
__emails__ = ["carlevaler@wit.edu", "kovacsa@wit.edu"]
__credits__ = ""

__license__ = ""


#/ @main.py
#/ Purpose: Main file of the entire program. Runs all other classes and files underneath it.

#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

import debug
import guiHandle
import os


#/
#/ @Classes
#/ Purpose: Define classes in this file.

#/ @class_main
#/Purpose: Main class of the file. Meant to call and run the entire program.

class class_main:

    #/ @func_createPath
    #/ Purpose: Creates program's path where it stores config files for network devices if the path does not exist.
    def func_createPath():
        filepath = debug.func_loadConfig()["fileSettings"]["filePath"]

        if not os.path.isdir(filepath):
            os.mkdir(filepath)
 
    #/ @func_main
    #/ Purpose: Main function in the main class.
    def func_main():
        #/ Calling createPath for it's purpose.
        class_main.func_createPath()

        #/ Calling debug to output the program has started.
        debug.class_debug.func_debugOut("class_main", "func_main", "Program Started")

        guiHandle.class_guiHandle.func_guiHandleMain()

        debug.class_debug.func_debugOut("class_main", "func_main", "Program Stopped")
        

#/
#/ @Calls
#/ Purpose: Calling the main class in this program which initliazes the program and starts everything.
if __name__ == "__main__":
    class_main.func_main()


#///
#/ End of Code