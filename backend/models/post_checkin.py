from pydantic import BaseModel


class CheckinBody(BaseModel):
    trainer_name: str
    comment: str | None = None
    amount_refueled: float
