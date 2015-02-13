#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup and install for DNVGLPyFramework.
"""

from __future__ import division, print_function, absolute_import

# Standard libraries.
import sys
from setuptools import setup, find_packages

# Third party libraries.
import py

# DNV GL libraries.
from dnvgl.setup_utils.version import Version

# ID: $Id$"
__date__ = "$Date$"[6:-1]
__scm_version__ = "$Revision$"[10:-1]
__author__ = "`Berthold Höllmann <berthold.hoellmann@dnvgl.com>`__"
__copyright__ = "Copyright © 2010 by DNV GL SE"

VERSION = Version('version.txt', release=False)

VERSION.write(py.path.local("dnvgl/framework/__version__.py"))

EXTRA = {}
if sys.version_info >= (3,):
    EXTRA['use_2to3'] = True

if __name__ == '__main__':
    setup(name='DNVGLPyFramework',
          version=VERSION(),
          install_requires=('py',),
          description='Lightweight framwork for DNV GL Python applications.',
          author='Berthold Höllmann, DNV GL SE',
          author_email='berthold.hoellmann@dnvgl.com',
          url='http://www.dnvgl.com',
          namespace_packages = ['dnvgl'],
          #package_dir={'': 'src'},
          packages=find_packages('.', exclude=[
              "*.__pycache__", "*.__pycache__.*", "__pycache__.*",
              "__pycache__"]),
          **EXTRA)

# Local Variables:
# mode: python
# ispell-local-dictionary: "english"
# compile-command: "make test"
# End:
