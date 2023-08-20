from tests.config import Forum


def test_function_101():
    forum = Forum() #создаем экземпляр класса и присваиваем его переменной
    posts = forum.get_user_posts(user_id=2659).json()# вызываем метод обьекта с аругментом (юзер_ид) и преобразуем в фомат json, результат сохраняя в переменную  posts
    for post in posts: #проходимя по каждому элементу в списке
        print(post)

