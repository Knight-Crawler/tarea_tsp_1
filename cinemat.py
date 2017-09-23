#!/usr/bin/python
import numpy as np
import math as m
from T1_1 import *
import sympy
from sympy import Matrix

class Cinematica(object):

    def __init__(self,theta_i,d_i,a_i,alpha_i,A0_n,zetas,oi,on):
        self.theta = m.radians(theta_i)
        self.d = d_i
        self.alpha = m.radians(alpha_i)
        self.a = a_i
	self.A0n=A0_n
	self.Zetas=zetas
	self.Oi=oi
	self.On=on
    def compute_dh(self):
        c_th,s_th = m.cos(self.theta), m.sin(self.theta)
        c_alp,s_alp = m.cos(self.alpha), m.sin(self.alpha)
        return np.array([[c_th,(-1*s_th*c_alp),(s_th*s_alp),(self.a*c_th)],
                         [s_th,(c_th*c_alp),(-1*c_th*s_th),(self.a*s_th)],
                         [0,s_alp,c_alp,self.d],
                         [0,0,0,1]])

    def compute_jacobian(self): #----------------------------------------------------------------------------------------------------------
	z=self.Zetas
	z=z.reshape(1,3)
	Oi=self.Oi
	Oi=Oi.reshape(1,3)
	On=self.On
	On=On.reshape(1,3)    
	Jv=np.cross(z,On-Oi)
	Jv=Jv.reshape(3,1)
	return Jv
	#A_0n,np.array([0,0,1,0]).reshape(4,1)

       #Ti = Cinematica(thetas[i],ds[i],a_s[i],alphas[i],A0n).compute_dh()

print("----------Ingrese el numero de GDL----------")
GDL = int(input())
#N=GDL
thetas=[]
alphas=[]
ds=[]
a_s=[]
#thetas = [0,90,-90,0]
print("-----Ahora ingrese los angulos Thetas-----")
for i in range(GDL):
    print 'Ingresa theta',i+1
    thetas.append(int(input()))

#alphas = [0,0,0,0]
print("-----Ingrese los angulos alphas-----")
for i in range(GDL):
    print 'Ingresa alpha',i+1
    alphas.append(int(input()))

#ds = [l3,l4,0,2]2,1,0,2
print("-----Ingrese los desplazamientos en Z-----")
for i in range(GDL):
    print 'Ingresa d',i+1
    ds.append(int(input()))

#a_s = [l1,l2,0,0]1,1,0,0
print("-----Ingrese los desplazamientos en X-----")
for i in range(GDL):
    print 'Ingresa a',i+1
    a_s.append(int(input()))

def main():             #----------------------------------------------------------------------------------------------------------------
    A_0n = np.eye(4)
    z=[]	
    Oi=[]
    o=mat_x_vec(A_0n,np.array([0,0,0,1]).reshape(4,1))
    o=newArray=o[[0,1,2],:]
    Oi.append(o)
   #print(O)
    for i,v in enumerate(thetas):

    	A0n=sympy.Matrix(A_0n)
        print("Params A0"+str(i+1))
        print(thetas[i],ds[i],a_s[i],alphas[i])
        Ti = Cinematica(thetas[i],ds[i],a_s[i],alphas[i],A0n,0,0,0).compute_dh()
        print(Ti)
        A_0n = mat_x_mat(A_0n,Ti)
    	M=mat_x_vec(A_0n,np.array([0,0,1,0]).reshape(4,1))
        M=newArray=M[[0,1,2],:]
        z.append(M)
        #print(z[i])

        o=mat_x_vec(A_0n,np.array([0,0,0,1]).reshape(4,1))
        o=newArray=o[[0,1,2],:]
        Oi.append(o)
#	print(O)


    A0n=sympy.Matrix(A_0n)

    #x=mat_x_vec(A_0n,np.array([0,0,0,1]).reshape(4,1))
    #print(x)

    print 'Transformation Matrix A0',GDL
    print(A_0n)
    print('End Effector Position Vector:')
    #multiply Transformation matrix times n = (0,0,0,1)
    #x_0n = mat_x_vec(A_0n,np.array([0,0,0,1]).reshape(4,1))

    x=mat_x_vec(A_0n,np.array([0,0,0,1]).reshape(4,1))
    #print(x)
    Jv=[]
    Jw=[]
    for i in range(GDL):
	if thetas[i] == 0:
	    Jv.append(z[i])
	    Jw.append([[0],[0],[0]])
	else:
    	    Jv.append(Cinematica(0,0,0,0,0,z[i],Oi[i],Oi[GDL]).compute_jacobian())	
	    Jw.append(z[i])
    Jv=np.asmatrix(np.array(Jv))
    Jv=Jv.T
    Jw=np.asmatrix(np.array(Jw))
    Jw=Jw.T	
    #print np.array(Jw)
    print 'Matriz Jacobiana\n'
    print 'Jv=\n',Jv
    print 'Jw=\n',Jw

if __name__ == '__main__':
    main()


#        Ti = Cinematica(thetas[i],ds[i],a_s[i],alphas[i],A0n).compute_dh()























