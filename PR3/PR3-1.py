def main():
    n = int(input()) #система счисления
    data = input().split()
    c = int(input())
    new_data = []
    variants = []
    near = 10**10
    for i in range(n**len(data)):
        k = i
        s = ''
        while k > 0:
            s += str(k%n)
            k //= n
        s = s[::-1]
        while len(s) != len(data):
            s = '0' + s
        variants.append(s)
    fin_variants = []
    for i in range(len(variants)):
        test = []
        for x in variants[i]:
            if x not in test:
                test.append(x)
        if len(test) == len(variants[i]):
            fin_variants.append(test)
    for i in range(len(fin_variants)):
        s = []
        for j in range(len(fin_variants[i])):
            s.append(int(data[int(fin_variants[i][j])]))
        if s[:-(n-4)] not in new_data:
            if abs(c - sum(s[:-(n-4)])) < near:
                near = abs(c - sum(s[:-(n-4)]))
                answer = s[:-(n-4)]
    print(answer)
    print(sum(answer))

if __name__ == '__main__':
    main()