from pydantic import BaseModel


class VerificationRequest(BaseModel):
    token: str
    challenge: str
    type: str
