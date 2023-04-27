# Первый тест отправляет POST-запрос на эндпоинт /api/users,
# создавая нового пользователя. Тест проверяет, что статус ответа равен 201 (успех создания), имя и
# работа пользователя соответствуют отправленным данным, и ответ содержит поля "id" и "createdAt".:
def test_create_user(session):
    url = "https://reqres.in/api/users"
    data = {
        "name": "morpheus",
        "job": "leader"
    }
    response = session.post(url, json=data)
    assert response.status_code == 201
    assert response.json()["name"] == "morpheus"
    assert response.json()["job"] == "leader"
    assert "id" in response.json()
    assert "createdAt" in response.json()


# Второй тест отправляет PUT-запрос на эндпоинт /api/users/2, обновляя данные пользователя с
# идентификатором 2. Тест проверяет, что статус ответа равен 200 (успех обновления),
# имя и работа пользователя соответствуют отправленным данным, и ответ содержит поле "updatedAt".

def test_update_user(session):
    url = "https://reqres.in/api/users/2"
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = session.put(url, json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "morpheus"
    assert response.json()["job"] == "zion resident"
    assert "updatedAt" in response.json()


# Мы проверяем, что статус код ответа равен 200, что говорит о том, что запрос выполнен успешно.

def test_list_users_status_code_equals_200(session):
    response = session.get('https://reqres.in/api/users')
    assert response.status_code == 200


# Мы проверяем, что ответ содержит поле "data" и что количество элементов в поле "data" больше нуля.
def test_list_users_contains_data(session):
    response = session.get('https://reqres.in/api/users')
    data = response.json()
    assert 'data' in data
    assert len(data['data']) > 0


# Мы проверяем, что первый пользователь в списке имеет все необходимые поля, такие как "id", "email", "first_name",
# "last_name" и "avatar".
def test_list_users_first_user_has_required_fields(session):
    response = session.get('https://reqres.in/api/users')
    data = response.json()
    first_user = data['data'][0]
    required_fields = ['id', 'email', 'first_name', 'last_name', 'avatar']
    assert all(field in first_user for field in required_fields)
