# Descripcion de un robot Kobuki en urdf

* En este paquete se encuentra la descripcion en formato urdf de un robot kobuki.
* Con el archivo <code>view_robot.launch </code> se abre rviz para visualizar el robot.

* Con el archivo <code>gazebo_kobuki.launch </code> se abren rviz y gazebo con el robot.

* El paquete contiene 4 archivos de python, de los cuales solo <code>kobuki_control_node</code> y <code>kobuki_teleop_node</code> son ejecutables.

* El archivo <code>kobuki_teleop_node</code> lanza un nodo, lee cuando se oprimen las teclas del teclado y publica un mensaje con la velocidad deseada. 
    * Con la tecla "q" se mata el nodo.
    * Con la tecla "p" se detiene el robot.
    * Con las flechas hacia arriba y hacia abajo se ordena al robot moverse de forma lineal
    * Con las flechas hacia la derecha y hacia la izquierda se ordena al robot girar.

*    El archivo <code>kobuki_control_node</code> lanza un nodo, recibe la velocidad publicada, calcula las velocidades apropiadas para las ruedas, y publica esta informacion en los nodos que controlan las ruedas.

* Con el archivo <code>control_nodes.launch </code> se lanzan los dos nodos <code>kobuki_teleop_node</code> y <code>kobuki_control_node</code>.