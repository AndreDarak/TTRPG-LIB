from ward import test
from test_Configs import client
from http import HTTPStatus


@test('Cria Usuario FastApi')
def _(client=client):
    response = client.post(
        '/users/',
        json={
            'username': 'Darak',
            'passworld': 'Teste123',
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
