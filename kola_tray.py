import numpy as np
import cv2 as cv

KERNEL_SHARP_FILTER = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])


def process_and_find_coins(img_gray, img_draw):
    gray = img_gray
    cimg = img_draw

    gray = cv.medianBlur(gray, 5)
    gray = cv.fastNlMeansDenoising(gray, gray, 14, 3, 5)
    gray = cv.filter2D(gray, -1, KERNEL_SHARP_FILTER)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 50, param1=180, param2=33, minRadius=15, maxRadius=47)
    circles = np.uint16(np.around(circles))
    radius = []
    cords = []
    for i_num, i in enumerate(circles[0, :]):
        radius.append(i[2])
        cords.append((i[0], i[1]))
        # draw the outer circle
        cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
        cv.putText(cimg, str(i_num), (i[0], i[1]), cv.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255))

    return cimg, radius, cords
