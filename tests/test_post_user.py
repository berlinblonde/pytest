from tests.config import GoRestService
from tests.static import Errors, Data, StatusCode, Headers



def test_user_creating_ok(create_user):
    response = GoRestService().post_user(headers=Headers.headers, data=create_user)

    assert response.status_code == StatusCode.created


def test_user_creating_failed(create_user):
    data = create_user
    data['adress'] = 'Berlin'

    response = GoRestService().post_user(headers=Headers.headers, data=data)

    assert response.status_code == StatusCode.created


def test_create_user_different_gender(create_user):
    data = create_user
    data['gender'] = 'Berlin'

    response = GoRestService().post_user(headers=Headers.headers, data=data)

    assert response.status_code == StatusCode.user_error


def test_function_220():
    response = GoRestService().add_garbage(headers=Headers.headers, data={"body": "0000"})

    response_data = response.json()

    assert response.status_code == StatusCode.user_error
    assert len(response_data) > 0
    assert response_data[0] == Errors.blank_field  # приводим к одному типу данных


def test_function_288():
    response = GoRestService().add_garbage(headers=Headers.headers, data={})

    response_data = response.json()

    assert response.status_code == StatusCode.user_error
    assert len(response_data) > 0
    assert response_data[0] == Errors.blank_field


def test_function_889():
    response = GoRestService().add_garbage(headers=Headers.headers, data={"body": "0000", "title": "99999999"})

    response_data = response.json()

    print(response_data)


def test_function_009():

    response = GoRestService().add_garbage(headers=Headers.headers, data={"body": "0000", "title": "99999999"})

    assert response.status_code == StatusCode.created


def test_dict_creating(generate_post_dict):

    response = GoRestService().create_user_post(headers=Headers.headers, data=generate_post_dict)

    assert response.status_code == StatusCode.created
    assert response.json()['title'] == generate_post_dict['title']
    assert response.json()['body'] == generate_post_dict['body']
    assert str(response.json()['user_id']) == Data.test_id


def test_create_user_to_do(generate_to_do_dict):

    response = GoRestService().create_user_todos(headers=Headers.headers, data=generate_to_do_dict)

    assert response.status_code == StatusCode.created
    assert response.json()['title'] == generate_to_do_dict['title']
    assert response.json()['status'] == generate_to_do_dict['status']
    assert str(response.json()['user_id']) == Data.test_id


def test_create_user_comment(generate_comment_dict):

    response = GoRestService().create_user_comment(headers=Headers.headers, data=generate_comment_dict)

    assert response.status_code == StatusCode.user_error
