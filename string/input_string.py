ii = int(input())
dd = float(input())
ss = input() #Input String

n = int(input())
arr = map(int, input().split())
print(sorted(list(set(arr)))[-2])



# Input
# This is a string
# Output
# This-is-a-string

def split_and_join(line):
    
    a = line.split(' ')
    a = '-'.join(a)
    return(a)



# Tuple 
n = int(input())
integer_list = tuple(map(int, input().split()))
    
print(hash(integer_list))



# String, Sub_String
import re, sys

def count_substring(string, sub_string):
    haystack = string.strip()
    needle = sub_string.strip()

# finds overlapping matches
    return(len(re.findall("(?=%s)" % needle, haystack)))



# .discard(), .remove(), .pop()
n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in range(m):
    p=input().split()
    if p[0]=="remove":
        s.remove(int(p[1]))
    elif p[0]=="discard":
        s.discard(int(p[1]))
    else:
        s.pop()

print (sum(list(s)))

# 2D Array - Hourglass

A = []

    for arr_i in range(6):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        A.append(arr_t)

    smax = -9 * 7

    for row in range(len(A) - 2):
        for column in range(len(A[row]) - 2):
            tl = A[row][column]
            tc = A[row][column + 1]
            tr = A[row][column + 2]
            mc = A[row + 1][column + 1]
            bl = A[row + 2][column]
            bc = A[row + 2][column + 1]
            br = A[row + 2][column + 2]
            s = tl + tc + tr + mc + bl + bc + br
            smax = max(s, smax)

    print(smax)

    
# Nested Logic
from datetime import date


actual = map(int, input().split())
expected = map(int, input().split())

actual = list(actual)
expected = list(expected)

actual = date(day=actual[0], month=actual[1], year=actual[2])
expected = date(day=expected[0], month=expected[1], year=expected[2])

fine = 0

if actual > expected:
    if actual.year == expected.year:
        if actual.month == expected.month:
            fine = 15 * (actual.day - expected.day)
        else:
            fine = 500 * (actual.month - expected.month)
    else:
        fine = 10000

print(fine)
