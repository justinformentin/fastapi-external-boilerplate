from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

class ResponseModel(BaseModel):
    message: Optional[str] = None
