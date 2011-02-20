import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from setuptools import setup, find_packages
from langacore.thingsweforget import __author__, __release__, __contact__

__description__ = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name = "langacore.thingsweforget",
    version = __release__,
    description = "Synchronization of images from thingsweforget.blogspot.com for offline use.",
    author = __author__,
    author_email = __contact__,
    license = "BSD",
    #url = "FIXME",
    #download_url = "FIXME",
    packages = find_packages('src'),
    namespace_packages = ['langacore'],
    include_package_data = True,
    package_dir = {'':'src'},
    keywords = ["http", "downloader", "sync", "www", "crawler", "blogspot"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    install_requires = [
        'distribute',
        'lxml',
   ],
    long_description = __description__)
