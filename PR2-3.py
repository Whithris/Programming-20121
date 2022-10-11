def main():
    s = input()
    brackets = '(){}[]'
    max_buffer = ''
    for i in range(len(s)):
        buffer = ''
        bracket_index = brackets.index(s[i])
        if bracket_index%2 == 0:
            bracket1 = s[i]
            bracket2 = brackets[bracket_index+1]
            k = 1
            for j in range(i+1, len(s)):
                if s[j] == bracket1: k += 1
                if s[j] == bracket2:
                    k -= 1
                    if k == 0:
                        buffer = s[i:j+1]
            new_buf = ''
            flag = 1
            for j in range(len(buffer)):
                br = brackets.index(buffer[j])
                if br%2 == 0: new_buf += buffer[j]
                else:
                    if not(new_buf.endswith(brackets[br-1])):
                        flag = 0
                        break
                    else: new_buf = new_buf[:-1]
            if flag == 1:
                if buffer == s:
                    print(True)
                    return 0
                if len(max_buffer) < len(buffer):
                    max_buffer = buffer
    if max_buffer == '': print(False)
    else: print(max_buffer)


if __name__ == "__main__":
    main()