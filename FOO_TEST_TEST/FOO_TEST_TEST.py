#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import cv2
import numpy as np


def get_game_board(img__or__file_name):
    if isinstance(img__or__file_name, str):
        img = cv2.imread(img__or__file_name)
    else:
        img = img__or__file_name

    # cv2.imshow('img', img)

    edges = cv2.Canny(img, 100, 200)
    # cv2.imshow('edges_img', edges)

    ret, thresh = cv2.threshold(edges, 200, 255, cv2.THRESH_BINARY)
    image, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.imshow('image_', image)

    if not contours:
        print('Не получилсоь найти контуры')
        quit()

    print(len(contours))
    print([cv2.contourArea(i) for i in contours if cv2.contourArea(i) > 10000])
    contours = [i for i in contours if 249000 < cv2.contourArea(i) < 255000]
    if not contours:
        print('Не получилсоь найти контур поля игры')
        quit()

    # img_with_contour = img.copy()
    # cv2.drawContours(img_with_contour, contours, -1, (0, 255, 0), 3)
    # cv2.imshow('img_with_contour', img_with_contour)

    rect_board = cv2.boundingRect(contours[-1])
    x, y, h, w = rect_board
    crop_img = img[y:y+h, x:x+w]
    # cv2.imshow("cropped", crop_img)
    #
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    return crop_img


def get_cell_point_by_contour(board_img):
    # cv2.imshow("board_img", board_img)
    temp_board_img = board_img.copy()
    w, h, _ = temp_board_img.shape

    indent = 15
    size_cell = 122

    for i in range(5):
        cv2.rectangle(temp_board_img, (0, size_cell * i), (w, size_cell * i + indent), 0, cv2.FILLED)
        cv2.rectangle(temp_board_img, (size_cell * i, 0), (size_cell * i + indent, h), 0, cv2.FILLED)

    # cv2.imshow("temp_board_img", temp_board_img)

    gray_img = cv2.cvtColor(temp_board_img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_img, 50, 255, cv2.THRESH_BINARY)
    gray_img_contours, cell_contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.imshow("gray_img_contours", gray_img_contours)

    print(len(cell_contours))
    if len(cell_contours) != 16:
        print('Нужно ровно 16 контуров ячеек')
        quit()

    # img_with_contour = board_img.copy()
    # cv2.drawContours(img_with_contour, cell_contours, -1, (0, 255, 0), 3)
    # # cv2.imshow('img_with_contour_' + str(hex(id(board_img))), img_with_contour)

    sort_x = sorted([cv2.boundingRect(x)[0] for x in cell_contours])
    mean_of_points = [
        sum(sort_x[0:4]) // 4,
        sum(sort_x[4:8]) // 4,
        sum(sort_x[8:12]) // 4,
        sum(sort_x[12:16]) // 4,
    ]

    # print(mean_of_points)
    MEAN_EPS = 5
    # print(sorted([cv2.boundingRect(x)[1] for x in cell_contours]))

    point_by_contour = dict()
    for contour in cell_contours:
        x, y, _, _ = cv2.boundingRect(contour)
        # print(x, y)

        for mean_point in mean_of_points:
            # Максимальное отклонение от средней позиции
            if abs(x - mean_point) <= MEAN_EPS:
                x = mean_point

            if abs(y - mean_point) <= MEAN_EPS:
                y = mean_point

        point_by_contour[(x, y)] = contour

    # cell_contours.sort(key=lambda x: (cv2.boundingRect(x)[1], cv2.boundingRect(x)[0]))
    # print([(cv2.boundingRect(contour)[0], cv2.boundingRect(contour)[1]) for contour in cell_contours])

    return point_by_contour

    # i = 1
    #
    # # for contour in cell_contours:
    # for pos, contour in sorted(point_by_contour.items(), key=lambda x: (x[0][1], x[0][0])):
    #     rect_cell = cv2.boundingRect(contour)
    #     x, y, w, h = rect_cell
    #     # x, y = pos
    #
    #     cv2.putText(img_with_contour, str(i), (x, y + h//4), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 0, 0))
    #     cv2.putText(img_with_contour, '{}x{}'.format(x, y), (x, y + h // 2), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (0, 0, 0))
    #
    #     # x, y = pos
    #     # cv2.putText(crop_img, '{}x{}'.format(x, y), (x, y + h // 2), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (0, 0, 0))
    #     i += 1
    #
    # cv2.drawContours(img_with_contour, cell_contours, -1, (0, 255, 0), 3)
    # cv2.imshow("img_with_contour_cell_contours_" + str(hex(id(img_with_contour))), img_with_contour)
    #
    # # copy_crop_img = crop_img.copy()
    # # cv2.drawContours(copy_crop_img, contours, -1, (0, 255, 0), 3)
    # # cv2.imshow("all_cropped_contours", copy_crop_img)


def show_cell_on_board(board_img, point_by_contour):
    col = 0
    row = 0

    i = 1

    cell_contours = list(point_by_contour.values())

    # for contour in cell_contours:
    for pos, contour in sorted(point_by_contour.items(), key=lambda x: (x[0][1], x[0][0])):
        rect_cell = cv2.boundingRect(contour)
        x, y, w, h = rect_cell
        # x, y = pos

        cv2.putText(board_img, str(i), (x, y + h//4), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0))
        cv2.putText(board_img, '{}x{}'.format(x, y), (x + w // 2, y + h // 7), cv2.FONT_HERSHEY_PLAIN, 0.8, (0, 0, 0))
        cv2.putText(board_img, '{}x{}'.format(col, row), (x + w // 8, y + int(h // 1.2)), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))

        row += 1
        if row == 4:
            row = 0
            col += 1

        # x, y = pos
        # cv2.putText(crop_img, '{}x{}'.format(x, y), (x, y + h // 2), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (0, 0, 0))
        i += 1

    cv2.drawContours(board_img, cell_contours, -1, (0, 255, 0), 3)
    cv2.imshow("img_with_contour_cell_contours_" + str(hex(id(board_img))), board_img.copy())

    # copy_crop_img = crop_img.copy()
    # cv2.drawContours(copy_crop_img, contours, -1, (0, 255, 0), 3)
    # cv2.imshow("all_cropped_contours", copy_crop_img)


# import glob
# for file_name in glob.glob('*.jpg'):
#     show_cell_on_board(get_game_board(file_name))

# show_cell_on_board(get_game_board(cv2.imread('img_bad.png')))
board_img = get_game_board(cv2.imread('img.png'))
point_by_contour = get_cell_point_by_contour(board_img)
show_cell_on_board(board_img, point_by_contour)
print(point_by_contour.keys())

# img = cv2.imread('img.png')
# img = cv2.imread('img_bad.png')
# board_img = get_game_board(img)
# # cv2.imshow("board_img", board_img)
#
# show_cell_on_board(board_img)

cv2.waitKey()
cv2.destroyAllWindows()
