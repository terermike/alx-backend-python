#!/usr/bin/env python3
"""Adding typing annotations"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) \
        -> Union[T, Any]:
    """ Returns dict or default"""
    if key in dct:
        return dct[key]
    else:
        return default
