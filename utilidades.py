#En este modulo agregar funciones
import random as r





def random_muro():
    """Funcion encargada de generar listas aleatorias en un rango del (0-31)

    Returns:
        list: retorna una lista de numeros en generada de forma aleatoria 
    """
    muro=[]
    for i in range(0,4):
        fcana = r.randrange(31)
        muro.append(fcana)

    return muro 

def definir_muro(lista_filas,lista_columna,lista_ancho,lista_largos):
    """Función encargada de generar las coordenadas del muro

    Args:
        lista_filas (list): lista de 4 posiciones numericas
        lista_columna (list): lista de 4 posiciones numericas
        lista_ancho (list): lista de 4 posiciones numericas
        lista_largos (list): lista de 4 posiciones numericas

    Returns:
        list: retorna una lista de coordenadas
    """
    coord = []

    for i in range(4):
        a = muro(lista_filas[i],lista_columna[i],lista_ancho[i],lista_largos[i])
        coord.append(a)
    return coord

def muro(fila,columna,ancho,alto):
    """Funcion que permite generar las coordenadas de un solo muro

    Args:
        fila (list): lista de 4 posiciones numericas
        columna (list): lista de 4 posiciones numericas
        ancho (list): lista de 4 posiciones numericas
        alto (list): lista de 4 posiciones numericas

    Returns:
        list: retorna coordenadas
    """
    coordenadas = []
    for a in range(0,1):
            for i in range(0, alto):
                # print("fila: ", i)
                for j in range(0, ancho):
                    # print("ancho: ", j)
                    coordenadas.append(str(fila+i) + ":" + str(columna+j))
    return coordenadas
