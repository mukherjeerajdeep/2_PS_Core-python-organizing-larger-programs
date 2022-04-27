# Execution of directories instead of packages

## importing the directories when a package is distributed over many directories

![demo_reader_spread_out_in_multiple_dirs](C:\Rajdeep_Mukherjee\PluralSight_Python\2_PS_Core-python-organizing-larger-programs\04\demo_reader_spread_out_in_multiple_dirs.PNG)

```python
PS C:\Rajdeep_Mukherjee\PluralSight_Python\2_PS_Core-python-organizing-larger-programs\04> py
Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>                                                                   
>>> from pprint import pprint
>>> pprint(locals()) 
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,


>>> import sys
>>> sys.path.extend(['./path1','./path2'])
>>>
>>> import demo_reader
>>> demo_reader.__path__
_NamespacePath(['C:\\Rajdeep_Mukherjee\\PluralSight_Python\\2_PS_Core-python-organizing-larger-programs\\04\\./path
>>> demo_reader.util.__path__
['C:\\Rajdeep_Mukherjee\\PluralSight_Python\\2_PS_Core-python-organizing-larger-programs\\04\\./path1\\demo_reader\\util']
>>>
>>> demo_reader.compressed.__path__
['C:\\Rajdeep_Mukherjee\\PluralSight_Python\\2_PS_Core-python-organizing-larger-programs\\04\\./path2\\demo_reader\\compressed']       
```
