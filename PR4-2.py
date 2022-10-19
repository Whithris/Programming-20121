def main():
    a = [[int(x) for x in input().split()] for _ in range(int(input()))]
    n = len(a)-1
    prev_steps = []
    for i in range(n+1): a[i] = a[i][::-1]
    for i in range(n+1):
        for j in range(n+1):
            if [i, j] not in prev_steps and [n-j, n-i] not in prev_steps:
                a[i][j], a[n-j][n-i] = a[n-j][n-i], a[i][j]
                prev_steps.append([i, j])
    for i in range(n+1):
        print(*a[i])
if __name__ == '__main__':
    main()



