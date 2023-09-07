import random
import string

import pytest


@pytest.fixture
def create_user():
    user = {}
    email = ''.join(random.choices(string.ascii_lowercase, k=4)) + '@hophop.com'
    name = ''.join(random.choices(string.ascii_lowercase, k=10)) + ' ' + 'Pupkin'
    gender = random.choice(['male', 'female'])
    status = random.choice(['active', 'inactive'])
    user['email'] = email
    user['name'] = name
    user['gender'] = gender
    user['status'] = status
    return user


@pytest.fixture
def page_filter():
    return {'page': random.randint(0, 3), 'per_page': random.randint(0, 3)}

@pytest.fixture
def generate_random_string(lenght): #функция генерации случайных значений (строку) для ключей title и body
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(lenght)) #создаю случайную строку - случайный символ из letters и длину

@pytest.fixture
def generate_random_dict(number):
    random_dict = {}
    for _ in range(number):
        title = generate_random_string(5)
        body = generate_random_string(5)
        key = "title" + str(_)#соединяю строку со значением
        random_dict[key] = {"title": title, "body": body}#
    return random_dict

number = 10 #задаю количество записей в переменную
data = generate_random_dict(number)#генерим словарь с использовнием функции
print(data)
