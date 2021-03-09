"""Build with
   > py setup.py sdist"""

from setuptools import setup, find_packages
from os.path import join, dirname
from contests import __version__

setup(
    author = 'phantie',
    name = 'contests',
    version = __version__,
    packages = find_packages(),
    long_description = open(join(dirname(__file__), 'README.rst')).read(),
)