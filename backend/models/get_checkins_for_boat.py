from pydantic import BaseModel


class GetCheckinsForBoat(BaseModel):
    trainer_name: str
