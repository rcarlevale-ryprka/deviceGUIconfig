#/
#/ @Imports
#/ Purpose: Define classes in this file.

from logging import root
import tftpy


#/
#/ @Classes
#/ Purpose: Define classes in this file.

class class_tftpInstance:
    def func_tftp():
        tftpSvr = tftpy.TftpServer("C:/TFTP/")
        tftpSvr.listen('0.0.0.0', 69)

class_tftpInstance.func_tftp()