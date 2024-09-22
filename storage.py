import portalocker
class Storage(object):
	def lock(self):
		if not self.locked:
			portalocker.lock(self._f, portalocker.LOCK_EX)
			self.locked = True
			return True
		return False
