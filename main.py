import os
import cv2 as cv

from kola_tray import process_and_find_coins
from linie_tray import process_and_find_trays
from coin_predict import predict_groups, fix_groups_ids
from money_calculator import calculate_money

DATA_PATH = './data'

for im_name in os.listdir(DATA_PATH):
    im_path = os.path.join(DATA_PATH, im_name)

    img = cv.imread(im_path)
    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    img, radius, cords = process_and_find_coins(img_gray, img)
    img, xyposs = process_and_find_trays(img_gray, img)
    groups = predict_groups(radius)
    groups = fix_groups_ids(radius, groups)
    money_in, money_all = calculate_money(groups, cords, xyposs)

    cv.putText(img, f"Pieniędzy na tacy jest; {money_in / 100}pln a w sumie na zdjęciu jest: {money_all / 100}pln",
               (0, 30),
               cv.FONT_HERSHEY_DUPLEX, 3 / 5, (255, 255, 255))

    img = cv.resize(img, [500, 500])
    cv.imshow(im_name, img)
k = cv.waitKey(0)
