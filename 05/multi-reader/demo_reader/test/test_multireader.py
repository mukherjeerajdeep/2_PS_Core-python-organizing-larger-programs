import unittest

# Test is not inside the demo_reader package, sw can't do relative import
import demo_reader


class TestMultiReader(unittest.TestCase):
    def test_initialization(self):
        demo_reader.multireader.MultiReader('test_file.txt')