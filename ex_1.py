#Metodo que multiplica matrices
import numpy as np

def multiplicar_matrices():
	print("----------Ingrese el numero de matrices a multiplicar----------\n")

	numero = int(input())

	matriz=[] 
	print("\n Ingrese las matrices del modo numpy:\nejemplo: 0 3 1 0;90 0 1 0;-90 2 0 0")
	for i in range(numero):



		print("\n	 Ingrese la matriz",i+1)
		matriz.append(np.matrix(input()))

		if i < 1:
			sol=matriz[i]
		else:
			sol=sol*matriz[i]

	print("El producto de las siguientes matrices:\n")
	for i in range(numero):
		print(matriz[i],"\n")

	print("\nEs:\n\n",sol)

	#0.45 1.3 0.94 1.23;0 0.83 0.2 2.37;0.2 0.65 0.4 0.3;0 0 0 1
	#1 0.2 0.85 2.467;0.54 1.3 0 0.77;0.12 0.68 1 0.8;0 0 0 1
	#2.3;0;24.4;1