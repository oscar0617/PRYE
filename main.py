from sys import stdin
from collections import Counter
import math

def sumatoria(arreglo):
    cont = 0
    for i in range(len(arreglo)):
        cont += arreglo[i]
    return cont

def promedio(arreglo):
    arreglo = sorted(arreglo)
    n = int(len(arreglo))
    cont = 0
    for i in range(n):
        cont += arreglo[i]
    promedio = cont/n
    return promedio

def mediana(arreglo):
    arreglo = sorted(arreglo)
    n = int(len(arreglo))
    if n % 2 == 0:
        res = (arreglo[int(n/2 - 1)] + arreglo[int((n//2))]) / 2
        return res
    else:
        res = (arreglo[int((n+1)/2 +1)])
        return res

def moda(arreglo):
    arreglo = sorted(arreglo)
    res = Counter(arreglo)
    return (max(res, key=res.get))

def media_recortada(arreglo):
    arreglo = sorted(arreglo)
    porcentaje = 30
    x = int((porcentaje*len(arreglo))/100)
    print(x)
    for i in range(x):
        arreglo.pop(0)
    for i in range(x):
        arreglo.pop()
    return promedio(arreglo)

def desviacionMedia(arreglo):
    cont = 0
    prom = promedio(arreglo)
    for i in range(len(arreglo)):
        cont+= abs(arreglo[i]-prom)
    res = cont/len(arreglo)
    return res

def varianza(arreglo):
    cont= 0
    prom = promedio(arreglo)
    for i in range(len(arreglo)):
        cont+= (arreglo[i]-prom)**2
    res = cont/len(arreglo)-1
    return res

def desviacionEstandar(arreglo):
    r = varianza(arreglo)
    res = math.sqrt(r)
    return res

def main():
    arreglo = list(map(int, stdin.readline().strip().split()))
    print("Mediana", mediana(arreglo))
    print("Moda", moda(arreglo))
    print("Media Recortada", media_recortada(arreglo))
    print("Desviación Media", desviacionMedia(arreglo))
    print("Varianza", varianza(arreglo))
    print("Desviación estandar", desviacionEstandar(arreglo))
main()