def main():
    s = input()
    max_len = 0
    res = chars = finres = ''
    for j in range(len(s)):
        for i in range(j, len(s)):
            if s[i] in chars:
                res = ''
                chars = ''
                if len(res) > max_len:
                    max_len = len(res)
                    finres = res
            res += s[i]
            chars += s[i]
        print(finres)
if __name__ == '__main__':
    main()