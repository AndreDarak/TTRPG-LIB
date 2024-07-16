from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from TTRPG.schemas import UserSchema, UserPublic, UserDB, UserList, Message

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
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User Not Found'
        )
    user_With_id = UserDB(id=user_id, **user.model_dump())
    database[user_id - 1] = user_With_id
    return user_With_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    del database[user_id - 1]

    return {'Message': 'User deleted'}  
