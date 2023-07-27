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
