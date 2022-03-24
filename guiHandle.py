#/ @guiHandle.py
#/ Purpose: Handles the GUI, GUI objects, and calls to other files, classes, and methods.

#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

import tkinter
import json

# Defining tkinter module as a variable.
guiHandle = tkinter.Tk()


#/
#/ @Classes
#/ Purpose: Define classes in this file.

#/ @class_name_filler
#/ Purpose: Filler purpose. 

class class_guiHandle:

    #/ @func_guiHandlePack
    #/ Purpose: Packs GUI objects (such as buttons) and registers them with tkinter.
    def func_guiHandlePack(guiObject):
        guiObject.pack()

    #/ @func_guiHandlePrgMenu
    #/ Purpose: 
    def func_guiHandlePrgMenu():
        # Exit Button
        guiObj_exitButton = tkinter.Button(guiHandle)
        guiObj_exitButton["text"] = "EXIT"
        guiObj_exitButton.place(x = 10, y = 10, width = 4, height = 2)
        guiObj_exitButton["command"] = guiHandle.destroy

        class_guiHandle.func_guiHandlePack(guiObj_exitButton)


    #/ @func_guiHandleMain
    #/ Purpose: Main function for handling gui functions.
    def func_guiHandleMain():

        # Loading .json config file.
        #configFile = json.load('settings.json')

        # Defining title of program window.
        #guiHandle.title(configFile['guiSettings'][0])
        guiHandle.title("TEMP TITLE")

        # Handles Screensize
        #val_scrnW = winfo_screenheight()
        #val_scrnH = winfo_screenheight()
        guiHandle.geometry('1920x1080+400+200')

        # Calling method that will load the GUI objects.
        class_guiHandle.func_guiHandlePrgMenu()

        # Starts GUI and loops it's existence.
        guiHandle.mainloop()
        