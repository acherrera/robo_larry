import numpy as np
import mss
import cv2
import time
from larry.getkeys.getkeys import key_check
import os


def main():

    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    while True:
        # 1024x748 windowed mode
        monitor = {"top": 40, "left": 0, "width": 1024, "height": 748}
        img = np.array(sct.grab(monitor))aaa
        last_time = time.time()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        # resize to something a bit more acceptable for a CNN
        screen = cv2.resize(screen, (80, 60))

        # TODO - need to 
        keys = key_check()

        output = keys_to_output(keys)
        training_data.append([screen, output])

        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

        if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_name, training_data)
