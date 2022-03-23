#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

import tkinter


#/
#/ @Classes
#/ Purpose: Define classes in this file.

#/ @class_name_filler
#/ Purpose: Filler purpose. 

class class_guiHandle:

    #/ @func_guiElements
    #/ Purpose: 

    #/ @func_guiHandleMain
    #/ Purpose: Main function for handling gui functions.

    def func_guiHandleMain(guiPrgTitle):

        # Defining tkinter module as a variable.
        guiHandle = tkinter.Tk()

        # Defining title of program window.
        guiHandle.title(guiPrgTitle)

        # Starts GUI and loops it's existence.
        guiHandle.mainloop()