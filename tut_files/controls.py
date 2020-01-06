import pyautogui
import time


def presss_multi(key_list, sec):
    start_t = time.time()

    while (time.time() - start_t < sec):
        for keyval in key_list:
            pyautogui.press(keyval)

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)


asdf = ['a', 'd']
presss_multi(asdf, 3)



# pyautogui.keyDown('s')
# time.sleep(3)
# pyautogui.keyUp('s')

# pyautogui.keyDown('s')
# time.sleep(2)
# pyautogui.keyUp('s')
# 
# pyautogui.keyDown('w')
# time.sleep(3)
# pyautogui.keyUp('w')

