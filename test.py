a1, b1, a2, b2 = [input() for _ in range(4)]
if a2 < a1:
    c = a1
    a1 = a2
    a2 = c
    c = b1
    b1 = b2
    b2 = c
if b1 < a2:
    print("пустое множество")
elif b1 > a2:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif b1 == a2:
    print(b1)



