``langacore.thingsweforget``
----------------------------

This is a simple script that synchronizes all post-it images from
http://thingsweforget.blogspot.com A couple of reasons why you would
want to keep a separate copy of all these pictures:

* they are highly motivational
* you don't always have Internet access
* you might want to create an `awesome screensaver <>`_ by simply
  pointing it to the directory where you store those post-its * you can
  shuffle the post-its and e-mail yourself daily one of them * anything
  creative of the sorts, maybe you want to do a massive collage of the
  images for your next yellow t-shirt?

Installation
------------

The best bet will probably to use a stable package from `PyPI
<http://pypi.python.org/>`_ which you can install by simply issuing::

  pip install langacore.thingsweforget

It will download the package and hopefully successfully build its
depedencies (it's ``lxml`` for its awesome XML/HTML querying abilities).

Alternatively, you can `download the source from GitHub
<http://github.com/LangaCore/thingsweforget-fetcher>`_ and install it
manually::

  git clone git://github.com/ambv/thingsweforget-fetcher.git
  cd thingsweforget-fetcher
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -e .

Usage
-----

Change your curren directory to where you want your files to be fetched
and run this command::

  python3 -m langacore.thingsweforget

which will download all first images from every post on the website.

Need more details?
------------------
The code is rather thoroughly documented, you can request more documentation from me
directly: lukasz@langa.pl.
