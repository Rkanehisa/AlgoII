n = 0
tiles = []
memo = []

def pd(l,m):
      global n
      global tiles
      global memo
      
      if(l == 0 or m == 0):
            return 0
      if(l == 1 and m == 1):
            return tiles[1][1]
      if(memo[l][m] != -1):
            return memo[l][m]

      aux1 = pd(l-1,m)
      aux2 = pd(l,m-1)
      maxValue = max(aux1,aux2)
      memo[l][m] = maxValue+tiles[l][m]
      return memo[l][m] 

def main():
      global n
      global tiles
      global memo
      
      while(True):
            n = int(input())
            if(n == 0):
                  print("*")
                  break
            
            tiles = [[0 for x in range(101)] for y in range(101)]
            memo = [[-1 for x in range(101)] for y in range(101)]
            for i in range(n):
                  t = tuple(map(int,input().split()))
                  tiles[int(t[0])][int(t[1])] += 1
            print(pd(100,100))
      
main()
