#!/usr/bin/env python
#
# Robotica Autonoma 2018-2
# Prof. Oscar Ramos
# Universidad de Ingenieria y Tecnologia - UTEC
#
# Este nodo hace que el kobuki gire con un radio 0.5 y con una velocidad lineal de 0.2 m/s.
#


import rospy
import numpy as np

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


f = open('/tmp/log.txt', 'w')

def callback(msg):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    ez = msg.pose.pose.orientation.z
    w  = msg.pose.pose.orientation.w
    th = 2.0*np.arctan2(ez, w)/np.pi*180.0
    print(str(x) + " " + str(y) + " " + str(th))
    f.write(str(x) + " " + str(y) + " " + str(th) + "\n")

def main():
    # Inicializar el nodo de ROS y asignarle un nombre
    rospy.init_node('nodo_publicador')
    # Publicador de mensajes de tipo Twist en el topico "topico_velocidad"
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
    # Suscriptor al topico de odometria
    rospy.Subscriber('/odom', Odometry, callback)
    # Crear el mensaje a enviar (sin contenido)
    mensaje = Twist()
    # Frecuencia con la que se envia el mensaje (en Hz)
    rate = rospy.Rate(10)
    # Contador
    cnt = 0
    # Velocidades dado el radio
    v = 0.1; R = 0.1; w = v/R;
    # Bucle principal
    while not rospy.is_shutdown():
        # Ingresar los datos del mensaje
        mensaje.linear.x = 0.0 # v
        mensaje.linear.y = 0.0
        mensaje.linear.z = 0.0
        mensaje.angular.x = 0.0
        mensaje.angular.y = 0.0
        mensaje.angular.z = -w
        # Publicar el mensaje
        pub.publish(mensaje)
        # Mostrar el mensaje
        # print(mensaje)
        # Incrementar el contador
        cnt += 1
        # Delay del bucle para que cumpla la frecuencia indicada
        rate.sleep()
    f.close()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
