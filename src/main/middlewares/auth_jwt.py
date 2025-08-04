from flask import request
from src.drivers.jwt_handler import JwtHandler
from src.errors.types.http_unauthorized import HttpUnauthorizedError

def auth_jwt_verify():
    jwt_handle = JwtHandler()
    raw_token = request.headers.get("Authorization")
    user_id = request.headers.get("uid")

    if not raw_token or not user_id:
        raise HttpUnauthorizedError("Invalid Auth information")
    
    token = raw_token.split()[1]
    token_information = jwt_handle.decode_jwt_token(token)
    token_uid = token_information["user_id"]

    if user_id and token_uid and (int(token_uid) == int(user_id)):
        return token_information
    
    raise HttpUnauthorizedError("User Unauthorized")
