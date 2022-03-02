#Stivel Pinilla - 20191020024

matriz = []
matriz2 = []

filas = 3 + 1
columnas = 4 + 1

matriz = [[10,2,20,11,15],[12,7,9,20,25],[4,14,16,18,10],[5,15,15,15,0]]
matriz2 = [[0,0,0,0,15],[0,0,0,0,25],[0,0,0,0,10],[5,15,15,15,0]]
for f in range(filas-1):
    for c in range(columnas-1):
        matriz2[f][c]=0

posF, posC = 0, 0 #Posicion donde nos ubicamos
vOferta, vDemanda = 0, 0 #Son los valores restante de la oferta o demanda en esa posicion
sumaF, sumaC = 0, 0 #Es la suma de los alores en las casillas de costos

while(True):
    sumaF, sumaC = 0, 0
    for f in range(filas-1):
        sumaF += matriz2[f][posC]
    for c in range(columnas-1):
        sumaC += matriz2[posF][c]
    
    vOferta = matriz[filas-1][posC] - sumaF
    vDemanda = matriz[posF][columnas-1] - sumaC

    if(vOferta < vDemanda):
        matriz2[posF][posC] = vOferta
        posC += 1
    elif(vDemanda < vOferta):
        matriz2[posF][posC] = vDemanda
        posF += 1
    elif(vOferta == vDemanda):
        matriz2[posF][posC] = (vOferta+vDemanda)//2
        posC += 1
        posF += 1

    if(posF == filas-1 or posC == columnas-1):
        break

print("Matriz Original")
for f in range(filas):
    print(matriz[f])

print("\nMatriz Final")
for f in range(filas):
    print(matriz2[f])

sumCos = 0

for f in range(filas-1):
    for c in range(columnas-1):
        sumCos += matriz[f][c]*matriz2[f][c]

print("\nCosto Total: ",sumCos)