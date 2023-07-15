import requests

def test_function():
    params={'latitude':56.5,
            'longitude':-180.0}
    a=requests.get('https://api.open-meteo.com/v1/forecast',params=params)#передаем параметры после запятой
    assert a.json()['longitude']==params['longitude']
    print(a.status_code)
    print(a.json())

def test_fuction_post():
    body={'id':1,
          'name':'Anna'}
    a=requests.post('https://httpbin.org/post',data=body)
    assert body==a.json()['form']
    print(a.status_code)
    print(a.json())
