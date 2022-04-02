#/ @guiHandle.py
#/ Purpose: Handles the GUI, GUI objects, and calls to other files, classes, and methods.

#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

from asyncio.windows_events import NULL
import tkinter
import random
import time

import debug


#/ 
#/ @Var Setup
#/ Setup global variables for this file.

# Defining tkinter module as a variable.
guiHandle = tkinter.Tk()

# Defines how far down of a row shift func_guiHandleInterfaceMenu() and
# func_guiHandleInterfaceDetails() need to take.
var_intMenuRowShift = 0


#/ 
#/ @Var Setup TEST
#/ Setup global variables for this file. Has testing variables that will be replaced later.

#Test values for network device information.
netDevInfo = ["Switch", "Layer 2"]

netDevPort = []
netDevPortConStatus = []
netDevPortVLAN = []
netDevPortDuplex = []
netDevPortSpeed = []
netDevPortType = []

num = 0
while num <= 23:
    netDevPort.append("Fa" + str(num))
    num += 1


for i in netDevPort:
    netDevPortConStatus.append("notconnect")
    netDevPortVLAN.append(random.randint(0, 99))
    netDevPortDuplex.append("auto")
    netDevPortSpeed.append("auto")
    netDevPortType.append("10/100 BaseTX")

netDevMatrix = [netDevInfo, netDevPort, netDevPortConStatus, netDevPortVLAN, netDevPortDuplex, netDevPortSpeed, netDevPortType]





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

    
    #/ @func_guiHandleInterfaceDetails
    #/ Purpose: 


    def func_guiHandleInterfaceDetails(var_shIntDetails, portNum):
        global var_intMenuRowShift


        if 'guiObj_portStatusLabelpt1' not in globals():
            
            # Port Status
            global guiObj_portStatusLabelpt1
            guiObj_portStatusLabelpt1 = tkinter.Label(guiHandle)
            global guiObj_portStatusLabelpt2
            guiObj_portStatusLabelpt2 = tkinter.Label(guiHandle)

            global arr_portStatusArr
            arr_portStatusArr = [guiObj_portStatusLabelpt1, guiObj_portStatusLabelpt2]

            # VLAN
            global guiObj_portVLANLabelpt1
            guiObj_portVLANLabelpt1 = tkinter.Label(guiHandle)
            global guiObj_portVLANLabelpt2
            guiObj_portVLANLabelpt2 = tkinter.Label(guiHandle)

            global arr_portVLANArr
            arr_portVLANArr = [guiObj_portVLANLabelpt1, guiObj_portVLANLabelpt2]

            # Duplex
            global guiObj_portDuplexLabelpt1
            guiObj_portDuplexLabelpt1 = tkinter.Label(guiHandle)
            global guiObj_portDuplexLabelpt2
            guiObj_portDuplexLabelpt2 = tkinter.Label(guiHandle)

            global arr_portDuplexArr
            arr_portDuplexArr = [guiObj_portDuplexLabelpt1, guiObj_portStatusLabelpt2]

            # Port Speed
            global guiObj_portSpeedLabelpt1
            guiObj_portSpeedLabelpt1 = tkinter.Label(guiHandle)
            global guiObj_portSpeedLabelpt2
            guiObj_portSpeedLabelpt2 = tkinter.Label(guiHandle)

            global arr_portSpeedArr
            arr_portSpeedArr = [guiObj_portSpeedLabelpt1, guiObj_portSpeedLabelpt2]


            # Array Matrix
            global matrix_interfaceDetailsGui
            matrix_interfaceDetailsGui = [arr_portStatusArr, arr_portVLANArr, arr_portDuplexArr, arr_portSpeedArr]

            

        if var_shIntDetails == True:
            # Port Status
            guiObj_portStatusLabelpt1["text"] = "Port Status: "
            guiObj_portStatusLabelpt1["width"] = 16
            guiObj_portStatusLabelpt1["height"] = 3
            guiObj_portStatusLabelpt1.grid(row = (2 + var_intMenuRowShift), column = 1, sticky = tkinter.E, padx = 0, pady = 10)

            guiObj_portStatusLabelpt2["text"] = str(netDevMatrix[2][portNum])
            guiObj_portStatusLabelpt2["width"] = 16
            guiObj_portStatusLabelpt2["height"] = 3
            guiObj_portStatusLabelpt2.grid(row = (2 + var_intMenuRowShift), column = 2, sticky = tkinter.W, padx = 0, pady = 10)


            # VLAN
            guiObj_portVLANLabelpt1["text"] = "Port VLAN: "
            guiObj_portVLANLabelpt1["width"] = 16
            guiObj_portVLANLabelpt1["height"] = 3
            guiObj_portVLANLabelpt1.grid(row = (3 + var_intMenuRowShift), column = 1, sticky = tkinter.E, padx = 0, pady = 10)

            guiObj_portVLANLabelpt2["text"] = str(netDevMatrix[3][portNum])
            guiObj_portVLANLabelpt2["width"] = 16
            guiObj_portVLANLabelpt2["height"] = 3
            guiObj_portVLANLabelpt2.grid(row = (3 + var_intMenuRowShift), column = 2, sticky = tkinter.W, padx = 0, pady = 10)


            #Duplex
            guiObj_portDuplexLabelpt1["text"] = "Duplex: "
            guiObj_portDuplexLabelpt1["width"] = 16
            guiObj_portDuplexLabelpt1["height"] = 3
            guiObj_portDuplexLabelpt1.grid(row = (4 + var_intMenuRowShift), column = 1, sticky = tkinter.E, padx = 0, pady = 10)

            guiObj_portDuplexLabelpt2["text"] = str(netDevMatrix[4][portNum])
            guiObj_portDuplexLabelpt2["width"] = 16
            guiObj_portDuplexLabelpt2["height"] = 3
            guiObj_portDuplexLabelpt2.grid(row = (4 + var_intMenuRowShift), column = 2, sticky = tkinter.W, padx = 0, pady = 10)


            #Speed
            guiObj_portSpeedLabelpt1["text"] = "Port Speed: "
            guiObj_portSpeedLabelpt1["width"] = 16
            guiObj_portSpeedLabelpt1["height"] = 3
            guiObj_portSpeedLabelpt1.grid(row = (5 + var_intMenuRowShift), column = 1, sticky = tkinter.E, padx = 0, pady = 10)

            guiObj_portSpeedLabelpt2["text"] = str(netDevMatrix[4][portNum])
            guiObj_portSpeedLabelpt2["width"] = 16
            guiObj_portSpeedLabelpt2["height"] = 3
            guiObj_portSpeedLabelpt2.grid(row = (5 + var_intMenuRowShift), column = 2, sticky = tkinter.W, padx = 0, pady = 10)

        # Removes interface objects from screen.
        elif var_shIntDetails == False:
            for guiSet in matrix_interfaceDetailsGui:
                for guiObj in guiSet:
                    print(guiObj["text"])
                    guiObj.grid_forget()


    #/ @func_guiHandleInterfaceMenu
    #/ Purpose: To handle the button interaction menu for how many interfaces the network device has.
    def func_guiHandleInterfaceMenu(var_shBoolIntMenu):
        #/ If the object variables are not created yet, this creates them and stores them as a global variable
        #/ to be referenced if this parent method is ran again.
        for interface in netDevMatrix[1]:
            if ('guiObj_netdevIntButton' + interface) not in globals():
                #/ Variable created for each button that holds it's visibility True or False.
                #/ Should result in a variable in this format:  guiObj_netdevIntButtonFa0Vis
                globals()['guiObj_netdevIntButton' + str(interface) + 'Vis'] = False 
                #/ Creates global variable for GUI button.
                #/ Should result in a variable in this format:  guiObj_netdevIntButtonFa0
                globals()['guiObj_netdevIntButton' + str(interface)] = NULL


        #/ Tests if the visibility of the buttons is true or not and swiches the visibility.
        if var_shBoolIntMenu == True and globals()['guiObj_netdevIntButton' + str(interface) + 'Vis'] == False:
            var_intMenuColShift = -1

            for interface in netDevMatrix[1]:

                #/ Shifts GUI down 1 row if the amount of interfaces on the device is 8 or greater.
                var_intMenuColShift += 1
                var_guiShiftNum = netDevMatrix[1].index(interface) / 8
                if var_guiShiftNum >= 1 and var_intMenuColShift > 7:
                    global var_intMenuRowShift
                    var_intMenuRowShift += 1
                    var_intMenuColShift -= 8
                

                

                globals()['guiObj_netdevIntButton' + str(interface)] = tkinter.Button(
                    guiHandle,
                    text = interface,
                    width = 16,
                    height = 3) #/ Sets button variable to register with tkinter GUI manager.

                #/ Sends variabless to another function when the button is clicked.
                #/ This temporarily just prints whatever port interface.
                globals()['guiObj_netdevIntButton' + str(interface)]["command"] = lambda int = netDevMatrix[1].index(interface): class_guiHandle.func_guiHandleInterfaceDetails(var_shBoolIntMenu, int)

                globals()['guiObj_netdevIntButton' + str(interface)].grid(row = (1 + var_intMenuRowShift), column = (1 + var_intMenuColShift), sticky = tkinter.N, padx = 10, pady = 10) #/Sets position in window.

                globals()['guiObj_netdevIntButton' + str(interface) + 'Vis'] = True

            #/ Updates show/hide network device button text and comamnd.
            guiObj_shInterfacesButton["text"] = "Hide Network Device Ports"
            guiObj_shInterfacesButton["command"] = lambda: class_guiHandle.func_guiHandleInterfaceMenu(False)

        elif var_shBoolIntMenu == False:
            for interface in netDevMatrix[1]:
                globals()['guiObj_netdevIntButton' + str(interface)].grid_forget()
                globals()['guiObj_netdevIntButton' + str(interface) + 'Vis'] = False

            class_guiHandle.func_guiHandleInterfaceDetails(var_shBoolIntMenu, int)

            #/ Updates show/hide network device button text and comamnd.
            guiObj_shInterfacesButton["text"] = "Show Network Device Ports"
            guiObj_shInterfacesButton["command"] = lambda: class_guiHandle.func_guiHandleInterfaceMenu(True)

            var_intMenuRowShift = 0



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
        guiObj_shInterfacesButton["command"] = lambda: [class_guiHandle.func_guiHandleInterfaceMenu(True), class_guiHandle.func_guiHandleInterfaceDetails(False, 0)] #For whatever reason this doesn't work without lambda.
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
        guiHandle.title(debug.func_loadConfig()["projectDetails"]["projectName"])

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


#///
#/ End of Code