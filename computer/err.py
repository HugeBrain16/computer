# exceptions
class Computer_ValueError(Exception):
	pass

class Computer_TypeError(Exception):
	pass

def prs_int(x):
	try:
		x = int(x)
	except:
		raise Computer_TypeError(f'Invalid binary value for `{x}`')
	if x > 1 or x < 0: raise Computer_ValueError('Value can\'t be lower than 0 or higher than 1')

def Handler(func):
	def wrp(*args):
		for a in args:
			prs_int(a)
		return func(*args)
	return wrp