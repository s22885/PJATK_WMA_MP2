import os
import numpy as np
import cv2 as cv

import coin_predict

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

#
# for im_name in os.listdir('./data/'):
#     cimg = cv.imread(os.path.join('./data', im_name))
#     img = cv.cvtColor(cimg, cv.COLOR_RGB2GRAY)
#     img = cv.medianBlur(img, 5)
#     img = cv.fastNlMeansDenoising(img, img, 14, 3, 5)
#     img = cv.filter2D(img, -1, KERNEL_SHARP_FILTER)
#     circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 50, param1=180, param2=33, minRadius=15, maxRadius=47)
#     circles = np.uint16(np.around(circles))
#     radius = []
#     cords = []
#     for i_num, i in enumerate(circles[0, :]):
#         radius.append(i[2])
#         cords.append((i[0], i[1]))
#         # draw the outer circle
#         cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
#         # draw the center of the circle
#         cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
#         cv.putText(cimg, str(i_num), (i[0], i[1]), cv.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255))
#     print(im_name)
#     print(np.array([i for i in range(len(radius))]))
#     print(coin_predict.predict_groups(radius))
#     print()
#     cimg = cv.resize(cimg, [400, 400])
#     cv.imshow(im_name, cimg)
# cv.waitKey(0)
# cv.destroyAllWindows()
