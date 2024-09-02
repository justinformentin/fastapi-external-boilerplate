from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

class UnauthResponse(BaseModel):
    message: Optional[str] = None

class ResponseModel(BaseModel):
    results: Optional[str] = None
