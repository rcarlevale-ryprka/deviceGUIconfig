#/ @guiHandle.py
#/ Purpose: Handles the GUI, GUI objects, and calls to other files, classes, and methods.

#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

import tkinter
from tkinter import filedialog

import debug
import cmdAPI


#/ 
#/ @Var Setup
#/ Setup global variables for this file.

# Defining tkinter module as a variable.
guiHandle = tkinter.Tk()

# Value that defines if the menu area is busy.
bool_menuBusy = False

# Defines how far down of a row shift func_guiHandleInterfaceMenu() and
# func_guiHandleInterfaceDetails() need to take.
var_intMenuRowShift = 0


#/ 
#/ @Var Setup TEST
#/ Setup global variables for this file. Has testing variables that will be replaced later.

#Test values for network device information.
netDevInfo = []

netDevPort = []
netDevPortConStatus = []
netDevPortVLAN = []
netDevPortDuplex = []
netDevPortSpeed = []

netDevMatrix = [netDevInfo, netDevPort, netDevPortConStatus, netDevPortVLAN, netDevPortDuplex, netDevPortSpeed]

global var_netDevInterfaces



#/
#/ @Classes
#/ Purpose: Define classes in this file.

#/ @class_guiHandle
#/ Purpose: Handles all GUI objects and window management.

class class_guiHandle:
    #/ @func_guiHandleExit
    #/ Purpose: Closes the GUI and ends the program.
    def func_guiHandleExit():
        debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleExit", "GUI Destroy Call")
        guiHandle.destroy()


    #/ @gunc_guiHandleGrabTextInp
    #/ Purpose: Grabs information from text boxes in which the user can type into.
    def func_guiHandleGrabTextInp(guiObj_textInpBox):
        guiObjParse = guiObj_textInpBox.get(1.0, tkinter.END + "-1c")
        print(guiObjParse)


    #/ @func_guiHandleNDconfigManage()
    #/ Purpose: GUI that handles loading and downloading the config.
    def func_guiHandleNDconfigManage():
        global bool_menuBusy
        global guiObj_shConfigLoadButton

        if 'arr_configGUIObjs' not in globals():
            global guiObj_downNDconfig
            guiObj_downNDconfig = tkinter.Button(guiHandle)

            global guiObj_upNDconfig
            guiObj_upNDconfig = tkinter.Button(guiHandle)

            global arr_configGUIObjs
            arr_configGUIObjs = [guiObj_downNDconfig, guiObj_upNDconfig]


        if bool_menuBusy == False:
            guiObj_downNDconfig["text"] = "Download Config"
            guiObj_downNDconfig["width"] = 20
            guiObj_downNDconfig["height"] = 3
            guiObj_downNDconfig["command"] = lambda: cmdAPI.class_commandAPI.func_downConfFile()
            guiObj_downNDconfig.grid(row = 1, column = 1, sticky = tkinter.E, padx = 10, pady = 10)

            def func_subGuiHandle_selectUpFile():
                file_upConfig = filedialog.askopenfile(mode = 'r')
                arr_fileContents = file_upConfig.readlines()
                cmdAPI.class_commandAPI.func_upConfFile(arr_fileContents)
                

            guiObj_upNDconfig["text"] = "Upload Config"
            guiObj_upNDconfig["width"] = 20
            guiObj_upNDconfig["height"] = 3
            guiObj_upNDconfig["command"] = lambda: func_subGuiHandle_selectUpFile()
            guiObj_upNDconfig.grid(row = 1, column = 2, sticky = tkinter.E, padx = 10, pady = 10)
 
            guiObj_shConfigLoadButton["text"] = "Hide Config Loader"
            bool_menuBusy = True


        elif bool_menuBusy == True:
            for guiObj in arr_configGUIObjs:
                guiObj.grid_forget()

            guiObj_shConfigLoadButton["text"] = "Show Config Loader"
            bool_menuBusy = False

    
    #/ @func_guiHandleInterfaceDetails
    #/ Purpose: Handle details of gui objects of the interfaces.
    def func_guiHandleInterfaceDetails(var_shIntDetails, var_portNum):
        # Referencing global variables to grab into method.
        global var_intMenuRowShift
        global bool_menuBusy

        # Checks if GUI objects are in global then creates variables. Redundant as fuck.
        if 'matrix_interfaceDetailsGui' not in globals():
            # Port Current Connection GUI Object registering.
            global guiObj_portNameLabelpt1
            guiObj_portNameLabelpt1 = tkinter.Label(guiHandle)
            global guiObj_portNameLabelpt2
            guiObj_portNameLabelpt2 = tkinter.Label(guiHandle)

            global arr_portNameArr
            arr_portNameArr = [guiObj_portNameLabelpt1, guiObj_portNameLabelpt2]

            # Port Status GUI Object registering.
            global guiObj_portStatusLabelpt1
            guiObj_portStatusLabelpt1 = tkinter.Label(guiHandle)
            global guiObj_portStatusLabelpt2
            guiObj_portStatusLabelpt2 = tkinter.Label(guiHandle)

            global arr_portStatusArr
            arr_portStatusArr = [guiObj_portStatusLabelpt1, guiObj_portStatusLabelpt2]

            # VLAN GUI Object registering.
            global guiObj_portVLANLabelpt1
            guiObj_portVLANLabelpt1 = tkinter.Label(guiHandle)
            global guiObj_portVLANLabelpt2
            guiObj_portVLANLabelpt2 = tkinter.Label(guiHandle)

            global guiObj_portVLANInpBox
            guiObj_portVLANInpBox = tkinter.Text(guiHandle)
            global guiObj_portVLANSetButton
            guiObj_portVLANSetButton = tkinter.Button(guiHandle)

            global arr_portVLANArr
            arr_portVLANArr = [guiObj_portVLANLabelpt1, guiObj_portVLANLabelpt2, guiObj_portVLANInpBox, guiObj_portVLANSetButton]

            # Duplex GUI Object registering.
            global guiObj_portDuplexLabelpt1
            guiObj_portDuplexLabelpt1 = tkinter.Label(guiHandle)
            global guiObj_portDuplexLabelpt2
            guiObj_portDuplexLabelpt2 = tkinter.Label(guiHandle)
            
            global guiObj_portDuplexSetButtonAuto
            guiObj_portDuplexSetButtonAuto = tkinter.Button(guiHandle)
            global guiObj_portDuplexSetButtonFull
            guiObj_portDuplexSetButtonFull = tkinter.Button(guiHandle)
            global guiObj_portDuplexSetButtonHalf
            guiObj_portDuplexSetButtonHalf = tkinter.Button(guiHandle)

            global arr_portDuplexArr
            arr_portDuplexArr = [guiObj_portDuplexLabelpt1, guiObj_portDuplexLabelpt2, guiObj_portDuplexSetButtonAuto, guiObj_portDuplexSetButtonFull, guiObj_portDuplexSetButtonHalf]

            # Port Speed GUI Object registering.
            global guiObj_portSpeedLabelpt1
            guiObj_portSpeedLabelpt1 = tkinter.Label(guiHandle)
            global guiObj_portSpeedLabelpt2
            guiObj_portSpeedLabelpt2 = tkinter.Label(guiHandle)
            
            global guiObj_portSpeedInpBox
            guiObj_portSpeedInpBox = tkinter.Text(guiHandle)
            global guiObj_portSpeedSetButton
            guiObj_portSpeedSetButton = tkinter.Button(guiHandle)

            global arr_portSpeedArr
            arr_portSpeedArr = [guiObj_portSpeedLabelpt1, guiObj_portSpeedLabelpt2]

            # Array Matrix
            global matrix_interfaceDetailsGui
            matrix_interfaceDetailsGui = [arr_portNameArr, arr_portStatusArr, arr_portVLANArr, arr_portDuplexArr, arr_portSpeedArr]

            
        # Checks if menu area is busy, if it isn't, shows menu items.
        if var_shIntDetails == False:

            var_shIntDetails = True

            var_guiSetRow = 2


            # Port Name GUI Objects Creation.
            guiObj_portNameLabelpt1["text"] = "Current Interface: "
            guiObj_portNameLabelpt1.grid(row = (var_guiSetRow + var_intMenuRowShift), column = 1, sticky = tkinter.E, padx = 10, pady = 10)
            debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleInterfaceDetails", "guiObj_portNameLabelpt1 Loaded")

            netDevMatrix[1] = cmdAPI.class_commandAPI.func_getInts()
            guiObj_portNameLabelpt2["text"] = str(netDevMatrix[1][var_portNum])
            guiObj_portNameLabelpt2.grid(row = (var_guiSetRow + var_intMenuRowShift), column = 2, sticky = tkinter.W, padx = 10, pady = 10)
            debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleInterfaceDetails", "guiObj_portNameLabelpt2 Loaded")

            var_guiSetRow += 1

            # Port Status GUI Objects Creation.
            guiObj_portStatusLabelpt1["text"] = "Port Status: "
            guiObj_portStatusLabelpt1.grid(row = (var_guiSetRow + var_intMenuRowShift), column = 1, sticky = tkinter.E, padx = 10, pady = 10)
            debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleInterfaceDetails", "guiObj_portStatusLabelpt1 Loaded")

            netDevMatrix[2] = cmdAPI.class_commandAPI.func_getConStatus()
            guiObj_portStatusLabelpt2["text"] = str(netDevMatrix[2][var_portNum])
            guiObj_portStatusLabelpt2.grid(row = (var_guiSetRow + var_intMenuRowShift), column = 2, sticky = tkinter.W, padx = 10, pady = 10)
            debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleInterfaceDetails", "guiObj_portStatusLabelpt2 Loaded")

            var_guiSetRow += 1


            # VLAN GUI Creation.
            def func_subGuiHandle_setVLANobj():
                guiObj_portVLANLabelpt2["text"] = guiObj_portVLANInpBox.get(1.0, tkinter.END + "-1c")

            guiObj_portVLANLabelpt1["text"] = "Port VLAN: "
            guiObj_portVLANLabelpt1.grid(row = (var_guiSetRow + var_intMenuRowShift), column = 1, sticky = tkinter.E, padx = 10, pady = 10)
            debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleInterfaceDetails", "guiObj_portVLANLabelpt1 Loaded")

            netDevMatrix[3] = cmdAPI.class_commandAPI.func_getVLAN()
            guiObj_portVLANLabelpt2["text"] = str(netDevMatrix[3][var_portNum])
            guiObj_portVLANLabelpt2.grid(row = (var_guiSetRow + var_intMenuRowShift), column = 2, sticky = tkinter.W, padx = 10, pady = 10)
            debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleInterfaceDetails", "guiObj_portVLANLabelpt2 Loaded")

            guiObj_portVLANInpBox["height"] = 1
            guiObj_portVLANInpBox["width"] = 16
            guiObj_portVLANInpBox.grid(row = (var_guiSetRow + var_intMenuRowShift), column = 3, sticky = tkinter.E, padx = 10, pady = 10)
            debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleInterfaceDetails", "guiObj_portVLANInpBox Loaded")

            guiObj_portVLANSetButton["text"] = "Set VLAN"
            guiObj_portVLANSetButton["height"] = 3
            guiObj_portVLANSetButton["width"] = 16
            guiObj_portVLANSetButton["command"] = lambda: [cmdAPI.class_commandAPI.func_setVLAN(var_portNum, guiObj_portVLANInpBox.get(1.0, tkinter.END + "-1c")), func_subGuiHandle_setVLANobj()]
            guiObj_portVLANSetButton.grid(row = (var_guiSetRow + var_intMenuRowShift), column = 4, sticky = tkinter.E, padx = 10, pady = 10)
            debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleInterfaceDetails", "guiObj_portVLANSetButton Loaded")

            var_guiSetRow += 1


            #Duplex GUI Objects Creation.
            def func_subGuiHandle_setDuplexObj(str_typeDuplex):
                guiObj_portDuplexLabelpt2["text"] = str_typeDuplex

            guiObj_portDuplexLabelpt1["text"] = "Duplex: "
            guiObj_portDuplexLabelpt1.grid(row = (var_guiSetRow + var_intMenuRowShift), column = 1, sticky = tkinter.E, padx = 10, pady = 10)
            debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleInterfaceDetails", "guiObj_portDuplexLabelpt1 Loaded")

            netDevMatrix[4] = cmdAPI.class_commandAPI.func_getDuplexStats()
            guiObj_portDuplexLabelpt2["text"] = str(netDevMatrix[4][var_portNum])
            guiObj_portDuplexLabelpt2.grid(row = (var_guiSetRow + var_intMenuRowShift), column = 2, sticky = tkinter.W, padx = 10, pady = 10)
            debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleInterfaceDetails", "guiObj_portDuplexLabelpt2 Loaded")

            guiObj_portDuplexSetButtonAuto["text"] = "Set Duplex to Auto"
            guiObj_portDuplexSetButtonAuto["height"] = 3
            guiObj_portDuplexSetButtonAuto["width"] = 16
            guiObj_portDuplexSetButtonAuto["command"] = lambda: [cmdAPI.class_commandAPI.func_setDuplexStats(var_portNum, "Auto"), func_subGuiHandle_setDuplexObj("Auto")]
            guiObj_portDuplexSetButtonAuto.grid(row = (var_guiSetRow + var_intMenuRowShift), column = 3, sticky = tkinter.E, padx = 10, pady = 10)
            debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleInterfaceDetails", "gguiObj_portDuplexSetButtonAuto Loaded")

            guiObj_portDuplexSetButtonFull["text"] = "Set Duplex to Full"
            guiObj_portDuplexSetButtonFull["height"] = 3
            guiObj_portDuplexSetButtonFull["width"] = 16
            guiObj_portDuplexSetButtonFull["command"] = lambda: [cmdAPI.class_commandAPI.func_setDuplexStats(var_portNum, "Full"), func_subGuiHandle_setDuplexObj("Full")]
            guiObj_portDuplexSetButtonFull.grid(row = (var_guiSetRow + var_intMenuRowShift), column = 4, sticky = tkinter.E, padx = 10, pady = 10)
            debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleInterfaceDetails", "guiObj_portDuplexSetButtonFull Loaded")

            guiObj_portDuplexSetButtonHalf["text"] = "Set Duplex to Half"
            guiObj_portDuplexSetButtonHalf["height"] = 3
            guiObj_portDuplexSetButtonHalf["width"] = 16
            guiObj_portDuplexSetButtonHalf["command"] = lambda: [cmdAPI.class_commandAPI.func_setDuplexStats(var_portNum, "Half"), func_subGuiHandle_setDuplexObj("Half")]
            guiObj_portDuplexSetButtonHalf.grid(row = (var_guiSetRow + var_intMenuRowShift), column = 5, sticky = tkinter.E, padx = 10, pady = 10)
            debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleInterfaceDetails", "guiObj_portDuplexSetButtonHalf Loaded")

            var_guiSetRow += 1


            #Speed GUI Objects Creation.
            guiObj_portSpeedLabelpt1["text"] = "Port Speed: "
            guiObj_portSpeedLabelpt1.grid(row = (var_guiSetRow + var_intMenuRowShift), column = 1, sticky = tkinter.E, padx = 10, pady = 10)
            debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleInterfaceDetails", "guiObj_portSpeedLabelpt1 Loaded")

            netDevMatrix[5] = cmdAPI.class_commandAPI.func_getPortSpeed()
            guiObj_portSpeedLabelpt2["text"] = str((netDevMatrix[5])[var_portNum])
            guiObj_portSpeedLabelpt2.grid(row = (var_guiSetRow + var_intMenuRowShift), column = 2, sticky = tkinter.W, padx = 10, pady = 10)
            debug.class_debug.func_debugOut("class_guiHandle", "func_guiHandleInterfaceDetails", "guiObj_portSpeedLabelpt2 Loaded")

            var_guiSetRow += 1

        # Removes interface objects from screen.
        elif var_shIntDetails == True:
            for guiSet in matrix_interfaceDetailsGui:
                for guiObj in guiSet:
                    guiObj.grid_forget()

            var_shIntDetails = False


    #/ @func_guiHandleInterfaceMenu
    #/ Purpose: To handle the button interaction menu for how many interfaces the network device has.
    def func_guiHandleInterfaceMenu():
        global bool_menuBusy

        #/ If the object variables are not created yet, this creates them and stores them as a global variable
        #/ to be referenced if this parent method is ran again.
        for interface in netDevMatrix[1]:
            if ('guiObj_netdevIntButton' + interface) not in globals():
                #/ Variable created for each button that holds it's visibility True or False.
                #/ Should result in a variable in this format:  guiObj_netdevIntButtonFa0Vis
                #/ Creates global variable for GUI button.
                #/ Should result in a variable in this format:  guiObj_netdevIntButtonFa0
                globals()['guiObj_netdevIntButton' + str(interface)] = None


        #/ Tests if the visibility of the buttons is true or not and swiches the visibility.
        if bool_menuBusy == False:
            var_intMenuColShift = -1

            global var_netDevInterfaces
            var_netDevInterfaces = (cmdAPI.class_commandAPI.func_getInts())

            for interface in var_netDevInterfaces:
                #/ Shifts GUI down 1 row if the amount of interfaces on the device is 8 or greater.
                var_intMenuColShift += 1
                var_guiShiftNum = var_netDevInterfaces.index(interface) / 8
                if var_guiShiftNum >= 1 and var_intMenuColShift > 7:
                    global var_intMenuRowShift
                    var_intMenuRowShift += 1
                    var_intMenuColShift -= 8
                
                #/ Sets up interface button.
                globals()['guiObj_netdevIntButton' + str(interface)] = tkinter.Button(
                    guiHandle,
                    text = interface,
                    width = 16,
                    height = 3) #/ Sets button variable to register with tkinter GUI manager.

                #/ Sends variabless to another function when the button is clicked.
                #/ This temporarily just prints whatever port interface.
                globals()['guiObj_netdevIntButton' + str(interface)]["command"] = lambda int = var_netDevInterfaces.index(interface), intname = globals()['guiObj_netdevIntButton' + str(interface)]["text"]: class_guiHandle.func_guiHandleInterfaceDetails(False, int)

                globals()['guiObj_netdevIntButton' + str(interface)].grid(row = (1 + var_intMenuRowShift), column = (1 + var_intMenuColShift), sticky = tkinter.N, padx = 10, pady = 10) #/Sets position in window.

            #/ Updates show/hide network device button text and comamnd.
            guiObj_shInterfacesButton["text"] = "Hide Network Device Ports"
            guiObj_shInterfacesButton["command"] = lambda: class_guiHandle.func_guiHandleInterfaceMenu()

            bool_menuBusy = True

        elif bool_menuBusy == True:
            #global var_netDevInterfaces
            for interface in (var_netDevInterfaces):
                globals()['guiObj_netdevIntButton' + str(interface)].grid_forget()

            class_guiHandle.func_guiHandleInterfaceDetails(True, int)

            #/ Updates show/hide network device button text and comamnd.
            guiObj_shInterfacesButton["text"] = "Show Network Device Ports"
            #guiObj_shInterfacesButton["command"] = lambda: class_guiHandle.func_guiHandleInterfaceMenu(bool_menuBusy)

            var_intMenuRowShift = 0

            bool_menuBusy = False



    #/ @func_guiHandleMiscConfMenu
    #/ Purpose: 
    def func_guiHandleMiscConfMenu():
        # Grabs global variables.
        global bool_menuBusy

        # Tests if certain global variables have not been created and stored in memory, if not, creates them.
        if 'guiObj_ndHostnameButton' not in globals():
            # Hostname GUI 
            global guiObj_ndHostnameLabelpt1
            guiObj_ndHostnameLabelpt1 = tkinter.Label()
            global guiObj_ndHostnameLabelpt2
            guiObj_ndHostnameLabelpt2 = tkinter.Label()

            global guiObj_ndHostnameInpBox
            guiObj_ndHostnameInpBox = tkinter.Text()
            global guiObj_ndHostnameButton
            guiObj_ndHostnameButton = tkinter.Button()

            global arr_ndHostnameArr
            arr_ndHostnameArr = [guiObj_ndHostnameLabelpt1, guiObj_ndHostnameLabelpt2, guiObj_ndHostnameInpBox, guiObj_ndHostnameButton]


            global matrix_miscMenu
            matrix_miscMenu = [arr_ndHostnameArr]


        if bool_menuBusy == False:

            bool_menuBusy = True

            var_guiSetRow = 1
        
            # Hostname
            def func_subGuiHandle_setHostnameObj():
                guiObj_ndHostnameLabelpt2["text"] = cmdAPI.class_commandAPI.func_getHostname()

            guiObj_ndHostnameLabelpt1["text"] = "Device Hostname: "
            guiObj_ndHostnameLabelpt1["width"] = 16
            guiObj_ndHostnameLabelpt1["height"] = 3
            guiObj_ndHostnameLabelpt1.grid() 

            guiObj_ndHostnameLabelpt2["text"] = cmdAPI.class_commandAPI.func_getHostname()
            guiObj_ndHostnameLabelpt2["width"] = 16
            guiObj_ndHostnameLabelpt2["height"] = 3
            guiObj_ndHostnameLabelpt2.grid() 

            guiObj_ndHostnameInpBox["width"] = 16
            guiObj_ndHostnameInpBox["height"] = 1
            guiObj_ndHostnameInpBox.grid() 

            guiObj_ndHostnameButton["text"] = "Set Hostname"
            guiObj_ndHostnameButton["width"] = 16
            guiObj_ndHostnameButton["height"] = 3
            guiObj_ndHostnameButton["command"] = lambda: [cmdAPI.class_commandAPI.func_setHostname(guiObj_ndHostnameInpBox.get(1.0, tkinter.END + "-1c")), func_subGuiHandle_setHostnameObj()]
            guiObj_ndHostnameButton.grid()

            for guiArr in matrix_miscMenu:
                for guiObj in guiArr:
                    print(arr_ndHostnameArr.index(guiObj))
                    guiObj.grid(row = var_guiSetRow, column = (1 + arr_ndHostnameArr.index(guiObj)), sticky = tkinter.E, padx = 10, pady = 10)

            var_guiSetRow += 1

            guiObj_shOtherConfigButton["text"] = "Hide Misc. Config Menu"


        elif bool_menuBusy == True:
            for guiArr in matrix_miscMenu:
                for guiObj in guiArr:
                    guiObj.grid_forget()

            guiObj_shOtherConfigButton["text"] = "Show Misc. Config Menu"

            bool_menuBusy = False

            





    #/ @func_guiHandlePrgMenu
    #/ Purpose: 
    def func_guiHandlePrgMenu():
        global guiObj_exitButton
        global guiObj_shInterfacesButton
        global guiObj_shConTypeButton
        global guiObj_shConfigLoadButton
        global guiObj_shOtherConfigButton

        # Exit Button
        guiObj_exitButton = tkinter.Button(guiHandle)
        guiObj_exitButton["text"] = "EXIT"
        guiObj_exitButton["width"] = 20
        guiObj_exitButton["height"] = 3
        guiObj_exitButton["command"] = lambda: class_guiHandle.func_guiHandleExit()
        guiObj_exitButton.grid(row = 0, column = 0, sticky = tkinter.W, padx = 10, pady = 10)

        # Show & Hide Config Load Button
        guiObj_shConfigLoadButton = tkinter.Button(guiHandle)
        guiObj_shConfigLoadButton["text"] = "Show Config Loader"
        guiObj_shConfigLoadButton["width"] = 30
        guiObj_shConfigLoadButton["height"] = 3
        guiObj_shConfigLoadButton["command"] = lambda: class_guiHandle.func_guiHandleNDconfigManage()
        guiObj_shConfigLoadButton.grid(row = 1, column = 0, sticky = tkinter.S, padx = 10, pady = 10)


        # Show & Hide Interfaces Button
        guiObj_shInterfacesButton = tkinter.Button(guiHandle)
        guiObj_shInterfacesButton["text"] = "Show Network Device Port Menu"
        guiObj_shInterfacesButton["width"] = 30
        guiObj_shInterfacesButton["height"] = 3
        guiObj_shInterfacesButton["command"] = lambda: [class_guiHandle.func_guiHandleInterfaceMenu(), class_guiHandle.func_guiHandleInterfaceDetails(True, 0)] #For whatever reason this doesn't work without lambda.
        guiObj_shInterfacesButton.grid(row = 2, column = 0, sticky = tkinter.S, padx = 10, pady = 10)

        # Show & Hide Interfaces Button
        guiObj_shOtherConfigButton = tkinter.Button(guiHandle)
        guiObj_shOtherConfigButton["text"] = "Show Misc. Config Menu"
        guiObj_shOtherConfigButton["width"] = 30
        guiObj_shOtherConfigButton["height"] = 3
        guiObj_shOtherConfigButton["command"] = lambda: class_guiHandle.func_guiHandleMiscConfMenu() #For whatever reason this doesn't work without lambda.
        guiObj_shOtherConfigButton.grid(row = 3, column = 0, sticky = tkinter.S, padx = 10, pady = 10)     



    #/ @func_guiHandleMain
    #/ Purpose: Main function for handling how to GUI is shown.
    def func_guiHandleMain():

        # Loading .json config file.
        #configFile = json.load('settings.json')

        # Defining title of program window.
        #guiHandle.title(configFile['guiSettings'][0])
        guiHandle.title(debug.func_loadConfig()["projectDetails"]["projectName"])

        # Handles window size accoring to config.json.
        guiHandle.geometry(debug.func_loadConfig()["guiSettings"]["prgWidth"] + 'x' + debug.func_loadConfig()["guiSettings"]["prgHeight"] + '+400+200')

        # Sets 
        guiHandle.resizable(0, 0)
        guiHandle.columnconfigure(20, weight = 200)
        guiHandle.rowconfigure(20, weight = 200)

        # Calling method that will load the GUI objects.
        class_guiHandle.func_guiHandlePrgMenu()

        # Starts GUI and loops it's existence.
        guiHandle.mainloop()


#///
#/ End of Code