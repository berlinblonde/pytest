import requests

def test_function():
    a=requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m')
    print(a)



def test_function_1():
    a=requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m')
    print(len(a.json()))

def test_function_2():
    a=requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m')
    data=a.json()
    timezone=data['timezone']
    print(timezone)

def test_function_3():
    a=requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m')
    data=a.json()
    latitude=data['latitude']
    if data['latitude']==53.54:
       print(True)
    else:
       print(False)

def test_function_4():
    a=requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m')
    data=a.json()
    latitude=data['latitude']
    if data['latitude']==53.54:
       print(True)
    else:
       print(False)

def test_function_5():
    a=requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m')
    data=a.json()
    elevation=data['elevation']
    if data['elevation']==65:
       print('ok')
    else:
       print('not ok')


