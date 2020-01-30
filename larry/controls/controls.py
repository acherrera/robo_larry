import pyautogui
import time
import logging
from itertools import compress

logger = logging.getLogger(__name__)


def press_key(keyval=None):
    """
        Presses the given key and releases the other keys in 'wasd'
    """

    stop_press = ['w', 'a', 'd', 's']
    if keyval:
        stop_press.remove(keyval)
        pyautogui.keyDown(keyval)

    for i in stop_press:
        pyautogui.keyUp(i)

    if keyval:
        pyautogui.keyUp(keyval)


def array_press(key_array: dict):
    """
        Presses the keys based on the input
        [0, 0, 0, 0] & ['w', 'a', 's', 'd'] = all keys released
        [1, 0, 0, 1] & ['w', 'a', 's', 'd'] = 'w', 'd' pressed, others released

    """
    base_array = ['w', 'a' , 's', 'd']
    to_press = list(compress(base_array, key_array))

    for key in to_press:
        pyautogui.keyDown(key)
        base_array.remove(key)

    # print(f'press: {to_press} \t\t release: {base_array}')

    for key in base_array:
        pyautogui.keyUp(key)


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
        Run test
    """

    array_press([0,0,0,0])
    array_press([1,0,0,0])
    array_press([1,1,0,0])
    array_press([1,0,0,1])
    array_press([0,0,0,0])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    control_test()
