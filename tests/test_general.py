#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for tpDcc-libs-composite
"""

from tpDcc.libs.composite import __version__

import pytest


def test_version(self):
    assert __version__.get_version()
