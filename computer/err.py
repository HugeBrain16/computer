class _Logger_ERR_HDN:
	def __init__(self,filename=None,code=None,fxist=None,fexist=None):
		if filename: _Logger_ERR.file(filename)
		if code: _Logger_ERR.code(code)
		if fxist: _Logger_ERR.efile(fxist)
		if fexist: _Logger_ERR.exfile(fexist)

class _Logger_ERR:
	def code(x):
		try:
			from .__init__ import _ltype
			tmp=_ltype[x]
		except:
			from .__init__ import Logger_CodeError
			raise Logger_CodeError(f'Logger_CodeError: invalid log code for `{x}`')
	
	def file(fname):
		from .api import Logger_UTILS
		tmp=Logger_UTILS.checkf(fname)
		if tmp == False: 
			from .__init__ import Logger_FileError
			raise Logger_FileError(f'Logger_FileError: invalid file format for `{fname}`')
	
	def efile(fname):
		from .api import Logger_UTILS
		tmp=Logger_UTILS.fexist(fname)
		if not tmp:
			from .__init__ import Logger_FileError
			raise Logger_FileError(f'Logger_FileError: File `{fname}` did not exists')
	
	def exfile(fname):
		from .api import Logger_UTILS
		tmp=Logger_UTILS.fexist(fname)
		if tmp:
			from .__init__ import Logger_FileError
			raise Logger_FileError(f'File `{fname}` already exists')
