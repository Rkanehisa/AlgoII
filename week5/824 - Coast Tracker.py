def solve(d):
	for i in range(8):
		next_x = 1 + dx[(d+i+5)%8]
		next_y = 1 + dy[(d+i+5)%8]
		if M[next_y,next_x]:
			return (d+i+5)%8

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
M = {(i,j):False for i in range(3) for j in range(3)}

while True:
	inp = input()
	if inp == "-1":
		break
	x, y, d = list(map(int, inp.split()))
	for i in range(8):
		xx, yy, t = list(map(int, input().split()))
		xx -= x-1
		yy -= y-1
		M[2-yy,xx] = bool(t)
	print(solve(d))
