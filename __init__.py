def connect(dbname):
	try:
		f = open(dbname, 'r+b')
	except IOError:
		fd = os.open(dbname, os.ORDWR | os.CREATE)
		f = os.fdopen(fd, 'r+b')
		#this function calls create a file object ('f') from a file decriptor ('fd')
	return DBDB(f)
	
