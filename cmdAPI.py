#/ @cmdAPI.py
#/ Purpose: API that reads and sends commands to network devices.

#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

import conAPI


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
        

        arr_intList = []

        for command in arr_runningConf:
            if str(command).__contains__("/"):
                var_cmdCut = command.replace("interface ", "")
                arr_intList.append(str(var_cmdCut))
        
        return arr_intList



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
    def func_getVLAN():
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

        for command in arr_runningConf:
            if str(command).__contains__("/") or str(command).__contains__("switchport access vlan"):
                var_cmdCut = command.replace("interface ", "")
                arr_intVlanList.append(str(var_cmdCut))

        print(arr_intVlanList)

        


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
        class_commandAPI.func_getVLAN()

    


#/

testBool = True
if testBool == True:
    class_commandAPI.func_testMethod()