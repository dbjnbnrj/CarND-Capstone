from styx_msgs.msg import TrafficLight

import cv2
import numpy as np

class TLClassifier(object):
    def __init__(self):
        pass

    def get_classification(self, img):
        # Convert input image to HSV
        img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # lower mask (0-10)
        lower_red = np.array([0,50,50])
        upper_red = np.array([10,255,255])
        mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

        # upper mask (170-180)
        lower_red = np.array([170,50,50])
        upper_red = np.array([180,255,255])
        mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

        # join my masks
        mask = mask0+mask1

        # set my output img to zero everywhere except my mask
        output_img = img.copy()
        output_img[np.where(mask==0)] = 0
        output_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2GRAY)
        # Use the Hough transform to detect circles in the images
        red_circles = cv2.HoughCircles(output_img, cv2.HOUGH_GRADIENT, 1, output_img.shape[0] / 8.0, 100, 20, 20, 1)

        # Loop over all detected circles and outline them on the original image
        if red_circles is not None:
            TrafficLight.RED
        else:
            TrafficLight.UNKNOWN
