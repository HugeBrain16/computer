from .err import Handler

@Handler
def OR(x,y):
	if x or y: return 1
	else: return 0

@Handler
def NOR(x,y):
	if x or y: return 0
	else: return 1

@Handler
def AND(x,y):
	if x or y:
		if x == y: return 1
		else: return 0
	else: return 0

@Handler
def NAND(x,y):
	if x or y:
		if x != y: return 1
		else: return 0
	else: return 1

@Handler
def XOR(x,y):
	if x or y:
		if x != y: return 1
		else: return 0
	else: return 0

@Handler
def XNOR(x,y):
	if x or y:
		if x != y: return 0
		else: return 1
	else: return 1

@Handler
def BUFFER(x):
	return x

@Handler
def INVERTER(x):
	if x: return 0
	else: return 1