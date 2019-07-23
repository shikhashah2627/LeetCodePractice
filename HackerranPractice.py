#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    ar.sort()
    ar2 = []
    for i in range(0,len(ar)):
        if ar[i] in ar2 and len(ar2) == 1:
            ar2.append(ar[i])
            count += 1
        else:
            ar2.clear()
            ar2.append(ar[i])
    return count


def jumpingOnClouds(c):
    route = []
    for i in range(0,len(c)):
        if c[i] == 0:
            route.append(i)
    copyRoute = route
    for item in route:
        if item+1 in route and item+2 in route:
            copyRoute.remove(item+1)
    return len(copyRoute) - 1

def hourglassSum(arr):
    allSums = []
    for i in range(0, 4):
        for j in range(0, 4):
           sum1 = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
           allSums.append(sum1)
    return max(allSums)
        
def minimumBribes(q):
    bribeCount = 0
    for i in range(0,len(q)):
        # print("i: ",i+1)
        # print("q[i]:",q[i])
        if i+1 != q[i] and q[i] == i+2:
            bribeCount += 1
        elif i+1 != q[i] and q[i] == i + 3:
            bribeCount += 2
        elif i+1 != q[i] and q[i] > i+3:
            # print(q[i])
            return 'Too chaotic'
        else:
            continue
    return bribeCount            

def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    # First create the temp array and store the respective positions at the value index.
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
    return swaps

def arrayManipulation(n, queries):
    #  Not an optimal solution
    arrayGeneration = [0] * (n + 2)
    # for i in range(len(queries)):
    #     for j in range(queries[i][0]-1, queries[i][1]):
    #         arrayGeneration[j] += queries[i][2]
    #     print(arrayGeneration)
    # return max(arrayGeneration)
    # Optimal solution- apply prefix sum algoritm
    for i in range(len(queries)):
        arrayGeneration[queries[i][0]] += queries[i][2]
        arrayGeneration[queries[i][1]+1] -= queries[i][2]
    for i in range(1, len(arrayGeneration)):
        arrayGeneration[i] += arrayGeneration[i-1]
    return max(arrayGeneration)
    
def twoStrings(s1, s2):
    return 'YES' if any(i in s2 for i in s1 ) else 'NO'    
if __name__ == '__main__':

    # n = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]

    # ar = [42] * 100

    n = 10
    s = 'abc'
    arr = [[1, 1, 1, 0, 0, 0], [0, 1 ,0 ,0 ,0 ,0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4,0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    # result = hourglassSum(arr)
    # result = jumpingOnClouds(n)
    # result = minimumBribes(n)
    # result = minimumSwaps(n)
    # n = [2, 1, 5,  3, 4]
    # n = [1, 2, 5, 3, 7, 8, 6, 4]
    queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
    result = arrayManipulation(n, queries)

    print(result)


