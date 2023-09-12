from tests.config import GoRestService
from tests.static import Headers, StatusCode

def test_delete_user():
    response = GoRestService().delete_user(headers=Headers.headers)

    assert response.status_code==StatusCode.success_no_body

