#! /usr/bin/env python

def makerow(nums):
    try:
        rownum, ntotal = nums
    except:
        raise Exception('Not enough elements to unpack!')
    rowstr = list('0'*(ntotal-rownum-1) + '1'*(2*rownum+1) + '0'*(ntotal-rownum-1))
    row = [int(r) for r in rowstr]
    return row