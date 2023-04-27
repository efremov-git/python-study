# Тест отправляет POST-запрос на эндпоинт /api/login с отсутствующим параметром "password".
# Тест проверяет,что статус ответа равен 400 (ошибка на стороне клиента)
# и что ответ содержит сообщение об ошибке "Missing password".:
def test_missing_password(session):
    url = "https://reqres.in/api/login"
    data = {
        "email": "peter@klaven"
    }
    response = session.post(url, json=data)
    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"


# Тест отправляет POST-запрос на эндпоинт /api/register с данными пользователя,
# которого нет в списке разрешенных для регистрации. Тест проверяет, что статус ответа
# равен 400 и что ответ содержит сообщение об ошибке "Note: Only defined users succeed registration".
def test_invalid_user_registration(session):
    url = "https://reqres.in/api/register"
    data = {
        "email": "sydney@fife",
        "password": "pistol"
    }
    response = session.post(url, json=data)
    assert response.status_code == 400
    assert response.json()["error"] == "Note: Only defined users succeed registration"

# Тест проверяет, что статус-код ответа равен 200 и что список пользователей не пустой.
def test_list_users(session):
    response = session.get('https://reqres.in/api/users')
    assert response.status_code == 200
    assert len(response.json()['data']) > 0

# Тест проверяет, что сервер вернет статус-код 400 и возвращает ошибку, содержащую текст "page".
def test_list_users_with_invalid_page(session):
    response = session.get('https://reqres.in/api/users?page=0')
    assert response.status_code == 400
    assert 'page' in response.json()['error']