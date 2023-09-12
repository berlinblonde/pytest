class Tokens:
    token='Bearer 4ce0bb65c5a42326b76b6a1c14e373bc58729241c5bf931110a552ff84959126'

class Data:
    user_id='5124733'
    test_id='3030'

class Errors:
    blank_field={'field': 'title', 'message': "can't be blank"}

class StatusCode:
    created=201
    user_error=422
    success=200
    success_no_body=204

class Headers:
    headers={'Authorization': Tokens.token}
