import win32api, win32con, sys
from time import sleep

# while (True):  # run forever
#     win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1, 0, 0, 0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 0, 0, 0)
#     sleep(3)

import pyautogui#, sys
while (True):  # run forever
    pyautogui.moveRel(1, 1)     # move the mouse
    pyautogui.moveRel(-1, -1 )    # move it back!
    sleep(3)  # wait then start jiggling again
