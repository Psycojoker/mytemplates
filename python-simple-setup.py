#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='software_name',
      version='version number',
      description='short description',
      author='you',
      long_description='long description',
      # or you can also do something like this
      # long_description=open("README").read(),
      author_email='you@example.com',
      url='http://example.com',
      install_requires=['lib_with_a_certain_version>=0.9.9.1', 'another_lib'],
      # list of packages you want you application/lib install
      packages=['packagdescription', 'package_two'],
      license= 'the licence you are distributing your software under',
      # list of scripts supplied by your application
      scripts=['script1', 'bin/script2'],
      keywords='a series of keywords separates by spaces',
     )

# vim:set shiftwidth=4 tabstop=4 expandtab:
