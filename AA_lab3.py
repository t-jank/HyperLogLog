import math
import hashlib
import matplotlib.pyplot as plt
import scipy.integrate
import numpy


######### zadanie 8 ###########

def integrand(u,m):
    return math.log((2+u)/(1+u),2)**m

def HyperLogLog(multizbior,m,h): # m - liczba podstrumieni, potega dwojki
    Z=0
    M=[]
    b = math.log(m,2)
    alfam = ( m * scipy.integrate.quad(integrand, 0, numpy.inf, args=(m))[0] )**(-1)
    for i in range(0,m):
        M.append(0)
    for e in range(0,len(multizbior)):
        h = h(e)
        j = 1########+
        w = 0
        M[j] = max(M[j],g(w))
    for i in range(0,m):
        Z += 2**(-M[j])
    nzd = alfam*m**2*Z
    
    #korekty:
    if nzd <= 5*m/2:
        V=j###
        if V!=0:
            nzd = -m*math.log(V/m)
    elif nzd > 2**32/30:
        H=2**32
        nzd = -H*math.log((H-nzd)/H)

    return nzd

def g(x): # zwraca pozycje pierwszej jedynki od lewej strony
    g=0
    while x[g]!=49:
        g+=1
    return g+1

def md5(x):
    return int(hashlib.md5(str(x).encode()).hexdigest(),16)/2**128

'''
def hash_sha256_hll(x):
    x= str(int(x)).encode('utf-8')
    return hashlib.sha256(x).hexdigest()
'''
#HyperLogLog([1,2],32,md5)
