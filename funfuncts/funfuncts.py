# -*- coding: utf-8 -*-

"""Main module."""
import types

def ff(el):
    if type(el) is dict:
        return fdict(el)
    elif type(el) is list:
        return flist(el)


def _make_functional(el):
    output_dict = None
    output_list = None

    _type = type(el)
    if _type is dict:
        output_dict = fdict(el)
    elif _type is list:
        output_list = flist(el)
    else:
        raise MustBeDictOrListError()

    return output_dict, output_list


class flist(list):

    def __init__(self, *args, **kwargs):

        if args:
            if isinstance(args[0], list):
                for val in args[0]:
                    self.append(val)
            else:
                raise MustBeListError()

        list.__init__(self, *args, **kwargs)


    def map(self, _lambda, output=None):
        output_dict, output_list = self._prepare(output)

        for val in self:

            result = _lambda(val)
            if output_list is not None:
                output_list.append(result)
            else:
                output_dict[val] = result

        # returns the first non-None element
        return output_list or output_dict

    def filter(self, _lambda, output=None):
        output_dict, output_list = self._prepare(output)

        for val in self:

            result = _lambda(val)
            if result:
                if output_list is not None:
                    output_list.append(val)
                else:
                    output_dict[val] = val

        # returns the first non-None element
        return output_list or output_dict

    def reduce(self, _lambda, accumulating=None):

        for val in self:
            if accumulating is None:
                accumulating = val
            else:
                accumulating = _lambda(accumulating, val)
        return accumulating

    def _prepare(self, output):
        output_dict = None
        output_list = None

        if output is None:
            output_list = flist()
        else:
            output_dict, output_list = _make_functional(output)

        return output_dict, output_list

    def __repr__(self):
        return super().__repr__() + '(functional)'


class fdict(dict):

    def __init__(self, *args, **kwargs):

        if args:
            if isinstance(args[0], dict):
                self.update(args[0])
            else:
                raise MustBeDictError()

        dict.__init__(self, *args, **kwargs)

    def map(self, _lambda, output=None):
        output_dict, output_list = self._prepare(output)

        for key, val in self.items():

            result = _lambda(val, key)
            if output_dict is not None:
                output_dict[key] = result
            else:
                output_list.append(result)

        # returns the first non-None element
        return output_dict or output_list

    def filter(self, _lambda, output=None):
        output_dict, output_list = self._prepare(output)

        for key, val in self.items():
            result = _lambda(val, key)
            if result:
                if output_dict is not None:
                    output_dict[key] = val
                else:
                    output_list.append(val)

        # returns the first non-None element
        return output_dict or output_list

    def reduce(self, _lambda, accumulating=None):

        for key, val in self.items():
            if accumulating is None:
                accumulating = val
            else:
                accumulating = _lambda(accumulating, val, key)

        return accumulating

    def _prepare(self, output):
        output_dict = None
        output_list = None

        if output is None:
            output_dict = fdict()
        else:
            output_dict, output_list = _make_functional(output)
        return output_dict, output_list

    def __repr__(self):
        return super().__repr__() + '(functional)'


class MustBeListError(Exception):
    pass


class MustBeDictError(Exception):
    pass


class MustBeDictOrListError(Exception):
    pass

