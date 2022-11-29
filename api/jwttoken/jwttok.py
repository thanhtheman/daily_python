from fastapi import FastAPI, Depends, HTTPException
from schema import Auth_Details
from auth import Auth_Handler

app = FastAPI()

auth_handle = Auth_Handler()
users = []

@app.post('/register')
def register(user_input: Auth_Details):
    for x in users:
        if user_input.username == x['username']:
            raise HTTPException(status_code=400, detail='Username is already taken!')
    hashed_password = auth_handle.get_password_hash(user_input.password)
    users.append({'username': user_input.username, 'password': hashed_password})
    print(users)
    return {'result':'You have successfully created your account'}

@app.post('/login')
def login(user_input: Auth_Details):
    user = None
    for x in users:
        if x['username'] == user_input.username:
            user = x
            break
    if (user is None) or (not auth_handle.verify_password(user_input.password, user['password'])):
        raise HTTPException(status_code=400, detail='Invalid Username or Password')
    token = auth_handle.encode(user['username'])
    return {'result': token}

@app.get('/')
def unprotected_routes():
    return {'name': 'unprotected routes'}

@app.get('/protected')
def protected_routes(username=Depends(auth_handle.auth_wrapper)):
    return {'status': username + ' is authorized',
            'post':'secret passcode is 123456'}
    
