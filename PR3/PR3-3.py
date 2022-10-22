def main():
    data = input().split()
    res = []
    for i in range(len(data)):
        if data[i] != 0:
            comp = sorted([x for x in data[i]])
            res.append([data[i]])
            for j in range(len(data)):
                if data[j] != 0 and i != j:
                    if sorted([x for x in data[j]]) == comp:
                        res[-1].append(data[j])
                        data[j] = 0
    print(res)

if __name__ == '__main__':
    main()
