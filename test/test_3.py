import requests

def test_fucntion1():
    a=requests.get('https://gorest.co.in/public/v2/users')
    print(len(a.json()))
    print(a.json())

def test_function2():
     a=requests.get('https://gorest.co.in/public/v2/users/?page=1&per_page=1')
     print(a.json())

def test_function3():
     a=requests.get('https://gorest.co.in/public/v2/users/?page=90&per_page=90000')
     print(a.json())


def test_function4():
     a=requests.get('https://gorest.co.in/public/v2/users/?gender=female&status=active&id=3681819')
     print(a.json())

def test_function5():
     a=requests.get('https://gorest.co.in/public/v2/users/?id=3681819&email=chanda_shah@schowalter.test')
     print(a.json())


