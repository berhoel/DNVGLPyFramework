#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

u"""
Generate dependecy rules for testing tribon module

:author: `Berthold Höllmann <hoel@GL-Group.com>`__
:newfield project: Project
:project: tribonXML converters
:copyright: Copyright (C) 2007 by Germanischer Lloyd AG"""

#  CVSID: $Id$
__date__      = "$Date$"
__version__   = "$Revision$"[10:-1]
__docformat__ = "restructuredtext en"

import sys

pybase = sys.argv[-1]

for filename in sys.argv[1:-1]:
    print "%s:\t%s/%s.py" % (filename[:-3], pybase, filename[:-8].replace('.', '/'))

# Local Variables:
# mode:python
# compile-command:"make test"
# End:
