# Functions to process images

import cv2
import numpy as np


def roi(img, vertices):
    """
        Removes extra image data that we do not want to processing
        Args:
            img: Numpy array of grayscale image values
            vertices: numpy array of corners to extract
        Returns:
            numpy array of image values with extra data removed
    """

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
        Args:
            processed_img: numpy array of grayscale image values
        Returns:
            images with lines added and a list of line
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


def perc_img_reduce(original_image, scale_percent):
    """
        Resize an image the a perctage of the original
    """

    width = int(original_image.shape[1] * scale_percent / 100)
    height = int(original_image.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(original_image, dim, interpolation = cv2.INTER_AREA)
    return resized


def abs_img_reduce(original_image, width, height):
    """
        Resize an image to an absolute value
    """
    dim = (width, height)
    # resize image
    resized = cv2.resize(original_image, dim, interpolation = cv2.INTER_AREA)
    return resized

