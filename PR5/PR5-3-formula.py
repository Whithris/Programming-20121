from functools import cache
@cache

def sol(n, k):
     if n == k:
         return 1
     if k == 0:
         return 0
     if k == 1 and n != 0:
         return 1
     if k > 1:
         return (k*sol(n-1, k) + sol(n-1, k-1))

def main():
    n, k = [int(x) for x in input().split()]
    if k > n:
        print('no solution')
    else: print(sol(n, k))

if __name__ == "__main__":
    main()