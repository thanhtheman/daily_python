import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
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
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=404, detail='Token has expired')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=404, detail='Invalid Token')
#the token is usually stored in the header of the request. Thus, to access the protected resource
# we need to check if the token is valid.
# the Security will take in HTTPBearer which stores the token
# we wrap this token in the HTTP AuthorizationCredentials, then we can access the token 
# by access its credentials.  
    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode(auth.credentials)
