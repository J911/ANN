#!/usr/bin/python
#
# Enable cython support for eval metric
# Run as
# setup.py build_ext --inplace
#
# WARNING: Only tested for Ubuntu 64bit OS.

try:
    from distutils.core import setup
    from Cython.Build import cythonize
except:
    print("Unable to setup. Please use pip to install: cython")
    print("sudo pip install cython")
import os
import numpy

os.environ["CC"]  = "g++"
os.environ["CXX"] = "g++"

setup(ext_modules = cythonize("metrics/seg/cityscapes/evaluation/addToConfusionMatrix.pyx"),
      include_dirs=[numpy.get_include()])
