


import numpy as np
import cv2

# Read an RGB image
I = cv2.imread("vasos.jpg")
# Convert to HSV
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
# Extract the hue component and show it
Ihue = Ihsv[:,:,0]
# Show images
cv2.imshow("Original image", I); cv2.waitKey(0)
cv2.imshow("Hue", Ihue); cv2.waitKey(0)

# Lower and upper bounds for yellow
lower_yellow = np.array([20, 50, 50])
upper_yellow = np.array([40, 255, 255])
# Mask that selects pixels within the bounds
Iyellow = cv2.inRange(Ihsv, lower_yellow, upper_yellow)
cv2.imshow("Yellow part of the image", Iyellow); cv2.waitKey(0)

# Opening
se = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
I2 = cv2.morphologyEx(Iyellow, cv2.MORPH_OPEN, se)
cv2.imshow('Yellow opened', I2); cv2.waitKey(0)

x,y,w,h = cv2.boundingRect(I2)
cv2.rectangle(I,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('Yellow opened', I); cv2.waitKey(0)

cv2.destroyAllWindows()

