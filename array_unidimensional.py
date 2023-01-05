A = int(input("Ingrese el tamaño de los arreglos: "))
B = []
C = []
for i in range (A):
    B.append(input("Ingrese nombre de las personas: "))
print(B)
for j in range (A):
    C.append(len(B[j]))
print(C)

