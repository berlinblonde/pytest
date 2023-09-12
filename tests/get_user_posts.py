from tests.config import GoRestService
from tests.static import StatusCode


def _asserts(response):
    assert response.status_code == StatusCode.success
    assert len(response.json()) > 0


def test_function_101():
    posts = GoRestService().get_user_posts(
        params={})  # вызываем метод обьекта с аругментом (юзер_ид) и преобразуем в фомат json, результат сохраняя в переменную  posts

    _asserts(response=posts)
    for post in posts.json():
        assert len(post['title']) != 0


def test_function_190():
    params = {'page': 1, 'per_page': 3}

    posts = GoRestService().get_user_posts(
        params=params)  # вызываем метод обьекта с аругментом (юзер_ид) и преобразуем в фомат json, результат сохраняя в переменную  posts

    _asserts(response=posts)
    assert len(posts.json()) <= params['per_page']


def test_function_199():
    params = {'page': 1, 'per_page': 0}

    posts = GoRestService().get_user_posts(
        params=params)  # вызываем метод обьекта с аругментом (юзер_ид) и преобразуем в фомат json, результат сохраняя в переменную  posts

    _asserts(response=posts)
    assert len(posts.json()) <= params['per_page']
