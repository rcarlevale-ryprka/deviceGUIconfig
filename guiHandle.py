#/ @guiHandle.py
#/ Purpose: Handles the GUI, GUI objects, and calls to other files, classes, and methods.

#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

from asyncio.windows_events import NULL
from glob import glob
from PIL import ImageTk, Image
import tkinter
import json

import time

import debug


# Defining tkinter module as a variable.
guiHandle = tkinter.Tk()



#Test values for port information.
netDev = "Layer 2 Switch"

netDevPort = ["Fa0", "Fa1", "Fa2","Fa3"]
netDevPortConStatus = ["notconnect", "notconnect", "notconnect", "notconnect"]
netDevPortVLAN = [1, 1, 1, 10]
netDevPortDuplex = ["auto", "auto", "auto", "auto"]
netDevPortSpeed = ["auto", "auto", "auto", "auto"]
netDevPortType = ["10/100 BaseTX", "10/100 BaseTX", "10/100 BaseTX", "10/100 BaseTX"]

netDevMatrix = [netDevPort, netDevPortConStatus, netDevPortVLAN, netDevPortDuplex, netDevPortSpeed, netDevPortType]


val_portButtonListShown = True


#/
#/ @Classes
#/ Purpose: Define classes in this file.

#/ @class_name_filler
#/ Purpose: Filler purpose. 

class class_guiHandle:

    #/ @func_guiHandleExit
    #/ Purpose: Closes the program.
    def func_guiHandleExit():
        debug.class_debug.func_debugOut("GUI Destroy Call")
        guiHandle.destroy()


    #/ @func_guiHandleInterfaceMenu
    #/ Purpose: To handle the button interaction menu for how many interfaces the network device has.
    def func_guiHandleInterfaceMenu(var_shBoolIntMenu):

        #/ If the object variables are not created yet, this creates them and stores them as a global value
        #/ to be referenced if this parent method is ran again.
        for interface in netDevMatrix[0]:
            if ('guiObj_netdevIntButton' + interface + 'Vis') not in globals():
                globals()['guiObj_netdevIntButton' + str(interface) + 'Vis'] = False

            if ('guiObj_netdevIntButton' + interface) not in globals():
                globals()['guiObj_netdevIntButton' + str(interface)] = NULL #/ Has to be null or set to a value or else error.


        #/ Tests if the visibility of the buttons is true or not and swiches the visibility.
        if var_shBoolIntMenu == True:
            for interface in netDevMatrix[0]:
                globals()['guiObj_netdevIntButton' + str(interface)] = tkinter.Button(guiHandle)
                globals()['guiObj_netdevIntButton' + str(interface)]["text"] = interface
                globals()['guiObj_netdevIntButton' + str(interface)]["width"] = 12
                globals()['guiObj_netdevIntButton' + str(interface)]["height"] = 3
                globals()['guiObj_netdevIntButton' + str(interface)].grid(row = 1, column = (1 + netDevMatrix[0].index(interface)), sticky = tkinter.S, padx = 10, pady = 10)
                globals()['guiObj_netdevIntButton' + str(interface) + 'Vis'] = True

            #/ Updates show/hide network device button text and comamnd.
            guiObj_shInterfacesButton["text"] = "Hide Network Device Ports"
            guiObj_shInterfacesButton["command"] = lambda: class_guiHandle.func_guiHandleInterfaceMenu(False)
        if var_shBoolIntMenu == False:
            for interface in netDevMatrix[0]:
                globals()['guiObj_netdevIntButton' + str(interface)].grid_forget()
                globals()['guiObj_netdevIntButton' + str(interface) + 'Vis'] = False

            #/ Updates show/hide network device button text and comamnd.
            guiObj_shInterfacesButton["text"] = "Show Network Device Ports"
            guiObj_shInterfacesButton["command"] = lambda: class_guiHandle.func_guiHandleInterfaceMenu(True)


    #/ @func_guiHandlePrgMenu
    #/ Purpose: 
    #/ TODO: Build GUI
    #/ TODO: Get Image import to work.
    def func_guiHandlePrgMenu():
        global guiObj_exitButton
        global guiObj_shInterfacesButton

        # Exit Button
        guiObj_exitButton = tkinter.Button(guiHandle)
        guiObj_exitButton["text"] = "EXIT"
        guiObj_exitButton["width"] = 20
        guiObj_exitButton["height"] = 3
        guiObj_exitButton["command"] = lambda: class_guiHandle.func_guiHandleExit()
        guiObj_exitButton.grid(row = 0, column = 0, sticky = tkinter.W, padx = 10, pady = 10)

        # Show & Hide Interfaces Button
        guiObj_shInterfacesButton = tkinter.Button(guiHandle)
        guiObj_shInterfacesButton["text"] = "Show Network Device Ports"
        guiObj_shInterfacesButton["width"] = 30
        guiObj_shInterfacesButton["height"] = 3
        guiObj_shInterfacesButton["command"] = lambda: class_guiHandle.func_guiHandleInterfaceMenu(True) #For whatever reason this doesn't work without lambda.
        guiObj_shInterfacesButton.grid(row = 1, column = 0, sticky = tkinter.S, padx = 10, pady = 10)


        


    #/ @func_guiHandleMain
    #/ Purpose: Main function for handling gui functions.
    #/ TODO: Make GUI go off of machine's monitor size or manual input in settings.json.
    #/ TODO: Get title from settings json file.
    def func_guiHandleMain():

        # Loading .json config file.
        #configFile = json.load('settings.json')

        # Defining title of program window.
        #guiHandle.title(configFile['guiSettings'][0])
        guiHandle.title("Network Device Manager")

        # Handles Screensize
        #val_scrnW = winfo_screenheight()
        #val_scrnH = winfo_screenheight()
        guiHandle.geometry('1920x1080+400+200')

        #Test GRID
        guiHandle.resizable(0, 0)
        guiHandle.columnconfigure(20, weight = 200)
        guiHandle.rowconfigure(20, weight = 200)

        # Calling method that will load the GUI objects.
        class_guiHandle.func_guiHandlePrgMenu()

        # Starts GUI and loops it's existence.
        guiHandle.mainloop()
        