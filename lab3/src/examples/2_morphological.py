#
# Robotica Autonoma 2018-2
# Universidad de Ingenieria y Tecnologia - UTEC
#
#   This script shows some morphological operations on a binary image. Press
#   any key to exit the program
#


import numpy as np
import cv2

I = cv2.imread('shapes.png', 0)

# Rectangular structuring element (kernel)
se = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
# Other structuring elements
if (False):
    se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    se = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))

# Basic morphology
Ierosion  = cv2.erode(I, se, iterations=1)
Idilation = cv2.dilate(I, se, iterations=1)
Iopening  = cv2.morphologyEx(I, cv2.MORPH_OPEN, se)
Iclosing  = cv2.morphologyEx(I, cv2.MORPH_CLOSE, se)
# Morphological gradient (edges): dilation - erosion
Igradient = Idilation - Ierosion

cv2.imshow('original', I)
cv2.imshow('eroded', Ierosion)
cv2.imshow('dilated', Idilation)
cv2.imshow('gradient', Igradient)
cv2.imshow('opened', Iopening)
cv2.imshow('closed', Iclosing)
cv2.waitKey(0)
cv2.destroyAllWindows()
