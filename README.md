# pyWikiCommons #
Python package for downloading images and videos from Wikimedia Commons using the Wikimedia API (https://commons.wikimedia.org/w/api.php).

[![PyPI](https://img.shields.io/pypi/v/pyWikiCommons)](https://pypi.org/project/pyWikiCommons/)
[![pytest](https://github.com/amckenna41/pyWikiCommons/workflows/Building%20and%20Testing%20%F0%9F%90%8D/badge.svg)](https://github.com/amckenna41/pyWikiCommons/actions?query=workflowBuilding%20and%20Testing%20%F0%9F%90%8D)
[![Platforms](https://img.shields.io/badge/platforms-linux%2C%20macOS%2C%20Windows-green)](https://pypi.org/project/pyWikiCommons/)
[![PythonV](https://img.shields.io/pypi/pyversions/pyWikiCommons?logo=2)](https://pypi.org/project/pyWikiCommons/)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
[![Build](https://img.shields.io/github/workflow/status/amckenna41/pyWikiCommons/Deploy%20to%20PyPI%20%F0%9F%93%A6)](https://github.com/amckenna41/pyWikiCommons/actions)
[![Build Status](https://travis-ci.com/amckenna41/pyWikiCommons.svg?branch=main)](https://travis-ci.com/amckenna41/pyWikiCommons)
<!-- [![CircleCI](https://circleci.com/gh/amckenna41/pyWikiCommons.svg?style=svg&circle-token=d860bb64668be19d44f106841b80eb47a8b7e7e8)](https://app.circleci.com/pipelines/github/amckenna41/pyWikiCommons) -->
<!-- [![codecov](https://codecov.io/gh/amckenna41/DCBLSTM_PSP/branch/master/graph/badge.svg?token=4PQDVGKGYN)](https://codecov.io/gh/amckenna41/DCBLSTM_PSP) -->
[![Issues](https://img.shields.io/github/issues/amckenna41/pyWikiCommons)](https://github.com/amckenna41/pyWikiCommons/issues)
[![Size](https://img.shields.io/github/repo-size/amckenna41/pyWikiCommons)](https://github.com/amckenna41/pyWikiCommons)
[![Commits](https://img.shields.io/github/commit-activity/w/amckenna41/pyWikiCommons)](https://github.com/amckenna41/pyWikiCommons)

```

In Development...

```
Table of Contents
-----------------

  * [Introduction](#introduction)
  * [Requirements](#requirements)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Directory Folders](#directories)
  * [Tests](#tests)
  * [Issues](#Issues)
  * [Contact](#contact)
  * [References](#references)


Introduction
------------
https://www.mediawiki.org/wiki/API:Main_page

Requirements
------------
* [Python][python] >= 3.6
* [requests][requests] >= 2.25.0

Installation
-----------------
Install the latest version of pyWikiCommons using pip:

```bash
pip3 install pyWikiCommons
```

Installation from source:
```bash
git clone -b master https://github.com/amckenna41/pyWikiCommons.git
python3 setup.py install
cd pyWikiCommons
```

Usage
-----
https://www.mediawiki.org/wiki/API:Main_page

Directories
-----------
* `/docs` - documentation for pyWikiCommons (pending).
* `/images` - all images used throughout the repo.
* `/pyWikiCommons` - source code for pyWikiCommons software.
* `/tests` - unit and integration tests for pyWikiCommons.

Issues
-----
Any issues, errors or bugs can be raised via the [Issues](https://github.com/amckenna41/pyWikiCommons/issues) tab in the repository.

Tests
-----
To run all tests, from the main pyWikiCommons repo folder run:
```
python3 -m unittest discover
```

To run tests for specific module, from the main pyWikiCommons repo folder run:
```
python -m unittest tests.MODULE_NAME -v
```

License
-----------
Distributed under the MIT License. See `LICENSE` for more details.  

Contact
-------
If you have any questions or comments, please contact amckenna41@qub.ac.uk or raise an issue on the [Issues][Issues] tab. <br><br>
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adam-mckenna-7a5b22151/)

References
----------
\[1\]: https://www.mediawiki.org/wiki/API:Main_page<br>
\[2\]: https://commons.wikimedia.org/w/api.php<br><br>

[Back to top](#TOP)

[python]: https://www.python.org/downloads/release/python-360/
[requests]: https://requests.readthedocs.io/en/latest/
[Issues]: https://github.com/amckenna41/pyWikiCommons/issues
