------------------------------------------------------------------------------------------------------------
                                        WORLD CRAFT ASCII: PARTE 2
------------------------------------------------------------------------------------------------------------

                                                IDENTIFICAR
------------------------------------------------------------------------------------------------------------
Este reto trata de la creación del mundo  del juego (world craft ASCII) en el que asignaremos de manera
aleatoria el mundo al jugador.


                                                DEFINICIÓN
------------------------------------------------------------------------------------------------------------
Se debe implementar una función que reciba como parametros:
    * lista filas
    * lista columnas
    * lista anchos
    * lista largos
las listas deberan tener una longitud igual a 4 y dicha funcion nos devolvera las coordenadas del respectivo muro
en un mundo de (32 x 32) bloques en esta matriz se ubicaran los muros gracias a las coordenadas devueltas por 
la función.

    EJEMPLO: muros=["0:2”,”1:0","1:1","1:2","2:1","2:2",”3:1”,”3:2”,”4:1”,”4:2”] -> retorno de la función