def main():
    a = input()
    if -2**7 < int(a) < 2**7 - 1:
        if int(a) < 0:
            if -2**7 < str(int(a)*-1)[::-1] < 2**7 - 1:
                print(str(int(a)*-1)[::-1])
        else:
            if -2**7 < int(a[::-1]) < 2**7 - 1:
                print(a[::-1])
    else:
        print('no solution')

if __name__ == "__main__":
    main()
