"""
Rewriting this machine learning model for Windows 
"""

import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui


def key_test():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    print('down')
    pyautogui.keyDown('w')
    print('up')
    pyautogui.keyUp('w')



def screen_record():
    while(True):

        last_time = time.time()
        monitor =  ( 0, 40, 1024, 748)
        printscreen = np.array(ImageGrab.grab(bbox=monitor))

        print(f'Loop took {time.time()-last_time} seconds')
        cv2.imshow('window', 
                    cv2.cvtColor(printscreen,
                    cv2.COLOR_BGR2GRAY))
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
            
if __name__ == "__main__":
    key_test()
