#!/usr/bin/env python
#
# Robotica Autonoma 2018-2
# Prof. Oscar Ramos
# Universidad de Ingenieria y Tecnologia - UTEC
#
# Este nodo hace que el kobuki se mueva hacia adelante y luego hacia atras
#


import rospy
from geometry_msgs.msg import Twist

def main():
    # Inicializar el nodo de ROS y asignarle un nombre
    rospy.init_node('nodo_publicador')
    # Publicador de mensajes de tipo Twist en el topico "topico_velocidad"
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
    # Crear el mensaje a enviar (sin contenido)
    mensaje = Twist()
    # Frecuencia con la que se envia el mensaje (en Hz)
    rate = rospy.Rate(10)
    # Contador
    cnt = 0
    # Velocidad lineal
    mensaje.linear.x = 0.1
    # Bucle principal
    while not rospy.is_shutdown():
        # Ingresar los datos del mensaje
        if (cnt%20 == 0):
            mensaje.linear.x = -mensaje.linear.x
        mensaje.linear.y = 0.0
        mensaje.linear.z = 0.0
        mensaje.angular.x = 0.0
        mensaje.angular.y = 0.0
        mensaje.angular.z = 0.0
        # Publicar el mensaje
        pub.publish(mensaje)
        # Mostrar el mensaje
        print(mensaje)
        # Incrementar el contador
        cnt += 1
        # Delay del bucle para que cumpla la frecuencia indicada
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
