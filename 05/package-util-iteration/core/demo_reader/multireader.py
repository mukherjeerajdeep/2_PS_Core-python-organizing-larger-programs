# demo_reader/multireader.py
# Now import the other helpers named bzipped and gzipped to use here
import importlib
import os
import pkgutil

import demo_reader.compressed


def iter_namespace(ns_pkg):
    """
    :param ns_pkg: Name-Space package argument
    - it finds all the sub packages
    - Ensure absolute package names
    :return: package
    """
    return pkgutil.iter_modules(
        ns_pkg.__path__,
        ns_pkg.__name__+"."
    )

"""Set comprehension to build the set of modules"""
compression_plugins = {
    importlib.import_module(module_name)
    for _, module_name, _
    in iter_namespace(demo_reader.compressed)
}

"""dict comprehension to build the extension_map"""
extension_map = {
    module.extension: module.opener  # look for module-level attributes
    for module in compression_plugins  # get modules from compression_plugins
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
