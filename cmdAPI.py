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
    
 

    #/ Sets a port's VLAN.
    def func_setVLAN():
        ... #/ Filler. Remove when you write code.

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


    def func_getVLAN():
        arr_cmdInp = [
            '\r',
            'en',
            'show vlan',
            'end'
        ]

        print(conAPI.class_connectAPI.func_serialConInstance(arr_cmdInp))


    def func_setVLAN(var_hostnameConf):
        arr_cmdInp = [
            '\r',
            'en',
            'conf t',
            ('hostname ' + var_hostnameConf),
            'end',
            'end'
        ]

        conAPI.class_connectAPI.func_serialConInstance(arr_cmdInp)

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

testBool = False
if testBool == True:
    class_commandAPI.func_testMethod()