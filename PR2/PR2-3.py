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
    if max_buffer == '' or len(max_buffer) == 2:
        olds = s
        result = ''
        i = 0
        while '()' in s or '{}' in s or '[]' in s:
            bracket_index = brackets.index(s[i])
            if bracket_index % 2 == 0:
                if s[i+1] == brackets[bracket_index + 1]:
                    result += s[i] + s[i+1]
                    s = s[i+1:]
                    i = 0
            i += 1
        if result == '':
            print(False)
        else:
            if result == olds:
                print(True)
            else: print(result)
    else: print(max_buffer)


if __name__ == "__main__":
    main()