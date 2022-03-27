#/ @conAPI.py
#/ Purpose: API for refering to how a switch device is connected.

#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

import serial
import time


#/
#/ @Classes
#/ Purpose: Define classes in this file.

#/ @class_name_filler
#/ Purpose: Filler purpose. 

class class_connectAPI:
    #/ @func_connectionPrintOut
    #/ Purpose: Write to console & debugging function what the output of each command is in a connection with a network device.
    def func_connectionPrintOut(var_string):
        print(serial.read(str(var_string)).decode("utf-8"), end = "")



    #/ @func_serialConInstance
    #/ Purpose: 
    def func_serialConInstance(arr_cmdInp):
        #/ Initializes the serial connection.
        with serial.Serial("COM12", timeout = 9600) as ser:
            #/ Establishes serial connection in console.
            print(f"Connecting to {ser.name}...")

            for command in arr_cmdInp:
                ser.write(str(command).encode("utf-8"))
                ser.write('\r'.encode("utf-8"))
                time.sleep(0.5)

            ser.close()