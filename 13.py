#1, Cree un objeto ndarray unidimensional con una longitud de 10 y todos 0, y luego haga que elquinto elemento sea igual a 1.
import numpy as np
data1=np.zeros((1,10))
data1[0,4]=1
print(data1)

#2, Crea un objeto ndarray con elementos del 10 al 49.
data2=np.arange(10,49,1)
print(data2)

#3, Cree una matriz bidimensional de 4 * 4 y genere el tipo de elemento de matriz
data3=np.zeros((4,4,))
data3.dtype.name

#4, Crea una matriz, que puede completar la transposición de la posición de las coordenadas de(0,1,3) a (3,0,1). ...
data4=np.arange(64).reshape(4,4,4)
print(data4)
data4=data4.transpose(2,0,1)

print("SEXO")
print(data4)

#5Convierta el tipo de datos en las 4 preguntas a float64.
print(data4.dtype.name)
data4.dtype="float32"
print("----")
data4.dtype.name

#6, Consulte el material didáctico para completar las operaciones vectoriales, las operaciones detransmisión y las operaciones escalares entre
#arreglos. A
d1=np.arange(1,6,1)
d2=np.arange(6,11,1)
print(d1)
print(d2)

data6=d1+d2
print("--------")
print(data7[1,0])
print("----------")
print(data7[2,1])