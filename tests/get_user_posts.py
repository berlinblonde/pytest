from tests.config import GoRestService
from tests.static import Data


def test_function_101():
    posts = GoRestService().get_user_posts(params={})# вызываем метод обьекта с аругментом (юзер_ид) и преобразуем в фомат json, результат сохраняя в переменную  posts
    assert posts.status_code == 200
    assert len(posts.json())>0
    for post in posts.json():
        #assert post['user_id']==int(Data.user_id)
        #assert len(post['body'])!=0
        assert len(post['title'])!=0

def test_function_190():
    params={'page':1,'per_page':3}
    posts = GoRestService().get_user_posts(params=params)# вызываем метод обьекта с аругментом (юзер_ид) и преобразуем в фомат json, результат сохраняя в переменную  posts
    assert posts.status_code == 200
    assert len(posts.json())>0
    assert len(posts.json())<=params['per_page']


def test_function_199():
    params={'page':1,'per_page':0}
    posts = GoRestService().get_user_posts(params=params)# вызываем метод обьекта с аругментом (юзер_ид) и преобразуем в фомат json, результат сохраняя в переменную  posts
    assert posts.status_code == 200
    assert len(posts.json())>0
    assert len(posts.json())<=params['per_page']
