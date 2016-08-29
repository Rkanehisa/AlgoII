from queue import PriorityQueue
from sys import stdin

class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item

def main():
        T = int(stdin.readline())

        for t in range(T):
                q = MyPriorityQueue()
                m = int(stdin.readline())
                n = int(stdin.readline())
                matrix = [[int(x) for x in stdin.readline().split()]for y in range(m)]
                dj = [[1000000 for x in range(n)]for y in range(m)]
        
                #dijkstra
                dj[0][0] = matrix[0][0]
                posX = 0
                posY = 0
                q.put((0,0),0)
                while(True):
                        if(posX > 0):
                                if(dj[posX][posY]+matrix[posX-1][posY] < dj[posX-1][posY]):
                                        dj[posX-1][posY] = dj[posX][posY]+matrix[posX-1][posY]
                                        q.put((posX-1,posY),dj[posX][posY]+matrix[posX-1][posY])
                                                
                        if(posY > 0):
                                if(dj[posX][posY]+matrix[posX][posY-1] < dj[posX][posY-1]):
                                        dj[posX][posY-1] = dj[posX][posY]+matrix[posX][posY-1]
                                        q.put((posX,posY-1),dj[posX][posY]+matrix[posX][posY-1])
                                     
                        if(posX < m-1):
                                if(dj[posX][posY]+matrix[posX+1][posY] < dj[posX+1][posY]):
                                        dj[posX+1][posY] = dj[posX][posY]+matrix[posX+1][posY]
                                        q.put((posX+1,posY),dj[posX][posY]+matrix[posX+1][posY])
                                
                        if(posY < n-1):
                                if(dj[posX][posY]+matrix[posX][posY+1] < dj[posX][posY+1]):
                                        dj[posX][posY+1] = dj[posX][posY]+matrix[posX][posY+1]
                                        q.put((posX,posY+1),dj[posX][posY]+matrix[posX][posY+1])
                                
                        posX,posY = q.get()
                        
                        if(q.empty()):
                                break
                print(dj[m-1][n-1])
main()
