``langacore.thingsweforget``
----------------------------

This is a simple script that synchronizes all post-it images from http://thingsweforget.blogspot.com
A couple of reasons why you would want to keep a separate copy of all these pictures:

* they are highly motivational
* you don't always have Internet access
* you might want to create an **awesome screensaver** by simply pointing it to the directory where you
  store those post-its
* you can shuffle these and for instance e-mail yourself daily one of those

Installation
------------

You need Python 3.1 with ``distribute``. Instructions on installing Python can be found on the `official
Website <http://python.org>`_, as for ``distribute``, download the ``distribute_setup.py`` file from
http://python-distribute.org and run it::

  python3.1 distribute_setup.py

Now you can install our humble package::

  python3.1 setup.py install

It will download and hopefully successfully build depedencies (it's ``lxml`` for its awesome
XML/HTML querying abilities).

Usage
-----

For now this comes to running this command::

  python3.1 -m langacore.thingsweforget

which will download all first images from every post on the website to the current folder.

Need more details?
------------------
The code is rather thoroughly documented, you can request more documentation from me
directly: lukasz@langa.pl.
