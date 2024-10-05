import portalocker
class Storage(object):
	def __init__(self, file):
		self._f = file  # This should accept the file object
		self.locked = False
	def lock(self):
		if not self.locked:
			portalocker.lock(self._f, portalocker.LOCK_EX)
			self.locked = True
			return True
		return False
