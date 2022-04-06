#/ @cmdAPI.py
#/ Purpose: API that reads and sends commands to network devices.

#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

from cProfile import run
import cmd
from numpy import var
import conAPI
import time


#/
#/ @Classes
#/ Purpose: Define classes in this file.

#/ @class_name_filler
#/ Purpose: Filler purpose. 

class class_commandAPI:





    #/ @func_parseData
    #/ Purpose: 
    def func_parseData(var_parseString):
        arr_parseString = var_parseString.splitlines()

        var_arrStartNum = 0
        arr_intDetailsList = []

        for cmdLine in arr_parseString:
            if cmdLine.__contains__("Port"):
                var_arrStartNum = arr_parseString.index(cmdLine) + 1
                break
            else:
                arr_parseString.pop(arr_parseString.index(cmdLine))

        
        for cmdLine in arr_parseString[var_arrStartNum:len(arr_parseString)]:
            while '  ' in cmdLine:
                cmdLine = cmdLine.replace('  ', ' ')

            arr_cmdLine = cmdLine.split(' ')

            arr_intDetailsList += [arr_cmdLine]

        arr_intDetailsList.pop(len(arr_intDetailsList) - 1)

        return arr_intDetailsList


    #/ @func_getIntStatus
    #/ Purpose: 
    def func_getIntDetails():
        arr_cmdInp = [
            '\r',
            'en',
            'terminal length 0',
            'show int status',
            'end'
        ]

        var_rawConfigString = conAPI.class_connectAPI.func_serialConInstance(arr_cmdInp)
        arr_intStatDetails = class_commandAPI.func_parseData(var_rawConfigString)

        #print("=============================")
        print(arr_intStatDetails)
        print(len(arr_intStatDetails))
        #print("=============================")
        return arr_intStatDetails
        
    
 
    ###/
    ###/ SECTION
    ###/ TFTP SERVER
    ###/




    ###/
    ###/ SECTION
    ###/ INTERFACES
    ###/

    #/ @func_getInts
    #/ Purpose: Grabs how many interfaces are on the given device.
    def func_getInts():
        arr_intStatDetails = class_commandAPI.func_getIntDetails()
        arr_intNames = []

        for arr_singleIntDetails in arr_intStatDetails:
            arr_intNames.append(arr_singleIntDetails[0])
        
        return arr_intNames



    ###/
    ###/ SECTION
    ###/ CONNECTION STATUS
    ###/

    #/ @func_getHostname
    #/ Sets a network devices hostname.
    def func_getHostname():
        arr_cmdInp = [
            '\r',
            'en'
        ]

        arr_cmdDetials =  conAPI.class_connectAPI.func_serialConInstance(arr_cmdInp)

        return arr_cmdDetials[0:(len(arr_cmdDetials) - 1)]


    #/ @func_setHostname
    #/ Sets a network devices hostname.
    def func_setHostname(var_hostnameConf):
        arr_cmdInp = [
            '\r',
            'en',
            'conf t',
            ('hostname ' + var_hostnameConf),
            'exit',
            'exit'
        ]

        conAPI.class_connectAPI.func_serialConInstance(arr_cmdInp)


    ###/
    ###/ SECTION
    ###/ CONNECTION STATUS
    ###/

    #/ @func_
    #/ Purpose: 
    def func_getConStatus():
        arr_intStatDetails = class_commandAPI.func_getIntDetails()
        arr_conStatus = []

        for arr_singleIntDetails in arr_intStatDetails:
            arr_conStatus.append(arr_singleIntDetails[1])
        
        return arr_conStatus


    ###/
    ###/ SECTION
    ###/ VLAN FUNCTIONS
    ###/

    #/ @func_getVLAN
    #/ Gets VLAN information.
    def func_getVLAN():
        arr_intStatDetails = class_commandAPI.func_getIntDetails()
        arr_vlanNums = []

        for arr_singleIntDetails in arr_intStatDetails:
            arr_vlanNums.append(arr_singleIntDetails[2])
        
        return arr_vlanNums


    #/ @func_setVLAN
    #/ Sets VLAN on cisco interface.
    def func_setVLAN(var_intNum, var_vlanNum):
        print(var_intNum, var_vlanNum)

        var_intRef = class_commandAPI.func_getInts()[var_intNum]

        arr_cmdInp = [
            '\r',
            'en',
            'conf t',
            ('int ' + var_intRef),
            'switchport mode access',
            ('switchport access vlan ' + var_vlanNum),
            'end',
            'end'
        ]
            
        conAPI.class_connectAPI.func_serialConInstance(arr_cmdInp)


    #/ @func_removeVLAN
    #/ Removes VLAN from interface.
    def func_removeVLAN(var_intNum, var_vlanNum):
        var_intNum = "GigabitEthernet1/0/" + var_intNum

        arr_cmdInp = [
            '\r',
            'en',
            'conf t',
            ('int ' + var_intNum),
            'switchport mode access',
            ('switchport access vlan ' + var_vlanNum),
            'end',
            'end'
        ]

        conAPI.class_connectAPI.func_serialConInstance(arr_cmdInp)



    ###/
    ###/ SECTION
    ###/ DUPLEX
    ###/

    #/ @func_
    #/ Purpose: 
    def func_getDuplexStats():
        arr_intStatDetails = class_commandAPI.func_getIntDetails()
        arr_duplexStats = []

        for arr_singleIntDetails in arr_intStatDetails:
            arr_duplexStats.append(arr_singleIntDetails[3])
        
        return arr_duplexStats




    ###/
    ###/ SECTION
    ###/ SPEED
    ###/

    #/ @func_
    #/ Purpose: 
    def func_getPortSpeed():
        arr_intStatDetails = class_commandAPI.func_getIntDetails()
        arr_portSpeed = []

        for arr_singleIntDetails in arr_intStatDetails:
            arr_portSpeed.append(arr_singleIntDetails[4])
        
        return arr_portSpeed









    #/ @func_testMethod
    #/ Purpose: Allows this file to be run and tested without other necessities.
    def func_testMethod():
        class_commandAPI.func_getHostname()

    


#/

testBool = False
if testBool == True:
    class_commandAPI.func_testMethod()