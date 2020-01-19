import numpy as np
import mss
import cv2
import time
import threading
import logging
import os
from datetime import datetime
from larry.getkeys.getkeys import key_check, keys_to_output, getKeys

logger = logging.getLogger(__name__)


def initialize_data(file_name):
    """
        Just loads the data if it exists
    """
    if os.path.isfile(file_name):
        print('File exists, loading previous data!')
        starting_data = list(np.load(file_name, allow_pickle=True))
    else:
        print('File does not exist, starting fresh!')
        starting_data = []
    return starting_data



def main():

    th = threading.Thread(target=getKeys)
    th.start()

    now = datetime.now()
    prefix = now.strftime("%Y-%m-%d-%H%M%S")
    file_name = f'./training_data/{prefix}-training_data.npy'
    training_data = initialize_data(file_name)
    fps_list = []
    last_print = time.time()

    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    while True:
        with mss.mss() as sct:
            last_time = time.time()
            last_frame = time.time()
            # 1024x748 windowed mode
            monitor = {"top": 40, "left": 0, "width": 1024, "height": 748}


            screen = np.array(sct.grab(monitor))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            # resize to something a bit more acceptable for a CNN
            screen = cv2.resize(screen, (80, 60))

            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen, output])

            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

            fps_list.append(1 / (time.time() - last_time))
            if time.time() - last_print > 2:
                # print(f"fps: {int(np.average(fps_list))}")
                last_print = time.time()
                fps_list = []

            target_fps = 60
            while (time.time() - last_frame) < 1/target_fps:
                pass

            if len(training_data) % 500 == 0:
                print(len(training_data))
                np.save(file_name, training_data)


if __name__ == "__main__":
    main()
