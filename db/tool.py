import sys
import getopt

def main(argv):
	print(argv[1])
	if not (4 <= len(argv) <= 5):
		usage() #define usage
		return BAD_ARGS
	dbname, verb, key, value = (argv[1:] + [None])[:4]
	print(dbname, verb, key)
	if verb not in {'get', 'set', 'delete'}:
		usage()
		return BAD_VERB
	db = PerishDb.connect(dbname)
	try:
		if verb == 'get':
			sys.stdout.write(db[key])
		elif verb == 'set':
			db[key] = value
			db.commit()
		else:
			del db[key]
			db.commit()
	except KeyError:
		print("Key not found", file = sys.stderr)
		return BAD_KEY
	return OK
if __name__ == "__main__":
	main(sys.argv)
