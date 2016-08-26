from distutils.util import convert_path
from setuptools import setup, find_packages
from icdiff_inprocess import __version__

setup(
    name="icdiff_inprocess",
    version=__version__,
    url="https://github.com/jlee-made/icdiff",
    author="Jeff Kaufman",
    author_email="jeff@jefftk.com",
    maintainer_email="john.lee@made.com",
    description="improved colored diff",
    long_description=open('README.md').read(),
    py_modules=['icdiff_inprocess']
)
