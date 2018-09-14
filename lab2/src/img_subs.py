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
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


bridge = CvBridge()

def callback(img):
    global bridge
    cv_image = bridge.imgmsg_to_cv2(img, "bgr8")
    cv2.imshow("Image window", cv_image)
    cv2.waitKey(30)

if __name__ == '__main__':

    rospy.init_node('read_image')
    isub = rospy.Subscriber("camera_frame", Image, callback)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down"
    cv2.destroyAllWindows()
       
