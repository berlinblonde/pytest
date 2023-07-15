import requests


def test_function4():
    bodies = [{"email": "hopoipa@opop.com", "name": "opop", "gender": "male", "status": "active"},
        {"email": "hopozopa@opop.com", "name": "zopop", "gender": "male", "status": "active"},
        {"email": "hoertozopa@opop.com", "name": "zofeFpop", "gender": "male", "status": "active"},
        {"email": "hsafrtozopa@opop.com", "name": "zosacfpop", "gender": "female", "status": "active"}, ]
    headers = {"Authorization": "Bearer c3842a0fdeb2501dc1288ddbc7df815f22367a29057ca2672e680ff81e61d3f3"}

    for element in bodies:
        b = requests.post('https://gorest.co.in/public/v2/users', headers=headers, data=element)
        print(b.json())


def test_function5():
    data = {
        "email": "hopsfsdgoip@ofspop.com",
        "name": "opopd",
        "gender": "male",
        "status": "afsba"
    }
    headers = {"Authorization": "Bearer c3842a0fdeb2501dc1288ddbc7df815f22367a29057ca2672e680ff81e61d3f3"}
    b = requests.post('https://gorest.co.in/public/v2/users', headers=headers, data=data)
    assert data==b.json()
    print(b.status_code)
    print(b.json())

def test_function7():
    data = {
        "email": "hopsfssadwrdgoip@ofspop.com",
        "name": "opofrpd",
        "gender": "female",
        "status": ["active", "inactive"]
    }
    headers = {"Authorization": "Bearer c3842a0fdeb2501dc1288ddbc7df815f22367a29057ca2672e680ff81e61d3f3"}
    b = requests.post('https://gorest.co.in/public/v2/users', headers=headers, data=data)
    assert b.status_code==200
    print(b.status_code)
    print(b.json())

def test_function8():
    data = {

    }
    headers = {"Authorization": "Bearer c3842a0fdeb2501dc1288ddbc7df815f22367a29057ca2672e680ff81e61d3f3"}
    b = requests.post('https://gorest.co.in/public/v2/users', headers=headers, data=data)
    print(b.status_code)
    print(b.json())
