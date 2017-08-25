#!/usr/bin/env python3

from setuptools import setup

setup(name='tpclassifydocs',
      version='0.1',
      description='Classify Textpresso documents into categories',
      url='',
      author='Valerio Arnaboldi',
      author_email='valearna@caltech.edu',
      license='MIT',
      packages=['tpclassifydocs'],
      setup_requires=['numpy'],
      install_requires=[
          'sklearn',
          'scipy',
          'numpy',
          'typing',
          'namedlist',
          'PyPDF2'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)