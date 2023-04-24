import cv2 as cv
import numpy as np


def process_and_find_trays(img_gray, img_draw):
    img = img_draw
    gray = img_gray
    gray = cv.fastNlMeansDenoising(gray, gray, 14, 3, 5)
    edges = cv.Canny(gray, 2, 88, apertureSize=3)
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, 90, minLineLength=100, maxLineGap=19)
    xyposs = {'xmin': np.inf, 'xmax': 0, 'ymin': np.inf, 'ymax': 0}
    for line in lines:
        x1, y1, x2, y2 = line[0]
        xyposs['xmax'] = max(xyposs['xmax'], x1, x2)
        xyposs['xmin'] = min(xyposs['xmin'], x1, x2)
        xyposs['ymax'] = max(xyposs['ymax'], y1, y2)
        xyposs['ymin'] = min(xyposs['ymin'], y1, y2)

    cv.line(img, (xyposs['xmin'], xyposs['ymin']), (xyposs['xmin'], xyposs['ymax']), (0, 255, 0), 2)
    cv.line(img, (xyposs['xmax'], xyposs['ymin']), (xyposs['xmax'], xyposs['ymax']), (0, 255, 0), 2)
    cv.line(img, (xyposs['xmax'], xyposs['ymin']), (xyposs['xmin'], xyposs['ymin']), (0, 255, 0), 2)
    cv.line(img, (xyposs['xmax'], xyposs['ymax']), (xyposs['xmin'], xyposs['ymax']), (0, 255, 0), 2)

    return img, xyposs
