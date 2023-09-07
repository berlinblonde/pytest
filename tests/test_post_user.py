from tests.config import GoRestService
from tests.static import Tokens, Errors, Data


def test_user_creating_ok(create_user):
    data=create_user
    headers = {"Authorization": Tokens.token}

    response = GoRestService().post_user(headers=headers, data=data)

    assert response.status_code==201

def test_user_creating_failed(create_user):
    data=create_user
    data['adress']='Berlin'
    headers = {"Authorization": Tokens.token}

    response = GoRestService().post_user(headers=headers, data=data)

    assert response.status_code==201


def test_create_user_different_gender(create_user):
    data=create_user
    data['gender']='Berlin'
    headers = {"Authorization": Tokens.token}

    response = GoRestService().post_user(headers=headers, data=data)

    assert response.status_code==422

def test_function_220():
    data = {"body": "0000"}
    headers = {"Authorization": Tokens.token}

    response = GoRestService().add_garbage(headers=headers, data=data)
    response_data = response.json()

    assert response.status_code==422
    assert len(response_data)>0
    assert response_data[0]==Errors.blank_field #приводим к одному типу данных


def test_function_288():
    data = {}
    headers = {"Authorization": Tokens.token}

    response = GoRestService().add_garbage(headers=headers, data=data)
    response_data = response.json()

    assert response.status_code==422
    assert len(response_data)>0
    assert response_data[0]==Errors.blank_field

def test_function_889():
    data = {"body": "0000", "title":"99999999"}
    headers = {"Authorization": Tokens.token}

    response = GoRestService().add_garbage(headers=headers, data=data)
    response_data = response.json()
    print(response_data)

def test_function_009():
    data = {"body": "0000", "title":"99999999"}
    headers = {"Authorization": Tokens.token}

    response = GoRestService().add_garbage(headers=headers, data=data)
    response_data = response.json()
    print(response_data)

def test_dict_creating(generate_post_dict):
    data=generate_post_dict
    headers = {"Authorization": Tokens.token}

    response = GoRestService().create_user_post(headers=headers, data=data)
    print(response)
    assert response.status_code==201
    assert response.json()['title']==data['title']
    assert response.json()['body']==data['body']
    assert str(response.json()['user_id'])==Data.test_id

def test_create_user_todos(generate_to_do_dict):
    data=generate_to_do_dict
    headers={"Authorization": Tokens.token}

    response=GoRestService().create_user_to_do(headers=headers, data=data)
    assert response.status_code==201
