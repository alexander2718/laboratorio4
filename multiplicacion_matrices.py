import numpy as np
filas = int(input('Ingrese el número de filas de la matriz 1: '))
columnas = int(input('Ingrese el número de columnas de la matriz 1: '))

filas1 = int(input('\nIngrese el número de filas de la matriz 2: '))
columnas1 = int(input('Ingrese el número de columnas de la matriz 2: '))


def crear_matriz (filas,columnas):
    f = -1
    c = -1
    e_fil = []

    for i in range (0,filas):
        e_col=[]
        f+=1
        for j in range (0,columnas):
            c+=1
            valor = int (input(f'Ingrese el valor del componente {i},{j} '))
            e_col.append(valor)
        e_fil.append(e_col)
    return e_fil
if (columnas==filas1):
    matrizA = np.array(crear_matriz(filas,columnas))
    matrizB = np.array(crear_matriz(filas,columnas))
    multiplicacion = matrizA * matrizB
    print(f"Multiplicacion de Matrices: \n{multiplicacion}")
else:
    print("\nNo se puede realizar la multiplicación de matrices")

