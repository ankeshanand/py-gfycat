py-gfycat
=========

A Python client for the `Gfycat API <https://gfycat.com/api>`__.

|PyPI version|

Installation
------------

::

    pip install gfycat

Getting Started
---------------

.. code:: python

    from gfycat import GfycatClient

    client = GfycatClient()

    # Example request
    client.upload_from_file('willsmith.gif')

Error Handling
--------------

* GfycatClientError - General error handler, access message and status code via

.. code:: python

    from gfycat.error import GfycatClientError

    try
        ...
    except GfycatClientError as e
        print(e.error_message)
        print(e.status_code)

GfycatClient Functions
----------------------

**Uploads**

-  ``upload_from_url(url)``
-  ``upload_from_file(filepath)``

**Query a GFY for URLs and more information**

-  ``query_gfy(gfyname)``

**Check if a link has been already converted**

-  ``check_link(link)``

.. |PyPI version| image:: https://badge.fury.io/py/gfycat.svg
   :target: http://badge.fury.io/py/gfycat
