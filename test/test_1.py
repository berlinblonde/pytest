import requests


def test_func():
    assert True is True

def test_function():
    a=requests.get('https://jsonplaceholder.typicode.com/posts')
    print(a)
    assert a.status_code==200
    if a.status_code==400:
       print(len(a.json()))
       b=[]
       assert type(a.json())==type(b)
       print(a.json()[2])
    else:
        print('blabla')


