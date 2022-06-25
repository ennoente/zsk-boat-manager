from pydantic import BaseModel


class GetAllCheckinsBody(BaseModel):
    username: str
    password: str
