#
# Robotica Autonoma 2018-2
# Universidad de Ingenieria y Tecnologia - UTEC
#
#   This script segmenta a color form an image using the hue component. After
#   an image is shown, press any key to continue showing the following image
#


import numpy as np
import cv2

# Read an RGB image
I = cv2.imread("kittens.jpg")
# Show the image. It is important to have waitKey
cv2.imshow("Original image", I); cv2.waitKey(0)

# Convert from RGB to Grayscale
Igray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", Igray); cv2.waitKey(0)

# Convert to HSV
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
# Extract the hue component and show it
Ihue = Ihsv[:,:,0]
cv2.imshow("Hue", Ihue); cv2.waitKey(0)

# ----------------------------------------
# Segment the yellow color using the "hue"
# ----------------------------------------
# Lower and upper bounds for yellow
lower_yellow = np.array([20, 50, 50])
upper_yellow = np.array([40, 255, 255])
# Mask that selects pixels within the bounds
mask = cv2.inRange(Ihsv, lower_yellow, upper_yellow)
# Apply the mast to the image to keep only the desired region
Iyellow = cv2.bitwise_and(I, I, mask=mask)

# Show the image
cv2.imshow("Yellow part of the image", Iyellow)
cv2.waitKey(0)
cv2.destroyAllWindows()
