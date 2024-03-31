# In this module the discovery procedure is different than others

The python path needs to be setup before the package is executed 

```text
$env:PYTHONPATH='core;bz2-plugin;gz-plugin' 
```

Here we used the setuptools entrypoint to setup the plugin discovery.

```python
import setuptools

setuptools.setup(
    name="demo_reader",
    version="1.0.0",
    description="Tools for reading various file formats",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'}
)
```

Each package is has its own setup which creates the virtual environemnt 

```text
demo-reader>python .\setup.py install
running install
running bdist_egg
running egg_info
creating src\demo_reader.egg-info
writing src\demo_reader.egg-info\PKG-INFO

```

And then get it discovered runtime

```text
multi-reader>
multi-reader>python.exe -m demo-reader test.gz
C:\Python\python.exe: No module named demo-reader.__main__; 'demo-reader' is a package and cannot be directly executed
m
```