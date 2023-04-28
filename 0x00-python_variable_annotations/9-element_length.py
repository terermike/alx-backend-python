#!/usr/bin/env python3
"""Annotate the below function’s parameters and return values with
the appropriate types"""
from typing import Tuple, Sequence


def element_length(lst: Sequence[str]) -> Sequence[Tuple[str, int]]:
    """returns a list"""
    return [(i, len(i)) for i in lst]
