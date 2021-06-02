import numpy as np
from math import *
from cmath import *
import matplotlib.pyplot as plt
 
w = np.linspace(0.6e6, 1.6e7, 100)
wc = 8.5e6
sigma = 16
 
#print(w)
 
L = sigma/wc
print("L", L)

C = 1/(sigma*wc)
print("C", C)

z = []
 
for i in w:
 numerador =(1j*i*L)*(1/(1j*i*C))
 denominador = (1j*i*L)+(1/(1j*i*C))
 soma = 2j*i*L
 result = (numerador/denominador)+soma
 
 z.append(result)
 
y = [ele.imag for ele in z]
 
print(y)
 
plt.plot(w,y)
plt.grid()
plt.show()

M = 