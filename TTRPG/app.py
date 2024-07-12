from http import HTTPStatus

from fastapi import FastAPI
from TTRPG.schemas import UserSchema, UserPublic, UserDB, UserList

app = FastAPI()

database = []


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_With_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_With_id)

    return user_With_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    user_With_id = UserDB(id=user_id, **user.model_dump())
    database[user_id - 1] = user_With_id
    return user_With_id