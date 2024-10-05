import sys
import getopt
from . import connect
#from PERISHDB import DBDB as PerishDb
from . import perish_db

def usage():
    print("Usage: python tool.py <dbname> <verb> <key> [value]")
    print("  <dbname>: The database file to use")
    print("  <verb>: 'get', 'set', or 'delete'")
    print("    'get' requires a <key>")
    print("    'set' requires a <key> and <value>")
    print("    'delete' requires a <key>")
    print("\nExample:")
    print("  python tool.py mydb.db set mykey myvalue")
    print("  python tool.py mydb.db get mykey")
    print("  python tool.py mydb.db delete mykey")

OK = 0         # Success
BAD_ARGS = 1   # Incorrect number of arguments
BAD_VERB = 2   # Invalid verb (not 'get', 'set', 'delete')
BAD_KEY = 3    # Key not found


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
	db = connect(dbname)
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
