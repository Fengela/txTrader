#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  version.py
  ----------

  TxTrader version module 

  Copyright (c) 2015 Reliance Systems Inc. <mkrueger@rstms.net>
  Licensed under the MIT license.  See LICENSE for details.

"""

VERSION_MAJOR = 1
VERSION_MINOR = 9
VERSION_PATCH = 6
BUILD=1995
DATE='2018-08-08'
TIME='16:48:07'
VERSION = '%s.%s.%s' % (VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH)
DATETIME = '%s %s' % (DATE, TIME)
LABEL = 'TxTrader Securities Trading API Controller'
HEADER = '%s %s (build %s) %s' % (LABEL, VERSION, BUILD, DATETIME)
