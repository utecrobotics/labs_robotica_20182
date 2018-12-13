#!/usr/bin/env python
#
# Robotica Autonoma 2018-2
# Universidad de Ingenieria y Tecnologia - UTEC
#
#   Este nodo se suscribe a un topico, convierte la imagen a formato OpenCV,
#   calcula los bordes (con Canny) y publica la imagen nuevamente en un topico
#   de ROS


import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class Camera(object):
    def __init__(self, cam_number = 0):
        self.cam = cv2.VideoCapture(cam_number)
        rospy.loginfo('Camera loaded ...')
        self.image_pub = rospy.Publisher("camera_frame", Image, queue_size=10)
        self.bridge = CvBridge()

    def __del__(self):
        self.cam.release()

    def publish(self):
        retval, frame = self.cam.read()
        frame = cv2.flip(frame, 1)
        if retval == True:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(frame, "bgr8"))
        
if __name__ == '__main__':
    cam = Camera(0)
    rospy.init_node('mycamera')

    # Frequency (in Hz)
    freq = 30
    rate = rospy.Rate(freq)
    # Main loop
    while not rospy.is_shutdown():
        cam.publish()
    cv2.destroyAllWindows()
