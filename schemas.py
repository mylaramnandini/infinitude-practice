from pydantic import BaseModel
class UserSchema(BaseModel):
    ID: int
    Name: str
    Nickname: str
    Email: str
