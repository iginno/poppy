#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='hampy',
      version='1.4.2',
      packages=find_packages(),

      install_requires=['numpy', 'matplotlib', 'scipy==1.8.1'],
      setup_requires=['setuptools_git >= 0.3', ],

      author='Pierre Rouanet',
      author_email='pierre.rouanet@gmail.com',
      description='Simple Hamming Marker Detection using OpenCV',
      url='https://github.com/pierre-rouanet/hampy',
      license='GNU GENERAL PUBLIC LICENSE Version 3',
      )
