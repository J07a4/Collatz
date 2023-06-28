from matplotlib import pyplot as plt
import math
import cmath
from matplotlib import cm as cm
from Color_functions import *
import os

res=1080 #540
xmax=10
ymax=10
xcent=1
ycent=0


#Cargamos en memoria los valores del gradiente
Gradient=Rainbow_Gradient()



def formamalla(res,xmax,ymax):
    PuntosX=[]
    PuntosY=[]
    for i in range(2*res):
        for t in range(2*res):
            PuntosX.append(2*xmax*(i/res)-2*xmax+xcent)
            PuntosY.append(2*ymax*(t/res)-2*ymax+ycent)
    return([PuntosX,PuntosY])

def color(Malla,funcion):
    Color=[]
    for i in range(len(Malla[0])):
        Color.append(funcion(Malla[0][i],Malla[1][i]))
    return(Color)

def ImprimePixeles(Malla, funcion):
    plt.figure(figsize=(6,6),constrained_layout=True,dpi=100)
    plt.scatter(Malla[0],Malla[1], marker=',', s=0.5, c=color(Malla, funcion))
    plt.axis('off')
    plt.savefig('g.eps', format='eps')
    plt.show()

def Zoom(funcion,pasos,xmax,ymax):
    xm=xmax
    ym=ymax
    for i in range(pasos):
        Malla=formamalla(res,xm,ym)
        plt.figure(figsize=(6,6),constrained_layout=True,dpi=100)
        plt.scatter(Malla[0],Malla[1], marker=',', s=0.5, c=color(Malla, funcion))
        plt.axis('off')
        plt.savefig('g.eps', format='eps')
        plt.savefig(".\Zoom\Zoom"+str(i)+".png")
        xm=xm*0.5
        ym=ym*0.5

#========================Función de Collatz=============================#

def Collatz (x,y):
    z=complex(x,y)
    rango=200
    for i in range(rango):
        z=0.5*z*cmath.cos(math.pi*z/2)**2+(3*z+1)*cmath.sin(math.pi*z/2)**2
        if z.real**2+z.imag**2 >=math.exp(8):
            return((0,0,0))
        if z.real**2+z.imag**2 <=4:
            return((1,1,1))
    return(Gradient[i])
#=============================================================================#

Zoom(Collatz,2,xmax,ymax)
#ImprimePixeles(formamalla(res,xmax, ymax),Collatz)
