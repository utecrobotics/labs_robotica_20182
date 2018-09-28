#!/usr/bin/env python
#
# Robotica Autonoma 2018-2
# Universidad de Ingenieria y Tecnologia - UTEC
#
#   Este nodo se suscribe a una imagen de ROS, la convierte en una matriz de
#   OpenCV y la muestra en pantalla
#

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class Cam(object):
    def __init__(self, topic_name="camera_frame"):
        self.bridge = CvBridge()
        self.image = np.zeros((10,10))
        isub = rospy.Subscriber(topic_name, Image, self.image_callback)

    def image_callback(self, img):
        self.image = self.bridge.imgmsg_to_cv2(img, "bgr8")

    def get_image(self):
        return self.image


if __name__ == '__main__':

    # Initialize the ROS node
    rospy.init_node('camera_node')
    # Instance that subscribes to the desired topic
    topic_name = "camera_frame"
    cam = Cam(topic_name)
    # Loop rate (in Hz)
    freq = 10
    dt = 1.0/freq
    rate = rospy.Rate(freq)
    # Continuous execution loop
    while not rospy.is_shutdown():
        # Get the image from the ROS topic
        I = cam.get_image()
        # Do some processing with the image here

        
        # Show the image(s)
        cv2.imshow("Image window", I)

        # Wait for the loop to update
        cv2.waitKey(1)
        rate.sleep()

    cv2.destroyAllWindows()
