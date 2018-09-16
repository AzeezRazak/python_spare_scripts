#Python 3
#Input >> 5
#Output >> 12345 NOT 1 2 3 4 5 thats in (n-2),(n-1),n

if __name__ == '__main__':
    n = int(input())
    print(*range(1,n+1),sep='')
