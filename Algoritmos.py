#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from math import sqrt
from random import randrange
import random



def factorizar(n):

    factores = []
    flag = True

    while flag:
        k = int(sqrt(n))
        for p in range(2, k+1):
            r = n % p
            q = int((n - r) / p)
            if r == 0:
                factores.append(p)
                n = q
                break

        if p == k:
            factores.append(n)
            flag = False
    return factores

def divisores(m):
    factor=factorizar(m)
    divisor=[1]
    potencias=[]
    n=len(factor)
    i=0
    while i<n:
        p=factor[i]
        pot=[p]
        d=p
        i+=1
        while i<n and p==factor[i]:
            d=d*p
            pot.append(d)
            i+=1
        potencias.append(pot)
    for a in potencias:
        n=len(divisor)
        for p in a:
            for j in range(n):
                divisor.append(divisor[j]*p)
    return divisor

def ParesOrdenados(vector1):
    vectorResultado = ''


    #Primer vector
    for j in range(len(vector1)):
        for i in range(len(vector1)):
            vectorResultado += '(' + str(vector1[j]) + ',' + str(vector1[i]) + ')'

    return vectorResultado

def SelectRandomValues(conjuntoD):
    NRand = randrange(2, len(conjuntoD))
    Resultado = []
    for i in range(NRand):
        a = random.choice(conjuntoD)
        NoRepetido = True
        while NoRepetido:
            if a in Resultado:
                b = random.choice(conjuntoD)
                if a != b:
                    Resultado.append(b)
                    NoRepetido = False
                else:
                    NoRepetido = True
            else:
                Resultado.append(a)
                NoRepetido = False

    return Resultado

def divisores(numeroNat):
    factores = []
    for i in range(1, numeroNat // 2 + 1):
        if numeroNat % i == 0:
            factores.append(i)
    factores.append(numeroNat)

    return factores

def HallarMatrizDelSubconjunto(conjunto): #1

    matriz = []
    for i in range(len(conjunto)):
        matriz.append([])
        for j in range(len(conjunto)):
            matriz[i].append(0)


    for i in range(len(conjunto)):
        for j in range(len(conjunto)):
            if conjunto[i] in divisores(conjunto[j]):
                matriz[i][j] = 1


    return matriz

def MultiplicarMatricesBooleanas(matriz): #2
    resultado = []
    lengthMatriz = len(matriz)

    for i in range(len(matriz)): #Rellenar matriz de 0
        resultado.append([])
        for j in range(len(matriz)):
            resultado[i].append(0)


    for k in range(lengthMatriz): #Verificar
        for j in range(lengthMatriz):
            for i in range(lengthMatriz):
                 if matriz[k][i] == matriz[i][j] and matriz[i][j] == 1:
                    resultado[k][j] = 1


    return resultado

def EliminarUnos(matriz1, matriz2): #3
    resultadoMatrizSinUnos = matriz1
    for i in range(len(matriz1)):
        for j in range(len(matriz2)):
            if matriz1[i][j] == matriz2[i][j] and matriz1[i][j] == 1:
                resultadoMatrizSinUnos[i][j] = 0

    return resultadoMatrizSinUnos

def ImprimirMatriz(conjuntoOutput):
    for i in range(len(conjuntoOutput)):
        for j in range(len(conjuntoOutput[i])):
            print conjuntoOutput[i][j],
        print

def ComprobarRelacionDeOrdenParcial(matrizM1, matrizM2):
    a = 0
    b = 0
    countsUnos = 0
    matrizAntisimetricaResultado = []
    boolAnsimetrica = False
    matrizTranspuesta = zip(*matrizM1) #Inverter matriz M1

    for i in range(len(matrizM2)):     #Verificar si es reflexiva
        if matrizM1[i][i] == 1:
            a += 1

    for i in range(len(matrizM2)):     #Verificar si es transitiva
        for j in range(len(matrizM1)):
            if matrizM2[j][i] == 1:
                countsUnos += 1
    for i in range(len(matrizM2)):
        for j in range(len(matrizM1)):
            if matrizM2[j][i] == matrizM1[j][i] and matrizM2[j][i] == 1:
                b += 1

    for i in range(len(matrizM1)): #Rellenar matriz matrizAntisimetricaResultado de 0
        matrizAntisimetricaResultado.append([])
        for j in range(len(matrizM1)):
            matrizAntisimetricaResultado[i].append(0)


    for i in range(len(matrizM1)):    #Verificar si es antisimetrica
        for j in range(len(matrizTranspuesta)):
            if matrizM1[i][j] == matrizTranspuesta[i][j] and matrizM1[i][j] == 1:
                matrizAntisimetricaResultado[i][j] = 1

    for i in range(len(matrizAntisimetricaResultado)):
            if matrizAntisimetricaResultado[i][i] == 1:
                boolAnsimetrica = True
            else:
                boolAnsimetrica = False

    if a == len(matrizM1) and b == countsUnos and boolAnsimetrica == True:
        return 'Si es de orden parcial'
    else:
        return 'No es de orden parcial'


if __name__ == "__main__":
    '''
    print divisores(5)

    print divisores2(5)

    ConjuntoD = [1,2,3,4,5,6]
    SubconjuntoD = SelectRandomValues(ConjuntoD)
    print 'ConjuntoD: '
    print ConjuntoD
    print '\n'
    print 'SubconjuntoD: '
    print SubconjuntoD
    print '\n'
    print ParesOrdenados([1,2,3,9,3])
    
    conjunto = [1, 2, 3, 9, 23]

    matrizOutput = HallarMatrizDelSubconjunto(conjunto)
    matrizOutput2 = [[0, 0, 1, 1, 1],
                       [0, 0, 0, 1, 1],
                       [0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0]]

    matrizOutput3 = [[0, 1, 1, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 1, 1]]

    MatrizAVerificar = matrizOutput

    print '\nM1: '
    ImprimirMatriz(MatrizAVerificar)
    MatrizMOutput = MultiplicarMatricesBooleanas(MatrizAVerificar)
    print '\n'
    ordenParcial = ComprobarRelacionDeOrdenParcial(MatrizAVerificar, MatrizMOutput)
    Matri3SinUnos = EliminarUnos(MatrizAVerificar, MatrizMOutput)
    print '\nM2 = M1 o M1: '
    ImprimirMatriz(MatrizMOutput)
    print '\n'
    print "M3 (Eliminar 1's):"
    ImprimirMatriz(Matri3SinUnos)
    print '\n' + ordenParcial
    vector = [1,2,3,4]

    a = ParesOrdenados(vector).replace('(', '').replace(')', '')
    print a
    print vector
    print len(a)/len(vector)
    '''
    a = divisores(40)
    print a
    print '\n'
    print ParesOrdenados(a)
