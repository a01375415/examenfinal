#Valores inicializados
nodos='12345678' #Aquí se introducen los nombres de los nodos
n=len(nodos)
menorval=[0]
path=[0]

#Matriz de conexiones: los nodos columna se conectan con las
#                       filas
    #1 2 3 4 5 6 7 8
M=[ [0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0],
    [2,1,0,0,0,0,0,0],
    [0,5,2,0,0,0,0,0],
    [0,2,1,3,0,0,0,0],
    [0,0,4,6,3,0,0,0],
    [0,0,0,8,7,5,0,0],
    [0,0,0,0,0,2,6,0]]

#Se encuentra la menor distancia para cada nodo y su ruta
for row in range(1,n):
    menor=[]
    nodo=[]
    for col in range(n):
        if M[row][col]!=0:
            menor.append(M[row][col]+menorval[col])
            nodo.append(nodos[col])
    menorval.append(min(menor))
    path.append(nodo[menor.index(min(menor))])

i=n-1
s=[]

#Obtención de ruta para el último nodo
while i!=0:
    s.insert(0,path[i])
    i=int(nodos.index(path[i]))
s.append(nodos[-1])

#Salida en pantalla
print("La distancia más corta es",menorval[-1],"unidades por la ruta",*s)