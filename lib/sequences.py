#!/usr/bin/env python3

def print_fibonacci(length):
    seq = []
    if length > 0:
        seq.append(0)
        if length > 1:
            seq.append(1)
            if length > 2:
                for i in range(2, length):
                    seq.append(
                        seq[i-1] + seq[i-2]
                    )
    print(seq)