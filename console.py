#!/bin/python3

import sys
import math
import bisect

input = sys.stdin.readline

MAX = sys.maxsize
MIN = -sys.maxsize - 1

# UTILITIES

def inp():
    return int(input())

def inpl():
    return list(map(int, input().split()))

def inpstr():
    return list(map(str, input().split()))

def inpstrl():
    res = []
    for c in str(input()):
        res.append(c)
    res.pop(-1)
    return res

# SOLUTION

def solve(n, k, arr):
    hash = {}
    for n in arr:
        if n in hash:
            hash[n] += 1
        else:
            hash[n] = 1
    s = list(set(arr))
    s.sort(reverse=True)
    f = None
    l = None
    option = []
    if len(s) == 1:
        if hash[s[0]] >= k:
            return [s[0], s[0]]
        else:
            return [-1]
    for n in range(s[0], s[len(s) - 1] - 1, -1):
        if l:
            if n not in hash:
                l = None
            elif hash[n] < k:
                l = None
            else:
                f = n
                option.append([f, l])
                f = None
        elif n in hash:
            if hash[n] >= k:
                l = n
                option.append([l, l])

    op = MIN
    opi = None
    for i in range(0, len(option)):
        if option[i][1] - option[i][0] > op:
            op = option[i][1] - option[i][0]
            opi = i

    if opi is not None:
        res = option[opi]
    else:
        res = [-1]
   
    return res



if __name__ == "__main__":
    res = []
    iter = inp()
    i = 0
    while i < iter:
        nk = inpl()
        n = nk[0]
        k = nk[1]
        arr = inpl()
        result = solve(n, k, arr)
        res.append(result)
        i += 1

    for r in res:
        print(*r)