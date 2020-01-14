import time
import logging
import numpy as np
import mss
import cv2
import matplotlib.pyplot as plt

from larry.lane_finder.lane_finder import draw_lanes
from larry.controls.controls import cont_straight, cont_left, cont_right, cont_slow, stop_all
from threading import Thread

logger = logging.getLogger(__name__)


def roi(img):
    """
        Removes extra image data that we do not want to processing
        Args:
            img: Numpy array of grayscale image values
        Returns:
            numpy array of image values with extra data removed
    """

    # Region of Interest Definitions

    y_max = 745
    x_max = 1024

    width = int(img.shape[1])
    height = int(img.shape[0])

    y_max = 100*height
    x_max = 100*width
    mirror1_x = 0.268*width
    mirror_y = 0.5*height
    mirror2_x = 0.8047*width
    nav_y = 0.43*height

    # Where we want to look
    vertices = np.array(
        [
            [10, y_max],
            [10, mirror_y],
            [mirror1_x, mirror_y],
            [mirror2_x, nav_y],
            [mirror2_x, mirror_y],
            [x_max, mirror_y],
            [x_max, y_max],
        ],
        np.int32,
    )

    vertices = [vertices]
    # blank mask:
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked

def edge_detection(img):
    """
        Take the original_image, reduces to grayscale, increase contrast, runs canny edge detection
    """

    processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cl1 = cv2.equalizeHist(processed_img)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(processed_img)
    cl1 = cv2.blur(cl1,(4,4))
    processed_img = cv2.Canny(cl1, threshold1=50, threshold2=200)

    return processed_img

def find_lines(processed_img):
    """
        Finds the lines in an image with edge detection already performed
    """
    lines = cv2.HoughLinesP(processed_img, 1, np.pi / 180, 100)

    # Draw lines on image
    try:
        for line in lines:
            coords = line[0]
            cv2.line(
                processed_img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 255, 255], 3
            )
    except TypeError:
        pass

    return  processed_img, lines

def process_img(original_image):

    processed_img = edge_detection(original_image)

    processed_img = roi(processed_img,)

    processed_img, lines = find_lines(processed_img)

    m1 = 0
    m2 = 0

    try:
        l1, l2, m1, m2= draw_lanes(original_image, lines)
        logger.debug(f"Lines are {l1} and {l2}")
        cv2.line(original_image, (l1[0], l1[1]), (l1[2], l1[3]), [0, 255, 0], 30)
        cv2.line(original_image, (l2[0], l2[1]), (l2[2], l2[3]), [0, 255, 0], 30)
    except Exception as e:
        pass

    if lines is None:
        lines = list()

    return processed_img, original_image, len(lines), m1, m2


def honey_i_shrunk_the_image(original_image, scale_percent):
    """
        Resize an image the a perctage of the original
    """

    width = int(original_image.shape[1] * scale_percent / 100)
    height = int(original_image.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(original_image, dim, interpolation = cv2.INTER_AREA)
    return resized


def main():

    turnval = 0
    turnval_list = list()
    timelast = time.time()
    while True:
        with mss.mss() as sct:
            # Part of the screen to capture
            monitor = {"top": 40, "left": 0, "width": 1024, "height": 748}

            fps_list = []
            line_count_list = []
            last_print = time.time()
            while "Screen capturing":
                last_time = time.time()

                # Get raw pixels from the screen, save it to a Numpy array
                img = np.array(sct.grab(monitor))

                per_reduce = 50
                img = honey_i_shrunk_the_image(img, 50)

                # Conver the image and show
                img, original_image, line_count, m1, m2= process_img(img)
                line_count_list.append(line_count)

                test_img_hstack = np.hstack((
                    cv2.cvtColor(img, cv2.COLOR_GRAY2BGRA),
                    original_image))

                cv2.imshow("American Truck Robo Simulator", test_img_hstack)
                # cv2.imshow("OpenCV/Numpy normal", img)
                # cv2.imshow("OpenCV/Numpy normal", original_image)

                # left is negative, right is positive
                max_turn = 1
                turn_rate = 1.5
                min_turn = 0-max_turn

                # Account for wheel returning to center on their own while driving
                do_controls = True

                if do_controls:

                    decay_rate = time.time() - timelast
                    if turnval < 0:
                        turnval += decay_rate
                    if turnval > 0:
                        turnval -= decay_rate

                    if m1<0 and m2<0:
                        if turnval < max_turn:
                            cont_right()
                            turnval += turn_rate

                    elif m1>0 and m2>0:
                        if turnval > min_turn:
                            cont_left()
                            turnval -= turn_rate
                    elif (m1 > 0 and m2 <0) or (m1 < 0 and m2 > 0):
                        cont_straight()

                    else:
                        pass
                    timelast = time.time()


                turnval_list.append(turnval)
                fps_list.append(1 / (time.time() - last_time))
                if time.time() - last_print > 2:
                    logger.info(f"fps: {int(np.average(fps_list))}")
                    logger.info(f"Average Turn value: {np.average(turnval):.2f}")
                    #logger.info(f"avg_line_count: {int(np.average(line_count_list))}")
                    last_print = time.time()
                    fps_list = []
                    line_count_list = []
                    turnval_list = list()

                # Press "q" to quit - does not work as intended
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
                    break

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
