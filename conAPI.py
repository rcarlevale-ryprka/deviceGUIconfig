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
        ... 


    #/ @func_serialConInstance
    #/ Purpose: Establish a connection through serial to a network device. Allow input and output of commands.
    def func_serialConInstance(arr_cmdInp):
        # Initializes the serial connection and connects to the serial device based off of the config file.
        with serial.Serial(debug.func_loadConfig()["conSettings"]["serialComNum"], timeout = debug.func_loadConfig()["conSettings"]["serialComSpeed"]) as ser:
            # Establishes serial connection in console.
            print(f"Connecting to {ser.name}...")

            var_serialReturn = ""

            # A loop that sends each command in an array of commands that have been sent.
            for command in arr_cmdInp:
                ser.write(str(command).encode("utf-8"))
                ser.write('\r'.encode("utf-8"))
                #arr_serialReturn.append(str(ser.read(ser.inWaiting()).decode("utf-8")))
                var_serialReturn += (str(ser.read(ser.inWaiting()).decode("utf-8")))
                #str(ser.read(ser.inWaiting()).decode("utf-8"), end = "")
                time.sleep(3)

            ser.close()

        return var_serialReturn


    #/ @func_sshConInstance()
    #/ Purpose: Establish a connection with an ssh instance to a network device.
    def func_sshConInstance(arr_cmdInp):
        # A loop that sends each command in an array of commands that have been sent.
        for command in arr_cmdInp:
            ... #FILLER REMOVE WHEN WRITE CODE


    #/ @func_sshConInstance()
    #/ Purpose: Establish a connection with an ssh instance to a network device.
    def func_telnetConInstance(arr_cmdInp):
        # A loop that sends each command in an array of commands that have been sent.
        for command in arr_cmdInp:
            ... #FILLER REMOVE WHEN WRITE CODE