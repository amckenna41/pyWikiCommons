###############################################################################
#####   Setup.py - installs all the required packages and dependancies    #####
###############################################################################

import pathlib
from setuptools import setup, find_packages
import sys
import pyWikiCommons

#ensure python version is greater than 3
if (sys.version_info[0] < 3):
    sys.exit('Python 3 is the minimum version requirement.')

#get path to README file
HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()

setup(name='pyWikiCommons',
      version=pyWikiCommons.__version__,
      description='Python package for downloading images and videos from Wikimedia Commons using the Wikimedia API.',
      long_description = README,
      long_description_content_type = "text/markdown",
      author=pyWikiCommons.__license__,
      author_email=pyWikiCommons.__authorEmail__,
      license=pyWikiCommons.__license__,
      url=pyWikiCommons.__url__,
      classifiers=[
        'Development Status :: 3 - Alpha', 
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Wiki',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Image Processing',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

      install_requires=[
          'requests>=2.25'
      ],
     # packages=find_packages(), #create Manifest file to ignore results folder in dist
     packages=find_packages(),
     include_package_data=True,
     zip_safe=False)