#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import with_statement

import sys


def bwt(s):
    """Apply Burrows-Wheeler transform to input string."""
    assert "\0" not in s, "Input string cannot contain null character ('\\0')"
    
    s += '\0'  # Add end of file marker.
    # Generate permutations.
    table = sorted(s[i:] + s[:i] for i in range(len(s)))
    last_column = [row[-1:] for row in table]
    result = "".join(last_column).replace('\0', '')
    return result


def main(filename):
    with open(filename, 'r') as f:
        print bwt(f.read())


if __name__ == "__main__":
    main(sys.argv[1])