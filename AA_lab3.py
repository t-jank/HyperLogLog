

######### zadanie 8 ###########

def HyperLogLog(multizbior,m,h):
    M=[]
    for i in range (0,m):
        M.append(0)
    for x in range(0,len(multizbior)):
        #########
