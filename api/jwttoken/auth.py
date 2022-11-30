from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt

class Auth_Hanlder():
    secret = 'This is JWT'
    pwd_context = CryptContext(schemes="bcrypt", deprecated="auto")
    security = HTTPBearer()

    def get_hash_password(self,plain_password):
        return self.pwd_context.hash(plain_password)
    
    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def encode(self, auth_details):
        payload = {
            'exp':datetime.utcnow() + timedelta(days=0, minutes=5),
            'iat': datetime.utcnow(),
            'sub': auth_details
        }
        return jwt.encode(payload, self.secret, algorithm="HS256")
    
    def decode(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=["HS256"])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=400, detail="Expired Token")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=400, detail="Invalid Token")

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode(auth.credentials)
