# Execution of directories instead of packages

## importing the directories when a package is distributed over many directories

![demo_reader_spread_out_in_multiple_dirs](C:\Rajdeep_Mukherjee\PluralSight_Python\2_PS_Core-python-organizing-larger-programs\04\demo_reader_spread_out_in_multiple_dirs.PNG)

Now we can see that the locals() has nothing as such
```python
PS C:\Rajdeep_Mukherjee\PluralSight_Python\2_PS_Core-python-organizing-larger-programs\04> py
Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>                                                                   
>>> from pprint import pprint
>>> pprint(locals()) 
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
```

**Note:** PEP420 says that the python `__init__.py` is not needed any more only to support the backward
compatibility. 

Now we can use the `sys.path.extend()` to extend the paths which are not being scanned by python. 
So this path is not either the `PYTHONPATH` or not in path searched by python. Remember the 
`multi-reader-program` is not a package it's just a directory with `**__main__.py**` inside it. 

In some earlier program we included some packages as sys.path.append method as well, because `**sys.path**` is
a list. See **exercise 02**.

```python
>>> import sys
>>> sys.path.extend(['./multi-reader-program','./path2'])
>>>
>>> import demo_reader
>>> demo_reader.__path__
_NamespacePath(['C:\\Rajdeep_Mukherjee\\PluralSight_Python\\2_PS_Core-python-organizing-larger-programs\\04\\./path
>>> demo_reader.util.__path__
['C:\\Rajdeep_Mukherjee\\PluralSight_Python\\2_PS_Core-python-organizing-larger-programs\\04\\./multi-reader-program\\demo_reader\\util']
>>>
>>> demo_reader.compressed.__path__
['C:\\Rajdeep_Mukherjee\\PluralSight_Python\\2_PS_Core-python-organizing-larger-programs\\04\\./path2\\demo_reader\\compressed']       
```
## Run the program from directory 

Now running the program with the already created text.bz2 file should work as a charm 

![](C:\Rajdeep_Mukherjee\PluralSight_Python\2_PS_Core-python-organizing-larger-programs\04\source root.PNG)

Don't forget to set the multi-reader-program to `source root` to alleviate the error marked
by pycharm.

```text
04>python multi-reader-program test.bz2
executing multi-reader-program/__main__.py
data compressed with bz2
```

## Create the zipped file

The zipfile **should be the contents of the directory** i.e. the files not the zip of the directory 
itself. 

```text
04>cd .\multi-reader-program\
multi-reader-program>python -m zipfile -c ../multi-reader-program.zip *

multi-reader-program>cd ..
04>
04>dir


    Directory: C:\Rajdeep_Mukherjee\PluralSight_Python\2_PS_Core-python-organizing-larger-programs\04


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         27-Apr-22     21:03                .idea
d-----         27-Apr-22     21:29                multi-reader-program
-a----         27-Apr-22     09:33          24629 demo_reader_spread_out_in_multiple_dirs.PNG
-a----         27-Apr-22     21:31             22 multi-reader-program.zip
-a----         07-Mar-19     19:47         706838 namespace-and-executable-packages-slides.pdf
-a----         27-Apr-22     21:30           2529 Readme.md
-a----         27-Apr-22     21:29          17925 source root.PNG
-a----         25-Apr-22     21:09             62 test.bz2

```
Now executing the zipped file should also work as it worked for the directory.

```text
multi-reader-program>py.exe -m zipfile --help
usage: zipfile.py [-h] (-l <zipfile> | -e <zipfile> <output_dir> | -c <name> [<file> ...] | -t <zipfile>)

A simple command-line interface for zipfile module.

options:
  -h, --help            show this help message and exit
  -l <zipfile>, --list <zipfile>
                        Show listing of a zipfile
  -e <zipfile> <output_dir>, --extract <zipfile> <output_dir>
                        Extract zipfile into target dir
  -c <name> [<file> ...], --create <name> [<file> ...]
                        Create zipfile from sources
  -t <zipfile>, --test <zipfile>
                        Test if a zipfile is valid
multi-reader-program>
```

Now try with the zipped folder. 

```text
04>
04>
04>python multi-reader-program.zip test.bz2            
executing multi-reader-program/__main__.py
data compressed with bz2
04>
04>

```