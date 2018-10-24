#!/usr/bin/env python
#

import rospy
import numpy as np

from apriltags_ros.msg import AprilTagDetectionArray
from geometry_msgs.msg import Twist

class AprilTags(object):
    def __init__(self):
        # Suscriptor al topico de informacion de tags
        rospy.Subscriber('/tag_detections', AprilTagDetectionArray, self.callback)
        self._tag = AprilTagDetectionArray()

    def callback(self, msg):
        self._tag = msg

    def getmsg(self):
        return self._tag

    
def main():

    # Inicializar el nodo de ROS y asignarle un nombre
    rospy.init_node('minodo')
    
    # Publicador de mensajes de tipo Twist en el topico "topico_velocidad"
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
    # Crear el mensaje a enviar (sin contenido)
    velocidad = Twist()

    # Instancia para leer informacion de los tags
    tags = AprilTags()

    # Frecuencia con la que se envia el mensaje (en Hz)
    rate = rospy.Rate(10)
    tag5 = False
    tag5center = False
    # Bucle principal
    while not rospy.is_shutdown():
        # Ingresar los datos del mensaje
        tag = tags.getmsg()
        Ndetections = len(tag.detections)
        if Ndetections==0:
            # No detecta nada
            print 'No detection'
            velocidad.angular.z = 0.4
            tag5 = False
        else:
            tag5 = False
            # Detecta algun tag
            for i in range(Ndetections):
                # print tag.detections[i].id
                # Detecta el tag 5
                if (tag.detections[i].id==5):
                    tag5 = True
                    x = tag.detections[i].pose.pose.position.x
                    y = tag.detections[i].pose.pose.position.y
                    print x,y
                    if (abs(x) > 0.1):
                        velocidad.angular.z = 0.2
                        velocidad.linear.x = 0.0
                    else:
                        tag5center = True
                        z = tag.detections[i].pose.pose.position.z
                        if (z > 0.4):
                            velocidad.angular.z = 0
                            velocidad.linear.x = 0.1
                        else:
                            velocidad.angular.z = 0
                            velocidad.linear.x = 0                        
                       
            if (tag5 == False):
                print 'No encuentra tag 5'
                velocidad.angular.z = 0.4

        # Publicar el mensaje
        pub.publish(velocidad)
        # Mostrar el mensaje
        # print(mensaje)
        # Delay del bucle para que cumpla la frecuencia indicada
        rate.sleep()
    

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

