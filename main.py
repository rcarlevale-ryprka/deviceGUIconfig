#/ 
#/ @Project Headers
#/ Purpose: Used for referencing outside of the file to identify informaiton about the program.

__projName__ = ""
__projDesc__ = ""
__projVer__ = "0.0.0"

__authors__ = ["Ryder Carlevale", "Amber Kovacs"]
__emails__ = ["carlevaler@wit.edu", "kovacsa@wit.edu"]
__credits__ = ""

__license__ = ""


#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

import debug
import gui
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

        #Testing debug class & methods.
        debug.class_debug.func_debugOut("This is a string!")
        


#/
#/ @Calls
#/ Purpose: Calling the main class in this program.

class_main.func_main()