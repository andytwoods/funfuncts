#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `funfuncts` package."""

import pytest


from funfuncts import funfuncts
from funfuncts.funfuncts import fdict, flist


class TestClass(object):

    def test_fdict_map(self):

        fd = fdict()
        assert isinstance(fd, dict)

        d = {'a':1, 'b': 2}
        fd = fdict(d)
        assert d == fd

        _lamdbda = lambda val, key: str(val)+key
        result = fd.map(_lamdbda, {})
        assert result == {'a': '1a', 'b': '2b'}

        # testing when returns list
        result_list = fd.map(_lamdbda, [])
        assert result_list == ['1a', '2b']


    def test_fdict_list(self):

        fl = flist()
        assert isinstance(fl, list)

        l = [1, 2]
        fl = flist(l)

        assert l == fl

        _lamdbda = lambda val, key: {val: str(val)+'v'}
        result = fl.map(_lamdbda, {})
        assert result == {1: '1v', 2: '2v'}
