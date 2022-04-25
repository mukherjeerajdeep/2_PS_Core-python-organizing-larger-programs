# Python module and search paths 

```python
import urllib
import urllib.request

type(urllib)
Out[6]: module

type(urllib.request)
Out[7]: module

# The above syntax is fine but there is an explicit import procedure

from urllib import request
# This will only bind the request and needless to know where it came from request
Out[11]: <module 'urllib.request' from 'C:\\Python\\lib\\urllib\\request.py'>

# The submodule still knows the hierarchy hence knows the urllib 
urllib.__path__
Out[13]: ['C:\\Python\\lib\\urllib']
urllib.request.__path__
Traceback (most recent call last):
  File "C:\Python\lib\site-packages\IPython\core\interactiveshell.py", line 3361, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-14-5f94591ece52>", line 1, in <cell line: 1>
    urllib.request.__path__
AttributeError: module 'urllib.request' has no attribute '__path__'

# urllib.__path__ has a attribute named __path__ whereas request doesn't, this presence of __path__ means where urrllib searches for nested modules 

```

## Python checks the `sys.path`

```python
import sys

sys.path
Out[3]: 
['C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.2\\plugins\\python-ce\\helpers\\pydev',
 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.2\\plugins\\python-ce\\helpers\\third_party\\thriftpy',
 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.2\\plugins\\python-ce\\helpers\\pydev',
 'C:\\Python\\python310.zip',
 'C:\\Python\\DLLs',
 'C:\\Python\\lib',
 'C:\\Python',
 'C:\\Python\\lib\\site-packages',
 'C:\\Rajdeep_Mukherjee\\PluralSight_Python\\2. PS_Core-python-organizing-larger-programs',
 'C:/Rajdeep_Mukherjee/PluralSight_Python/2. PS_Core-python-organizing-larger-programs']
```

