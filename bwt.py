#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bwt(s):
    """Apply Burrows-Wheeler transform to input string."""
    assert "\0" not in s, "Input string cannot contain null character ('\\0')"
    
    s += '\0'  # Add end of file marker.
    # Generate permutations.
    table = sorted(s[i:] + s[:i] for i in range(len(s)))
    last_column = [row[-1:] for row in table]
    result = "".join(last_column).replace('\0', '')
    return result
