from setuptools import setup
import sys
from os import path

import euclidean


with open(path.join(path.abspath(path.dirname(__file__)), 'README.md')) as f:
    long_description = f.read()


setup(
    name='euclidean',
    version=euclidean.__version__,
    author='jxpp',
    author_email='jxpp@chigui.re',
    description='Web app for euclidean rhythm conversions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jxpp/euclid',
    test_suite='tests',
)
