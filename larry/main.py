import time
import logging
import numpy as np
import mss
import cv2

from threading import Thread

logger = logging.getLogger(__name__)

def roi(img, vertices):
    #blank mask:
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked

def draw_lines(img,lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255,255,255], 3)
        return len(lines)
    except Exception as e:
        return 0


def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.equalizeHist(processed_img)
    processed_img = cv2.Canny(processed_img, threshold1=100, threshold2=200)
    vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500],
                         ], np.int32)
    processed_img = roi(processed_img, [vertices])
# more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
    #                          edges       rho   theta   thresh         # min length, max gap:        
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 200)
    line_count = draw_lines(processed_img,lines)
    return processed_img, line_count

    return processed_img, 0


def main():
    while True:
        with mss.mss() as sct:
            # Part of the screen to capture
            monitor = {"top": 40, "left": 0, "width": 1024, "height": 768}

            fps_list = []
            line_count_list = []
            last_print = time.time()
            while "Screen capturing":
                last_time = time.time()

                # Get raw pixels from the screen, save it to a Numpy array
                img = np.array(sct.grab(monitor))

                # Conver the image and show
                img, line_count = process_img(img)
                line_count_list.append(line_count)

                cv2.imshow("OpenCV/Numpy normal", img)

                fps_list.append(1 / (time.time() - last_time))
                if (time.time() - last_print > 2):
                    logger.info(f"fps: {int(np.average(fps_list))}")
                    logger.info(f"avg_line_count: {int(np.average(line_count_list))}")
                    last_print = time.time()
                    fps_list = []
                    line_count_list = []

                # Press "q" to quit - does not work as intended
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
                    break


if __name__ == "__main__":
   logging.basicConfig(level=logging.INFO)
   main()
