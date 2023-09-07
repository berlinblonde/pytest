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


def generate_random_string(lenght): #функция генерации случайных значений (строку) для ключей title и body
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(lenght)) #создаю случайную строку - случайный символ из letters и длину

@pytest.fixture
def generate_post_dict(number):
    post_dict = {}
    post_dict['title']=''.join(random.choices(string.ascii_lowercase, k=6))
    post_dict['body']=''.join(random.choices(string.ascii_lowercase, k=7))
    return post_dict

