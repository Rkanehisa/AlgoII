seq = ""
subseq = ""

def count(nSeq,nSubseq,table):
      global seq
      global subseq
      
      if(nSubseq == 0):
            return 1
      if(nSeq == 0):
            return 0

      
      result = table[nSeq-1][nSubseq]
      if(seq[-nSeq] == subseq[-nSubseq]):  
            result += table[nSeq - 1][nSubseq - 1]

      return result
      

def strSubseq():
      global seq
      global subseq
      m = len(seq)+1
      n = len(subseq)+1

      table = [[None for x in range(n)] for y in range(m)]

      for i in range(m):
            for j in range(n):
                  table[i][j] = count(i,j,table)
      
      
      print(table[m-1][n-1])
      
      
def main():
      global seq
      global subseq
      nTimes = int(input())
      for i in range(nTimes):
            seq = input()
            subseq = input()
            strSubseq()

main()
                  
