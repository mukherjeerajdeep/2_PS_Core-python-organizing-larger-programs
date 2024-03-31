# Executable packages

Here we execute a package with relative import with the use of __main__.py, we 
used last time as well. However now the demo_reader is not a directory but a
package, so we need to call it by `**-m**` flag instead. 

See that it didn't execute.

```python
Executable_Package>
Executable_Package>
Executable_Package>
  File "C:\Python\lib\runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Python\lib\runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "C:\Rajdeep_Mukherjee\PluralSight_Python\2_PS_Core-python-organizing-larger-programs\04\Executable_P
ackage\demo_reader\__main__.py", line 2, in <module>
    from .multireader import MultiReader
ImportError: attempted relative import with no known parent package
```

Now it is executed. The difference lies between mentioning python about the 
correct use of the package. For directories the package inside the directories are 
automatically added to `sys.path` but here it is not. 
```python
Executable_Package>
Executable_Package>python -m demo_reader test.gz
executing multi-reader-program/__main__.py
data compressed with gzip
Executable_Package>

```
It is impossible to execute the package from the console without the presence of `__main__.py` file. It can be executed from
the `__init__.py` but it will still complain. Let's copy the content inside the `__init__.py` and move `__main__.py` to 
somewhere else outside the package. 

```python
Executable_Package>python -m demo_reader test.gz
executing multi-reader-program/__main__.py
data compressed with gzip
C:\Python\python.exe: No module named demo_reader.__main__; 'demo_reader' is a package and cannot be directly executed
Executable_Package>

```
without moving anything obviously will fail to execute it. 

```python
Executable_Package>python -m demo_reader test.gz
C:\Python\python.exe: No module named demo_reader.__main__; 'demo_reader' is a package and cannot be directly executed
Executable_Package>

```
 
**Note**: `__main__.py` is needed to execute a directory **without any flag** when it is inside the directory or inside package when it is executed
as package/module with `-m` flag.

After everything is fixed 

```python
Executable_Package>
Executable_Package>python -m demo_reader test.gz
Executing __init__.py inside demo_reader
executing multi-reader-program/__main__.py
data compressed with gzip
Executable_Package>

```

