mat = []
walked = []
R = 0
C = 0
def walk(posY,posX):
      global R
      global C
      global walked
      global mat
      
      if((posX < 0 or posX >= C) or (posY < 0 or posY >= R)):
            print(len(walked),"step(s) to exit")
            return
      if(mat[posY][posX] == '1'):
            for i in range(len(walked)):
                  if((posY,posX) == walked[i]):
                        print(i,"step(s) before a loop of",len(walked[i:]),"step(s)")
            return
      walked.append((posY,posX))
      if(mat[posY][posX] == 'N'):
            mat[posY][posX] = '1'
            walk(posY-1,posX)
      if(mat[posY][posX] == 'S'):
            mat[posY][posX] = '1'
            walk(posY+1,posX)
      if(mat[posY][posX] == 'E'):
            mat[posY][posX] = '1'
            walk(posY,posX+1) 
      if(mat[posY][posX] == 'W'):
            mat[posY][posX] = '1'
            walk(posY,posX-1)
             
      

def main():
      global mat
      global R
      global C
      global walked
      while(True):
            R,C,S = list(map(int,input().split()))
            if(R == 0 and C == 0 and S == 0):
                  break

            mat = [[x for x in input()] for y in range(R)]
            walked = []
            walk(0,S-1)
            
main()
