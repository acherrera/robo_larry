import time
import logging
import numpy as np
import mss
import cv2

from larry.lane_finder.lane_finder import draw_lanes
from threading import Thread

logger = logging.getLogger(__name__)


def roi(img, vertices):
    # blank mask:
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked


def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(
                img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 255, 255], 3
            )
        return len(lines)
    except Exception as e:
        return 0


def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.equalizeHist(processed_img)
    processed_img = cv2.Canny(processed_img, threshold1=100, threshold2=200)

    y_max = 768
    x_max = 1024
    mirror1_x = 200
    mirror_y = 350
    mirror2_x = 824
    nav_y = 320
    vertices = np.array(
        [
            [10, y_max],
            [10, mirror_y],
            [mirror1_x, mirror_y],
            [mirror1_x, nav_y],
            [mirror2_x, nav_y],
            [mirror2_x, mirror_y],
            [x_max, mirror_y],
            [x_max, y_max],
        ],
        np.int32,
    )
    processed_img = roi(processed_img, [vertices])
    # more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
    #                          edges       rho   theta   thresh         # min length, max gap:
    lines = cv2.HoughLinesP(processed_img, 1, np.pi / 180, 200)
    line_count = draw_lines(processed_img, lines)


    lines = cv2.HoughLinesP(processed_img, 1, np.pi / 180, 180, 20, 15)
    try:
        l1, l2 = draw_lanes(original_image, lines)
        cv2.line(original_image, (l1[0], l1[1]), (l1[2], l1[3]), [0, 255, 0], 30)
        cv2.line(original_image, (l2[0], l2[1]), (l2[2], l2[3]), [0, 255, 0], 30)
    except Exception as e:
        print(str(e))
        pass
    try:
        for coords in lines:
            coords = coords[0]
            try:
                cv2.line(
                    processed_img,
                    (coords[0], coords[1]),
                    (coords[2], coords[3]),
                    [255, 0, 0],
                    3,
                )

            except Exception as e:
                print(str(e))
    except Exception as e:
        pass

    return processed_img, original_image

    return processed_img, line_count


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
                if time.time() - last_print > 2:
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
