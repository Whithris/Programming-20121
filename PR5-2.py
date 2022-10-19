from itertools import combinations

def main():
    list1 = input().split()
    res = set()
    for i in range(1, len(list1)+1):
        res.update((list(combinations(list1, i))))
    print(res)
    print(len(res))
if __name__ == "__main__":
    main()