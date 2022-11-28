import jwt
from fastapi import HttpException, Security
from fastapi.security import HttpAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta

#HTTPBearer will return an error if there is no bearer token
class Auth_Handler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret ="No Secret"

    def get_password_hash(self, plain_password):
        return self.pwd_context.hash(plain_password)
    
    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def encode(self, user_id):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=5),
            'iat': datetime.utcnow(),
            'sub': user_id 
        }
        return jwt.encode(payload, self.secret, algorithm="HS256")
    
    def decode(self, token):
        try:
            payload = jwt.decode(payload, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HttpException(status_code=404, detail='Token has expired')
        except jwt.InvalidTokenError as e:
            raise HttpException(status_code=404, detail='Invalid Token')
        
    def auth_wrapper(self, auth: HttpAuthorizationCredentials = Security(security)):
        return self.decode(auth.credentials)
