from jsonrpcserver import Success, method, serve, InvalidParams, Result, Error
import re

@method
def validate_email(email) -> Result:
    if email = '':
        return Error