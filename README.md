# py-gfycat
A Python client for the [Gfycat API](https://gfycat.com/api). 

[![PyPI version](https://badge.fury.io/py/gfycat.svg)](http://badge.fury.io/py/gfycat)

Installation
------------

    pip install gfycat
    
Getting Started
---------------

```python
from gfycat import GfycatClient

client = GfycatClient()

# Example request
client.upload_from_file('willsmith.gif')
```

Error Handling
--------------
Error types
* GfycatClientError - General error handler, access message and status code via

```python
from gfycat.error import GfycatClientError

try
    ...
except GfycatClientError as e
    print(e.error_message)
    print(e.status_code)
```
