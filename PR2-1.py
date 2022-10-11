def main():
    s = input()
    max_len = 0
    res = chars = finres = ''
    for i in range(len(s)):
        if s[i] in chars:
            res = ''
            chars = ''
        res += s[i]
        chars += s[i]
        if len(res) > max_len:
            max_len = len(res)
            finres = res
    print(finres)
if __name__ == '__main__':
    main()