from typing import Optional

from pydantic import BaseModel


class VerificationRequest(BaseModel):
    token: Optional[str] = None
    challenge: Optional[str] = None
    type: str
    event: Optional[any] = None
