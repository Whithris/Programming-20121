def from_rom_to_arab(n):
    roman_num = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
    arab_num = 0
    i = 0
    while i < len(n):
        k = 1
        check = n[i]
        flag = 0
        while i+k<len(n) and roman_num.get(n[i]) <= roman_num.get(n[i+k]):
            flag = 1
            check += n[i+k]
            k += 1
        else:
            if flag:
                i = i + k - 1
                if len(set(check)) == 1:
                    for j in check:
                        arab_num += roman_num.get(j)
                else:
                    for j in check[:-1]:
                        arab_num -= roman_num.get(j)
                    arab_num += roman_num.get(check[-1])
        if not(flag):
            arab_num += roman_num.get(n[i])
        i += 1
    return print(arab_num)

def main():
    s = input()
    from_rom_to_arab(s)

if __name__ == '__main__':
    main()