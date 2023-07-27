def test_function15():
    a = [{"email": "hopoip@opop.com", "name": "opop pupkin", "gender": "male", "status": "inactive"},
        {"email": "hopozop@opop.com", "name": "zopop hrupkin", "gender": "male", "status": "active"},
        {"email": "hoertozop@opop.com", "name": "zofeFpop pupkin", "gender": "male", "status": "active"},
        {"email": "hsafrtozop@opop.com", "name": "zosacfpop pupkin", "gender": "female", "status": "active"},
        {"email": "hsafrtozop@opop.com", "name": "zosacfpop lupkin", "gender": "female", "status": "inactive"},

    ]
    for element in a:
        assert element['name']
        assert 'pupkin' in element['name']


    assert 'pupkin' in a[4]['name']


def test_function16():
    a = [{"email": "hopoip@opop.com", "name": "opop pupkin", "gender": "male", "status": "inactive"},
        {"email": "hopozop@opop.com", "name": "zopop hrupkin", "gender": "male", "status": "active"},
        {"email": "hoertozop@opop.com", "name": "zofeFpop pupkin", "gender": "male", "status": "active"},
        {"email": "hsafrtozop@opop.com", "name": "zosacfpop pupkin", "gender": "female", "status": "active"},
        {"email": "hsafrtozop@opop.com", "name": "zosacfpop lupkin", "gender": "female", "status": "inactive"},

    ]
    assert a[3]['status']=='active' #зайти в элемент массива по индексу и ищем по ключу значение
    assert a[2]['gender']=='male'

