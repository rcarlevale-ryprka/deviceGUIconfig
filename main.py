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

class class_main:

    #/ @Define Connection
    #/ Purpose: Defines whether the network devices are through a console server or
    #/ are connected locally. If they are connected locally, then it tries to identify the connection  
    #/ or prompt the user.
    def func_defineConnection ():