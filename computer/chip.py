from .err import Handler

@Handler
def MUX(a,b,s):
	if not s:
		if a or b:
			if b and not a: return 0
			elif a and not b: return 1
			elif a and b: return 1
		else: return 0
	elif s:
		if a or b:
			if not a and b: return 1
			elif a and not b: return 0
			elif a and b: return 1
		else: return 0
	else: return 0

@Handler
def HALF_ADDER(a,b):
	from .gate import AND,OR,XOR
	cout, sum = AND(a,b),XOR(a,b)
	return sum, cout

@Handler
def FULL_ADDER(a,b,cin):
	from .gate import AND,OR,XOR
	sum, cout = HALF_ADDER(a,b)
	cout0, sum = AND(cin,sum),XOR(sum,cin)
	cout, sum = OR(cout,cout0), sum
	return sum, cout

@Handler
def ALU(a,b,cin,s0,s1):
	sum, cout = FULL_ADDER(a,b,cin)

	# Logic Units
	from .gate import AND,NOR,XOR
	l0 = AND(a,b)
	l1 = NOR(a,b)
	l2 = XOR(a,b)

	m0 = MUX(sum,l0,s0)
	m1 = MUX(l1,l2,s0)
	m2 = MUX(m0,m1,s1)
	return m2, cout

@Handler
def DEMUX2(x,s):
	if x:
		if s: return 0,1
		elif not s: return 1,0
	else: return 0,0

@Handler
def DEMUX4(x,s0,s1):
	if x:
		if not s0 and not s1: return 1,0,0,0
		elif s0 and not s1: return 0,1,0,0
		elif not s0 and s1: return 0,0,1,0
		elif s0 and s1: return 0,0,0,1
	else: return 0,0,0,0
