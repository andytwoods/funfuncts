# -*- coding: utf-8 -*-

"""Main module."""
import types

def ff(el):
    if type(el) is dict:
        return fd(el)
    elif type(el) is list:
        return fl(el)


def fd(el):
    orig_dict = el
    return el

def fl(el):
    orig_arr = el
    return el


class flist(list):

    def __init(self, *args, **kwargs):
        list.__init(self, *args, **kwargs)
        if args[0]:
            for val in args[0]:
                self.append(val)


class fdict(dict):

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        try:
            for key, val in args[0].items():
                self[key] = val
        except IndexError:
            pass


    def map(self, _lambda, output = None):

        if output is None:
            output = fdict()

        isDict = type(output) is dict
        if isDict is False:
            if type(output) is not list:
                raise MustBeDictOrMapError()

        for key, val in self.items():
           # perhaps we make output argumnent optional via lambda inpsection with
           # https://docs.python.org/3/library/inspect.html#inspect.signature
           result = _lambda(val, key)
           if isDict:
               output[key] = result
           else:
               output.append(result)

        return output




class MustBeDictOrMapError(Exception):
    pass
