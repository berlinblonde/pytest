from tests.static import Tokens
from tests.config import GoRestService

def test_function4():
    bodies = [{"email": "hopouipa@opop.com", "name": "opop", "gender": "male", "status": "active"},
              {"email": "hopozuopa@opop.com", "name": "zopop", "gender": "male", "status": "active"},
              {"email": "hoertuozopa@opop.com", "name": "zofeFpop", "gender": "male", "status": "active"},
              {"email": "hsafrtuozopa@opop.com", "name": "zosacfpop", "gender": "female", "status": "active"}, ]
    headers = {"Authorization":Tokens.token}

    for element in bodies:
        b = GoRestService().post_user(headers=headers,data=element),
        print(b)

