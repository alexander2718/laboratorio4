import numpy as np
filas = int(input('Ingrese el número de filas de la matriz: '))
columnas = int(input('Ingrese el número de columnas de la matriz: '))


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
if (columnas==filas):
    matrizA = np.array(crear_matriz(filas,columnas))
    matrizA_transpuesta=np.transpose(matrizA)
    comparacion = np.array_equal(matrizA,matrizA_transpuesta)
    if comparacion== True:
        print("\nLa matriz es simétrica")
    else:
        print("\nNo es una matriz simétrica")

else:
    print("\nLa matriz ingresada no es cuadrática")