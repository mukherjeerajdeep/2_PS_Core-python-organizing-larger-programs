# Organize the program inside the directory

## How to organize it and what it means 
```text
folder(03) : Without `__init__.py` file, neither a package or module
    demo_reader : seems like a folder however it is a importable package or 
                  as module because it contains `__init__.py` file inside
        __init__.py : the file due to which demo_reader becomes a package or a module 
        multireader.py : a single python file which can be used as submodule when accessing 
                         as `import demo_reader.multireader` way with full distinguished name from the 
                         main module.
        compressed:  package inside package
            __init__py : initialized subpackage inside demo_reader
            gzipped.py : submodule inside compressed which can be addressed from the demo_reader as wel.
                         
The can be subpackage as well, which are folders
```    
## import the `os` and change the directory

```python
import os
os.getcwd()
'C:\\Python'

os.chdir("C:\\Rajdeep_Mukherjee\\PluralSight_Python\\2. PS_Core-python-organizing-larger-programs\\03")
```

## Importing the module
## Remember that the `__init__` will be called only once

```text
import demo_reader
__init__.py is called for the import!
```


## From the other directory the import will not work as that directory is not a package 

```python
os.getcwd()
'C:\\Rajdeep_Mukherjee\\PluralSight_Python\\2. PS_Core-python-organizing-larger-programs\\03'
```

## Change the directory back again to the folder 03.
## Even if the same directory path is given the import works only once

```python
os.chdir("C:\\Rajdeep_Mukherjee\\PluralSight_Python\\2. PS_Core-python-organizing-larger-programs\\03")
import demo_reader
```

## Import the submodule as mentioned in the top with full distinguished name 
```python
import demo_reader.multireader

r = demo_reader.multireader.MultiReader('demo_reader/__init__.py')
r.read()
'print("__init__.py is called for the import!")'

```
## Now we can import multiple subpackages/submodules under a module

```python
import demo_reader // importing the module
__init__.py is called for the import! // init called as usual
import demo_reader.multireader // submodule is called
import demo_reader.compressed // subpackege is called
import demo_reader.compressed.gzipped // subpackage + submodule is called
import demo_reader.compressed.bzipped // same as above
```

## Use the console to run the program

```text
03>python -m demo_reader.compressed.bzipped test.bz2 data compressed with bz2
__init__.py is called for the import!
03>
03>python -m demo_reader.compressed.gzipped test.gz data compressed with gzip 
__init__.py is called for the import!
```

`python` - the interpreter
`-m` - run the module
`demo_reader.compressed.bzipped` - fully qualified dotted name format/ not file system path
`test.bz2 `- the sys.argv[1] passed for the file name to be created
`data compressed with bz2 `- the sys.argv[2] sys.argv[5]  


## This works in pycharm python terminal

```python
Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> from demo_reader.multireader import MultiReader
__init__.py is called for the import!
>>>
>>> r = MultiReader('test.bz2')
>>> r.read()
'data compressed with bz2'
>>> r.close()
>>> 
>>> 

```
## Relative import 

we extract the common parts of the bzipped and gzipped 
to a common writer module and import that as relatively from 
the current package/module. Each dot `.` is one package level
up from the current module package. 
```python
import gzip
from ..util import writer
```

## Dunder `__all__` will limit the scope of the visible python methods

using the dunder `__all__` we can limit the package visibility to public.
the local() is used to check the degree of exposure when importing a package.

```python
pprint(locals())
{'In': ['',
        "print('PyDev console: using IPython 8.1.1\\n')\n"
        '\n'
        "import sys; print('Python %s on %s' % (sys.version, sys.platform))\n"
        "sys.path.extend(['C:\\\\Rajdeep_Mukherjee\\\\PluralSight_Python\\\\2_PS_Core-python-organizing-larger-programs\\\\03', "
        "'C:/Rajdeep_Mukherjee/PluralSight_Python/2_PS_Core-python-organizing-larger-programs/03'])",
        'from pprint import pprint',
        'pprint(local())',
        'pprint(locals())'],
 'Out': {},
 '_': '',
 '__': '',
 '___': '',
 '__builtin__': <module 'builtins' (built-in)>,
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': 'Automatically created module for IPython interactive environment',
 '__loader__': None,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 '_dh': [WindowsPath('C:/Rajdeep_Mukherjee/PluralSight_Python/2_PS_Core-python-organizing-larger-programs/03')],
 '_i': 'pprint(local())',
 '_i1': "print('PyDev console: using IPython 8.1.1\\n')\n"
        '\n'
        "import sys; print('Python %s on %s' % (sys.version, sys.platform))\n"
        "sys.path.extend(['C:\\\\Rajdeep_Mukherjee\\\\PluralSight_Python\\\\2_PS_Core-python-organizing-larger-programs\\\\03', "
        "'C:/Rajdeep_Mukherjee/PluralSight_Python/2_PS_Core-python-organizing-larger-programs/03'])",
 '_i2': 'from pprint import pprint',
 '_i3': 'pprint(local())',
 '_i4': 'pprint(locals())',
 '_ih': ['',
         "print('PyDev console: using IPython 8.1.1\\n')\n"
         '\n'
         "import sys; print('Python %s on %s' % (sys.version, sys.platform))\n"
         "sys.path.extend(['C:\\\\Rajdeep_Mukherjee\\\\PluralSight_Python\\\\2_PS_Core-python-organizing-larger-programs\\\\03', "
         "'C:/Rajdeep_Mukherjee/PluralSight_Python/2_PS_Core-python-organizing-larger-programs/03'])",
         'from pprint import pprint',
         'pprint(local())',
         'pprint(locals())'],
 '_ii': 'from pprint import pprint',
 '_iii': "print('PyDev console: using IPython 8.1.1\\n')\n"
         '\n'
         "import sys; print('Python %s on %s' % (sys.version, sys.platform))\n"
         "sys.path.extend(['C:\\\\Rajdeep_Mukherjee\\\\PluralSight_Python\\\\2_PS_Core-python-organizing-larger-programs\\\\03', "
         "'C:/Rajdeep_Mukherjee/PluralSight_Python/2_PS_Core-python-organizing-larger-programs/03'])",
 '_oh': {},
 'exit': <IPython.core.autocall.ExitAutocall object at 0x000001C2E3A39390>,
 'get_ipython': <bound method InteractiveShell.get_ipython of <_pydev_bundle.pydev_ipython_console_011.PyDevTerminalInteractiveShell object at 0x000001C2E3A3A3B0>>,
 'pprint': <function pprint at 0x000001C2E2A10160>,
 'quit': <IPython.core.autocall.ExitAutocall object at 0x000001C2E3A39390>,
 'sys': <module 'sys' (built-in)>}
```
After the import of the `demo_reader`, here we see both bzipped/gzipped are exposed whereas we
want only to expose the methods/functions inside it not the whole module/package. In this case
`__all__` helps us. 

```python
from demo_reader.compressed import * 
__init__.py is called for the import!
 
pprint(locals())
{'In': ['',
        "print('PyDev console: using IPython 8.1.1\\n')\n"
        '\n'
        "import sys; print('Python %s on %s' % (sys.version, sys.platform))\n"
        "sys.path.extend(['C:\\\\Rajdeep_Mukherjee\\\\PluralSight_Python\\\\2_PS_Core-python-organizing-larger-programs\\\\03', "
......
......        
 'bz2_opener': <function open at 0x000001C2E05624D0>,
 'bzipped': <module 'demo_reader.compressed.bzipped' from 'C:\\Rajdeep_Mukherjee\\PluralSight_Python\\2_PS_Core-python-organizing-larger-programs\\03\\demo_reader\\compressed\\bzipped.py'>,`
 'exit': <IPython.core.autocall.ExitAutocall object at 0x000001C2E3A39390>,
 'get_ipython': <bound method InteractiveShell.get_ipython of <_pydev_bundle.pydev_ipython_console_011.PyDevTerminalInteractiveShell object at 0x000001C2E3A3A3B0>>,
 'gzip_opener': <function open at 0x000001C2E2746710>,
 'gzipped': <module 'demo_reader.compressed.gzipped' from 'C:\\Rajdeep_Mukherjee\\PluralSight_Python\\2_PS_Core-python-organizing-larger-programs\\03\\demo_reader\\compressed\\gzipped.py'>,`
......
......
```
Here we can see that only the methods/functions are exposed locally. 
 `'bz2_opener': <function open at 0x000001B75CFE8B80>,
 'gzip_opener': <function open at 0x000001B75CFEA290>,`

```python
Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> 
>>> from pprint import pprint
>>> pprint(locals()) 
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'pprint': <function pprint at 0x000001B75CB1A560>}
>>>
>>> 
>>> from demo_reader.compressed import *  
__init__.py is called for the import!
>>> 
>>> 
>>> pprint(locals())                      
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'bz2_opener': <function open at 0x000001B75CFE8B80>,
 'gzip_opener': <function open at 0x000001B75CFEA290>,
 'pprint': <function pprint at 0x000001B75CB1A560>}
>>>

```
