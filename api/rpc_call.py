from fastapi import FastAPI, Request, Response
from jsonrpcserver import Result, Success, dispatch, method, Error
import uvicorn
import re

app = FastAPI()


@method
def ping() -> Result:
    return Success("pong")

@method
def validate_email(email) -> Result:    
    if email == "":
        return Error(code=123, message="Empty email provided")
    if re.match("(.*?)@(.*?).com", email):    
        return Success(True)
    else:
        return Success(False)


@app.post("/")
async def index(request: Request):
    return Response(dispatch(await request.body()))


if __name__ == "__main__":
    uvicorn.run(app, port=5000)