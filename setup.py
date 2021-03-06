# -*- coding: utf-8 -*-
# Copyright (c) 2012-2013 Infrae. All rights reserved.
# See also LICENSE.txt

from setuptools import setup, find_packages
import os

version = '3.0.5dev'

setup(name='silva.core.interfaces',
      version=version,
      description="Define Zope interfaces used in Silva",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Zope2",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='silva cms interfaces zope',
      author='Infrae',
      author_email='info@infrae.com',
      url='http://infrae.com/products/silva',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src', exclude=['ez_setup']),
      namespace_packages=['silva', 'silva.core',],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'grokcore.component',
        'setuptools',
        'silva.translations',
        'zope.annotation',
        'zope.component',
        'zope.container',
        'zope.deferredimport',
        'zope.interface',
        'zope.lifecycleevent',
        'zope.schema',
        ],
      entry_points= """
        [zodbupdate]
        renames = silva.core.interfaces:CLASS_CHANGES
      """
      )
