#Código principal donde se implementa la lógica del juego WorldCraftASCII.

import utilidades as util

print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
print('/ \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ /  \     / \ / \ / \ / \ / \ / \ ')
print('(W )( o )( r )( l )( d )( C )( r )( a )( f )( t )   (A )( S )( C )( I )( I )')
print('\ / \ / \ / \  / \  / \ / \ / \ /  \ / \  / \  /    \  / \  / \  / \  / \  /')  
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
print('                              P A R T E 2                                   ')
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n\n\n')



numero_muros = int(input("Ingrese el número de muros que se generararan de manera\naleatoria: "))
for i in range(numero_muros):
    filas = util.random_muro()
    columnas = util.random_muro()
    anchos = util.random_muro()
    largos=util.random_muro()    
    
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    print(f"                          COORDENADAS MURO N.{i+1}")
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n')
    
    print("Lista filas:    ",filas)
    print("Lista columnas: ",columnas)
    print("lista anchos:   ",anchos)
    print("lista largos.   ",largos) 
    print("\n")  
    
    print(util.definir_muro(filas,columnas,anchos,largos))
