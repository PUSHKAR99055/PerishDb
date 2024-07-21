class Storage(object):
        def commit_root_address(self, root_address):
                self.lock()
                self._f.flush()
                self._seek_superblock()
                self._write_integer(root_address)
                self._f.flush()
                self.unlock()

