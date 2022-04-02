#/ @conAPI.py
#/ Purpose: API for refering to how a switch device is connected.

#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

import serial
import time

import debug


#/
#/ @Classes
#/ Purpose: Define classes in this file.

#/ @class_name_filler
#/ Purpose: Filler purpose. 

class class_connectAPI:

    #/ @func_serialConPrintOut
    #/ Purpose: Write to console & debugging function what the output of each command is in a connection with a network device if the connection is based through Serial.
    def func_serialConPrintOut(var_string):
        print(serial.read(str(var_string)).decode("utf-8"), end = "")


    #/ @func_serialConInstance
    #/ Purpose: Establish a connection through serial to a network device. Allow input and output of commands.
    def func_serialConInstance(arr_cmdInp):
        #/ Initializes the serial connection and connects to the serial device based off of the config file.
        with serial.Serial(debug.func_loadConfig()["conSettings"]["serialConNum"], timeout = debug.func_loadConfig()["conSettings"]["serialComSpeed"]) as ser:
            #/ Establishes serial connection in console.
            print(f"Connecting to {ser.name}...")

            for command in arr_cmdInp:
                ser.write(str(command).encode("utf-8"))
                ser.write('\r'.encode("utf-8"))
                time.sleep(0.5)

            ser.close()


    #/ @func_sshConInstance()
    #/ Purpose: Establish a connection with an ssh instance to a network device.
    def func_sshConInstance():
        ... #FILLER REMOVE WHEN WRITE CODE


    #/ @func_sshConInstance()
    #/ Purpose: Establish a connection with an ssh instance to a network device.
    def func_telnetConInstance():
        ... #FILLER REMOVE WHEN WRITE CODE