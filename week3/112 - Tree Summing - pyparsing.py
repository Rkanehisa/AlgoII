# This uses pyparsing and will
# give a Runtime Error on UVA
# --- Works with any input

from pyparsing import *
import re

def updateStack(string, stack):
	for i in string:
		if i == '(':
			stack += 1
		elif i == ')':
			stack -= 1
	return stack

def pScan(string, s):
	stack = updateStack(string, s)
	if stack == 0:
		return string
	else:
		new = input()
		return string + pScan(new, stack)

def traverse(T, num): 
	if T == []:
		return False
	elif T[1] == [] and T[2] == []:
		return int(T[0]) == num
	return traverse(T[1], num - int(T[0])) or traverse(T[2], num - int(T[0]))

def main():
	integer = Regex(r"(-?\d+)")
	sexp = Forward()
	LPAR = Suppress("(")
	RPAR = Suppress(")")
	sexp << ( Group(LPAR + RPAR) | LPAR + Group(integer + sexp + sexp) + RPAR)
	while True:
		try:
			input_ = input()
		except EOFError:
			break
		num, treeInput = input_.split(" ", 1)
		pattern = re.compile(r'\s+')
		treeInput = re.sub(pattern, '', pScan(treeInput, 0))
		tmp = sexp.parseString(treeInput)
		Tree = tmp.asList()
		f = lambda x: "yes" if x == True else "no"
		print(f(traverse(Tree[0], int(num))))
main()