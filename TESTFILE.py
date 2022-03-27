#/ Imports
from asyncio.windows_events import NULL
from itertools import count
import tkinter


#/ Create GUI Handle for tkinter.
guiHandle = tkinter.Tk()


#/ Array of numbers.
array = [0, 1, 2, 3, 4, 5, 6, 7]


#/ Main class.
class MainClass:
    #/ Prints information from button press.
    def func_printOut(string):
        str(string)
        print(string)

    #Creates array of buttons.
    def func_buttonMenu():
        global arr_buttonNum
        arr_buttonNum = []

        
        for item in array:
            arr_buttonNum.append(tkinter.Button(
                guiHandle,
                text = str(item),
                width = 16,
                height = 3,
            ))

            arr_buttonNum[item].grid(row = 1, column = (0 + item), sticky = tkinter.W, padx = 10, pady = 10)

        for 
            

            

            




    #/ Main GUI Handle.
    def func_mainHandle():
        #/ GUI Window Management.
        guiHandle.title("TEST")
        guiHandle.geometry('1920x1080+400+200')
        guiHandle.resizable(0, 0)
        guiHandle.columnconfigure(20, weight = 200)
        guiHandle.rowconfigure(20, weight = 200)

        #/ Exit button.
        global guiObj_exitButton
        guiObj_exitButton = tkinter.Button(guiHandle)
        guiObj_exitButton["text"] = "EXIT"
        guiObj_exitButton["width"] = 16
        guiObj_exitButton["height"] = 3
        guiObj_exitButton["command"] = guiHandle.destroy
        guiObj_exitButton.grid(row = 0, column = 0, sticky = tkinter.W, padx = 10, pady = 10)

        #/ Call to other methods to load other GUI elements.
        MainClass.func_buttonMenu()

        #/ Tkinter Mainloop
        guiHandle.mainloop()


#/ Calling main method within the main class to start program.
MainClass.func_mainHandle()