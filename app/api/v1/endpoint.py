from ...models import (
    UnauthResponse,
    ResponseModel,
)
from typing import Union
from fastapi import APIRouter, Request

router = APIRouter(prefix="/endpoint-prefix", tags=["endpointtag"])


@router.get(
    "/",
    status_code=200,
    response_model=ResponseModel,
    responses={
        "401": {"model": UnauthResponse},
    },
    tags=["endpointtag"],
)
def get_index(request: Request) -> Union[ResponseModel, UnauthResponse]:
    return {"message": "test message"}
