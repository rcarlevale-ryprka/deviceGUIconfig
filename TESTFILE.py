#/ Imports
import tkinter


#/ Create GUI Handle for tkinter.
guiHandle = tkinter.Tk()


#/ Array of numbers.
array = [0, 1, 2, 3, 4, 5, 6, 7]


#/ Main class.
class MainClass:
    #/ Prints information from button press.
    def func_printOut(string):
        print(string)

    #Creates array of buttons.
    def func_buttonMenu():
        if ('guiArr_buttonNumArray') not in globals():
            global guiArr_buttonNumArray

        #/ Create GUI button for each item in array.
        for item in array:
            #/ Creates a variable in the format of 'guiObj_buttonNum#' if it does not exist in global.
            if ('guiObj_buttonNum' + str(item)) not in globals():
                globals()['guiObj_buttonNum' + str(item)] = tkinter.Button(guiHandle)

            #/ Sets up button details and places it on the GUI tkinter grid.
            globals()['guiObj_buttonNum' + str(item)]["text"] = "Button Number " + str(item)
            globals()['guiObj_buttonNum' + str(item)]["width"] = 16
            globals()['guiObj_buttonNum' + str(item)]["height"] = 3
            globals()['guiObj_buttonNum' + str(item)]["command"] = lambda: MainClass.func_printOut(item)
            globals()['guiObj_buttonNum' + str(item)].grid(row = 1, column = (0 + item), sticky = tkinter.S, padx = 10, pady = 10)


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