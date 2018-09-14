#!/usr/bin/env python
#
# Robotica Autonoma 2018-2
# Prof. Oscar Ramos
# Universidad de Ingenieria y Tecnologia - UTEC
#
# Este nodo controla el movimiento del robot usando un joystick
#
# Para que pueda funcionar se requiere que antes se ejecute:
#     rosrun joy joy_node


import rospy
import numpy as np

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Joy


# Velocidad lineal y angular iniciales
v=0.0; w = 0.0

def callback_joy(msg):
    global v, w
    dv = 0.05 # Incremento en v
    dw = 0.1  # Incremento en w
    b1 = msg.buttons[4]
    b2 = msg.buttons[5]
    v1 = msg.buttons[0]
    v2 = msg.buttons[2]
    w1 = msg.axes[0]
    if (b1==1 or b2==2):
        w=0; v=0
    elif (v1==1):
        v += dv
    elif (v2==1):
        v -= dv
    elif (w1 == 1):
        w += dw
    elif (w1 == -1):
        w -= dw
        
def main():
    global v, w
    # Inicializar el nodo de ROS y asignarle un nombre
    rospy.init_node('nodo_publicador')
    # Publicador de mensajes de tipo Twist en el topico "topico_velocidad"
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
    # Suscriptor al topico de odometria
    rospy.Subscriber('/joy', Joy, callback_joy)
    # Crear el mensaje a enviar (sin contenido)
    mensaje = Twist()
    # Frecuencia con la que se envia el mensaje (en Hz)
    rate = rospy.Rate(10)
    # Bucle principal
    while not rospy.is_shutdown():
        # Ingresar los datos del mensaje
        mensaje.linear.x = v
        mensaje.linear.y = 0.0
        mensaje.linear.z = 0.0
        mensaje.angular.x = 0.0
        mensaje.angular.y = 0.0
        mensaje.angular.z = w
        # Publicar el mensaje
        pub.publish(mensaje)
        # Mostrar el mensaje
        # print(mensaje)
        # Delay del bucle para que cumpla la frecuencia indicada
        rate.sleep()

        
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
