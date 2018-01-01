#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `funfuncts` package."""

import pytest


from funfuncts import funfuncts
from funfuncts.funfuncts import fdict


class TestClass(object):

    def test_fdictClass(self):
        d = {'a':1, 'b': 2}
        fd = fdict(d)
        assert d == fd

        _lamdbda = lambda val, key, _: str(val)+key
        result = fd.map(_lamdbda, {})
        assert result == {'a': '1a', 'b': '2b'}

        result_list = fd.map(_lamdbda, [])
        assert result_list == ['1a', '2b']


