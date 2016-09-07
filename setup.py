#!/usr/bin/python

import os
import sys
from setuptools import setup, find_packages

# Must be ran as root or as sudo
if os.getuid() != 0:
    print('ERROR: Need to run as root')
    sys.exit(1)

# Install the requirements if the system does not have it installed
print('INFO: Checking and installing requirements')
os.system('! dpkg -S python-imaging-tk && apt-get -y install python-imaging-tk')

# Run setuptools for pip
setup(
    name='smartmirror',
    version='1.0.0',
    description='Raspberry powered mirror which can display news, weather, calendar events',
    author='HackerHouse',
    url='https://github.com/HackerHouseYT/Smart-Mirror',
    install_requires=['requests', 'feedparser', 'Pillow'],
    packages = find_packages(),
)
