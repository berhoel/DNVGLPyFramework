# Copyright (C) 2006 by Germanischer Lloyd AG

# ======================================================================
# Module    Makefile
# Task      makefile for tx2glshipmodel
# ----------------------------------------------------------------------
# Author    Berthold Höllmann <hoel@GL-Group.com>
# Project   TX2GlShipModel
# ----------------------------------------------------------------------
# Status    $State$
# Date      $Date$
# ======================================================================

# CVSID: $Id$

SHELL = /bin/sh

all:	build
	@echo "nothing to do"

test: build
	cd test ; make test

build:
	python setup.py build

.PHONY: build

# Local Variables: ***
# compile-command:"make test" ***
# coding:utf-8 ***
# End: ***
