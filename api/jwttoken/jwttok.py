from fastapi import FastAPI

app = FastAPI()

users =[]

@app.post('/register')
def register():
    return {'result': 'You have successfully created your account'}

@app.post('/login')
def login():
    return {'name': 'id'}

@app.get('/')
def unprotected_routes():
    return {'name': 'unprotected routes'}

@app.get('/protected')
def protected_routes():
    return {'status': 'authorized'}
    
