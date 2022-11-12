import numpy as np
import time

#Función a integrar
f= lambda x: np.sin(4*x)*np.exp(-2*x)

#Función para la regla de Simpson 3/8 compuesta
def simpson38comp(a,b,n,f):
    h=(b-a)/n
    mul=np.full(n-1,3)
    mul[2::3]=2
    val=f(np.linspace(a+h,b,n-1))
    suma=np.dot(val,mul.transpose())+f(a)+f(b)
    return suma*(3*h/8)

#Valor exacto
valorex=np.exp(-6)*(-np.sin(12)/10-np.cos(12)/5)+1/5

#Medición de tiempo y solución obtenida
start = time.time()
res=simpson38comp(0,3,99999999,f)
end = time.time()

#Salidas en pantalla
print("El resultado es",round(res,9))
print("Ejecutado en {} seg".format(round(end-start,4)))
print("Error absoluto de",abs(res-valorex))