import requests


def test_function20():
    a=requests.get('https://gorest.co.in/public/v2/users/2247/posts')
    print(len(a.json()))


def test_function21():
    x = [2,3,4,5,6,7,8]
    result = []
    for i in x:
        result.append(i**2)

    print(result)
    return result


def test_function_22(x):
    x = [23, 4, -6, 23, -9, 21, 3, -45, -8]
    negative, positive = [], []
    for i in x:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)

    print('Negative:', negative)
    print('Positive:', positive)
    return negative, positive



