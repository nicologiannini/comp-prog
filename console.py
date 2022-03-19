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

def findMaxCrossingSubarray(arr, low, mid, high):
    sum = 0
    leftSum = MIN
    rightSum = MIN
    i = mid
    while i >= low:
        sum += arr[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i
        i -= 1
    sum = 0
    j = mid + 1
    while j <= high:
        sum += arr[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j
        j += 1
    return maxLeft, maxRight, leftSum + rightSum

def findMaxSubarray(arr, low, high):
    if high == low:
        return low, high, arr[low]
    else:
        mid = math.floor((low + high) / 2)
        leftLow, leftHigh, leftSum = findMaxSubarray(arr, low, mid)
        rightLow, rightHigh, rightSum = findMaxSubarray(arr, mid + 1, high)
        crossLow, crossHigh, crossSum = findMaxCrossingSubarray(arr, low, mid, high)
        if leftSum >= rightSum and leftSum >= crossSum:
            return leftLow, leftHigh, leftSum
        elif rightSum >= leftSum and rightSum >= crossSum:
            return rightLow, rightHigh, rightSum
        else:
            return crossLow, crossHigh, crossSum

def binarySearch(x, mid, arr, n):
    if x == arr[mid - 1] or (x > arr[mid - 2] and x < arr[mid - 1]) or (mid == 1 and x < arr[mid - 1]):
        return mid
    elif x > arr[mid - 1]:
        return binarySearch(x, mid + math.ceil((n - mid) / 2), arr, n)
    else:
        return binarySearch(x, mid - math.ceil(mid / 2), arr, mid)

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def isPalindrome(s):
    return s == s[::-1]

def maxSum(arr, n, k):   
    res = 0
    for i in range(k):
        res += arr[i]
 
    curr_sum = res
    for i in range(k, n):
        curr_sum += arr[i] - arr[i - k]
        temp = max(res, curr_sum)
        if temp != res:
            res = temp
 
    return res

# SOLUTION

def solve(n, x, arr):
    res = 0
    map = {}
    arr.sort()

    for i in range(0, n):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
        
    for i in range(0, n):
        k = arr[i] * x
        if map[arr[i]] == 0:
            continue

        map[arr[i]] -= 1
        y = bisect.bisect_left(arr, k)
        
        if y < n and arr[y] == k:
            if map[k] > 0:
                map[k] -= 1
            else:
                res += 1
        else:
            res += 1

    return res

if __name__ == "__main__":
    res = []
    iter = inp()
    i = 0
    while i < iter:
        nx = inpl()
        arr = inpl()
        result = solve(nx[0], nx[1], arr)
        res.append(result)
        i += 1

    for r in res:
        print(r)