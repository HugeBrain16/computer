from .__init__ import _ltype, _lreg
from .err import _Logger_ERR_HDN, _Logger_ERR

import re, os

class Logger_UTILS:
	def checkf(filename):
		if re.match(_lreg['filename'],filename): return True
		else: return False

	def remove(fname):
		_Logger_ERR_HDN(filename=fname,fxist=fname)
		os.remove(fname)
	
	def fexist(fname):
		_Logger_ERR_HDN(filename=fname)
		return os.path.exists(fname)

class Logger:
	def __init__(self,filename):
		self.filename = filename
	
	def print(self,code,text):
		_Logger_ERR_HDN(self.filename,code,self.filename)
		with open(self.filename, 'a+') as f:
			f.write(f'{_ltype[code]}: {text}\r')
	
	def flush(self):
		_Logger_ERR_HDN(self.filename,fxist=self.filename)
		os.remove(self.filename)
		with open(self.filename,'x') as f: pass
	
	def create(self):
		_Logger_ERR_HDN(self.filename,fexist=self.filename)
		with open(self.filename,'x') as f: pass
	
	def remove(self):
		Logger_UTILS.remove(self.filename)
	
	def get(self,code):
		_Logger_ERR_HDN(self.filename,fxist=self.filename)
		ret = list()
		with open(self.filename, 'r') as f:
			buff=f.readlines()
			for i in range(len(buff)):
				tmp=Logger._get(self.filename,i)
				if tmp['CODE'] == code: ret.append(tmp)
		if len(ret): return ret
	
	def _get(filename,line):
		_Logger_ERR_HDN(filename,fxist=filename)
		with open(filename, 'r') as f:
			buff=f.readlines()
			ctx = re.split(': +', buff[line].strip())
			for c in _ltype:
				if _ltype[c] == ctx[0]:
					code = c
			return {'CODE': code, 'TEXT': ctx[1]}

if __name__ == '__main__':
	pass
