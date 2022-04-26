import math
import hashlib
import matplotlib.pyplot as plt
import scipy.integrate
import numpy
import random

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
        x_in_4_bytes = str(100000000*x)[:50] # trunc_x_to_4_bytes
        x_bits = "{0:032b}".format(int(float(x_in_4_bytes))) # trunc_x_in_32_bites
        j = x_bits[31] #0 / 32-b
        for p in range(30,30-b+1,-1): #0,b / 32-b+1,32
            j = j + x_bits[p]
    #    print('j bin:',j)
        j = int(j,2)  # bin(int(j)+1)
    #    print('j int:',j)
        w = x_bits[0] #b / 0 = b-1
        for p in range(32-b-1,-1,-1): #b+1,32 / 1,32-b = b-2,-1,-1
            w = w + x_bits[p]
        w = int(w,2)
        M[j] = max(M[j],ro(w))
    for i in range(0,m):
        Z += 2**(-M[j])
    nzd = alfam*m**2*Z
    print('nzd:',nzd)
    print('M:',M)
    
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
        if g==32:
            break
    return g+1

def md5(f):
    return int(hashlib.md5(str(f).encode()).hexdigest(),16)/2**128

def randsid(x):
    random.seed(x)
    return random.random()

def sha256(x):
    return int(hashlib.sha256(str(x).encode()).hexdigest(),16)/2**256

def randsid8192(x):
    random.seed(x)
    return random.randrange(1000000)%8192/8192

def MinCount(k,h,multizbior):
    M=[]
    for i in range(0,k):
        M.append(1)
    for x in range(0,len(multizbior)):
        if h(multizbior[x]) < M[k-1] and h(multizbior[x]) not in M:
            M[k-1]=h(multizbior[x])
            M.sort()
    if M[k-1]==1:
        i=k
        while M[i-1]==1 and i>0:
            i-=1
        nzd = i
        return nzd
    else:
        nzd = (k-1)/M[k-1]
        return nzd

'''
def hash_sha256_hll(x):
    x= str(int(x)).encode('utf-8')
    return hashlib.sha256(x).hexdigest()
'''

multizbior=[1]
q=1
zakres = 1000
m = 32
k = int(m*5/32)

'''
while len(multizbior)<zakres:
    for j in range(0,len(multizbior)):
        multizbior[j] = multizbior[j] + q
    multizbior.append(multizbior[len(multizbior)-1]+1)
    q+=1
    wynik = MinCount(k,randsid,multizbior)/len(multizbior)
    plt.scatter(len(multizbior),wynik, color='k', marker='.')
plt.xlim([0,zakres])
plt.xlabel('n')
plt.ylabel('nzd/n')
plt.show()
'''

mltzbr=[]
for i in range(50,1050):
    mltzbr.append(i)
print(HyperLogLog(mltzbr,m,md5))

