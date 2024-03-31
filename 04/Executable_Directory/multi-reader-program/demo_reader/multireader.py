# demo_reader/multireader.py
# Now import the other helpers named bzipped and gzipped to use here

import os
from demo_reader.compressed import bzipped, gzipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener
}


class MultiReader:
    def __init__(self, filename):
        # example.bz is a filename so index [1] is the type of the zip
        extension = os.path.splitext(filename)[1]
        # default is open for file reader if the file format is other than bz or gz.
        # The get() method on dict is used for that purpose.
        opener = extension_map.get(extension, open)
        self.f = opener(filename, mode='rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()
