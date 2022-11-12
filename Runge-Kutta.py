#Ecuación diferencial a obtener
f1=lambda x,y: x**2+y**2

#Función con Runge-Kutta de 4to orden
def rk(x0,y0,xf,h,f):
    while x0<=xf:
        k1=h*f(x0,y0)
        k2=h*f(x0+h/2,y0+k1/2)
        k3=h*f(x0+h/2,y0+k2/2)
        k4=h*f(x0+h,y0+k3)
        k=1/6*(k1+2*k2+2*k3+k4)
        y0+=k
        x0+=h
    return round(y0,6)

#Salida en pantalla
print(rk(0,1,0.8,0.01,f1))