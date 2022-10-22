def main():
    data = input().split()
    results = []
    ns = len(data) #система счисления
    variants = []
    for i in range(ns**len(data)):
        n = i
        s = ''
        while n > 0:
            s += str(n%ns)
            n //= ns
        s = s[::-1]
        while len(s) != len(data):
            s = '0' + s
        variants.append(s)
    check = sorted(data)
    for i in range(len(variants)):
        s = []
        for j in range(len(variants[i])):
            s.append(data[int(variants[i][j])])
        if s not in results and sorted(s) == check:
            results.append(s)
    print(results)

if __name__ == '__main__':
    main()

