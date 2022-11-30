from fastapi import FastAPI, HTTPException, Depends
from auth import Auth_Hanlder
from schema import Auth_Details

app = FastAPI()
users = []
auth_handle = Auth_Hanlder()

@app.post('/register')
def register(auth_details: Auth_Details):
    for x in users:
        if auth_details.username == x['username']:
            raise HTTPException(status_code=400, detail='This username has already been taken!')
    hashed_password = auth_handle.get_hash_password(auth_details.password)
    users.append({'username': auth_details.username, 'password': hashed_password})
    print(users)
    return {'status': 'You have successfully created an account with us'}


@app.post('/login')
def login(auth_details: Auth_Details):
    user = None
    for x in users:
        if auth_details.username == x['username']:
            user = x
            break
    if (user is None) or (not auth_handle.verify_password(auth_details.password, user['password'])):
        raise HTTPException(status_code=400, detail='Username or Password is incorrect')
    token = auth_handle.encode(user['username'])
    return {'status':'You have successfully logged in',
            'token': token}

@app.get('/')
def resources():
    return {'type': 'unprotected resources'}

@app.get('/protected')
def protected_routes(username=Depends(auth_handle.auth_wrapper)):
    return {'status': username + ' now have access to premium resources'}
