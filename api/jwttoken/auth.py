import jwt
from fastapi import HttpException, Security
from fastpai.security import HttpAuthorizationCredentials, HTTPBearer
from passlib.context import CryptoContext
from datetime import datetime, timedelta

#HTTPBearer will return an error if there is no bearer token
class Auth_Handler():
    security = HTTPBearer()
    pwd_context = Cryto