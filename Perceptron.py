from copyreg import pickle
from os import truncate
import os
import numpy as np
from numpy.core.fromnumeric import mean
import math
import pickle

class Perceptron_:
    def __init__(self, a, b, W, matriz):
        self.a = a
        self.b = b
        self.W = W
        self.matriz = matriz
        self.X = matriz[:, :2]
        self.Y = matriz[:,2]
        (self.m,self.n) = self.X.shape
        self.y = np.zeros((self.m,1))


    def normalizar(self):
        #NORMALIZACIÓN
        mu = np.mean(self.X,axis=0)
        sigma = np.std(self.X,axis=0)
        xNorm = np.zeros((self.m,self.n))#inicializa
        for j in range(0,self.m):
            for i in range(0,self.n):
                xNorm[j][i] = (self.X[j][i]-mu[i])/sigma[i]        
        self.X=xNorm

    def iniciar(self):
        self.guardar() #guarda los valores en el archivo

        error=0
        for i in range(0,self.m):
            error += np.absolute(self.Y[i]-self.y[i])

        v = np.zeros((self.m,1))

        while error != 0:
            self.guardar()
            for i in range(0,self.m):
                x1i=self.X[i][0]
                x2i=self.X[i][1]
                v[i] = self.W[0]*x1i + self.W[1] * x2i  + self.b # v=w1x1 + w2x2 + b 

                if v[i] > 0:
                    self.y[i] = 1
                else:
                    self.y[i] = 0

                #Calcular error
                print(error)
                error=0
                for j in range(0,self.m):
                    error += np.absolute(self.Y[j]-self.y[j])

                if (self.Y[i]-self.y[i]) != 0:
                    self.W = self.W + self.a * self.X[i,:]
                    self.b = self.b + self.a

        self.muestra()
            
        

    def muestra(self):
        print('w1 = %4f'% self.W[0]) 
        print('w2 = %4f'% self.W[1])
        print('b = %4f'% self.b)

    def guardar(self):
        p_ = self
        
        file = open("backup","wb")
        pickle.dump(p_,file)
        file.close()

    



'''


#DATO DE PRUEBA 1
datoPrueba1 = [34.6237,78.0247]
datoPruebaNorm1 = (datoPrueba1 - mu)/sigma
datoPrueba1 = datoPruebaNorm1
v_datoPrueba1 = v[i] = W[0]*datoPrueba1[0] + W[1] * datoPrueba1[1]  + b # v=w1x1 + w2x2 + b 

if v_datoPrueba1 > 0:
    y_datoPrueba1 = 1
else:
    y_datoPrueba1 = 0

print("\nDatoPrueba 1 = ",datoPrueba1)
print("Clase Dato 1 =", y_datoPrueba1)

#DATO DE PRUEBA 2
datoPrueba2 = [60.1826,86.3086]
datoPruebaNorm2 = (datoPrueba2 - mu)/sigma
datoPrueba2 = datoPruebaNorm2
v_datoPrueba2 = v[i] = W[0]*datoPrueba2[0] + W[1] * datoPrueba2[1]  + b # v=w1x1 + w2x2 + b 

if v_datoPrueba2 >0: 
    y_datoPrueba2 = 1
else:
    y_datoPrueba2 = 0

print("\nDatoPrueba 2 = ",datoPrueba2)
print("Clase Dato 2 =", y_datoPrueba2)
'''








        


