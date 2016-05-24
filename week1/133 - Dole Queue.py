#Flawless Nipponese Programming

#le entrada
#cria array
#declara os oficial
#laço(enquanto não acabar)
#   oficial_1 anda
#   oficial_2 anda
#   teste se é o mesmo
#   imprime
#   remove
#fim

def testaArray(array):
    k = 0
    for i in array:
        k += i
    pass
    return k == 0
pass

def walk(array,off,d,Size):
    tmp = (off)

    if(d == 0):
        tmp = (tmp+1)%Size
        if(array[tmp] == 0):
            return walk(array,tmp,d,Size)
        else:
            return tmp
        
    else:
        tmp = (tmp-1)%Size
        if(array[tmp] == 0):
            return walk(array,tmp,d,Size)
        else:
            return tmp
pass

def imprime(array):
    for i in range(0,len(array)-1):
        if(array[i][0] != array[i][1]):
            print("%3d%3d" % (array[i][0],array[i][1]),end=",")
        else:
            print("%3d" % (array[i][0]),end=",")

    if(array[len(array)-1][0] != array[len(array)-1][1]):
        print("%3d%3d" % (array[len(array)-1][0],array[len(array)-1][1]))
    else:
        print("%3d" % (array[len(array)-1][0]))

pass

def funcInput():
    tmp = input()
    tmp = tmp.split(" ")
    return int(tmp[0]),int(tmp[1]),int(tmp[2])
pass

N,k,m = funcInput()
while(N != 0 and k != 0 and m != 0):

    array = [i for i in range(1,N+1)]

    off1 = 0
    off2 = N-1

    string = []

    while(not testaArray(array)):
        for i in range(k-1):
            off1 = walk(array,off1,0,N)
        pass

        for i in range(m-1):
            off2 = walk(array,off2,1,N)
        pass
        
        string.append((array[off1],array[off2]))
        
        array[off1] = 0
        array[off2] = 0

        if(testaArray(array)):
            break
        pass

        off1 = walk(array,off1,0,N)
        off2 = walk(array,off2,1,N)
    pass

    imprime(string)
    N,k,m = funcInput()
pass
