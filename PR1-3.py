def main():
    word, numRows = input().split()
    numRows = int(numRows)
    between = numRows - 2
    newWord = ''
    x = between + numRows
    if x == 0:
        print(word)
        return
    for i in range(numRows):
        j = i
        if i == 0 or i == numRows-1:
            while j < len(word):
                newWord += word[j]
                j += x
        else:
            k = x - i
            while j < len(word) or k < len(word):
                if j < len(word) and k < len(word):
                    newWord += word[j]
                    newWord += word[k]
                else:
                    newWord += word[j]
                j += x
                k += x
    print(newWord)

if __name__ == '__main__':
    main()