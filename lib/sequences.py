#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    if length <= 0:
        print([])          # empty list when length is 0 or negative
        return

    # start the sequence
    fib = [0, 1]
    while len(fib) < length:
        fib.append(fib[-1] + fib[-2])

    # slice to requested length and print
    print(fib[:length])    