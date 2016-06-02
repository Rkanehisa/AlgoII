def stern_brocot_ancestors(p, q):
	while True:
		if p == q:
			return
		elif p < q:
			q = q - p
			yield "L"
		else:
			p = p - q
			yield "R"

def main():
	while True:
		inp = input().split()
		p, q = int(inp[0]), int(inp[1])
		if p == 1 and q == 1:
			break
		gen = stern_brocot_ancestors(p,q)
		for i in gen:
			print(i, end="")
		print()
main()