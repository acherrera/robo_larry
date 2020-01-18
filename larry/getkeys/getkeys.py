"""
    Script showing how to get keypresses for every key pressed
"""

# Close...
# import pyxhook
# 
# def OnKeyPress(event):
#     if event.Ascii == 32:
#         exit(0)
#     return event.Key
# 
# hm = pyxhook.HookManager()
# hm.KeyDown = OnKeyPress
# hm.HookKeyboard()
# hm.start()


import evdev
device = evdev.InputDevice('/dev/input/event1')
print(device)
