import portalocker
class LogicalBase(object):
	def get(self, key):
		if not self._storage.locked:
			self._refresh_tree_ref()
		return self._get(self._follow(self._tree_ref), key)
	def _refresh_tree_ref(self):
		self._tree_ref = self.node_ref_class(address = self._storage.get_root_address())
	def set(self, key, value):
		if self._storage_lock():
			self._refresh_tree_ref()
		self._tree_ref = self._insert(self._follow(self._tree_ref), key, self.value_ref_class(value))
	def lock(self):
		if not self.locked:
			portalocker.lock(self._f, portalocker.LOCK_EX)
			self.locked = True
			return True
		else:
			return False
	def commit(self):
		self._tree_ref.store(self._storage)
		self._storage.commit_root_address(self._tree_ref.address)

class ValueRef(object):
	def store(self, storage):
		if self._referent is not None and not self._address:
			self.prepare_to_store(storage)
			self._address = storage.write(self.referent_to_string(self._referent))
	def store(self, storage):
		if self._referent is not None and not self._address:
			self.prepare_to_store(storage)
			self._address = storage.write(self.referent_to_string(self._referent))
