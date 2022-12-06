def solution(numbers: list, cur_sum: int, need_sum: int, num_len: int, signs: str):
    #print(numbers, cur_sum, need_sum, num_len, signs)
    if cur_sum == need_sum and num_len == 0:
        return signs
    if num_len == 0:
        return ''
    return (solution(numbers[1:], cur_sum+int(numbers[0]), need_sum, num_len-1, signs + '+') +
            solution(numbers[1:], cur_sum-int(numbers[0]), need_sum, num_len-1, signs + '-'))

def main():
    f = open('file.txt', 'r+')
    a = f.readline().split()
    n, s = int(a[0]), int(a[-1])
    a = a[1:-1]
    fin_signs = solution(a[1:], int(a[0]), s, n-1, '')
    if fin_signs == '':
        result = 'no solution'
    else:
        result = ''
        for i in range(n):
            result += a[i]
            if i != (n-1): result += fin_signs[i]
        result += '=' + str(s)
    f.write('\n' + result)
    f.close()

if __name__ == "__main__":
    main()