import pyautogui
import time

import logging

logger = logging.getLogger(__name__)



def press_key(key_list, sec=None):
    """
        Press keys in "key_list" for a given number of seconds or once if no seconds given
        Args:
            key_list: list of keys to pressed at once
            sec: how many seconds to press keys for
    """
    if sec:
        logger.debug('{key_list) for {sec} seconds')
        for keyval in key_list:
            if keyval in ['w', 's']:
                pyautogui.press(keyval) # Shift forward if not already

            pyautogui.keyDown(keyval)

        time.sleep(sec)
        for keyval in key_list:
            pyautogui.keyUp(keyval)
    else:
        for keyval in key_list:
            pyautogui.press(keyval)


def control_test():
    """
        Give countdown and run the test
    """
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    FORWARD = ['w']
    LEFT = ['a']
    RIGHT = ['d']
    STOP = ['s']

    press_key(FORWARD)
    press_key(LEFT)
    press_key(RIGHT)
    press_key(STOP)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    control_test()
