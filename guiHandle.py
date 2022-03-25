#/ @guiHandle.py
#/ Purpose: Handles the GUI, GUI objects, and calls to other files, classes, and methods.

#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

from PIL import ImageTk, Image
import tkinter
import json

import debug


# Defining tkinter module as a variable.
guiHandle = tkinter.Tk()


#/
#/ @Classes
#/ Purpose: Define classes in this file.

#/ @class_name_filler
#/ Purpose: Filler purpose. 

class class_guiHandle:

    def func_guiHandleExit():
        debug.class_debug.func_debugOut("GUI Destroy Call")
        guiHandle.destroy()

    #/ @func_guiHandlePrgMenu
    #/ Purpose: 
    #/ TODO: Build GUI
    #/ TODO: Get Image import to work.
    def func_guiHandlePrgMenu():

        # Test Image
        guiObj_imageLabelExample =  tkinter.Label(guiHandle)
        guiObj_imageLabelExample["text"] = "TEST"
        guiObj_imageLabelExample["width"] = 10
        guiObj_imageLabelExample["height"] = 10
        guiObj_imageLabelExample["image"] = ImageTk.PhotoImage(Image.open("testIMG.png"))
        guiObj_imageLabelExample.grid(row = 2, column = 2, sticky = tkinter.S, padx = 10, pady = 10)

        # Test & Example Button
        guiObj_testButton = tkinter.Button(guiHandle)
        guiObj_testButton["text"] = "TEST"
        guiObj_testButton["width"] = 5
        guiObj_testButton["height"] = 5
        guiObj_testButton["command"] = lambda: debug.class_debug.func_debugOut("guiObj_testButton Button Pressed") #For whatever reason this doesn't work without lambda.
        guiObj_testButton.grid(row = 1, column = 0, sticky = tkinter.S, padx = 10, pady = 10)

        # Exit Button
        guiObj_exitButton = tkinter.Button(guiHandle)
        guiObj_exitButton["text"] = "EXIT"
        guiObj_exitButton["width"] = 20
        guiObj_exitButton["height"] = 3
        guiObj_exitButton["command"] = lambda: class_guiHandle.func_guiHandleExit()
        guiObj_exitButton.grid(row = 0, column = 0, sticky = tkinter.E, padx = 10, pady = 10)


    #/ @func_guiHandleMain
    #/ Purpose: Main function for handling gui functions.
    #/ TODO: Make GUI go off of machine's monitor size or manual input in settings.json.
    #/ TODO: Get title from settings json file.
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

        #Test GRID
        guiHandle.resizable(0, 0)
        guiHandle.columnconfigure(4, weight = 200)
        guiHandle.rowconfigure(4, weight = 200)

        # Calling method that will load the GUI objects.
        class_guiHandle.func_guiHandlePrgMenu()

        # Starts GUI and loops it's existence.
        guiHandle.mainloop()
        