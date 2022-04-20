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
    b = int(math.log(m,2))
    alfam = ( m * scipy.integrate.quad(integrand, 0, numpy.inf, args=(m))[0] )**(-1)
    for i in range(0,m):
        M.append(0)
    for e in range(0,len(multizbior)):
        x = h(multizbior[e])
        x_in_4_bytes = str(10000*x)[:4] # trunc_x_to_4_bytes
        x_bits = "{0:032b}".format(int(x_in_4_bytes)) # trunc_x_in_32_bites
        j = x_bits[0]
        for p in range(1,b):
            j = j + x_bits[p]
        j = int(j) + 1  # bin(int(j)+1)
        w = x_bits[b]
        for p in range(b+1,32):
            w = w + x_bits[p]
        M[j] = max(M[j],ro(int(w)))
    for i in range(0,m):
        Z += 2**(-M[j])
    nzd = alfam*m**2*Z
    
    #korekty:
    if nzd <= 5*m/2:
        V=0
        for j in range(0,len(M)):
            if(M[j]==0):
                V+=1
        if V!=0:
            nzd = -m*math.log(V/m)
    elif nzd > 2**32/30:
        H=2**32
        nzd = -H*math.log((H-nzd)/H)

    return nzd

def ro(y): # zwraca pozycje pierwszej jedynki od lewej strony
    g=0
    yy="{0:032b}".format(y)
    while yy[g]!='1':
        g+=1
    return g+1

def md5(x):
    return int(hashlib.md5(str(x).encode()).hexdigest(),16)/2**128

'''
def hash_sha256_hll(x):
    x= str(int(x)).encode('utf-8')
    return hashlib.sha256(x).hexdigest()
'''
print(HyperLogLog([1,2],32,md5))
