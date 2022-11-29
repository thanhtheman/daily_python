from pydantic import BaseModel

class Auth_Details(BaseModel):
    username: str
    password: str