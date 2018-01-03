#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `funfuncts` package."""

import pytest


from funfuncts.funfuncts import fdict, flist, MustBeDictError, MustBeListError


class TestClass(object):

    def test_fdict(self):

        fd = fdict()
        assert isinstance(fd, dict)

        fdict(fd)

        ###### map
        d = {'a': 1, 'b': 2}
        fd = fdict(d)
        assert d == fd

        with pytest.raises(MustBeDictError):
            fdict('will fail')

        _lamdbda = lambda val, key: str(val)+key
        result = fd.map(_lamdbda, {})

        assert result == {'a': '1a', 'b': '2b'}

        # testing when returns list
        result_list = fd.map(_lamdbda, [])
        assert result_list == ['1a', '2b']

        ###### filter
        _lamdbda = lambda val, key: val > 1

        result = fd.filter(_lamdbda, {})
        assert result == {'b': 2}

        result = fd.filter(_lamdbda, [])
        assert result == [2]

        ###### reduce
        _lamdbda = lambda accumulating, val, key:  accumulating + val
        result = fd.reduce(_lamdbda, 1)
        assert result == 4

        result = fd.reduce(_lamdbda)
        assert result == 3


    def test_flist(self):

        fl = flist()
        assert isinstance(fl, list)

        flist(fl)

        ###### map
        l = [1, 2]
        fl = flist(l)

        with pytest.raises(MustBeListError):
            flist('will fail')

        assert l == fl

        _lamdbda = lambda val: str(val)+'v'
        result = fl.map(_lamdbda, {})

        assert result == {1: '1v', 2: '2v'}

        ###### filter
        _lamdbda = lambda val: val > 1

        result = fl.filter(_lamdbda, {})
        assert result == {2: 2}

        result = fl.filter(_lamdbda, [])
        assert result == [2]

        ###### reduce
        _lamdbda = lambda accumulating,val:  accumulating + val
        result = fl.reduce(_lamdbda, 2)
        assert result == 5

        result = fl.reduce(_lamdbda)
        assert result == 3


    def test_chaining(self):

        fd = fdict()
        fd.update({'a': 1, 'b': 2, 'c': 3})

        result = fd\
            .filter(lambda val, key: val > 1)\
            .reduce(lambda accumulating, val, key: accumulating+val)
        assert result == 5

        result = fd \
            .filter(lambda val, key: val > 1) \
            .map(lambda val, key: key+str(val))\
            .reduce(lambda accumulating, val, key: accumulating + val)
        assert result == 'b2c3'


    def test_readme_egs(self):
        l = [1, 2, 3]
        r = flist(l).filter(lambda v: v > 1).map(lambda v: v + 1)
        assert r == [3, 4]

        d = {'a': 1, 'b': 2}
        result = fdict(d).map(lambda val, key: str(val) + key, {})
        assert result == {'a': '1a', 'b': '2b'}

        fd = fdict({'a': 1, 'b': 2, 'c': 3})
        result = fd \
            .filter(lambda val, key: val > 1) \
            .map(lambda val, key: key + str(val)) \
            .reduce(lambda accumulating, val, key: accumulating + val)
        assert result == 'b2c3'


