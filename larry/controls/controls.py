import pyautogui
import time

import logging

logger = logging.getLogger(__name__)


def press_key(keyval=None):
    """
        Presses the given key and releases the other keys in 'wasd'
    """

    stop_press = [ 'a', 'd']
    if keyval:
        stop_press.remove(keyval)
        pyautogui.keyDown(keyval)

    for i in stop_press:
        pyautogui.keyUp(i)

    if keyval:
        pyautogui.keyUp(keyval)



def cont_straight():
    press_key('w')

def cont_left():
    press_key('a')

def cont_right():
    press_key('d')

def cont_slow():
    press_key('s')

def stop_all():
    press_key()

def control_test():
    """
        Give countdown and run the test
    """
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    FORWARD = 'w'
    LEFT = 'a'
    RIGHT = 'd'
    STOP = 's'

    press_key(FORWARD)
    time.sleep(0.5)
    press_key(LEFT)
    time.sleep(0.5)
    press_key(RIGHT)
    time.sleep(0.5)
    press_key(STOP)
    time.sleep(0.5)
    press_key()



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    control_test()
