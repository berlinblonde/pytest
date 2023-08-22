def test_function30():
    a = 11
    b = 1
    while a >= 11:
        b += 1  # +1
    print(b)


def test_function31():
    a = 0
    while a < 6:
        a += 1
        print(a)


def test_function32():
    i = [1, 10]
    while i == 4:
        print(i)


def test_function33():
    a = "Python"
    # for letter in a:
    # print(letter)
    for letter in a:
        if letter == "o":
            continue
        print(letter)


def test_function34():
    a = 30
    b = 21
    if a < b:
        a, b = b, a
    d = a - b
    while d > 3:
        d = d - b
        print(d)


