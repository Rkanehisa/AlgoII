#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <stdio.h>

#define MAX 110

using namespace std;

typedef std::tuple<int,int,int, int> i4tuple;

vector<int> seq;
int graph[MAX][MAX];
int used[MAX][MAX];
int y_beg, y_end;
vector<i4tuple> solutions;

void getSeq(int n){
	int k, j, c;
	k = 0;
	j = 1;
	while(n--){
		if(k == j){
			j++;
			k = 0;
		}
		k ++;
		seq.push_back(k);
	}
}

void init(){
	for(int i = 0; i < MAX; i++){
		for(int j = 0; j < MAX; j++){
			graph[i][j] = 0;
			used[i][j] = 0;
		}
	}
}

void getMatrix(int n, int m){
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			cin >> graph[i][j];
		}
	}
}

void backtrack(int n, int m, int x, int y, int index){
	if(x >= n | x < 0 | y >= m | y < 0)
		return;
	if (graph[x][y] != seq[index])
		return;
	if (x == n - 1){
		i4tuple t = i4tuple(1, y_beg + 1, n, y + 1);
		solutions.push_back(t);
		return;
	}
	if (used[x][y] == 1)
		return;

	used[x][y] = 1;
	backtrack(n, m, x, y+1, index+1);
	backtrack(n, m, x, y-1, index+1);
	backtrack(n, m, x-1, y, index+1);
	backtrack(n, m, x+1, y, index+1);
	used[x][y] = 0;
}

int main(){
	getSeq(100*100);
	init();

	int n, m, q;
	cin >> q;
	while(q--){
		cin;
		cin >> n;
		cin >> m;
		getMatrix(n, m);
		for(int i = 0; i < m; i++){
			y_beg = i;
			backtrack(n, m, 0, i, 0);
		}
		sort(solutions.begin(), solutions.end());
		printf("%d %d\n%d %d\n", 1, get<1>(solutions[0]), n, get<3>(solutions[0]));
		if(q){
			printf("\n");
		}
		//cout << std::get<0>(solutions[0]) << " " << std::get<1>(solutions[0]) << "\n" 
		//<< std::get<2>(solutions[0]) << " " << std::get<3>(solutions[0]) << "\n" << endl;

		solutions.erase(solutions.begin(), solutions.end());
	}
	return 0;
}
