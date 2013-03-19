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
        content = f.read()
    content_bwt = bwt(content)
    CHUNK_SIZE = 64
    for i in range(1, len(content_bwt)/CHUNK_SIZE + 1):
        s = content_bwt[(i-1)*CHUNK_SIZE:i*CHUNK_SIZE]
        print s


if __name__ == "__main__":
    main(sys.argv[1])