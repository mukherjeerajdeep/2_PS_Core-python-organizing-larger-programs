# demo_reader/multireader.py

# Now import the other helpers named bzipped and gzipped to use here

import os
from path2.demo_reader.compressed import bzipped, gzipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener
}


class MultiReader:
    def __init__(self, filename):
        # self.filename = filename
        # self.f = open(filename, 'rt')

        # example.bz is a filename so index [1] is the type of the zip
        extension = os.path.splitext(filename)[1]
        # default is open for file reader if the file format is other than bz or gz.
        # The get() method on dict is used for that purpose.
        opener = extension_map.get(extension, open)
        self.f = opener(filename, mode='rt', encoding="utf-8")

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()
