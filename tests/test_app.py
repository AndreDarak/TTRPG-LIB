from ward import test
from test_Configs import client
from http import HTTPStatus


@test('Cria Usuario FastApi')
def _(client=client):
    response = client.post(
        '/users/',
        json={
            'username': 'Darak',
            'password': 'Teste123',
            'email': 'teste@gmail.com',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'Darak',
        'email': 'teste@gmail.com',
        'id': 1,
    }


@test('Consulta Usuarios no banco')
def _(client=client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'username': 'Darak', 'email': 'teste@gmail.com', 'id': 1}]
    }


@test('Troca dados do usuario no banco')
def _(client=client):
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'Andre DAvila Silva',
            'email': 'teste23@gmail.com',
            'id': 1,
        },
    )
    assert response.json() == {
        'username': 'Andre DAvila Silva',
        'email': 'teste23@gmail.com',
        'id': 1,
    }


@test('Delete usuario por ID')
def _(client=client):
    response = client.delete('/users/1')
    assert response.json() == {'Message': 'User deleted'}
      