from .api import *
from .err import *

_lreg = {'filename': r'^.*[A-Za-z0-9]\.+log$'}
_ltype = {0:'INFO', 1:'ERROR', 2: 'WARNING', 3: 'DEBUG'}


# Exceptions
class Logger_CodeError(Exception):
	pass

class Logger_FileError(Exception):
	pass

if __name__ == '__main__':
	pass
