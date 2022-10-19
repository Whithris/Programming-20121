def main():
    a = input()
    if (0 <= int(a) < (2**7) - 1) and (int(a[::-1]) < (2**7) - 1):
        print(int(a[::-1]))
    elif -2**7 < int(a) < 0 and (int(a[0] + str(int(a[1:][::-1]))) > -2**7):
        print((int(a[0] + str(int(a[1:][::-1])))))
    else:
        print('no solution')

if __name__ == "__main__":
    main()
