#!/usr/bin/env python
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup()
d['packages'] = ['baxter_essentials', 'baxter_vision_mapping', 'baxter_control']
d['package_dir'] = {'': 'src'}

setup(**d)
