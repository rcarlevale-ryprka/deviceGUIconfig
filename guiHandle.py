#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

import tkinter

# Defining tkinter module as a variable.
guiHandle = tkinter.Tk()

#/
#/ @Classes
#/ Purpose: Define classes in this file.

#/ @class_name_filler
#/ Purpose: Filler purpose. 

class class_guiHandle:

    #/ @func_guiHandlePack
    #/ Purpose: Packs GUI objects and registers them with tkinter.
    def func_guiHandlePack(guiObject):
        guiObject.pack()

    #/ @func_guiHandlePrgMenu
    #/ Purpose: 
    def func_guiHandlePrgMenu():
        # TEST
        guiObj_exitButton = tkinter.Button(guiHandle, text = "EXIT", width = 4, height = 2, command = guiHandle.destroy)
        class_guiHandle.func_guiHandlePack(guiObj_exitButton)


    #/ @func_guiHandleMain
    #/ Purpose: Main function for handling gui functions.

    def func_guiHandleMain(guiPrgTitle):
        #Defining title of program window.
        guiHandle.title(guiPrgTitle)

        # FILLER
        class_guiHandle.func_guiHandlePrgMenu()

        # Starts GUI and loops it's existence.
        guiHandle.mainloop()