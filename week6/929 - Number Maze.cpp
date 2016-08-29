#include<stdio.h>
#include<queue>
#include<vector>

using namespace std;

int matrix [1000][1000];
int dj [1000][1000];
int m,n;

typedef pair<int, int> pos;
typedef pair<int, pos> elm;
priority_queue<elm, vector<elm>, greater<elm> > q;

void init(){
    for(int i =0 ;i < m; i++){
        for (int j = 0; j < n; j++){
            dj[i][j] = 10000000;

        }
    }
}



int main(){
    int T;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&m);
        scanf("%d",&n);
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                scanf("%d",&matrix[i][j]);
            }
        }
        init();

        q.push(make_pair(matrix[0][0],pos(0,0)));
        dj[0][0] = matrix[0][0];
        //printf("%d,%d", q.top().first,q.top().second.first);
        while(true){
            elm atual = q.top();
            q.pop();
            int posX = atual.second.first;
            int posY = atual.second.second;
            if(posX > 0){
                if(dj[posX][posY]+matrix[posX-1][posY] < dj[posX-1][posY]){
                    dj[posX-1][posY] = dj[posX][posY]+matrix[posX-1][posY];
                    q.push(make_pair(matrix[posX-1][posY]+dj[posX][posY],pos(posX-1,posY)));
                }
            }

            if(posY > 0){
                if(dj[posX][posY]+matrix[posX][posY-1] < dj[posX][posY-1]){
                    dj[posX][posY-1] = dj[posX][posY]+matrix[posX][posY-1];
                    q.push(make_pair(matrix[posX][posY-1]+dj[posX][posY],pos(posX,posY-1)));
                }
            }
            if(posX < m-1){
                if(dj[posX][posY]+matrix[posX+1][posY] < dj[posX+1][posY]){
                    dj[posX+1][posY] = dj[posX][posY]+matrix[posX+1][posY];
                    q.push(make_pair(matrix[posX+1][posY]+dj[posX][posY],pos(posX+1,posY)));
                }
            }

            if(posY < n-1){
                if(dj[posX][posY]+matrix[posX][posY+1] < dj[posX][posY+1]){
                    dj[posX][posY+1] = dj[posX][posY]+matrix[posX][posY+1];
                    q.push(make_pair(matrix[posX][posY+1]+dj[posX][posY],pos(posX,posY+1)));
                }
            }
            if(q.empty()) break;


        }
        printf("%d\n",dj[m-1][n-1]);

    }


    return 0;
}
