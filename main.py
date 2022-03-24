#/ 
#/ @Project Headers
#/ Purpose: Used for referencing outside of the file to identify informaiton about the program.

__projName__ = "Cisco Network Device GUI API"
__projDesc__ = ""
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

import tkinter

import debug
import guiHandle
import cmdAPI
import conAPI


#/
#/ @Classes
#/ Purpose: Define classes in this file.

#/ @class_main
#/Purpose: Main class of the file. Meant to call and run the entire program.

class class_main:

    #/ @func_defineConnection
    #/ Purpose: Defines whether the network devices are through a console server or
    #/ are connected locally. If they are connected locally, then it tries to identify the connection  
    #/ or prompt the user.
    def func_defineConnection ():

        ...


    #/ @func_main
    #/ Purpose: Main function in the main class.

    def func_main():

        # Hello world.
        print("Hello World!")

        # Testing debug class & methods.
        debug.class_debug.func_debugOut("This is a string!")

        # Variables.
        varInteger = 1
        varString = "String"
        varBoolean = True
        varArray = [1, 2, 3]

        guiHandle.class_guiHandle.func_guiHandleMain()
        

#/
#/ @Calls
#/ Purpose: Calling the main class in this program.

class_main.func_main()