def rotation(a):
    n = len(a) - 1
    prev_steps = []
    for i in range(n + 1): a[i] = a[i][::-1]
    for i in range(n + 1):
        for j in range(n + 1):
            if [i, j] not in prev_steps and [n - j, n - i] not in prev_steps:
                a[i][j], a[n - j][n - i] = a[n - j][n - i], a[i][j]
                prev_steps.append([i, j])
    b = []
    for i in range(n, -1, -1): b.append(a[i][::-1])
    return b

def main():
    size = int(input())
    spiral = [[int(x) for x in input().split()] for _ in range(size)]
    moves = []
    while size > 0:
        moves.append(spiral[0][0])
        for _ in range(4):
            for i in range(1, size):
                moves.append(spiral[0][i])
            spiral = rotation(spiral)
        if len(spiral) != 1: moves = moves[:-1]
        newspiral = []
        for i in range(1, size-1):
            newspiral.append(spiral[i][1:-1])
        spiral = newspiral
        size -= 2
    print(*moves)

if __name__ == '__main__':
    main()