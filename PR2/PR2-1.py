def main():
    s = input()
    maxres = ''
    for start in range(len(s)):
        chars = ''
        res = ''
        for i in range(start, len(s)):
            res += s[i]
            if s[i] not in chars:
                chars += s[i]
            else:
                if len(res[:-1]) > len(maxres): maxres = res[:-1]
                break
        else:
            if len(res) > len(maxres): maxres = res

    print(maxres)
if __name__ == '__main__':
    main()