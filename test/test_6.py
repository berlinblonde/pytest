import requests


def test_function4():
    bodies = {"email": "hopoipaiii@opop.com", "name": "opop", "gender": "male", "status": "active"}
    newbody={"email": "pres_anish_ganaka@marks.biz", "name": "opop", "gender": "male", "status": "inactive"}
    headers = {"Authorization": "Bearer c3842a0fdeb2501dc1288ddbc7df815f22367a29057ca2672e680ff81e61d3f3"}
    #b = requests.post('https://gorest.co.in/public/v2/users', headers=headers, data=bodies)
    #print(b.json())
    a=requests.get('https://gorest.co.in/public/v2/users/2188', params=None)
    print(a.json())
    c=requests.put('https://gorest.co.in/public/v2/users/2188', headers=headers, data=newbody)
    print(c.json())
    assert c.json()['name']!=a.json()['name'] #проверка что данные не равны старым
    assert c.json()['name']==newbody['name'] #проверяем что данные равны тем которым мы хотели
