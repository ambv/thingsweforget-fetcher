``langacore.thingsweforget``
----------------------------

This is a simple script that synchronizes all post-it images from http://thingsweforget.blogspot.com
A couple of reasons why you would want to keep a separate copy of all these pictures:

* they are highly motivational
* you don't always have Internet access
* you might want to create an `awesome screensaver
  <http://ftp.langacore.org/pub/awesome_screensaver.png>`_ by simply pointing it to the directory
  where you store those post-its
* you can shuffle the post-its and e-mail yourself daily one of them
* anything creative of the sorts, maybe you want to do a massive collage of the images for your next
  yellow t-shirt?

Requirements
------------

You need Python 3.1 with ``distribute``. Instructions on installing Python can be found on the `official
Website <http://python.org>`_, as for ``distribute``, download the ``distribute_setup.py`` file from
http://python-distribute.org and run it::

  python3.1 distribute_setup.py

Installation
------------

The best bet will probably to use a stable package from `PyPI <http://pypi.python.org/>`_ which you
can install by simply issuing::

  python3.1 -m easy_install langacore.thingsweforget

It will download the package and hopefully successfully build its depedencies (it's ``lxml`` for its
awesome XML/HTML querying abilities).

Alternatively, you can `download the source from GitHub
<http://github.com/LangaCore/thingsweforget-fetcher>`_ and install it manually::

  git clone git://github.com/LangaCore/thingsweforget-fetcher.git
  cd thingsweforget-fetcher
  python3.1 setup.py install

Usage
-----

For now this comes to running this command::

  python3.1 -m langacore.thingsweforget

which will download all first images from every post on the website to the current folder.

Need more details?
------------------
The code is rather thoroughly documented, you can request more documentation from me
directly: lukasz@langa.pl.
