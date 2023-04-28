#!/usr/bin/env python3
""" a type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies a float
by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as an argument and returns a
    function"""
    def mul_function(x: float) -> float:
        """multiplies a float by the multiplier"""
        return x * multiplier
    return mul_function
