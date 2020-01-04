import time
import logging

import numpy as np
import mss
import cv2

logger = logging.getLogger(__name__)



def screen_record():
    while True:
        with mss.mss() as sct:
            # Part of the screen to capture
            monitor = {"top": 40, "left": 0, "width": 1024, "height": 768}

            fps_list = []
            last_print = time.time()
            while "Screen capturing":
                last_time = time.time()

                # Get raw pixels from the screen, save it to a Numpy array
                img = np.array(sct.grab(monitor))

                # Display the picture
                cv2.imshow("OpenCV/Numpy normal", img)

                # Display the picture in grayscale
                # cv2.imshow('OpenCV/Numpy grayscale',
                #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

                fps_list.append(1 / (time.time() - last_time))

                if (time.time() - last_print > 2):
                    print(f"fps: {int(np.average(fps_list))}")
                    last_print = time.time()
                    fps_list = []

                # Press "q" to quit - does not work as intended
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
                    break


if __name__ == "__main__":
   screen_record()
