#include <iostream>
#include <cmath>
#include <stdio.h>

using namespace std;

int x[200];
int y[200];
double M[200][200];
 
int main ()
{
    int n, T=1;
 
    while (true) {
        cin >> n;

        if(n==0)
            break;
 
        for(int i = 0; i < n; i++)
            cin >> x[i] >> y[i];

        for(int i = 0; i < n; i++)
            for(int j = i+1; j < n; j++)
                M[i][j] = M[j][i] = sqrt(pow(x [i] - x [j], 2) + pow(y [i] - y [j], 2));

        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                for(int k = 0; k < n; k++)
                    M[j][k] = min(M[j][k], max(M[j][i], M[i][k]));

 
        cout << "Scenario #" << T << "\n" << "Frog Distance = ";
        printf("%.3lf\n\n", M[0][1]);
        T++;
    }
 
    return 0;
}