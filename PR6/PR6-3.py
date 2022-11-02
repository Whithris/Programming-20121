import itertools as it

def near_indexes(n):
    if 0 < n < 3:
        return[n-1, n+1]
    else: return [abs(n-1)]

def get_pins(s):
    all_digit = [['1', '2', '3'],
                 ['4', '5', '6'],
                 ['7', '8', '9'],
                 ['', '0', '']]
    dict = {}
    all_digits = ''
    ind = 0
    for i in s:
        if i not in dict:
            cur_row = []
            row_num = -1
            cur_column = []
            column_num = -1
            res = i
            for j in all_digit:
                if i in j:
                    row_num = all_digit.index(j)
                    column_num = j.index(i)
            for a in near_indexes(column_num):
                if all_digit[row_num][a]: cur_row.append(all_digit[row_num][a])
            for b in near_indexes(row_num):
                if all_digit[b][column_num]: cur_column.append(all_digit[b][column_num])
            res += ''.join(cur_row)
            res += ''.join(cur_column)
            res = sorted(res)
            all_digits += ''.join(res)
            dict[ind] = res
        ind += 1
    all_combs = set(it.product(all_digits, repeat=len(s)))
    fin_res = []
    for i in all_combs:
        flag = 1
        for j in range(len(s)):
            a = dict.get(j)
            #print(i, i[j], a)
            if i[j] not in a:
                flag = 0
                break
        if flag: fin_res.append(''.join(i))
    return sorted(fin_res)


def main():
    print(get_pins(input()))

if __name__ == "__main__":
    main()