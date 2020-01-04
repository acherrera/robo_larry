import time
import logging

import numpy as np
import mss
import cv2

logger = logging.getLogger(__name__)

def roi(img, vertices):
    #blank mask:
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_image(image):
    """
        Convert to grayscale and run edge detection
    """
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(
        processed_image, threshold1=100, threshold2=300)
    # TODO edit this!
    vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500],
                         ], np.int32)
    processed_image = roi(processed_image, [vertices])
    return processed_image



def main():
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

                # Conver the image and show
                img = process_image(img)
                cv2.imshow("OpenCV/Numpy normal", img)


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
   main()
