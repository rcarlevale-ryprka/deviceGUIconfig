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
    def func_parseData(var_parseString):
        arr_parseString = []
        arr_parseString = var_parseString.split("!")
        

        for command in arr_parseString:
            arr_parseString[arr_parseString.index(command)] = command.replace('\r\n','')

        #print(arr_parseString)
        return arr_parseString
        
    
 


    #/ @func_getInts
    #/ Purpose: Grabs how many interfaces are on the given device.
    def func_getInts():
        arr_cmdInp = [
            '\r',
            'en',
            'terminal length 0',
            'show running-config',
            'end'
        ]

        var_rawConfigString = conAPI.class_connectAPI.func_serialConInstance(arr_cmdInp)
        arr_runningConf = class_commandAPI.func_parseData(var_rawConfigString)
        
        arr_intListRaw = []
        arr_intList = []

        for cmdItem in arr_runningConf:
            if str(cmdItem).__contains__("0/") and not str(cmdItem).__contains__(":"):
                var_cmdCut = cmdItem.replace("interface ", "")
                arr_intListRaw.append(str(var_cmdCut))
                if var_cmdCut.__contains__(" "):
                    var_cmdCut = var_cmdCut[0:(var_cmdCut.index(" "))]
                arr_intList.append(str(var_cmdCut))
        
        return [arr_intListRaw, arr_intList]



    #/ @func_setHostname
    #/ Sets a network devices hostname.
    def func_setHostname(var_hostnameConf):
        arr_cmdInp = [
            '\r',
            'en',
            'conf t',
            ('hostname ' + var_hostnameConf),
            'exit',
            'exit '
        ]

        conAPI.class_connectAPI.func_serialConInstance(arr_cmdInp)


    #/ @func_getVLAN
    #/ Gets VLAN information.
    def func_getVLAN(var_intName):
        arr_cmdInp = [
            '\r',
            'en',
            'terminal length 0',
            'show running-config',
            'end'
        ]

        var_rawConfigString = conAPI.class_connectAPI.func_serialConInstance(arr_cmdInp)
        arr_runningConf = class_commandAPI.func_parseData(var_rawConfigString)

        arr_intVlanList = []

        for cmdItem in arr_runningConf:
            if cmdItem.__contains__(var_intName) and cmdItem.__contains__("vlan"):
                print("if")
                if cmdItem[cmdItem.index("vlan"):(cmdItem.index("vlan") + 10)]:
                    var_vlanNum = (cmdItem[cmdItem.index("vlan"):(cmdItem.index("vlan") + 10)].split(" "))[1]
                    arr_intVlanList.append(var_vlanNum)
            elif cmdItem.__contains__(var_intName[0:(len(var_intName) - 3)]):
                print("elif")
                arr_intVlanList.append("1")
                    
        
        print(arr_intVlanList)
        return arr_intVlanList

        


    #/ @func_setVLAN
    #/ Sets VLAN on cisco interface.
    def func_setVLAN(var_intNum, var_vlanNum):
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


    #/ @func_testMethod
    #/ Purpose: Allows this file to be run and tested without other necessities.
    def func_testMethod():
        #class_commandAPI.func_setHostname(input("Switch Hostname: "))
        #class_commandAPI.func_removeVLAN(input("INT: "), input("VLAN: "))
        class_commandAPI.func_getVLAN("FastEthernet0/23")

    


#/

testBool = False
if testBool == True:
    class_commandAPI.func_testMethod()