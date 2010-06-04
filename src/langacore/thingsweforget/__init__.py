"""\
Synchronization of thingsweforget.blogspot.com content for offline use
----------------------------------------------------------------------

This project requires Python 3.1 or later.
"""

# UTF-8 in the variables below is PyPI incompatible
__version__ = "0.1"
__release__ = "0.1.0"
__author__ = "Lukasz Langa"
__contact__ = "lukasz@langa.pl"

import urllib.request, urllib.error, urllib.parse
from lxml import html

with urllib.request.urlopen("http://thingsweforget.blogspot.com/") as url:
    contents = url.read()

