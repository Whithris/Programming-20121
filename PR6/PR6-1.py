def santa_users(elf_list):
    for i in range(len(elf_list)):
        if ',' in elf_list[i]:
            elf_list[i] = elf_list[i].split(', ')
            elf_list[i][1] = int(elf_list[i][1])
        else:
            elf_list[i] = [elf_list[i], None]
    return dict(elf_list)


def main():
    n = int(input())
    a = [input() for _ in range(n)]  # e.g. Igor Semenov, 12345 or Igor Semenov
    print(santa_users(a))


if __name__ == '__main__':
    main()
