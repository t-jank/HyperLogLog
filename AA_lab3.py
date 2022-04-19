import math
import hashlib
import matplotlib.pyplot as plt

######### zadanie 8 ###########

def HyperLogLog(multizbior,m,h):
    Z=0
    M=[]
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


def md5(x):
    return int(hashlib.md5(str(x).encode()).hexdigest(),16)/2**128
