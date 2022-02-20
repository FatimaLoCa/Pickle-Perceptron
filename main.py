from os import remove
import numpy as np
import pickle
from Perceptron import Perceptron_

matriz = np.loadtxt('dataset_Perceptron.txt',delimiter = ',')
a = 0.03
b = -0.5
W = [0.2,0.5]

p = Perceptron_(a,b,W,matriz)
#p.normalizar()
#p.iniciar()

try:     
    file = open("backup","rb")
    print(file) # File handler

    p_ = pickle.load(file)
    p_.muestra()
    file.close()
    p_.iniciar() #continua 

    remove('C:/Users/lopez/Documents/INCO/9. noveno 2022A/Tolerante a fallas/Programas/Perceptron Checkpoint/backup')

except FileNotFoundError: 
    print('No existe el fichero pero ahorita lo creamos! ')
    #exit()
    p = Perceptron_(a,b,W,matriz)
    p.normalizar()
    p.iniciar()

    remove('C:/Users/lopez/Documents/INCO/9. noveno 2022A/Tolerante a fallas/Programas/Perceptron Checkpoint/backup')
