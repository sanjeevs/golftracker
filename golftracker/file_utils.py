#
# File manipulations.
import pathlib
import os


def basename(fname):
	"""
	Return the base name of windows file name. 

	>>> basename('c:/a/b/c.txt')
	'c.txt'

	>>> basename('a.txt')
	'a.txt'

	"""
	p = pathlib.Path(fname)
	return os.path.basename(p)

def search_file(search_dir, fname):
	"""
	Check whether the file exists in the search dir.

	>>> search_file(".", "file_utils.py")
	'.\\\\file_utils.py'

	"""
	p = pathlib.Path(fname)
	f = os.path.join(search_dir, fname)
	if os.path.exists(f):
		return f
	else:
		return None