#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 09:32:22 2022
@author: rivera

This is a math module for the 59th session.
"""


from .printer import print_message


def sample_function_fibonacci(n: int) -> int:
    """Calculates the fibonacci sequence given a number. Based on:
     https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/

    Parameters
    ----------
    :param n: int, required
        The input number

    Returns
    -------
    :return: int
        The nth Fibonacci number
    """
    if n < 0:
        print_message(message='Incorrect input for function sample_function_fibonacci', is_error=True)
        return -1
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return sample_function_fibonacci(n - 1) + sample_function_fibonacci(n - 2)