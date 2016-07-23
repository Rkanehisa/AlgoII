#include <stdio.h>
#include <stdlib.h>

int n, l;
int v[52];
int memo[52][52];

int pd(int esq, int dir) {

	if(esq+1>=dir) return memo[esq][dir]=0;

	if(memo[esq][dir]!=-1) return memo[esq][dir];

 

	int aux, min, i;
	int cost = v[dir] - v[esq];

	min = pd(esq, esq+1) + pd(esq+1, dir) + cost;

	for(i=esq+2; i<dir; i++) {
		aux = pd(esq, i) + pd(i,dir) + cost;
		if(aux<min) min = aux;
	}
	return memo[esq][dir] = min;
}

 

int main() {

	int i, j;
	
	while(1) {

		scanf("%d", &l);
		if(!l) break;

		scanf("%d", &n);

		for(i=1; i<=n; i++) {
			scanf("%d", &v[i]);
		}

		v[0] = 0;
		v[n+1] = l;

		for(i=0; i<52; i++)
			for(j=0; j<52; j++)
				memo[i][j] = -1;

		 

		printf("The minimum cutting is %d.\n", 

		pd(0, n+1) );
	}

}