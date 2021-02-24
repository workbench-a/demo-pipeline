#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
from pathlib import Path

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'demo_model'
DESCRIPTION = 'A demo model pipline.'
URL = 'https://github.com/workbench-a/mlops-demo'
EMAIL = 'na@na.com'
AUTHOR = 'workbench-a'
REQUIRES_PYTHON = '>=3.8.5'

# Packages that are required for this module to be executed
def list_reqs(fname='requirements.txt'):
    with open(fname) as fd:
        return fd.read().splitlines()

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in MANIFEST.in.
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / 'demo_model'
about = {}
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version
    print(f"THE VERSION IS!!!!: {_version}")

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    # Package data is not being installed correctly. Remove this when resolved.
    # package_data={'demo_model': ['VERSION'], 'demo_model': ['datasets/*.csv'], 'demo_model': ['datasets/testing/*.csv']},
    package_data={'demo_model': ['VERSION']},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)