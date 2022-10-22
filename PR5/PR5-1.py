def main():
    list1, list2 = input().split(), input().split()
    list1, list2 = set(list1), set(list2)
    print(len(list1.intersection(list2)))
    print(len(list1.symmetric_difference(list2)))
    print(len(list1 - list2))
    print(len(list2 - list1))
if __name__ == '__main__':
    main()