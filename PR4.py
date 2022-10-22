def main():
    n = int(input())
    banks = eval(input()) #eval использую только для удобства ввода как в примере
    result = [0]
    combs = []
    for i in range(1, 2**n):
        x = bin(i)[2:].zfill(n)
        if not '11' in x: combs.append(x)
    max_money = 0
    banks_list = []
    for i in range(len(combs)):
        money = 0
        robbed_banks = []
        cur_comb = combs[i]
        for j in range(n):
            if cur_comb[j] == '1':
                money += int(banks[j][1])
                robbed_banks.append(tuple([banks[j][0], j+1]))
        if money > max_money:
            max_money = money
            banks_list = robbed_banks
    result[0] = max_money
    for i in banks_list:
        result.append(i)
    print(result)

if __name__ == '__main__':
    main()