import numpy as np
from numpy import matrix
import math
class Cinematica:
	def __init__(self,thetai_1,di_1,ai,alphai):
		self.thetai_1 = thetai_1
		self.di_1= di_1
		self.alphai=alphai
		self.ai = ai

	def informacion():
		"""\n\nParametros:\nTheta_i-1: Giro en z\nd_i-1:     Distancia en z\nalpha_i:   Giro en x\na_i:         Distancia en x"""
	print(informacion.__doc__)
	informacion.__doc__= """\nLos parametros requieren entradas de numeros reales; la tabla va a desplegar el calculo de Denavit-Hartemberg\n\n"""
	print(informacion.__doc__)
	informacion.__doc__="""Escriba la matriz en el siguiente orden en una matriz de nx4 con n<=3:\n|thetai_1| di_1 | ai |alphai|\n"""
	print(informacion.__doc__)

	def compute_dh():
		ta=[]
		Mpaso=matrix([[0,0,0],[0,0,0],[0,0,0]])
		A=[]

		print("\nIntroduzca la tabla de parametros D-H en forma de matriz nx4 con n<=3 y los angulos en grados\nejemplo:  0 3 1 0;90 0 1 0;-90 2 0 0\n")
		ta=np.matrix(input())

		print("\nthetai_1|di_1| ai |alphai|\n")
		print(ta)

		renglones=ta.shape[0]

		for i in range(renglones):
			Mpaso[0,0]=math.cos(math.radians(ta[i,0]))
			Mpaso[0,1]=-math.cos(math.radians(ta[i,3]))*(math.sin(math.radians(ta[i,0])))
			Mpaso[0,2]=math.sin(math.radians(ta[i,3]))*math.sin(math.radians(ta[i,0]))

			Mpaso[1,0]=math.sin(math.radians(ta[i,0]))
			Mpaso[1,1]=math.cos(math.radians(ta[i,3]))*math.cos(math.radians(ta[i,0]))
			Mpaso[1,2]=-math.sin(math.radians(ta[i,3]))*math.cos(math.radians(ta[i,0]))
			
			Mpaso[2,1]=math.sin(math.radians(ta[i,3]))
			Mpaso[2,2]=math.cos(math.radians(ta[i,3]))
			
			A.append(Mpaso)

			if i ==0:
				mult=A[i]
			if i == 1:
				Costheta2=mult[0,0]
				Sintheta2=mult[1,0]
				mult=mult*A[i]
			else:
				mult=mult*A[i]

			print("\nLa matriz es A",i,"_",i+1,"es:\n",A[i])

		p=matrix([[ta[0,2]*math.cos(math.radians(ta[0,0]))],[ta[0,2]*math.sin(math.radians(ta[0,0]))+ta[1,2]*Sintheta2],[ta[0,1]+ta[1,1]+ta[2,1]]])		
 
		print("\n\nLa matriz de rotacion es igual a:\n",mult)
		print("\nEl desplazamiento es:\n",p)

		Mtotal=matrix([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]])
		for i in range(3):
			for j in range(3):
				Mtotal[i,j]=mult[i,j]
			Mtotal[i,3]= p[i]
		print("El calculo numerico de la transformacion D-H es:\n",Mtotal)