#!/usr/bin/env python
#
# Robotica Autonoma 2018-2
# Universidad de Ingenieria y Tecnologia - UTEC
#


import rospy
import numpy as np


# Archivo donde se guarda el log
f = open('/tmp/log.txt', 'w')
# Para almacenar x, y, th usar la siguiente linea en el lugar adecuado
# f.write(str(x) + " " + str(y) + " " + str(th) + "\n")


def main():
    # Inicializar el nodo de ROS y asignarle un nombre
    rospy.init_node('nodo_circulo')

    
    # Frecuencia con la que se ejecuta el bucle principal (en Hz)
    rate = rospy.Rate(10)
    # Bucle principal
    while not rospy.is_shutdown():

        # Delay del bucle para que cumpla la frecuencia indicada
        rate.sleep()

        
    # Cerrar el archivo donde se guarda el log
    f.close()

    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
