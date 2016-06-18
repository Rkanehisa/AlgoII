import re

def updateStack(string, stack):
	for i in string:
		if i == '(':
			stack += 1
		elif i == ')':
			stack -= 1
	return stack

def inputScan(string, s):
	stack = updateStack(string, s)
	if stack == 0:
		return string
	else:
		new = input()
	return string + inputScan(new, stack)

def getIndex(string):
	stack, pos = 1, 0
	for i in string[1:]:
		if stack == 0:
			break
		elif i == "[":
			stack += 1
		elif i == "]":
			stack -= 1
		pos += 1
	return pos

def parseString(num, string):
	if string == "[]":
		return False
		
	L = string[1:-1].split(",", 1)
	root, C = int(L[0]), L[1]
	index = getIndex(C)
	children = [C[:index+1], C[index+2:]]

	if children[0] == "[]" and children[1] == "[]":
		return root == num
	return parseString(num - root, children[0]) or parseString(num - root, children[1])

def main():
	while True:
		try:
			input_ = input()
		except EOFError:
			break
		num, string = input_.split(" ", 1)
		pattern = re.compile(r'\s+')
		string = re.sub(pattern, '', inputScan(string, 0))
		string = string.replace("(",",[").replace(")","]")[1:]
		match = parseString(int(num), string)
		f = lambda x: "yes" if x == True else "no"
		print(f(match))
main()