#!/usr/bin/env python
#
#


import rospy
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import Int8

def main():
    # Inicializar el nodo de ROS y asignarle un nombre
    rospy.init_node('nodo_publicador')
    # Publicador de mensajes
    pub = rospy.Publisher('/mygrid', OccupancyGrid, queue_size=10)
    # Crear el mensaje a enviar (sin contenido)
    msg = OccupancyGrid()
    # Frecuencia con la que se envia el mensaje (en Hz)
    rate = rospy.Rate(10)
    # Contador
    cnt = 0
    # Tamano
    w = 640
    h = 480
    # Datos del mensaje
    msg.header.stamp = rospy.Time.now()
    msg.info.width = w
    msg.info.height = h
    msg.info.resolution = 0.005
    msg.info.origin.position.x = 0.0
    msg.info.origin.position.y = 0.0
    msg.info.origin.position.z = 0.0
    msg.info.origin.orientation.x = 0.0
    msg.info.origin.orientation.y = 0.0
    msg.info.origin.orientation.z = 0.0
    msg.info.origin.orientation.w = 1.0
    msg.header.frame_id = 'mygrid'
    # Valores
    n = w*h
    mymap = n*[10.,]
    msg.data = mymap
        
    # Bucle principal
    while not rospy.is_shutdown():
        # Ingresar los datos del mensaje
        # if (cnt%20 == 0):
        #     mensaje.linear.x = -mensaje.linear.x
        # mensaje.linear.y = 0.0
        # mensaje.linear.z = 0.0
        # mensaje.angular.x = 0.0
        # mensaje.angular.y = 0.0
        # mensaje.angular.z = 0.0
        # Publicar el mensaje
        pub.publish(msg)
        # Mostrar el mensaje
        # print(mensaje)
        # Incrementar el contador
        # cnt += 1
        # Delay del bucle para que cumpla la frecuencia indicada
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
