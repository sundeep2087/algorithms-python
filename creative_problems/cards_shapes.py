# Created by Sai at 7/6/2024

import stddraw
import sys
import math
import numpy as np


def scale_canvas(scaler):
    if scaler >= 20:
        scaler = math.ceil((scaler / 2) // 10) * 10
        stddraw.setXscale(-scaler, scaler)
        stddraw.setYscale(-scaler, scaler)
    else:
        stddraw.setXscale(-10, 10)
        stddraw.setYscale(-10, 10)
    if scaler > 512:
        stddraw.setCanvasSize(scaler, scaler)


def draw_diamond_noshow(diag1, diag2, x_center=0, y_center=0):
    scale_canvas(max(diag1, diag2))
    stddraw.setPenRadius(0.005)
    stddraw.setPenColor(stddraw.RED)
    (t1x1, t1x2, t1x3) = (x_center-diag1/2, x_center, x_center)
    (t1y1, t1y2, t1y3) = (y_center, y_center+diag2/2, y_center-diag2/2)

    (t2x1, t2x2, t2x3) = (x_center+diag1/2, x_center, x_center)
    (t2y1, t2y2, t2y3) = (y_center, y_center+diag2/2, y_center-diag2/2)

    # print(x_center, y_center)
    # print(f"{t1x1, t1y1}\n"
    #       f"{t1x2, t1y2}\n"
    #       f"{t1x3, t1y3}\n"
    #       f"\n\n"
    #       f"{t2x1, t2y1}\n"
    #       f"{t2x2, t2y2}\n"
    #       f"{t2x3, t2y3}\n")

    stddraw.filledPolygon(x=[t1x1, t1x2, t1x3],
                          y=[t1y1, t1y2, t1y3])
    stddraw.filledPolygon(x=[t2x1, t2x2, t2x3],
                          y=[t2y1, t2y2, t2y3])


def draw_diamond(diag1, diag2, x_center=0, y_center=0, msec=float('inf')):
    draw_diamond_noshow(diag1, diag2, x_center=x_center, y_center=y_center)
    stddraw.show(msec)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++ Blink - Blink +++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

def diamonds_blinker():
    while True:
        draw_diamond(diag1=np.random.randint(5, 10, 1)[0],
                     diag2=np.random.randint(5, 10, 1)[0],
                     x_center=-3, y_center=0, msec=50)
        stddraw.clear(stddraw.WHITE)
        draw_diamond(diag1=np.random.randint(5, 10, 1)[0],
                     diag2=np.random.randint(5, 10, 1)[0],
                     x_center=3, y_center=0, msec=50)
        stddraw.clear(stddraw.WHITE)


def draw_hearts(diag1, diag2, x_center=0, y_center=0, msec=float('inf')):
    draw_diamond_noshow(diag1, diag2, x_center=x_center, y_center=y_center)
    (c1x, c1y) = (((x_center + diag1 / 2) + x_center) / 2, ((y_center + diag2 / 2) + y_center) / 2)
    (c2x, c2y) = (((x_center - diag1 / 2) + x_center) / 2, ((y_center + diag2 / 2) + y_center) / 2)
    radius = np.sqrt(np.power(((x_center + diag1 / 2) - c1x), 2) + np.power(c1y-y_center, 2))
    stddraw.filledCircle(c1x, c1y, radius)
    stddraw.filledCircle(c2x, c2y, radius)
    stddraw.show(msec)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++ Heart Beat Simulator +++++++++++++++++ #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

def heart_beat():
    # Alter msec args in the calls to draw_hearts to change heart rate
    while True:
        draw_hearts(diag1=10, diag2=10, x_center=0, y_center=0, msec=470)
        stddraw.clear(stddraw.WHITE)
        draw_hearts(diag1=5, diag2=5, x_center=0, y_center=0, msec=150)


def draw_diamond_black_noshow(diag1, diag2, x_center=0, y_center=0):
    scale_canvas(max(diag1, diag2))
    stddraw.setPenRadius(0.005)
    stddraw.setPenColor(stddraw.BLACK)
    (t1x1, t1x2, t1x3) = (x_center-diag1/2, x_center, x_center)
    (t1y1, t1y2, t1y3) = (y_center, y_center+diag2/2, y_center-diag2/2)

    (t2x1, t2x2, t2x3) = (x_center+diag1/2, x_center, x_center)
    (t2y1, t2y2, t2y3) = (y_center, y_center+diag2/2, y_center-diag2/2)

    stddraw.filledPolygon(x=[t1x1, t1x2, t1x3],
                          y=[t1y1, t1y2, t1y3])
    stddraw.filledPolygon(x=[t2x1, t2x2, t2x3],
                          y=[t2y1, t2y2, t2y3])


def draw_spade(diag1, diag2, x_center=0, y_center=0, msec=float("inf")):
    draw_diamond_black_noshow(diag1, diag2, 0, 0)
    (c1x, c1y) = (((x_center + diag1 / 2) + x_center) / 2, ((y_center + diag2 / 2) + y_center) / 2)
    (c2x, c2y) = (((x_center - diag1 / 2) + x_center) / 2, ((y_center + diag2 / 2) + y_center) / 2)
    radius = np.sqrt(np.power(((x_center + diag1 / 2) - c1x), 2) + np.power(c1y - y_center, 2))
    stddraw.filledCircle(c1x, c1y, radius)
    stddraw.filledCircle(c2x, c2y, radius)


    stddraw.show(msec)



def run_test_client():
    # draw_diamond(5, 5, 0, 0)
    # diamonds_blinker()
    # draw_hearts(10, 10, 0, 0)
    # heart_beat()
    draw_spade(5, 5, 0, 0)


if __name__ == "__main__":
    run_test_client()
