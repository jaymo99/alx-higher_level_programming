#!/usr/bin/python3
'''Defines a function that prints a square'''


def print_square(size):
    '''
    prints a square with the character #

    Args:
        size (int): is the size length of the square.
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for col in range(size):
            print('#', end='')
        print()
