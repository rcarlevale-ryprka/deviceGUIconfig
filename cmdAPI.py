#/ @cmdAPI.py
#/ Purpose: API that reads and sends commands to network devices.

#/
#/ @Imports
#/ Purpose: Used to import files to use for this main method.

import conAPI
import debug


#/
#/ @Classes
#/ Purpose: Define classes in this file.

#/ @class_name_filler
#/ Purpose: Filler purpose. 

class class_commandAPI:





    #/ @func_parseData
    #/ Purpose: 

    def func_altParseData(var_parseString):
        arr_intDetailsList = []
        arr_currInt = []

        print(var_parseString.splitlines())
        print("=============")


        for line in var_parseString.splitlines():

            if line.__contains__("net0/"):
                arr_tempParse = line.split(" ")
                arr_currInt = [arr_tempParse[0]]
                print("TEST1")

            arr_intDetailsList.append(arr_currInt)    

        print("============")
        print(arr_intDetailsList)

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

        return arr_intStatDetails
        
    
 
    ###/
    ###/ SECTION
    ###/ DOWN/UP CONFIG
    ###/

    #/ @func_
    #/ Purpose: 
    def func_downConfFile():
        arr_cmdInp = [
            '\r',
            'en',
            'terminal length 0',
            'show running-config',
            'exit'
        ]

        arr_downConf = conAPI.class_connectAPI.func_serialConInstance(arr_cmdInp)
        var_confFilePath = debug.func_loadConfig()["fileSettings"]["filePath"]

        try:
            file_configFile = open((var_confFilePath + '\\NDconfig.txt'), 'r+')
            file_configFile.close()
        except:
            debug.class_debug.func_debugOut("class_commandAPI", "func_downConfFile", "Creating network device configuration file.")
            file_configFile = open((var_confFilePath + '\\NDconfig.txt'), 'a')
            file_configFile.close()

        file_configFile = open((var_confFilePath + '\\NDconfig.txt'), 'w+')

        arr_downConf = arr_downConf.splitlines()[7:(len(arr_downConf.splitlines()) - 1)]

        for cmdItem in arr_downConf:
            file_configFile.write(cmdItem + "\r")

        file_configFile.close()


    #/ @func_
    #/ Purpose:
    def func_upConfFile(arr_fileContents):
        print(arr_fileContents)

        arr_cmdInp = [
            '\r',
            'en',
            'conf t'
        ]

        for cmdItem in arr_fileContents:
            arr_cmdInp.append(cmdItem)

        arr_cmdInp.append('exit')

        conAPI.class_connectAPI.func_serialConInstance(arr_cmdInp)



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
            '\r'
        ]

        arr_cmdDetials =  conAPI.class_connectAPI.func_serialConInstance(arr_cmdInp)
        var_strCmd = arr_cmdDetials.splitlines()[1]
        var_strCmd = (var_strCmd.replace('>', '')).replace('#', '')

        print(var_strCmd)

        return var_strCmd


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

    def func_setDuplexStats(var_intNum, str_duplexType):
        if str_duplexType == "Auto":
            str_duplexType = "auto"
        elif str_duplexType == "Full":
            str_duplexType = "full"
        elif str_duplexType == "Half":
            str_duplexType = "half"

        var_intRef = class_commandAPI.func_getInts()[var_intNum]

        arr_cmdInp = [
            '\r',
            'en',
            'conf t',
            ('int ' + var_intRef),
            ('duplex' + str_duplexType),
            'end',
            'end'
        ]





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


    def func_setPortSpeed():
        ...


    #/ @func_testMethod
    #/ Purpose: Allows this file to be run and tested without other necessities.
    def func_testMethod():
        class_commandAPI.func_getHostname()

    


#/

testBool = False
if testBool == True:
    class_commandAPI.func_testMethod()