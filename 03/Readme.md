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
```python
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

`python` - the interpreter
`-m` - run the module
`demo_reader.compressed.bzipped` - fully qualified dotted name format/ not file system path
`test.bz2 `- the sys.argv[1] passed for the file name to be created
`data compressed with bz2 `- the sys.argv[2] sys.argv[5]  

```

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
