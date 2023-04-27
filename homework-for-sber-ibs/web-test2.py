import requests


def test_create_user():
    # отправляем POST-запрос для создания нового пользователя
    response = requests.post('https://reqres.in/api/users', json={"name": "John", "job": "Developer"})

    # проверяем, что код ответа равен 201 (успешное создание пользователя)
    assert response.status_code == 201

    # проверяем, что вернувшийся ответ содержит корректные данные пользователя
    assert response.json()['name'] == "John"
    assert response.json()['job'] == "Developer"
    assert 'id' in response.json()


def test_list_users():
    # отправляем GET-запрос для получения списка всех пользователей
    response = requests.get('https://reqres.in/api/users')

    # проверяем, что код ответа равен 200 (успешный запрос)
    assert response.status_code == 200

    # проверяем, что вернувшийся ответ содержит корректный список пользователей
    assert 'data' in response.json()
    assert len(response.json()['data']) > 0
