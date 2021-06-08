import numpy as np
from math import *
from cmath import *
import matplotlib.pyplot as plt
from numpy import linalg


w = np.linspace(0.6e6, 1.6e7, 100)
wc = 8.5e6
sigma = 16
L = sigma/wc
C = 1/(sigma*wc)
z = []

for i in w:
    numerador =(1j*i*L)*(1/(1j*i*C))
    denominador = (1j*i*L)+(1/(1j*i*C))
    soma = 2j*i*L
    result = (numerador/denominador)+soma
    
    z.append(result)

y = [ele.imag for ele in z]

plt.plot(w,y)
plt.grid()
plt.show()



res_freq = 10.5e6
R1 = 1
R2 = 0
RC = 1
Uf = 1


M = 1/res_freq
ganhos=[]

def CalcularTransformador(Uf, Rc, m):
    Z=np.array([[R1, -m],[-m, R2+Rc]])
    V=np.array([Uf,0])
    i=np.dot(linalg.inv(Z),V)
    return i[0], i[1]


Ms = np.linspace(M,0,500)

for m in Ms:
    i1= CalcularTransformador(1,RC,m)[0] 
    i2 = CalcularTransformador(1,RC,m)[1]
    G = abs((i2**2/i1**2))
    print(G)
    print(i1, i2)
    ganhos.append(G)

plt.plot(Ms, ganhos)
plt.show()









