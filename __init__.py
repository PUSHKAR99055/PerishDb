import os
from .interface import DBDB
def connect(dbname):
	try:
		f = open(dbname, 'r+b')
	except IOError:
		fd = os.open(dbname, os.O_RDWR | os.O_CREAT)
		f = os.fdopen(fd, 'r+b')
		#this function calls create a file object ('f') from a file decriptor ('fd')
	return DBDB(f)
	
