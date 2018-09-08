#!/usr/bin/env python
#
# Robotica Autonoma 2018-2
# Prof. Oscar Ramos
# Universidad de Ingenieria y Tecnologia - UTEC
#
# Este nodo se suscribe al topico llamado '/topico_velocidad', que contiene
# mensajes de tipo Twist, y muestra el mensaje recibido en dicho topico
#


import rospy
from geometry_msgs.msg import Twist

def callback(msg):
    # Mostrar un mensaje con la velocidad lineal y angular medidas
    print("\nVelocidad lineal en y:" + str(msg.linear.y))
    print("Velocidad angular en x:" + str(msg.angular.x))
    print("Velocidad angular en y:" + str(msg.angular.y))

def main():
    # Inicializar el nodo de ROS y asignarle un nombre
    rospy.init_node('nodo_suscriptor')
    # Suscriptor al topico "topico_velocidad" que tiene mensajes Twist
    rospy.Subscriber('topico_velocidad', Twist, callback)
    # Evitar que Python termine hasta que este nodo sea detenido (no es
    # necesario si hay un rate.sleep dentro de un while)
    rospy.spin()

    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
