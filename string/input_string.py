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
