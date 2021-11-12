#!/usr/bin/env python
import numpy as np
import cv2 as cv

def drawbar(pos_x, pos_y, length, precent, width = 50, b_color = (255, 255, 255), f_color = None):
    if f_color == None: f_color = b_color
    pt1 = (pos_x, pos_y)
    pt2 = (pos_x + length, pos_y + width)
    fill = min(int(length * precent / 100), length)
    ptp = (pos_x + fill, pos_y + width)
    cv.rectangle(image, pt1, ptp, f_color, -1)
    cv.rectangle(image, pt1, pt2, b_color, 2)

def getValueFromFile(filename):
    infile = open(filename, "r")
    inp = infile.readline()
    infile.close()
    return int(inp)

def drawtext(text, pos_x, pos_y, scale = 1, color = (255, 255, 255)):
    textsize = cv.getTextSize(text, 2, scale, 1)
    pt = (pos_x, pos_y)
    cv.putText(image, text, pt, 2, scale, color, 1)

if __name__ == '__main__':
    wndname = "Voortgang"
    cv.namedWindow(wndname, cv.WND_PROP_FULLSCREEN)
    cv.setWindowProperty(wndname, cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    width, height = 1920, 1080
    herten_, zwijnen_ = 0, 0
    while True:
        image = np.zeros((height, width, 3), dtype = np.uint8)
        herten = getValueFromFile('herten')
        zwijnen = getValueFromFile('zwijnen')
        if abs(herten - herten_) > 0.8:
            herten_ += (herten - herten_) * 0.1
        else: herten_ = herten
        if abs(zwijnen - zwijnen_) > 0.8:
            zwijnen_ += (zwijnen - zwijnen_) * 0.1
        else: zwijnen_ = zwijnen
        y_ = 300
        drawtext("Voortgang van de Herten:", 100, y_-25, 2)
        drawbar(100, y_, width-420, int(herten_), f_color=(138,43,226))
        drawtext("{0:.2f}%".format(herten_), width-300, y_+40, 1.5)
        y_ = 500
        drawtext("Voortgang van de Zwijnen:", 100, y_-25, 2)
        drawbar(100, y_, width-420, int(zwijnen_), f_color=(255,20,147))
        drawtext("{0:.2f}%".format(zwijnen_), width-300, y_+40, 1.5)
        cv.imshow(wndname, image)
        if cv.waitKey(100) == 27: break
    cv.destroyAllWindows()
    exit()
