import requests
from tests.static import Data


class GoRestService:
    url = 'https://gorest.co.in/public/v2'
    create_user = '/users'  # переменные-путь к ресурсу который будет добавлен к адресу
    get_users = '/users/'
    posts_path = '/posts'  # переменная-путь к ресурсу который будет добавлен к адресу
    create_user_to_do = '/todos'
    create_comment = '/comments'

    def __init__(self):  # метод конструктор
        pass

    def post_user(self, headers, data):  # метод http-post на создание юзера, принимает два аргумента заголовок и данные
        r = requests.post(self.url + self.create_user, headers=headers,
                          data=data)  # функция внутри метода отправляет post добавляя заголовок и данные
        return r  # возвращаем результат из метода

    def get_user_posts(self, params):  # метод класса, получение постов юзера с форума, принмает один аргумент
        r = requests.get(self.url + self.get_users + Data.user_id + self.posts_path,
                         params=params)  # переменная внутри метода, где хранится результат запроса (переменная урл+аргрумент+переменная post_path) формируя полный урл
        return r  # результат запроса возвращается из метода

    def add_garbage(self, headers, data):
        r = requests.post(self.url + self.get_users + Data.user_id + self.posts_path, headers=headers, data=data)
        return r

    def create_user_post(self, headers, data):
        r = requests.post(self.url + self.get_users + Data.test_id + self.posts_path, headers=headers, data=data)
        return r

    def create_user_todos(self, headers, data):
        r = requests.post(self.url + self.get_users + Data.test_id + self.create_user_to_do, headers=headers, data=data)
        return r

    def create_user_comment(self, headers, data):
        r = requests.post(self.url + self.posts_path + '/' + Data.test_id + self.create_comment, headers=headers,
                          data=data)
        return r
